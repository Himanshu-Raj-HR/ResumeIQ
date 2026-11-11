import streamlit as st
import streamlit.components.v1 as components

def load_futuristic_animations():
    """Injects global glassmorphism, interactive hover physics, cursor tracking, and background neural graphs."""
    
    # 1. GLOBAL CSS: Glassmorphism + Universal Hover Animations
    st.markdown("""
    <style>
        /* App Background with subtle cyber grid */
        .stApp {
            background-color: #07090e !important;
            background-image: 
                radial-gradient(circle at 50% 10%, rgba(0, 173, 181, 0.12), transparent 60%),
                linear-gradient(rgba(0, 173, 181, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 173, 181, 0.03) 1px, transparent 1px) !important;
            background-size: 100% 100%, 40px 40px, 40px 40px !important;
            color: #f0f2f6 !important;
        }

        /* Transparent Glass Effect on Sidebar */
        [data-testid="stSidebar"] {
            background: rgba(12, 16, 23, 0.55) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border-right: 1px solid rgba(0, 245, 212, 0.18) !important;
        }

        /* Glass Effect & Cursor Hover Animation on Cards, Metrics, Expanders, Uploads */
        [data-testid="stMetric"], 
        [data-testid="stExpander"], 
        [data-testid="stFileUploader"],
        .stAlert,
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div {
            background: rgba(20, 26, 36, 0.45) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(0, 173, 181, 0.25) !important;
            border-radius: 14px !important;
            transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
        }

        /* Universal Hover Reaction when cursor touches any object */
        [data-testid="stMetric"]:hover, 
        [data-testid="stExpander"]:hover, 
        [data-testid="stFileUploader"]:hover,
        .stAlert:hover,
        div[data-baseweb="select"] > div:hover,
        div[data-baseweb="input"] > div:hover {
            transform: translateY(-5px) scale(1.015) !important;
            border-color: #00f5d4 !important;
            box-shadow: 0 10px 30px rgba(0, 245, 212, 0.25), inset 0 0 12px rgba(0, 173, 181, 0.12) !important;
        }

        /* Frosted Glass Effect on EVERY Button + Sweeping Shine Animation */
        .stButton > button, [data-testid="stDownloadButton"] > button {
            background: rgba(0, 173, 181, 0.12) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(0, 245, 212, 0.45) !important;
            color: #e0fbfc !important;
            border-radius: 12px !important;
            padding: 0.55rem 1.4rem !important;
            font-family: monospace !important;
            font-weight: 600 !important;
            letter-spacing: 1px !important;
            position: relative !important;
            overflow: hidden !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(0, 173, 181, 0.15) !important;
        }

        .stButton > button::before, [data-testid="stDownloadButton"] > button::before {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 245, 212, 0.35), transparent);
            transition: left 0.5s ease;
        }

        .stButton > button:hover::before, [data-testid="stDownloadButton"] > button:hover::before {
            left: 100%;
        }

        .stButton > button:hover, [data-testid="stDownloadButton"] > button:hover {
            background: rgba(0, 173, 181, 0.28) !important;
            border-color: #00f5d4 !important;
            color: #ffffff !important;
            transform: translateY(-3px) scale(1.04) !important;
            box-shadow: 0 0 25px rgba(0, 245, 212, 0.55) !important;
        }

        /* Blinking Live Status Dot */
        .live-dot {
            height: 10px;
            width: 10px;
            background-color: #39ff14;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 8px #39ff14;
            animation: blink 1.5s infinite;
            margin-right: 8px;
        }

        @keyframes blink {
            0%, 100% { opacity: 0.2; }
            50% { opacity: 1; }
        }

        /* Always-on Futuristic Telemetry Equalizer Graph */
        .telemetry-box {
            background: rgba(16, 22, 32, 0.45);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 245, 212, 0.25);
            border-radius: 12px;
            padding: 12px 18px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.3s ease;
        }
        .telemetry-box:hover {
            border-color: #00f5d4;
            box-shadow: 0 0 20px rgba(0, 245, 212, 0.25);
            transform: scale(1.01);
        }
        .eq-bars {
            display: flex;
            align-items: flex-end;
            gap: 4px;
            height: 28px;
        }
        .eq-bar {
            width: 5px;
            background: linear-gradient(to top, #00adb5, #00f5d4);
            border-radius: 3px;
            animation: equalize 1.2s ease-in-out infinite;
        }
        .telemetry-box:hover .eq-bar {
            animation-duration: 0.35s;
            background: linear-gradient(to top, #00f5d4, #39ff14);
        }
        @keyframes equalize {
            0%, 100% { height: 20%; }
            50% { height: 100%; }
        }
    </style>
    """, unsafe_allow_html=True)

    # 2. JAVASCRIPT: Interactive Cursor Spotlight + Mouse-Sensitive Neural Network Graph
    components.html("""
    <script>
    (function() {
        const parentDoc = window.parent.document;
        if (parentDoc.getElementById('cyber-neural-canvas')) return;

        // Interactive neural network canvas in background
        const canvas = parentDoc.createElement('canvas');
        canvas.id = 'cyber-neural-canvas';
        canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;opacity:0.55;';
        parentDoc.body.appendChild(canvas);

        // Glowing spotlight aura attached to cursor movement
        const glow = parentDoc.createElement('div');
        glow.id = 'cyber-cursor-glow';
        glow.style.cssText = 'position:fixed;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle, rgba(0,245,212,0.13) 0%, rgba(0,173,181,0.04) 45%, transparent 70%);pointer-events:none;z-index:1;transform:translate(-50%,-50%);transition:width 0.2s, height 0.2s;';
        parentDoc.body.appendChild(glow);

        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.parent.innerWidth;
        let height = canvas.height = window.parent.innerHeight;

        window.parent.addEventListener('resize', () => {
            width = canvas.width = window.parent.innerWidth;
            height = canvas.height = window.parent.innerHeight;
        });

        let mouse = { x: width / 2, y: height / 2 };
        parentDoc.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
            glow.style.left = e.clientX + 'px';
            glow.style.top = e.clientY + 'px';
        });

        // Create floating graph nodes
        const nodes = Array.from({length: 50}, () => ({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.8,
            vy: (Math.random() - 0.5) * 0.8,
            r: Math.random() * 2 + 1
        }));

        function animate() {
            ctx.clearRect(0, 0, width, height);
            for (let i = 0; i < nodes.length; i++) {
                let n = nodes[i];
                n.x += n.vx;
                n.y += n.vy;

                if (n.x < 0 || n.x > width) n.vx *= -1;
                if (n.y < 0 || n.y > height) n.vy *= -1;

                // Draw node
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                ctx.fillStyle = '#00f5d4';
                ctx.fill();

                // Connect to cursor if close (interactive movement sensitivity)
                let dxMouse = mouse.x - n.x;
                let dyMouse = mouse.y - n.y;
                let distMouse = Math.hypot(dxMouse, dyMouse);
                if (distMouse < 170) {
                    ctx.beginPath();
                    ctx.moveTo(n.x, n.y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = `rgba(0, 245, 212, ${1 - distMouse / 170})`;
                    ctx.lineWidth = 1.2;
                    ctx.stroke();
                }

                // Connect nearby nodes into a live graph mesh
                for (let j = i + 1; j < nodes.length; j++) {
                    let n2 = nodes[j];
                    let dist = Math.hypot(n.x - n2.x, n.y - n2.y);
                    if (dist < 110) {
                        ctx.beginPath();
                        ctx.moveTo(n.x, n.y);
                        ctx.lineTo(n2.x, n2.y);
                        ctx.strokeStyle = `rgba(0, 173, 181, ${(1 - dist / 110) * 0.35})`;
                        ctx.lineWidth = 0.7;
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animate);
        }
        animate();
    })();
    </script>
    """, height=0)


def render_futuristic_header(title="RESUMEIQ // AI NEURAL CORE"):
    """Renders a cyberpunk glass header along with an always-playing reactive telemetry graph."""
    bars_html = "".join(
        [f'<div class="eq-bar" style="animation-delay: {(i * 0.1) % 0.9:.1f}s;"></div>' for i in range(18)]
    )
    st.markdown(f"""
        <div class="telemetry-box">
            <div style="border-left: 4px solid #00f5d4; padding-left: 14px;">
                <h2 style="color: #f0f2f6; font-family: monospace; letter-spacing: 2px; margin: 0; font-size: 1.5rem;">{title}</h2>
                <p style="color: #00f5d4; font-family: monospace; font-size: 12px; margin: 4px 0 0 0; display: flex; align-items: center;">
                    <span class="live-dot"></span>SYS_STATUS: ONLINE // NEURAL GRAPH ACTIVE
                </p>
            </div>
            <div style="text-align: right;">
                <div class="eq-bars">{bars_html}</div>
                <span style="font-family: monospace; font-size: 10px; color: #00adb5;">LIVE TELEMETRY // HOVER TO BOOST</span>
            </div>
        </div>
    """, unsafe_allow_html=True)