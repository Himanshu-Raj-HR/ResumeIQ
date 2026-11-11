import streamlit as st

def load_futuristic_animations():
    """Injects futuristic CSS animations, neon borders, and scanning effects."""
    st.markdown("""
    <style>
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 5px rgba(0, 173, 181, 0.2); }
            50% { box-shadow: 0 0 20px rgba(0, 173, 181, 0.6); }
            100% { box-shadow: 0 0 5px rgba(0, 173, 181, 0.2); }
        }

        @keyframes scanline {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(1000%); }
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
            position: relative;
            overflow: hidden;
        }

        .futuristic-card:hover {
            border-color: #00adb5;
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 173, 181, 0.4);
        }

        /* Blinking Live Neural Status Dot */
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
            0% { opacity: 0.2; }
            50% { opacity: 1; }
            100% { opacity: 0.2; }
        }
    </style>
    """, unsafe_allow_html=True)

def render_futuristic_header(title="RESUMEIQ // AI NEURAL CORE"):
    """Renders a cyberpunk / futuristic header component with a live status indicator."""
    st.markdown(f"""
        <div style="border-left: 4px solid #00adb5; padding-left: 14px; margin-bottom: 20px; background: rgba(0,173,181,0.05); padding: 12px 16px; border-radius: 0 12px 12px 0;">
            <h2 style="color: #f0f2f6; font-family: monospace; letter-spacing: 2px; margin: 0;">{title}</h2>
            <p style="color: #00adb5; font-family: monospace; font-size: 13px; margin: 4px 0 0 0; display: flex; align-items: center;">
                <span class="live-dot"></span>SYS_STATUS: ONLINE // SECURE PROTOCOL ACTIVE
            </p>
        </div>
    """, unsafe_allow_html=True)