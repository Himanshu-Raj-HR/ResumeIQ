# Developed by Himanshu Raj [https://github.com/Himanshu-Raj-HR/ResumeIQ] | Made with Streamlit

###### Packages Used ######
import streamlit as st
import pandas as pd
import base64, random
import time, datetime
import pymysql
import sqlite3
import os
import socket
import platform
import geocoder
import secrets
import io
import getpass
import plotly.express as px
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
from streamlit_tags import st_tags
from PIL import Image
from Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos
import nltk

# ==========================================
# 1. NLTK DEPENDENCY GUARD
# ==========================================
for resource in ['stopwords', 'punkt']:
    try:
        nltk.data.find(f'corpora/{resource}')
    except LookupError:
        nltk.download(resource, quiet=True)

# ==========================================
# 2. SPACY V3 & PYRESPARSER COMPATIBILITY PATCH
# ==========================================
import spacy
import os

_original_spacy_load = spacy.load

def _patched_spacy_load(name, **kwargs):
    try:
        return _original_spacy_load(name, **kwargs)
    except Exception:
        return _original_spacy_load('en_core_web_sm', **kwargs)

spacy.load = _patched_spacy_load

# Fix spaCy v3 matcher compatibility error in pyresparser
import pyresparser.utils as pyres_utils

def patched_extract_name(nlp_text, matcher=None):
    from spacy.matcher import Matcher
    if matcher is None:
        matcher = Matcher(nlp_text.vocab)
    
    patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}],
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]
    ]
    
    try:
        matcher.add('NAME', patterns)
    except TypeError:
        for pat in patterns:
            matcher.add('NAME', [pat])
            
    matches = matcher(nlp_text)
    for _, start, end in matches:
        span = nlp_text[start:end]
        return span.text
    return None

pyres_utils.extract_name = patched_extract_name

# ==========================================
# 3. NOW IMPORT PYRESPARSER
# ==========================================
from pyresparser import ResumeParser

###### Preprocessing functions ######

