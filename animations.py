import streamlit as st

def load_futuristic_animations():
    """Injects futuristic CSS animations, glowing neon borders, and smooth hover transitions."""
    st.markdown("""
    <style>
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 5px rgba(0, 173, 181, 0.2); }
            50% { box-shadow: 0 0 20px rgba(0, 173, 181, 0.6); }
            100% { box-shadow: 0 0 5px rgba(0, 173, 181, 0.2); }
        }

        .futuristic-card {
            background: rgba(22, 27, 34, 0.7);
            border: 1px solid rgba(0, 173, 181, 0.3);
            padding: 24px;
            border-radius: 16px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
            animation: pulseGlow 4s infinite;
        }

        .futuristic-card:hover {
            border-color: #00adb5;
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 173, 181, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

def render_futuristic_header(title="RESUMEIQ // AI NEURAL CORE"):
    """Renders a cyberpunk / futuristic header component."""
    st.markdown(f"""
        <div style="border-left: 4px solid #00adb5; padding-left: 14px; margin-bottom: 20px;">
            <h2 style="color: #f0f2f6; font-family: monospace; letter-spacing: 2px; margin: 0;">{title}</h2>
            <p style="color: #00adb5; font-family: monospace; font-size: 13px; margin: 0;">STATUS: ONLINE // SECURE PROTOCOL ACTIVE</p>
        </div>
    """, unsafe_allow_html=True)