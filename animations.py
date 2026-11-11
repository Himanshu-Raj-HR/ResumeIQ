import streamlit as st
import streamlit.components.v1 as components

def load_futuristic_animations():
    """Injects sci-fi typography, angled cyber buttons, staggered skill animations, and scroll-reveal physics."""
    
    # 1. GLOBAL SCI-FI FONTS, CYBER BUTTONS & SCROLL ANIMATION CSS
    st.markdown("""
    <style>
        /* Import Futuristic Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@500;600;700&display=swap');

        /* Global App Background & Base Typography */
        .stApp {
            background-color: #05070b !important;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(0, 245, 212, 0.14), transparent 55%),
                radial-gradient(circle at 85% 80%, rgba(0, 173, 181, 0.1), transparent 50%),
                linear-gradient(rgba(0, 245, 212, 0.025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 245, 212, 0.025) 1px, transparent 1px) !important;
            background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 18px !important;
            color: #e6f1ff !important;
        }

        /* Futuristic Headers */
        h1, h2, h3, [data-testid="stSubheader"] {
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 2px !important;
            text-transform: uppercase !important;
            color: #ffffff !important;
            text-shadow: 0 0 18px rgba(0, 245, 212, 0.35) !important;
        }

        h2, [data-testid="stSubheader"] {
            font-size: 1.45rem !important;
            border-bottom: 1px solid rgba(0, 245, 212, 0.2);
            padding-bottom: 6px;
            margin-top: 18px !important;
        }

        p, li, label, .stMarkdown, .stText {
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.12rem !important;
            font-weight: 500 !important;
            letter-spacing: 0.4px !important;
        }

        /* Monospace Readouts for Code & Basic Info st.text */
        pre, code, .stText {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.96rem !important;
            color: #00f5d4 !important;
            background: rgba(10, 16, 26, 0.65) !important;
            border-left: 3px solid #00f5d4 !important;
            padding: 8px 14px !important;
            border-radius: 0 8px 8px 0 !important;
            margin-bottom: 6px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
        }

        /* Transparent Frosted Sidebar */
        [data-testid="stSidebar"] {
            background: rgba(8, 12, 20, 0.72) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(0, 245, 212, 0.22) !important;
        }

        /* =====================================================
           TOP-NOTCH FUTURISTIC CYBERPUNK BUTTONS
           ===================================================== */
        .stButton > button, 
        [data-testid="stDownloadButton"] > button,
        [data-testid="stFormSubmitButton"] > button {
            min-height: 54px !important;
            width: 100% !important;
            padding: 14px 30px !important;
            font-family: 'Orbitron', sans-serif !important;
            font-size: 15px !important;
            font-weight: 700 !important;
            letter-spacing: 2.5px !important;
            text-transform: uppercase !important;
            color: #00f5d4 !important;
            background: linear-gradient(135deg, rgba(0, 245, 212, 0.14) 0%, rgba(10, 18, 30, 0.88) 50%, rgba(0, 173, 181, 0.2) 100%) !important;
            border: 1.5px solid rgba(0, 245, 212, 0.65) !important;
            border-radius: 4px !important;
            /* Angled Sci-Fi Cut Corners */
            clip-path: polygon(14px 0%, 100% 0%, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0% 100%, 0% 14px) !important;
            box-shadow: 0 0 20px rgba(0, 245, 212, 0.18), inset 0 0 15px rgba(0, 245, 212, 0.08) !important;
            position: relative !important;
            overflow: hidden !important;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
            cursor: pointer !important;
        }

        /* Sweeping Laser Beam Inside Button */
        .stButton > button::before, 
        [data-testid="stDownloadButton"] > button::before,
        [data-testid="stFormSubmitButton"] > button::before {
            content: "" !important;
            position: absolute !important;
            top: 0 !important;
            left: -120% !important;
            width: 60% !important;
            height: 100% !important;
            background: linear-gradient(120deg, transparent, rgba(0, 245, 212, 0.6), rgba(255, 255, 255, 0.8), rgba(0, 245, 212, 0.6), transparent) !important;
            transform: skewX(-25deg) !important;
            transition: left 0.65s ease !important;
        }

        .stButton > button:hover::before, 
        [data-testid="stDownloadButton"] > button:hover::before,
        [data-testid="stFormSubmitButton"] > button:hover::before {
            left: 140% !important;
        }

        /* Button Hover Energy Surge */
        .stButton > button:hover, 
        [data-testid="stDownloadButton"] > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
            color: #04080e !important;
            background: linear-gradient(135deg, #00f5d4 0%, #00bbff 100%) !important;
            border-color: #ffffff !important;
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 0 10px 35px rgba(0, 245, 212, 0.65), 0 0 15px #00f5d4 !important;
            letter-spacing: 3.5px !important;
        }

        /* Button Active Press Physics */
        .stButton > button:active, 
        [data-testid="stDownloadButton"] > button:active {
            transform: translateY(1px) scale(0.98) !important;
        }

        /* =====================================================
           ONE-BY-ONE STAGGERED SKILL TAGS & PILLS
           ===================================================== */
        @keyframes skillPopIn {
            0% {
                opacity: 0;
                transform: translateY(18px) scale(0.75);
                filter: blur(6px);
            }
            70% {
                transform: translateY(-3px) scale(1.04);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
                filter: blur(0);
            }
        }

        span[data-baseweb="tag"], .cyber-skill-tag {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 13.5px !important;
            font-weight: 600 !important;
            background: linear-gradient(135deg, rgba(0, 245, 212, 0.16), rgba(0, 173, 181, 0.08)) !important;
            border: 1px solid rgba(0, 245, 212, 0.55) !important;
            color: #e0fbfc !important;
            border-radius: 6px !important;
            padding: 6px 14px !important;
            margin: 5px !important;
            box-shadow: 0 0 14px rgba(0, 245, 212, 0.18) !important;
            animation: skillPopIn 0.55s cubic-bezier(0.22, 1, 0.36, 1) both !important;
            transition: all 0.25s ease !important;
        }

        span[data-baseweb="tag"]:hover {
            background: rgba(0, 245, 212, 0.32) !important;
            border-color: #39ff14 !important;
            color: #ffffff !important;
            transform: translateY(-4px) scale(1.08) !important;
            box-shadow: 0 0 22px rgba(57, 255, 20, 0.5) !important;
        }

        /* =====================================================
           GLASS CARDS, ALERTS, EXPANDERS & RECOMMENDATIONS
           ===================================================== */
        [data-testid="stMetric"], 
        [data-testid="stExpander"], 
        [data-testid="stFileUploader"],
        .stAlert,
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div {
            background: rgba(14, 21, 33, 0.55) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            border: 1px solid rgba(0, 245, 212, 0.28) !important;
            border-radius: 12px !important;
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1) !important;
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.35) !important;
        }

        [data-testid="stMetric"]:hover, 
        [data-testid="stExpander"]:hover, 
        [data-testid="stFileUploader"]:hover,
        .stAlert:hover {
            transform: translateY(-4px) scale(1.01) !important;
            border-color: #00f5d4 !important;
            box-shadow: 0 12px 32px rgba(0, 245, 212, 0.24), inset 0 0 14px rgba(0, 245, 212, 0.08) !important;
        }

        /* Futuristic Progress Bar (if Streamlit st.progress is used) */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #00adb5, #00f5d4, #39ff14) !important;
            background-size: 200% 100% !important;
            animation: progressPulse 2s linear infinite !important;
            box-shadow: 0 0 16px rgba(0, 245, 212, 0.7) !important;
        }

        @keyframes progressPulse {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }

        /* =====================================================
           SCROLL-REVEAL ANIMATION CLASSES
           ===================================================== */
        .cyber-scroll-hidden {
            opacity: 0;
            transform: translateY(28px) scale(0.98);
            filter: blur(4px);
            transition: opacity 0.65s cubic-bezier(0.22, 1, 0.36, 1), 
                        transform 0.65s cubic-bezier(0.22, 1, 0.36, 1),
                        filter 0.65s ease;
        }

        .cyber-scroll-visible {
            opacity: 1 !important;
            transform: translateY(0) scale(1) !important;
            filter: blur(0) !important;
        }

        /* Live Status Dot & Header Telemetry */
        .live-dot {
            height: 10px;
            width: 10px;
            background-color: #39ff14;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 10px #39ff14;
            animation: blink 1.4s infinite;
            margin-right: 8px;
        }
        @keyframes blink {
            0%, 100% { opacity: 0.25; }
            50% { opacity: 1; }
        }

        .telemetry-box {
            background: rgba(12, 18, 28, 0.6);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(0, 245, 212, 0.32);
            border-radius: 12px;
            padding: 14px 20px;
            margin-bottom: 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.3s ease;
        }
        .telemetry-box:hover {
            border-color: #00f5d4;
            box-shadow: 0 0 25px rgba(0, 245, 212, 0.28);
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
            animation: equalize 1.1s ease-in-out infinite;
        }
        .telemetry-box:hover .eq-bar {
            animation-duration: 0.3s;
            background: linear-gradient(to top, #00f5d4, #39ff14);
        }
        @keyframes equalize {
            0%, 100% { height: 20%; }
            50% { height: 100%; }
        }
    </style>
    """, unsafe_allow_html=True)

    # 2. JAVASCRIPT ENGINE: Background Neural Mesh + Scroll-Reveal + One-by-One Skill Cascade
    components.html("""
    <script>
    (function() {
        const parentDoc = window.parent.document;

        // --- A. BACKGROUND NEURAL PARTICLE MESH ---
        if (!parentDoc.getElementById('cyber-neural-canvas')) {
            const canvas = parentDoc.createElement('canvas');
            canvas.id = 'cyber-neural-canvas';
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;opacity:0.5;';
            parentDoc.body.appendChild(canvas);

            const glow = parentDoc.createElement('div');
            glow.id = 'cyber-cursor-glow';
            glow.style.cssText = 'position:fixed;width:380px;height:380px;border-radius:50%;background:radial-gradient(circle, rgba(0,245,212,0.14) 0%, rgba(0,173,181,0.04) 45%, transparent 70%);pointer-events:none;z-index:1;transform:translate(-50%,-50%);';
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

            const nodes = Array.from({length: 48}, () => ({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.75,
                vy: (Math.random() - 0.5) * 0.75,
                r: Math.random() * 2 + 1
            }));

            function animateMesh() {
                ctx.clearRect(0, 0, width, height);
                for (let i = 0; i < nodes.length; i++) {
                    let n = nodes[i];
                    n.x += n.vx;
                    n.y += n.vy;
                    if (n.x < 0 || n.x > width) n.vx *= -1;
                    if (n.y < 0 || n.y > height) n.vy *= -1;

                    ctx.beginPath();
                    ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                    ctx.fillStyle = '#00f5d4';
                    ctx.fill();

                    let distMouse = Math.hypot(mouse.x - n.x, mouse.y - n.y);
                    if (distMouse < 165) {
                        ctx.beginPath();
                        ctx.moveTo(n.x, n.y);
                        ctx.lineTo(mouse.x, mouse.y);
                        ctx.strokeStyle = `rgba(0, 245, 212, ${1 - distMouse / 165})`;
                        ctx.lineWidth = 1.1;
                        ctx.stroke();
                    }

                    for (let j = i + 1; j < nodes.length; j++) {
                        let n2 = nodes[j];
                        let dist = Math.hypot(n.x - n2.x, n.y - n2.y);
                        if (dist < 105) {
                            ctx.beginPath();
                            ctx.moveTo(n.x, n.y);
                            ctx.lineTo(n2.x, n2.y);
                            ctx.strokeStyle = `rgba(0, 173, 181, ${(1 - dist / 105) * 0.32})`;
                            ctx.lineWidth = 0.7;
                            ctx.stroke();
                        }
                    }
                }
                requestAnimationFrame(animateMesh);
            }
            animateMesh();
        }

        // --- B. SCROLL-REVEAL & STAGGERED SKILL CASCADE ENGINE ---
        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('cyber-scroll-visible');
                }
            });
        }, { threshold: 0.08 });

        function applyScrollAndSkillAnimations() {
            // 1. Animate blocks on scroll (headers, alerts, expanders, recommendations, text blocks)
            const blocks = parentDoc.querySelectorAll(
                '[data-testid="stVerticalBlock"] > div > div > [data-testid="stMarkdownContainer"], ' +
                '.stAlert, [data-testid="stExpander"], [data-testid="stMetric"], .stText'
            );
            blocks.forEach((el) => {
                if (!el.dataset.cyberScrollBound) {
                    el.dataset.cyberScrollBound = 'true';
                    el.classList.add('cyber-scroll-hidden');
                    scrollObserver.observe(el);
                }
            });

            // 2. Stagger skill tags (both main page & st_tags iframes) one-by-one
            const mainTags = parentDoc.querySelectorAll('span[data-baseweb="tag"]');
            mainTags.forEach((tag, idx) => {
                if (!tag.dataset.staggered) {
                    tag.dataset.staggered = 'true';
                    tag.style.animationDelay = `${idx * 0.09}s`;
                }
            });

            // Check inside st_tags component iframes so skills pop in one-by-one
            const iframes = parentDoc.querySelectorAll('iframe');
            iframes.forEach((frame) => {
                try {
                    const frameDoc = frame.contentDocument || frame.contentWindow.document;
                    if (!frameDoc) return;

                    if (!frameDoc.getElementById('cyber-tag-style')) {
                        const styleEl = frameDoc.createElement('style');
                        styleEl.id = 'cyber-tag-style';
                        styleEl.innerHTML = `
                            @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600&display=swap');
                            @keyframes tagCascade {
                                0% { opacity: 0; transform: translateY(15px) scale(0.7); filter: blur(4px); }
                                75% { transform: translateY(-3px) scale(1.05); }
                                100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
                            }
                            span, .ReactTags__tag {
                                font-family: 'JetBrains Mono', monospace !important;
                                background: linear-gradient(135deg, rgba(0, 245, 212, 0.22), rgba(10, 20, 34, 0.9)) !important;
                                border: 1px solid #00f5d4 !important;
                                color: #e0fbfc !important;
                                border-radius: 6px !important;
                                padding: 6px 13px !important;
                                margin: 5px !important;
                                display: inline-block !important;
                                box-shadow: 0 0 12px rgba(0, 245, 212, 0.28) !important;
                                animation: tagCascade 0.5s cubic-bezier(0.22, 1, 0.36, 1) both !important;
                                transition: all 0.25s ease !important;
                            }
                            span:hover, .ReactTags__tag:hover {
                                transform: translateY(-3px) scale(1.07) !important;
                                border-color: #39ff14 !important;
                                box-shadow: 0 0 20px rgba(57, 255, 20, 0.6) !important;
                            }
                        `;
                        frameDoc.head.appendChild(styleEl);
                    }

                    const innerTags = frameDoc.querySelectorAll('.ReactTags__tag, span');
                    innerTags.forEach((t, i) => {
                        if (!t.dataset.staggered) {
                            t.dataset.staggered = 'true';
                            t.style.animationDelay = `${i * 0.11}s`;
                        }
                    });
                } catch (e) {}
            });
        }

        applyScrollAndSkillAnimations();
        setInterval(applyScrollAndSkillAnimations, 700);
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
                <h2 style="color: #f0f2f6; font-family: 'Orbitron', sans-serif; letter-spacing: 2px; margin: 0; font-size: 1.45rem; border: none; padding: 0;">{title}</h2>
                <p style="color: #00f5d4; font-family: 'JetBrains Mono', monospace; font-size: 12px; margin: 4px 0 0 0; display: flex; align-items: center;">
                    <span class="live-dot"></span>SYS_STATUS: ONLINE // NEURAL TELEMETRY ACTIVE
                </p>
            </div>
            <div style="text-align: right;">
                <div class="eq-bars">{bars_html}</div>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #00adb5;">LIVE TELEMETRY // HOVER TO BOOST</span>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_interactive_hud_graph(score=85):
    """Renders an animated 0-to-score counter, spinning holographic radar ring, and continuous waveform HUD."""
    html_code = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Orbitron:wght@700;900&display=swap');
        
        @keyframes spinSlow {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @keyframes pulseRing {
            0%, 100% { filter: drop-shadow(0 0 6px #00f5d4); }
            50% { filter: drop-shadow(0 0 16px #39ff14); }
        }
    </style>

    <div id="hud-container" style="
        background: linear-gradient(135deg, rgba(12, 19, 31, 0.85), rgba(7, 11, 18, 0.92));
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 245, 212, 0.4);
        border-radius: 16px;
        padding: 18px 24px;
        color: #e0fbfc;
        font-family: 'JetBrains Mono', monospace;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(0, 245, 212, 0.05);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap;">
            
            <!-- Left: Title & Live Telemetry Wave Canvas -->
            <div style="flex: 1; min-width: 240px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                    <span style="color: #00f5d4; font-family: 'Orbitron', sans-serif; font-weight: 800; font-size: 15px; letter-spacing: 2px;">
                        ⚡ NEURAL ATS SCORE TELEMETRY
                    </span>
                    <span style="background: rgba(57, 255, 20, 0.15); border: 1px solid #39ff14; color: #39ff14; font-size: 10px; padding: 2px 8px; border-radius: 4px;">
                        LIVE STREAM
                    </span>
                </div>
                <div style="font-size: 11px; color: #8b949e; margin-bottom: 10px;">
                    HOVER & MOVE CURSOR ACROSS WAVEFORM TO AMPLIFY NEURAL HARMONICS
                </div>
                <canvas id="waveCanvas" height="115" style="width: 100%; display: block; cursor: crosshair;"></canvas>
            </div>

            <!-- Right: Animated 0-to-Score Circular Holographic Gauge -->
            <div style="position: relative; width: 135px; height: 135px; display: flex; align-items: center; justify-content: center;">
                <!-- Outer Rotating Dashed Cyber Ring -->
                <svg width="135" height="135" style="position: absolute; top: 0; left: 0; animation: spinSlow 14s linear infinite;">
                    <circle cx="67.5" cy="67.5" r="61" fill="none" stroke="rgba(0, 245, 212, 0.35)" stroke-width="2" stroke-dasharray="10 6" />
                </svg>

                <!-- Animated Progress Ring (Loads 0 to Score) -->
                <svg width="135" height="135" style="position: absolute; top: 0; left: 0; transform: rotate(-90deg); animation: pulseRing 3s ease-in-out infinite;">
                    <circle cx="67.5" cy="67.5" r="50" fill="none" stroke="rgba(255, 255, 255, 0.08)" stroke-width="8" />
                    <circle id="scoreArc" cx="67.5" cy="67.5" r="50" fill="none" stroke="url(#cyberGrad)" stroke-width="8"
                            stroke-linecap="round" stroke-dasharray="314.16" stroke-dashoffset="314.16" />
                    <defs>
                        <linearGradient id="cyberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#00f5d4" />
                            <stop offset="100%" stop-color="#39ff14" />
                        </linearGradient>
                    </defs>
                </svg>

                <!-- Center Animated Counter -->
                <div style="text-align: center; z-index: 2;">
                    <div id="scoreCounter" style="font-family: 'Orbitron', sans-serif; font-size: 26px; font-weight: 900; color: #ffffff; text-shadow: 0 0 12px #00f5d4;">
                        0%
                    </div>
                    <div style="font-size: 9px; color: #00f5d4; letter-spacing: 1.5px; margin-top: 2px;">
                        MATCH INDEX
                    </div>
                </div>
            </div>

        </div>
    </div>

    <script>
    (function() {
        const targetScore = Math.max(0, Math.min(100, Number(SCORE_VAL) || 85));
        const counterEl = document.getElementById('scoreCounter');
        const arcEl = document.getElementById('scoreArc');
        const circumference = 2 * Math.PI * 50; // 314.16

        // 1. Smooth 0 -> Target Score Load Animation + Continuous Micro-Fluctuation
        let startTime = null;
        const duration = 1800; // 1.8s smooth count-up

        function animateCounter(timestamp) {
            if (!startTime) startTime = timestamp;
            const progress = Math.min((timestamp - startTime) / duration, 1);
            // Ease-out cubic curve
            const eased = 1 - Math.pow(1 - progress, 3);
            const currentVal = Math.round(eased * targetScore);

            counterEl.innerText = currentVal + '%';
            arcEl.style.strokeDashoffset = circumference - (eased * targetScore / 100) * circumference;

            if (progress < 1) {
                requestAnimationFrame(animateCounter);
            } else {
                // Continuous subtle breathing glow after reaching target score
                setInterval(() => {
                    const jitter = (Math.random() - 0.5) * 1.8;
                    const dynamicScore = Math.min(100, Math.max(0, targetScore + jitter));
                    arcEl.style.strokeDashoffset = circumference - (dynamicScore / 100) * circumference;
                }, 180);
            }
        }
        requestAnimationFrame(animateCounter);

        // 2. Continuous Reactive Multi-Wave + Scanning Bar Graph
        const canvas = document.getElementById('waveCanvas');
        const container = document.getElementById('hud-container');
        const ctx = canvas.getContext('2d');
        
        function resize() {
            canvas.width = canvas.clientWidth;
            canvas.height = 115;
        }
        resize();
        window.addEventListener('resize', resize);

        let phase = 0;
        let scanX = 0;
        let mouseX = 0.5;
        let mouseY = 0.5;
        let isHovering = false;

        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouseX = (e.clientX - rect.left) / canvas.width;
            mouseY = (e.clientY - rect.top) / canvas.height;
            isHovering = true;
            container.style.borderColor = '#00f5d4';
            container.style.boxShadow = '0 0 30px rgba(0, 245, 212, 0.35)';
        });

        canvas.addEventListener('mouseleave', () => {
            isHovering = false;
            mouseY = 0.5;
            container.style.borderColor = 'rgba(0, 245, 212, 0.4)';
            container.style.boxShadow = '0 10px 35px rgba(0, 0, 0, 0.5)';
        });

        function drawWave() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Background HUD Grid
            ctx.strokeStyle = 'rgba(0, 245, 212, 0.08)';
            ctx.lineWidth = 1;
            for (let x = 0; x < canvas.width; x += 28) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
            }
            for (let y = 0; y < canvas.height; y += 24) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
            }

            // Animated Vertical Telemetry Bars in Background
            const barCount = 32;
            const barWidth = (canvas.width / barCount) - 4;
            for (let i = 0; i < barCount; i++) {
                const barH = 12 + Math.abs(Math.sin(phase * 0.8 + i * 0.35)) * (canvas.height * 0.45 * (targetScore / 100));
                ctx.fillStyle = 'rgba(0, 245, 212, 0.12)';
                ctx.fillRect(i * (barWidth + 4), canvas.height - barH, barWidth, barH);
            }

            // 3 Continuous Overlapping Neural Waves
            const waves = [
                { color: '#00f5d4', width: 2.4, freq: 0.024, amp: 28 },
                { color: '#39ff14', width: 1.6, freq: 0.038, amp: 18 },
                { color: '#00bbff', width: 1.3, freq: 0.016, amp: 14 }
            ];

            waves.forEach((w, idx) => {
                ctx.beginPath();
                const dynamicAmp = isHovering ? w.amp * (1.65 - mouseY) : w.amp;
                const dynamicFreq = isHovering ? w.freq * (0.75 + mouseX) : w.freq;

                for (let x = 0; x < canvas.width; x++) {
                    const envelope = Math.sin((x / canvas.width) * Math.PI);
                    const y = canvas.height / 2 + 
                              Math.sin(x * dynamicFreq + phase * (idx + 1)) * dynamicAmp * envelope;
                    if (x === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }
                ctx.strokeStyle = w.color;
                ctx.lineWidth = w.width;
                ctx.shadowBlur = isHovering ? 14 : 6;
                ctx.shadowColor = w.color;
                ctx.stroke();
                ctx.shadowBlur = 0;
            });

            // Moving Vertical Laser Scanner Line across Graph
            scanX = (scanX + 2.2) % canvas.width;
            const grad = ctx.createLinearGradient(scanX - 20, 0, scanX + 5, 0);
            grad.addColorStop(0, 'transparent');
            grad.addColorStop(1, 'rgba(0, 245, 212, 0.45)');
            ctx.fillStyle = grad;
            ctx.fillRect(scanX - 20, 0, 25, canvas.height);

            phase += isHovering ? 0.14 : 0.06;
            requestAnimationFrame(drawWave);
        }
        drawWave();
    })();
    </script>
    """.replace("SCORE_VAL", str(score))
    
    components.html(html_code, height=205)


def render_cyberpunk_title_intro():
    """Renders an animated, glowing matrix title intro for ResumeIQ."""
    components.html("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600&family=Orbitron:wght@800;900&display=swap');
        @keyframes scanlineMove {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        @keyframes titlePulse {
            0%, 100% { text-shadow: 0 0 15px rgba(0, 245, 212, 0.6), 0 0 30px rgba(0, 173, 181, 0.3); }
            50% { text-shadow: 0 0 25px rgba(0, 245, 212, 0.95), 0 0 45px rgba(57, 255, 20, 0.45); }
        }
    </style>
    <div style="
        background: radial-gradient(circle, rgba(0,245,212,0.12) 0%, rgba(7,9,14,0.95) 80%);
        border: 1px solid rgba(0, 245, 212, 0.5);
        border-radius: 14px;
        padding: 26px;
        text-align: center;
        box-shadow: 0 0 35px rgba(0, 245, 212, 0.22);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 0; left: 0; width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, #00f5d4, #39ff14, transparent);
            animation: scanlineMove 2.8s linear infinite;
        "></div>

        <h1 style="
            color: #f0f2f6;
            font-family: 'Orbitron', sans-serif;
            font-size: 2.8rem;
            font-weight: 900;
            letter-spacing: 7px;
            margin: 0;
            animation: titlePulse 3s ease-in-out infinite;
        ">
            RESUME<span style="color: #00f5d4;">IQ</span>
        </h1>
        
        <p style="
            color: #39ff14;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12.5px;
            letter-spacing: 3.5px;
            margin: 10px 0 0 0;
            text-shadow: 0 0 8px rgba(57, 255, 20, 0.6);
        ">
            // NEXT-GEN AI CAREER & NEURAL RESUME ANALYZER
        </p>
    </div>
    """, height=145)