def get_csv_download_link(df, filename, text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href


def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()
    return text


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    
    # Use <embed> instead of <iframe> so Chrome/Safari don't block the PDF preview
    pdf_display = f'''
        <embed 
            src="data:application/pdf;base64,{base64_pdf}#toolbar=0&navpanes=0&scrollbar=0" 
            width="100%" 
            height="800px" 
            type="application/pdf"
            style="border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);"
        />
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)


def course_recommender(course_list):
    st.subheader("**Courses & Certificates Recommendations 👨‍🎓**")
    c = 0
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 5)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course


###### Database Stuffs ######

class SQLiteCursorWrapper:
    """Wraps sqlite3 cursor so MySQL queries and syntax work seamlessly on cloud SQLite."""
    def __init__(self, cursor):
        self._cursor = cursor

    def execute(self, sql, params=None):
        if sql.strip().upper().startswith("CREATE DATABASE"):
            return
        # Strip MySQL-specific convert(... using utf8) for SQLite compatibility in Admin queries
        import re
        sql = re.sub(r'convert\(([^)]+?)\s+using\s+utf8\)', r'\1', sql, flags=re.IGNORECASE)
        if params is not None:
            sql = sql.replace("%s", "?")
            return self._cursor.execute(sql, params)
        return self._cursor.execute(sql)

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def __getattr__(self, name):
        return getattr(self._cursor, name)


def get_db_connection():
    """Tries connecting to local MySQL; falls back to SQLite3 for cloud deployment."""
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root@MySQL4admin',
            database='cv',
            charset='utf8mb4'
        )
        return conn, conn.cursor(), 'mysql'
    except Exception:
        conn = sqlite3.connect('cv_database.db', check_same_thread=False)
        return conn, SQLiteCursorWrapper(conn.cursor()), 'sqlite'


connection, cursor, db_type = get_db_connection()


def insert_data(sec_token, ip_add, host_name, dev_user, os_name_ver, latlong, city, state, country, act_name, act_mail, act_mob, name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses, pdf_name):
    conn, cur, dtype = get_db_connection()
    insert_sql = """INSERT INTO user_data (
        sec_token, ip_add, host_name, dev_user, os_name_ver, latlong, city, state, country,
        act_name, act_mail, act_mob, Name, Email_ID, resume_score, Timestamp, Page_no,
        Predicted_Field, User_level, Actual_skills, Recommended_skills, Recommended_courses, pdf_name
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    rec_values = (
        str(sec_token), str(ip_add), str(host_name), str(dev_user), str(os_name_ver),
        str(latlong), str(city), str(state), str(country), str(act_name), str(act_mail),
        str(act_mob), str(name), str(email), str(res_score), str(timestamp),
        str(no_of_pages), str(reco_field), str(cand_level), str(skills),
        str(recommended_skills), str(courses), str(pdf_name)
    )
    cur.execute(insert_sql, rec_values)
    conn.commit()
    conn.close()


def insertf_data(feed_name, feed_email, feed_score, comments, Timestamp):
    conn, cur, dtype = get_db_connection()
    insertfeed_sql = "INSERT INTO user_feedback (feed_name, feed_email, feed_score, comments, Timestamp) VALUES (%s,%s,%s,%s,%s)"
    rec_values = (str(feed_name), str(feed_email), str(feed_score), str(comments), str(Timestamp))
    cur.execute(insertfeed_sql, rec_values)
    conn.commit()
    conn.close()


###### Setting Page Configuration ######
st.set_page_config(
    page_title="ResumeIQ - AI Resume Analyzer",
    page_icon='./Logo/recommend.png' if os.path.exists('./Logo/recommend.png') else "📄",
)


###### Main function run() ######

def run():
    # ==========================================
    # HIGH-IMPACT UI THEME INJECTION (CSS)
    # ==========================================
    st.markdown("""
    <style>
        /* Global Dark Theme & Background */
        .stApp {
            background-color: #0e1117;
            color: #f0f2f6;
        }
        
        /* Sleek Header Styling */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        /* Glassmorphism Cards for Metrics & Results */
        .metric-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(4px);
            text-align: center;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .metric-card:hover {
            transform: translateY(-3px);
            border-color: #00adb5;
        }
        
        /* Custom Sidebar Polish */
        [data-testid="stSidebar"] {
            background-color: #161b22;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
    </style>
    """, unsafe_allow_html=True)

    img = Image.open('./Logo/RESUM.png')
    st.image(img)
    st.sidebar.markdown("# Choose Something...")
    activities = ["User", "Feedback", "About", "Admin"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)
    link = '<b>Built with 🤍 by Himanshu Raj</b>'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    st.sidebar.markdown('''
        <div id="sfct2xghr8ak6lfqt3kgru233378jya38dy" hidden></div>
        <noscript>
            <a href="https://www.freecounterstat.com" title="hit counter">
                <img src="https://counter9.stat.ovh/private/freecounterstat.php?c=t2xghr8ak6lfqt3kgru233378jya38dy" border="0" title="hit counter" alt="hit counter">
            </a>
        </noscript>
        <p>Visitors <img src="https://counter9.stat.ovh/private/freecounterstat.php?c=t2xghr8ak6lfqt3kgru233378jya38dy" title="Free Counter" Alt="web counter" width="60px" border="0" /></p>
    ''', unsafe_allow_html=True)

    ###### Creating Database and Table ######
    global connection, cursor, db_type
    connection, cursor, db_type = get_db_connection()

    if db_type == 'mysql':
        db_sql = """CREATE DATABASE IF NOT EXISTS cv;"""
        cursor.execute(db_sql)
        id_col_def = "ID INT NOT NULL AUTO_INCREMENT"
        pk_def = ", PRIMARY KEY (ID)"
    else:
        id_col_def = "ID INTEGER PRIMARY KEY AUTOINCREMENT"
        pk_def = ""

    # Create table user_data
    DB_table_name = 'user_data'
    table_sql = f"""CREATE TABLE IF NOT EXISTS {DB_table_name} (
                    {id_col_def},
                    sec_token varchar(20) NOT NULL,
                    ip_add varchar(50) NULL,
                    host_name varchar(50) NULL,
                    dev_user varchar(50) NULL,
                    os_name_ver varchar(50) NULL,
                    latlong varchar(50) NULL,
                    city varchar(50) NULL,
                    state varchar(50) NULL,
                    country varchar(50) NULL,
                    act_name varchar(50) NOT NULL,
                    act_mail varchar(50) NOT NULL,
                    act_mob varchar(20) NOT NULL,
                    Name varchar(500) NOT NULL,
                    Email_ID VARCHAR(500) NOT NULL,
                    resume_score VARCHAR(8) NOT NULL,
                    Timestamp VARCHAR(50) NOT NULL,
                    Page_no VARCHAR(5) NOT NULL,
                    Predicted_Field BLOB NOT NULL,
                    User_level BLOB NOT NULL,
                    Actual_skills BLOB NOT NULL,
                    Recommended_skills BLOB NOT NULL,
                    Recommended_courses BLOB NOT NULL,
                    pdf_name varchar(50) NOT NULL
                    {pk_def}
                    );"""
    cursor.execute(table_sql)

    # Create table user_feedback
    DBf_table_name = 'user_feedback'
    tablef_sql = f"""CREATE TABLE IF NOT EXISTS {DBf_table_name} (
                    {id_col_def},
                    feed_name varchar(50) NOT NULL,
                    feed_email VARCHAR(50) NOT NULL,
                    feed_score VARCHAR(5) NOT NULL,
                    comments VARCHAR(100) NULL,
                    Timestamp VARCHAR(50) NOT NULL
                    {pk_def}
                    );"""
    cursor.execute(tablef_sql)
    connection.commit()

    ###### CODE FOR CLIENT SIDE (USER) ######
    if choice == 'User':
        act_name = st.text_input('Name*')
        act_mail = st.text_input('Mail*')
        act_mob  = st.text_input('Mobile Number*')
        sec_token = secrets.token_urlsafe(12)
        try:
            host_name = socket.gethostname()
            ip_add = socket.gethostbyname(host_name)
        except Exception:
            host_name = "unknown"
            ip_add = "0.0.0.0"
        try:
            dev_user = getpass.getuser()
        except Exception:
            dev_user = "cloud_user"
        os_name_ver = platform.system() + " " + platform.release()
        try:
            g = geocoder.ip('me')
            latlong = g.latlng
            geolocator = Nominatim(user_agent="resumeiq_app")
            location = geolocator.reverse(latlong, language='en', timeout=5)
            address = location.raw.get('address', {})
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
        except Exception:
            latlong = ''
            city = ''
            state = ''
            country = ''

        st.markdown('''<h5 style='text-align: left; color: #021659;'> Upload Your Resume, And Get Smart Recommendations</h5>''', unsafe_allow_html=True)

       pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        if pdf_file is not None:
            with st.spinner('Hang On While We Cook Magic For You...'):
                time.sleep(2)

            os.makedirs('./Uploaded_Resumes', exist_ok=True)
            save_image_path = os.path.join('./Uploaded_Resumes', pdf_file.name)
            pdf_name = pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            
            # Display the PDF preview once
            show_pdf(save_image_path)

            resume_data = ResumeParser(save_image_path).get_extracted_data()
            if resume_data:
                resume_text = pdf_reader(save_image_path)

                st.header("**Resume Analysis 🤘**")
                st.success("Hello " + str(resume_data.get('name', '')))
                st.subheader("**Your Basic info 👀**")
                try:
                    st.text('Name: ' + str(resume_data.get('name', '')))
                    st.text('Email: ' + str(resume_data.get('email', '')))
                    st.text('Contact: ' + str(resume_data.get('mobile_number', '')))
                    st.text('Degree: ' + str(resume_data.get('degree', '')))
                    st.text('Resume pages: ' + str(resume_data.get('no_of_pages', 1)))
                except Exception:
                    pass

                cand_level = ''
                if resume_data.get('no_of_pages', 1) < 1:
                    cand_level = "NA"
                    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>You are at Fresher level!</h4>''', unsafe_allow_html=True)
                elif any(w in resume_text for w in ['INTERNSHIP', 'INTERNSHIPS', 'Internship', 'Internships']):
                    cand_level = "Intermediate"
                    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>You are at intermediate level!</h4>''', unsafe_allow_html=True)
                elif any(w in resume_text for w in ['EXPERIENCE', 'WORK EXPERIENCE', 'Experience', 'Work Experience']):
                    cand_level = "Experienced"
                    st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at experience level!</h4>''', unsafe_allow_html=True)
                else:
                    cand_level = "Fresher"
                    st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at Fresher level!!</h4>''', unsafe_allow_html=True)

                st.subheader("**Skills Recommendation 💡**")
                keywords = st_tags(
                    label='### Your Current Skills',
                    text='See our skills recommendation below',
                    value=resume_data.get('skills', []),
                    key='1'
                )

                ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning', 'flask', 'streamlit']
                web_keyword = ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento', 'wordpress', 'javascript', 'angular js', 'c#', 'asp.net', 'flask']
                android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
                ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
                uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes', 'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator', 'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro', 'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp', 'user research', 'user experience']
                n_any = ['english', 'communication', 'writing', 'microsoft office', 'leadership', 'customer management', 'social media']

                recommended_skills = []
                reco_field = ''
                rec_course = ''

                for i in (resume_data.get('skills') or []):
                    if i.lower() in ds_keyword:
                        reco_field = 'Data Science'
                        st.success("** Our analysis says you are looking for Data Science Jobs.**")
                        recommended_skills = ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 'Data Mining', 'Clustering & Classification', 'Data Analytics', 'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras', 'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', 'Flask', 'Streamlit']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='2')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(ds_course)
                        break

                    elif i.lower() in web_keyword:
                        reco_field = 'Web Development'
                        st.success("** Our analysis says you are looking for Web Development Jobs **")
                        recommended_skills = ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel', 'Magento', 'wordpress', 'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='3')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(web_course)
                        break

                    elif i.lower() in android_keyword:
                        reco_field = 'Android Development'
                        st.success("** Our analysis says you are looking for Android App Development Jobs **")
                        recommended_skills = ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java', 'Kivy', 'GIT', 'SDK', 'SQLite']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='4')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(android_course)
                        break

                    elif i.lower() in ios_keyword:
                        reco_field = 'IOS Development'
                        st.success("** Our analysis says you are looking for IOS App Development Jobs **")
                        recommended_skills = ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode', 'Objective-C', 'SQLite', 'Plist', 'StoreKit', 'UI-Kit', 'AV Foundation', 'Auto-Layout']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='5')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(ios_course)
                        break

                    elif i.lower() in uiux_keyword:
                        reco_field = 'UI-UX Development'
                        st.success("** Our analysis says you are looking for UI-UX Development Jobs **")
                        recommended_skills = ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 'Prototyping', 'Wireframes', 'Storyframes', 'Adobe Photoshop', 'Editing', 'Illustrator', 'After Effects', 'Premier Pro', 'Indesign', 'Wireframe', 'Solid', 'Grasp', 'User Research']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='6')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(uiux_course)
                        break

                    elif i.lower() in n_any:
                        reco_field = 'NA'
                        st.warning("** Currently our tool only predicts and recommends for Data Science, Web, Android, IOS and UI/UX Development**")
                        recommended_skills = ['No Recommendations']
                        st_tags(label='### Recommended skills for you.', text='Currently No Recommendations', value=recommended_skills, key='7')
                        st.markdown('''<h5 style='text-align: left; color: #092851;'>Maybe Available in Future Updates</h5>''', unsafe_allow_html=True)
                        rec_course = "Sorry! Not Available for this Field"
                        break

                ## ResumeIQ Executive ATS Dashboard & Scoring Engine
                st.markdown("""
                    <style>
                        .stTabs [data-baseweb="tab-list"] {
                            gap: 12px;
                        }
                        .stTabs [data-baseweb="tab"] {
                            height: 45px;
                            white-space: pre-wrap;
                            background-color: #f8f9fa;
                            border-radius: 8px;
                            color: #333;
                            font-weight: 600;
                            padding: 0 20px;
                        }
                        .stTabs [aria-selected="true"] {
                            background-color: #021659 !important;
                            color: white !important;
                        }
                    </style>
                """, unsafe_allow_html=True)

                resume_score = 0
                resume_text_lower = resume_text.lower()
                strengths = []
                improvements = []
                score_breakdown = {}

                
            if resume_data:
                resume_text = pdf_reader(save_image_path)

                st.header("**Resume Analysis 🤘**")
                st.success("Hello " + str(resume_data.get('name', '')))
                st.subheader("**Your Basic info 👀**")
                try:
                    st.text('Name: ' + str(resume_data.get('name', '')))
                    st.text('Email: ' + str(resume_data.get('email', '')))
                    st.text('Contact: ' + str(resume_data.get('mobile_number', '')))
                    st.text('Degree: ' + str(resume_data.get('degree', '')))
                    st.text('Resume pages: ' + str(resume_data.get('no_of_pages', 1)))
                except Exception:
                    pass

                cand_level = ''
                if resume_data.get('no_of_pages', 1) < 1:
                    cand_level = "NA"
                    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>You are at Fresher level!</h4>''', unsafe_allow_html=True)
                elif any(w in resume_text for w in ['INTERNSHIP', 'INTERNSHIPS', 'Internship', 'Internships']):
                    cand_level = "Intermediate"
                    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>You are at intermediate level!</h4>''', unsafe_allow_html=True)
                elif any(w in resume_text for w in ['EXPERIENCE', 'WORK EXPERIENCE', 'Experience', 'Work Experience']):
                    cand_level = "Experienced"
                    st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at experience level!</h4>''', unsafe_allow_html=True)
                else:
                    cand_level = "Fresher"
                    st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at Fresher level!!</h4>''', unsafe_allow_html=True)

                st.subheader("**Skills Recommendation 💡**")
                keywords = st_tags(
                    label='### Your Current Skills',
                    text='See our skills recommendation below',
                    value=resume_data.get('skills', []),
                    key='1'
                )

                ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning', 'flask', 'streamlit']
                web_keyword = ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento', 'wordpress', 'javascript', 'angular js', 'c#', 'asp.net', 'flask']
                android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
                ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
                uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes', 'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator', 'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro', 'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp', 'user research', 'user experience']
                n_any = ['english', 'communication', 'writing', 'microsoft office', 'leadership', 'customer management', 'social media']

                recommended_skills = []
                reco_field = ''
                rec_course = ''

                for i in resume_data.get('skills', []):
                    if i.lower() in ds_keyword:
                        reco_field = 'Data Science'
                        st.success("** Our analysis says you are looking for Data Science Jobs.**")
                        recommended_skills = ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 'Data Mining', 'Clustering & Classification', 'Data Analytics', 'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras', 'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', 'Flask', 'Streamlit']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='2')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(ds_course)
                        break

                    elif i.lower() in web_keyword:
                        reco_field = 'Web Development'
                        st.success("** Our analysis says you are looking for Web Development Jobs **")
                        recommended_skills = ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel', 'Magento', 'wordpress', 'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='3')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(web_course)
                        break

                    elif i.lower() in android_keyword:
                        reco_field = 'Android Development'
                        st.success("** Our analysis says you are looking for Android App Development Jobs **")
                        recommended_skills = ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java', 'Kivy', 'GIT', 'SDK', 'SQLite']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='4')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(android_course)
                        break

                    elif i.lower() in ios_keyword:
                        reco_field = 'IOS Development'
                        st.success("** Our analysis says you are looking for IOS App Development Jobs **")
                        recommended_skills = ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode', 'Objective-C', 'SQLite', 'Plist', 'StoreKit', 'UI-Kit', 'AV Foundation', 'Auto-Layout']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='5')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(ios_course)
                        break

                    elif i.lower() in uiux_keyword:
                        reco_field = 'UI-UX Development'
                        st.success("** Our analysis says you are looking for UI-UX Development Jobs **")
                        recommended_skills = ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 'Prototyping', 'Wireframes', 'Storyframes', 'Adobe Photoshop', 'Editing', 'Illustrator', 'After Effects', 'Premier Pro', 'Indesign', 'Wireframe', 'Solid', 'Grasp', 'User Research']
                        st_tags(label='### Recommended skills for you.', text='Recommended skills generated from System', value=recommended_skills, key='6')
                        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h5>''', unsafe_allow_html=True)
                        rec_course = course_recommender(uiux_course)
                        break

                    elif i.lower() in n_any:
                        reco_field = 'NA'
                        st.warning("** Currently our tool only predicts and recommends for Data Science, Web, Android, IOS and UI/UX Development**")
                        recommended_skills = ['No Recommendations']
                        st_tags(label='### Recommended skills for you.', text='Currently No Recommendations', value=recommended_skills, key='7')
                        st.markdown('''<h5 style='text-align: left; color: #092851;'>Maybe Available in Future Updates</h5>''', unsafe_allow_html=True)
                        rec_course = "Sorry! Not Available for this Field"
                        break

                ## ResumeIQ Executive ATS Dashboard & Scoring Engine
                st.markdown("""
                    <style>
                        .stTabs [data-baseweb="tab-list"] {
                            gap: 12px;
                        }
                        .stTabs [data-baseweb="tab"] {
                            height: 45px;
                            white-space: pre-wrap;
                            background-color: #f8f9fa;
                            border-radius: 8px;
                            color: #333;
                            font-weight: 600;
                            padding: 0 20px;
                        }
                        .stTabs [aria-selected="true"] {
                            background-color: #021659 !important;
                            color: white !important;
                        }
                    </style>
                """, unsafe_allow_html=True)

                resume_score = 0
                resume_text_lower = resume_text.lower()
                strengths = []
                improvements = []
                score_breakdown = {}

                # 1. Summary / Objective (10 pts)
                if any(k in resume_text_lower for k in ['objective', 'summary', 'profile', 'about me']):
                    s_pts = 10
                    strengths.append("Professional Summary / Objective included (+10/10)")
                else:
                    s_pts = 0
                    improvements.append("Add a clear Professional Summary or Career Objective (+10 pts)")
                resume_score += s_pts
                score_breakdown['Summary (10)'] = s_pts

                # 2. Education (10 pts)
                if any(k in resume_text_lower for k in ['education', 'b.tech', 'bachelor', 'university', 'college', 'degree', 'cgpa', 'gpa', 'school']):
                    e_pts = 10
                    strengths.append("Education qualifications clearly stated (+10/10)")
                else:
                    e_pts = 0
                    improvements.append("Add your Education details, degree, and CGPA/percentage (+10 pts)")
                resume_score += e_pts
                score_breakdown['Education (10)'] = e_pts

                # 3. Skills (15 pts)
                extracted_skills = resume_data.get('skills', []) if resume_data.get('skills') else []
                skill_count = len(extracted_skills)
                if skill_count >= 8:
                    sk_pts = 15
                    strengths.append(f"Strong technical skill set ({skill_count} skills detected) (+15/15)")
                elif skill_count >= 4:
                    sk_pts = 10
                    strengths.append(f"Moderate skill set ({skill_count} skills detected) (+10/15)")
                    improvements.append("Add more domain-relevant technical skills (8+ skills for full 15 pts)")
                elif skill_count >= 1 or 'skill' in resume_text_lower:
                    sk_pts = 5
                    improvements.append("Expand your Skills section with more specific tools (+10 more pts available)")
                else:
                    sk_pts = 0
                    improvements.append("Add a dedicated Technical Skills section (+15 pts)")
                resume_score += sk_pts
                score_breakdown['Skills (15)'] = sk_pts

                # 4. Experience / Internships (20 pts)
                if any(k in resume_text_lower for k in ['experience', 'work experience', 'internship', 'internships', 'intern', 'employment', 'work history']):
                    ex_pts = 20
                    strengths.append("Work Experience / Internships included (+20/20)")
                else:
                    ex_pts = 0
                    improvements.append("Add Internships, Work Experience, or Industrial Training (+20 pts)")
                resume_score += ex_pts
                score_breakdown['Experience (20)'] = ex_pts

                # 5. Projects (20 pts)
                if any(k in resume_text_lower for k in ['projects', 'project', 'personal projects', 'academic projects']):
                    p_pts = 20
                    strengths.append("Hands-on Projects showcased (+20/20)")
                else:
                    p_pts = 0
                    improvements.append("Add Academic or Personal Projects with tech stack details (+20 pts)")
                resume_score += p_pts
                score_breakdown['Projects (20)'] = p_pts

                # 6. Certifications (10 pts)
                if any(k in resume_text_lower for k in ['certifications', 'certification', 'certificates', 'certificate', 'nptel', 'coursera', 'udemy']):
                    c_pts = 10
                    strengths.append("Certifications included (+10/10)")
                else:
                    c_pts = 0
                    improvements.append("Add relevant Certifications or online courses (+10 pts)")
                resume_score += c_pts
                score_breakdown['Certifications (10)'] = c_pts

                # 7. Achievements (10 pts)
                if any(k in resume_text_lower for k in ['achievements', 'achievement', 'awards', 'award', 'honors', 'hackathon', 'winner', 'rank']):
                    a_pts = 10
                    strengths.append("Achievements / Awards highlighted (+10/10)")
                else:
                    a_pts = 0
                    improvements.append("Add Achievements, hackathons, or academic/sports awards (+10 pts)")
                resume_score += a_pts
                score_breakdown['Achievements (10)'] = a_pts

                # 8. Resume Length (5 pts)
                num_pages = resume_data.get('no_of_pages', 1)
                if num_pages in [1, 2]:
                    l_pts = 5
                    strengths.append(f"Optimal resume length ({num_pages} page(s)) (+5/5)")
                else:
                    l_pts = 3
                    improvements.append(f"Keep resume concise (currently {num_pages} pages; 1-2 pages is ideal)")
                resume_score += l_pts
                score_breakdown['Length (5)'] = l_pts

                if resume_score >= 85:
                    rating = "Excellent 🌟"
                    bar_color = "#1ed760"
                elif resume_score >= 70:
                    rating = "Good 👍"
                    bar_color = "#2ecc71"
                elif resume_score >= 50:
                    rating = "Average ⚠️"
                    bar_color = "#f39c12"
                else:
                    rating = "Needs Improvement 🔧"
                    bar_color = "#e74c3c"

                st.markdown("---")
                st.subheader("**ResumeIQ Executive ATS Dashboard 🚀**")

                m1, m2, m3, m4 = st.columns(4)
                m1.metric("ATS Score", f"{resume_score}/100", rating)
                m2.metric("Detected Skills", f"{skill_count} Items")
                m3.metric("Experience Level", cand_level)
                m4.metric("Resume Length", f"{num_pages} Page(s)")

                tab1, tab2, tab3 = st.tabs(["📊 Score & Rubric Analysis", "🎯 JD Matcher & Impact Audit", "🚀 Interview Prep & Roadmap"])

                with tab1:
                    c1, c2 = st.columns(2)
                    with c1:
                        fig_gauge = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=resume_score,
                            domain={'x': [0, 1], 'y': [0, 1]},
                            title={'text': "Overall Profile Health", 'font': {'size': 16}},
                            gauge={
                                'axis': {'range': [0, 100], 'tickwidth': 1},
                                'bar': {'color': bar_color},
                                'steps': [
                                    {'range': [0, 50], 'color': '#fadbd8'},
                                    {'range': [50, 70], 'color': '#fdebd0'},
                                    {'range': [70, 85], 'color': '#d5f5e3'},
                                    {'range': [85, 100], 'color': '#abebc6'}
                                ],
                            }
                        ))
                        fig_gauge.update_layout(height=280, margin=dict(l=20, r=20, t=40, b=10))
                        st.plotly_chart(fig_gauge, use_container_width=True)

                    with c2:
                        bd_df = pd.DataFrame({
                            'Category': list(score_breakdown.keys()),
                            'Points': list(score_breakdown.values())
                        })
                        fig_bar = px.bar(bd_df, x='Points', y='Category', orientation='h', text='Points', title="Rubric Points Breakdown", color='Points', color_continuous_scale='Blues')
                        fig_bar.update_layout(height=280, margin=dict(l=10, r=10, t=40, b=10), coloraxis_showscale=False)
                        st.plotly_chart(fig_bar, use_container_width=True)

                    st.markdown("#### Detailed Action Items")
                    col_s, col_i = st.columns(2)
                    with col_s:
                        st.markdown("##### ✅ Strengths")
                        for s in strengths:
                            st.write(f"• {s}")
                    with col_i:
                        st.markdown("##### 🎯 Areas to Improve")
                        if improvements:
                            for imp in improvements:
                                st.write(f"• {imp}")
                        else:
                            st.write("All criteria met successfully!")

                with tab2:
                    st.markdown("#### 🎯 Target Job Description (JD) Matcher & Skill Gap Analysis")
                    target_jd = st.text_area("Paste target job description here to check keyword match:", placeholder="Paste job requirements, tech stack, and responsibilities...")
                    
                    if target_jd:
                        jd_lower = target_jd.lower()
                        matched_keywords = [word for word in extracted_skills if word.lower() in jd_lower]
                        missing_keywords = [word for word in extracted_skills if word.lower() not in jd_lower]
                        match_pct = int((len(matched_keywords) / max(len(extracted_skills), 1)) * 100)
                        
                        st.metric("Job Description Compatibility", f"{match_pct}%", "ATS Keyword Overlap")
                        
                        col_m1, col_m2 = st.columns(2)
                        with col_m1:
                            st.markdown("##### ✅ Matched Keywords")
                            if matched_keywords:
                                for mk in matched_keywords:
                                    st.write(f"• `{mk}`")
                            else:
                                st.write("No direct skill keywords matched.")
                        with col_m2:
                            st.markdown("##### ⚠️ Missing / Suggested Keywords")
                            if missing_keywords:
                                for mik in missing_keywords:
                                    st.write(f"• `{mik}`")
                            else:
                                st.write("All extracted skills match the job description!")
                    else:
                        st.caption("Paste a job description above to evaluate keyword overlap and identify skill gaps instantly.")

                with tab3:
                    st.markdown("#### 🚀 AI Interview Prep & Career Roadmap")
                    
                    col_r1, col_r2 = st.columns(2)
                    with col_r1:
                        st.markdown("##### 💡 Technical Interview Focus Areas")
                        if reco_field == 'Data Science':
                            st.write("• Prepare for questions on **Machine Learning algorithms**, overfitting, regularization, and SQL joins.")
                            st.write("• Be ready to explain your model evaluation metrics (Precision, Recall, F1-Score).")
                        elif reco_field == 'Web Development':
                            st.write("• Brush up on **RESTful APIs**, state management, asynchronous JavaScript, and database indexing.")
                            st.write("• Prepare system design concepts for scalable web architectures.")
                        else:
                            st.write("• Focus on core computer science fundamentals: **Data Structures & Algorithms** and system design.")
                            st.write("• Review past project architectural decisions and code optimizations.")
                            
                    with col_r2:
                        st.markdown("##### 📈 Strategic Growth Roadmap")
                        st.write(f"• **Target Domain:** {reco_field if reco_field else 'Software Engineering'}")
                        st.write(f"• **Experience Tier:** {cand_level}")
                        st.write("• **Action Plan:** Add quantifiable impact metrics (e.g., 'Reduced latency by 30%') to your project bullet points.")
                        
                    st.markdown("---")
                    st.markdown("##### ❓ Sample Evaluator / Technical Viva Questions")
                    st.info("1. *'Can you walk through the most complex bug you solved in your featured project?'*\n2. *'How does your resume layout ensure fast parsing by Applicant Tracking Systems (ATS)?'*")

                st.warning("** Note: This evaluation is generated locally using the ResumeIQ ATS audit engine. **")

                ts = time.time()
                cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                timestamp = str(cur_date + '_' + cur_time)

                insert_data(
                    str(sec_token), str(ip_add), host_name, dev_user, os_name_ver,
                    latlong, city, state, country, act_name, act_mail, act_mob,
                    resume_data.get('name', ''), resume_data.get('email', ''),
                    str(resume_score), timestamp, str(resume_data.get('no_of_pages', 1)),
                    reco_field, cand_level, str(resume_data.get('skills', [])),
                    str(recommended_skills), str(rec_course), pdf_name
                )

                st.balloons()

    ###### CODE FOR FEEDBACK SIDE ######
    elif choice == 'Feedback':
        ts = time.time()
        cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        timestamp = str(cur_date + '_' + cur_time)

        with st.form("my_form"):
            st.write("Feedback form")
            feed_name = st.text_input('Name')
            feed_email = st.text_input('Email')
            feed_score = st.slider('Rate Us From 1 - 5', 1, 5)
            comments = st.text_input('Comments')
            Timestamp = timestamp
            submitted = st.form_submit_button("Submit")
            if submitted:
                insertf_data(feed_name, feed_email, feed_score, comments, Timestamp)
                st.success("Thanks! Your Feedback was recorded.")
                st.balloons()

        query = 'SELECT * FROM user_feedback'
        plotfeed_data = pd.read_sql(query, connection)

        if not plotfeed_data.empty:
            labels = plotfeed_data.feed_score.unique()
            values = plotfeed_data.feed_score.value_counts()

            st.subheader("**Past User Rating's**")
            fig = px.pie(values=values, names=labels, title="Chart of User Rating Score From 1 - 5", color_discrete_sequence=px.colors.sequential.Aggrnyl)
            st.plotly_chart(fig)

            cursor.execute('SELECT feed_name, comments FROM user_feedback')
            plfeed_cmt_data = cursor.fetchall()

            st.subheader("**User Comment's**")
            dff = pd.DataFrame(plfeed_cmt_data, columns=['User', 'Comment'])
            st.dataframe(dff, width=1000)
        else:
            st.info("No feedback submitted yet.")

    ###### CODE FOR ABOUT PAGE ######
    elif choice == 'About':
        st.subheader("**About ResumeIQ**")
        st.markdown('''
        <p align='justify'>
            ResumeIQ is an AI-powered resume analysis system designed to help students
            and job seekers understand and improve their resumes. It extracts important
            information and skills from uploaded resumes using Natural Language Processing,
            analyzes the candidate's profile, and provides relevant recommendations and
            insights based on the extracted information.
        </p>

        <p align="justify">
            <b>How to use it: -</b> <br/><br/>
            <b>User -</b> <br/>
            In the Side Bar choose yourself as user and fill the required fields and upload your resume in pdf format.<br/>
            Just sit back and relax our tool will do the magic on it's own.<br/><br/>
            <b>Feedback -</b> <br/>
            A place where user can suggest some feedback about the tool.<br/><br/>
            <b>Admin -</b> <br/>
            For login use your admin username and password.<br/>
            It will load all the required stuffs and perform analysis.
        </p><br/><br/>

        <p align="justify">
            Built with 🤍 as a College Project by <b>Himanshu Raj</b><br/>
            Department of Computer Science & Engineering<br/>
            LNJPIT Chhapra
        </p>
        ''', unsafe_allow_html=True)

    ###### CODE FOR ADMIN SIDE (ADMIN) ######
    else:
        st.success('Welcome to Admin Side')

        ad_user = st.text_input("Username")
        ad_password = st.text_input("Password", type='password')

        if st.button('Login'):
            if ad_user == 'himanshuraj21' and ad_password == '851118':
                cursor.execute('''SELECT ID, ip_add, resume_score, convert(Predicted_Field using utf8), convert(User_level using utf8), city, state, country from user_data''')
                datanalys = cursor.fetchall()
                plot_data = pd.DataFrame(datanalys, columns=['Idt', 'IP_add', 'resume_score', 'Predicted_Field', 'User_Level', 'City', 'State', 'Country'])

                values = plot_data.Idt.count()
                st.success("Welcome Himanshu Raj ! Total %d " % values + " User's Have Used Our Tool : )")

                cursor.execute('''SELECT ID, sec_token, ip_add, act_name, act_mail, act_mob, convert(Predicted_Field using utf8), Timestamp, Name, Email_ID, resume_score, Page_no, pdf_name, convert(User_level using utf8), convert(Actual_skills using utf8), convert(Recommended_skills using utf8), convert(Recommended_courses using utf8), city, state, country, latlong, os_name_ver, host_name, dev_user from user_data''')
                data = cursor.fetchall()

                st.header("**User's Data**")
                df = pd.DataFrame(data, columns=[
                    'ID', 'Token', 'IP Address', 'Name', 'Mail', 'Mobile Number', 'Predicted Field', 'Timestamp',
                    'Predicted Name', 'Predicted Mail', 'Resume Score', 'Total Page', 'File Name',
                    'User Level', 'Actual Skills', 'Recommended Skills', 'Recommended Course',
                    'City', 'State', 'Country', 'Lat Long', 'Server OS', 'Server Name', 'Server User'
                ])
                st.dataframe(df)
                st.markdown(get_csv_download_link(df, 'User_Data.csv', 'Download Report'), unsafe_allow_html=True)

                cursor.execute('''SELECT * from user_feedback''')
                data = cursor.fetchall()

                st.header("**User's Feedback Data**")
                df_feed = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'Feedback Score', 'Comments', 'Timestamp'])
                st.dataframe(df_feed)

                query = 'select * from user_feedback'
                plotfeed_data = pd.read_sql(query, connection)

                if not plotfeed_data.empty:
                    labels = plotfeed_data.feed_score.unique()
                    values = plotfeed_data.feed_score.value_counts()
                    st.subheader("**User Rating's**")
                    fig = px.pie(values=values, names=labels, title="Chart of User Rating Score From 1 - 5 🤗", color_discrete_sequence=px.colors.sequential.Aggrnyl)
                    st.plotly_chart(fig)

                if not plot_data.empty:
                    labels = plot_data.Predicted_Field.unique()
                    values = plot_data.Predicted_Field.value_counts()
                    st.subheader("**Pie-Chart for Predicted Field Recommendation**")
                    fig = px.pie(df, values=values, names=labels, title='Predicted Field according to the Skills 👽', color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
                    st.plotly_chart(fig)

                    labels = plot_data.User_Level.unique()
                    values = plot_data.User_Level.value_counts()
                    st.subheader("**Pie-Chart for User's Experienced Level**")
                    fig = px.pie(df, values=values, names=labels, title="Pie-Chart 📈 for User's 👨‍💻 Experienced Level", color_discrete_sequence=px.colors.sequential.RdBu)
                    st.plotly_chart(fig)

                    labels = plot_data.resume_score.unique()
                    values = plot_data.resume_score.value_counts()
                    st.subheader("**Pie-Chart for Resume Score**")
                    fig = px.pie(df, values=values, names=labels, title='From 1 to 100 💯', color_discrete_sequence=px.colors.sequential.Agsunset)
                    st.plotly_chart(fig)

                    labels = plot_data.IP_add.unique()
                    values = plot_data.IP_add.value_counts()
                    st.subheader("**Pie-Chart for Users App Used Count**")
                    fig = px.pie(df, values=values, names=labels, title='Usage Based On IP Address 👥', color_discrete_sequence=px.colors.sequential.matter_r)
                    st.plotly_chart(fig)

                    labels = plot_data.City.unique()
                    values = plot_data.City.value_counts()
                    st.subheader("**Pie-Chart for City**")
                    fig = px.pie(df, values=values, names=labels, title='Usage Based On City 🌆', color_discrete_sequence=px.colors.sequential.Jet)
                    st.plotly_chart(fig)

                    labels = plot_data.State.unique()
                    values = plot_data.State.value_counts()
                    st.subheader("**Pie-Chart for State**")
                    fig = px.pie(df, values=values, names=labels, title='Usage Based on State 🚉', color_discrete_sequence=px.colors.sequential.PuBu_r)
                    st.plotly_chart(fig)

                    labels = plot_data.Country.unique()
                    values = plot_data.Country.value_counts()
                    st.subheader("**Pie-Chart for Country**")
                    fig = px.pie(df, values=values, names=labels, title='Usage Based on Country 🌏', color_discrete_sequence=px.colors.sequential.Purpor_r)
                    st.plotly_chart(fig)
            else:
                st.error("Wrong ID & Password Provided")


run()