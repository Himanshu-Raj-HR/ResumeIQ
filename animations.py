import streamlit as st
import streamlit.components.v1 as components

def load_futuristic_animations():
    """Injects sci-fi typography, fixed st_tags auto-height, Plotly rubric/gauge animations, and persistent background neural mesh."""
    
    # 1. GLOBAL CSS: Fonts, Glassmorphism, Buttons, Plotly Charts & High-Contrast Text Fixes
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@500;600;700&display=swap');

        /* App Background - Transparent layers so background canvas shines through */
        .stApp {
            background-color: #05070b !important;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(0, 245, 212, 0.14), transparent 55%),
                radial-gradient(circle at 85% 80%, rgba(0, 173, 181, 0.1), transparent 50%),
                linear-gradient(rgba(0, 245, 212, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 245, 212, 0.03) 1px, transparent 1px) !important;
            background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 18px !important;
            color: #e6f1ff !important;
        }

        /* Ensure main containers don't hide the neural canvas */
        [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Futuristic Headers */
        h1, h2, h3, h4, h5, [data-testid="stSubheader"] {
            font-family: 'Orbitron', sans-serif !important;
            letter-spacing: 2px !important;
            text-transform: uppercase !important;
            color: #ffffff !important;
            text-shadow: 0 0 18px rgba(0, 245, 212, 0.4) !important;
        }

        /* Fix dark unreadable text like "Maybe Available in Future Updates" */
        h4, h5, h6, [data-testid="stMarkdownContainer"] font, [data-testid="stMarkdownContainer"] span {
            color: #00f5d4 !important;
        }

        p, li, label, .stMarkdown {
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.15rem !important;
            font-weight: 600 !important;
            color: #e0fbfc !important;
            letter-spacing: 0.5px !important;
        }

        /* Basic Info Monospace Readouts */
        pre, code, .stText {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.96rem !important;
            color: #00f5d4 !important;
            background: rgba(10, 16, 26, 0.7) !important;
            border-left: 3px solid #00f5d4 !important;
            padding: 8px 14px !important;
            border-radius: 0 8px 8px 0 !important;
            margin-bottom: 6px !important;
        }

        /* Sidebar Glass */
        [data-testid="stSidebar"] {
            background: rgba(8, 12, 20, 0.75) !important;
            backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(0, 245, 212, 0.25) !important;
        }

        /* =====================================================
           EXECUTIVE ATS DASHBOARD METRIC CARDS
           ===================================================== */
        [data-testid="stMetric"] {
            background: linear-gradient(135deg, rgba(14, 22, 36, 0.78), rgba(8, 13, 22, 0.88)) !important;
            backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(0, 245, 212, 0.35) !important;
            border-radius: 14px !important;
            padding: 18px 20px !important;
            box-shadow: 0 8px 28px rgba(0, 0, 0, 0.45), inset 0 0 15px rgba(0, 245, 212, 0.06) !important;
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1) !important;
            position: relative !important;
            overflow: hidden !important;
        }

        [data-testid="stMetric"]::after {
            content: "";
            position: absolute;
            top: 0; left: -100%; width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, #00f5d4, #39ff14, transparent);
            animation: cardScan 3.5s linear infinite;
        }

        @keyframes cardScan {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-6px) scale(1.02) !important;
            border-color: #00f5d4 !important;
            box-shadow: 0 12px 35px rgba(0, 245, 212, 0.3), 0 0 15px rgba(0, 245, 212, 0.2) !important;
        }

        [data-testid="stMetricLabel"] {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 0.9rem !important;
            letter-spacing: 1.5px !important;
            color: #00f5d4 !important;
            text-transform: uppercase !important;
        }

        [data-testid="stMetricValue"] {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 2rem !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            text-shadow: 0 0 14px rgba(0, 245, 212, 0.5) !important;
        }

        /* =====================================================
           PLOTLY CHARTS (OVERALL PROFILE HEALTH & RUBRIC BARS)
           ===================================================== */
        [data-testid="stPlotlyChart"] {
            background: rgba(10, 16, 26, 0.65) !important;
            backdrop-filter: blur(14px) !important;
            border: 1px solid rgba(0, 245, 212, 0.3) !important;
            border-radius: 16px !important;
            padding: 12px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45) !important;
            transition: all 0.35s ease !important;
        }

        [data-testid="stPlotlyChart"]:hover {
            border-color: #00f5d4 !important;
            box-shadow: 0 0 28px rgba(0, 245, 212, 0.28) !important;
            transform: translateY(-3px) !important;
        }

        /* Make Plotly chart backgrounds transparent so glass shows */
        .js-plotly-plot .plotly .main-svg {
            background: transparent !important;
        }

        /* Animate Rubric Breakdown Bars & Gauge */
        @keyframes rubricBarGrow {
            0% {
                transform: scaleX(0);
                filter: brightness(2) drop-shadow(0 0 12px #00f5d4);
            }
            100% {
                transform: scaleX(1);
                filter: brightness(1.1) drop-shadow(0 0 6px rgba(0, 245, 212, 0.5));
            }
        }

        @keyframes rubricPulseGlow {
            0%, 100% { filter: drop-shadow(0 0 4px rgba(0, 245, 212, 0.4)); }
            50% { filter: drop-shadow(0 0 12px rgba(0, 245, 212, 0.9)); }
        }

        .js-plotly-plot .plot .bars .point path {
            transform-box: fill-box;
            transform-origin: left center;
            animation: rubricBarGrow 1.3s cubic-bezier(0.22, 1, 0.36, 1) forwards,
                       rubricPulseGlow 2.8s ease-in-out infinite 1.3s !important;
            transition: all 0.25s ease !important;
        }

        .js-plotly-plot .plot .bars .point path:hover {
            filter: brightness(1.4) drop-shadow(0 0 15px #39ff14) !important;
        }

        /* Animate Overall Profile Health Gauge Arc */
        @keyframes gaugeSweep {
            0% { opacity: 0; transform: scale(0.85); filter: blur(6px); }
            100% { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 10px rgba(0, 245, 212, 0.5)); }
        }

        .js-plotly-plot .indicatorlayer .trace {
            transform-box: fill-box;
            transform-origin: center bottom;
            animation: gaugeSweep 1.2s cubic-bezier(0.22, 1, 0.36, 1) forwards !important;
        }

        /* =====================================================
           FUTURISTIC CYBERPUNK BUTTONS & TABS
           ===================================================== */
        .stButton > button, 
        [data-testid="stDownloadButton"] > button,
        [data-testid="stFormSubmitButton"] > button {
            min-height: 54px !important;
            width: 100% !important;
            padding: 14px 28px !important;
            font-family: 'Orbitron', sans-serif !important;
            font-size: 15px !important;
            font-weight: 700 !important;
            letter-spacing: 2.5px !important;
            text-transform: uppercase !important;
            color: #00f5d4 !important;
            background: linear-gradient(135deg, rgba(0, 245, 212, 0.16) 0%, rgba(10, 18, 30, 0.9) 50%, rgba(0, 173, 181, 0.22) 100%) !important;
            border: 1.5px solid rgba(0, 245, 212, 0.7) !important;
            clip-path: polygon(14px 0%, 100% 0%, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0% 100%, 0% 14px) !important;
            box-shadow: 0 0 20px rgba(0, 245, 212, 0.2) !important;
            position: relative !important;
            overflow: hidden !important;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        }

        .stButton > button:hover, 
        [data-testid="stDownloadButton"] > button:hover {
            color: #04080e !important;
            background: linear-gradient(135deg, #00f5d4 0%, #00bbff 100%) !important;
            border-color: #ffffff !important;
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 0 10px 35px rgba(0, 245, 212, 0.65), 0 0 15px #00f5d4 !important;
        }

        /* Futuristic Tabs (Score & Rubric Analysis | JD Matcher | Interview Prep) */
        button[data-baseweb="tab"] {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            letter-spacing: 1px !important;
            padding: 10px 18px !important;
            transition: all 0.3s ease !important;
        }
        button[data-baseweb="tab"]:hover {
            color: #00f5d4 !important;
            text-shadow: 0 0 10px #00f5d4 !important;
        }

        /* Glass Expanders, Alerts & Uploads */
        [data-testid="stExpander"], [data-testid="stFileUploader"], .stAlert {
            background: rgba(14, 21, 33, 0.6) !important;
            backdrop-filter: blur(14px) !important;
            border: 1px solid rgba(0, 245, 212, 0.3) !important;
            border-radius: 12px !important;
        }

        /* Scroll-Reveal Classes */
        .cyber-scroll-hidden {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        .cyber-scroll-visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }

        /* Telemetry Header */
        .live-dot {
            height: 10px; width: 10px; background-color: #39ff14;
            border-radius: 50%; display: inline-block;
            box-shadow: 0 0 10px #39ff14; animation: blink 1.4s infinite; margin-right: 8px;
        }
        @keyframes blink { 0%, 100% { opacity: 0.25; } 50% { opacity: 1; } }
        .telemetry-box {
            background: rgba(12, 18, 28, 0.65); backdrop-filter: blur(14px);
            border: 1px solid rgba(0, 245, 212, 0.35); border-radius: 12px;
            padding: 14px 20px; margin-bottom: 22px;
            display: flex; align-items: center; justify-content: space-between;
        }
        .eq-bars { display: flex; align-items: flex-end; gap: 4px; height: 28px; }
        .eq-bar {
            width: 5px; background: linear-gradient(to top, #00adb5, #00f5d4);
            border-radius: 3px; animation: equalize 1.1s ease-in-out infinite;
        }
        @keyframes equalize { 0%, 100% { height: 20%; } 50% { height: 100%; } }
    </style>
    """, unsafe_allow_html=True)

    # 2. JAVASCRIPT ENGINE: Self-Healing Background Mesh + Fixed Skill Tags + Plotly Score/Rubric Animator
    components.html("""
    <script>
    (function() {
        const parentWin = window.parent;
        const parentDoc = parentWin.document;

        // =========================================================================
        // A. ALWAYS-RUNNING BACKGROUND NEURAL GRAPH (SELF-HEALING ON STREAMLIT RERUN)
        // =========================================================================
        let canvas = parentDoc.getElementById('cyber-neural-canvas');
        if (!canvas) {
            canvas = parentDoc.createElement('canvas');
            canvas.id = 'cyber-neural-canvas';
            parentDoc.body.appendChild(canvas);
        }
        // Keep z-index above base background but non-blocking so it never disappears
        canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:1;opacity:0.65;';

        let glow = parentDoc.getElementById('cyber-cursor-glow');
        if (!glow) {
            glow = parentDoc.createElement('div');
            glow.id = 'cyber-cursor-glow';
            parentDoc.body.appendChild(glow);
        }
        glow.style.cssText = 'position:fixed;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle, rgba(0,245,212,0.15) 0%, rgba(0,173,181,0.05) 45%, transparent 70%);pointer-events:none;z-index:1;transform:translate(-50%,-50%);';

        if (!parentWin.__cyberMeshRunning) {
            parentWin.__cyberMeshRunning = true;
            const ctx = canvas.getContext('2d');
            let width = canvas.width = parentWin.innerWidth;
            let height = canvas.height = parentWin.innerHeight;

            parentWin.addEventListener('resize', () => {
                width = canvas.width = parentWin.innerWidth;
                height = canvas.height = parentWin.innerHeight;
            });

            let mouse = { x: width / 2, y: height / 2 };
            parentDoc.addEventListener('mousemove', (e) => {
                mouse.x = e.clientX;
                mouse.y = e.clientY;
                glow.style.left = e.clientX + 'px';
                glow.style.top = e.clientY + 'px';
            });

            const nodes = Array.from({length: 55}, () => ({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.9,
                vy: (Math.random() - 0.5) * 0.9,
                r: Math.random() * 2.2 + 1
            }));

            function renderNeuralMesh() {
                // Re-verify canvas dimensions in case layout shifted
                if (canvas.width !== parentWin.innerWidth || canvas.height !== parentWin.innerHeight) {
                    width = canvas.width = parentWin.innerWidth;
                    height = canvas.height = parentWin.innerHeight;
                }
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
                    if (distMouse < 180) {
                        ctx.beginPath();
                        ctx.moveTo(n.x, n.y);
                        ctx.lineTo(mouse.x, mouse.y);
                        ctx.strokeStyle = `rgba(0, 245, 212, ${1 - distMouse / 180})`;
                        ctx.lineWidth = 1.3;
                        ctx.stroke();
                    }

                    for (let j = i + 1; j < nodes.length; j++) {
                        let n2 = nodes[j];
                        let dist = Math.hypot(n.x - n2.x, n.y - n2.y);
                        if (dist < 115) {
                            ctx.beginPath();
                            ctx.moveTo(n.x, n.y);
                            ctx.lineTo(n2.x, n2.y);
                            ctx.strokeStyle = `rgba(0, 173, 181, ${(1 - dist / 115) * 0.38})`;
                            ctx.lineWidth = 0.8;
                            ctx.stroke();
                        }
                    }
                }
                parentWin.requestAnimationFrame(renderNeuralMesh);
            }
            parentWin.requestAnimationFrame(renderNeuralMesh);
        }

        // =========================================================================
        // B. FIX SKILL TAGS & RECOMMENDATIONS (NO DOUBLE-BOX, AUTO-EXPAND HEIGHT)
        // =========================================================================
        function fixSkillsAndAnimateDashboard() {
            const iframes = parentDoc.querySelectorAll('iframe');
            iframes.forEach((frame) => {
                try {
                    const frameDoc = frame.contentDocument || frame.contentWindow.document;
                    if (!frameDoc || !frameDoc.body) return;

                    // Detect if this iframe is a streamlit_tags (st_tags) component
                    const tagContainer = frameDoc.querySelector('.ReactTags__tags');
                    if (tagContainer) {
                        // Replace broken double-box style with clean single-pill style
                        let styleEl = frameDoc.getElementById('cyber-tag-style-v2');
                        if (!styleEl) {
                            // Remove old broken style if present
                            const oldStyle = frameDoc.getElementById('cyber-tag-style');
                            if (oldStyle) oldStyle.remove();

                            styleEl = frameDoc.createElement('style');
                            styleEl.id = 'cyber-tag-style-v2';
                            styleEl.innerHTML = `
                                @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600&display=swap');
                                @keyframes tagPopIn {
                                    0% { opacity: 0; transform: translateY(12px) scale(0.8); }
                                    70% { transform: translateY(-2px) scale(1.04); }
                                    100% { opacity: 1; transform: translateY(0) scale(1); }
                                }
                                html, body {
                                    background: transparent !important;
                                    overflow: visible !important;
                                    margin: 0 !important;
                                    padding: 4px !important;
                                }
                                .ReactTags__tags {
                                    background: rgba(10, 17, 28, 0.75) !important;
                                    border: 1px solid rgba(0, 245, 212, 0.35) !important;
                                    border-radius: 12px !important;
                                    padding: 12px !important;
                                    display: flex !important;
                                    flex-wrap: wrap !important;
                                    gap: 8px !important;
                                    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35) !important;
                                }
                                .ReactTags__selected {
                                    display: flex !important;
                                    flex-wrap: wrap !important;
                                    gap: 8px !important;
                                    width: 100% !important;
                                }
                                /* Style ONLY the outer tag pill, never inner spans */
                                .ReactTags__tag {
                                    font-family: 'JetBrains Mono', monospace !important;
                                    font-size: 13.5px !important;
                                    font-weight: 600 !important;
                                    background: linear-gradient(135deg, rgba(0, 245, 212, 0.18), rgba(0, 173, 181, 0.08)) !important;
                                    border: 1px solid #00f5d4 !important;
                                    color: #ffffff !important;
                                    border-radius: 8px !important;
                                    padding: 6px 12px !important;
                                    margin: 0 !important;
                                    display: inline-flex !important;
                                    align-items: center !important;
                                    gap: 6px !important;
                                    box-shadow: 0 0 12px rgba(0, 245, 212, 0.22) !important;
                                    animation: tagPopIn 0.45s cubic-bezier(0.22, 1, 0.36, 1) both !important;
                                    transition: all 0.25s ease !important;
                                }
                                .ReactTags__tag span, .ReactTags__tag a {
                                    border: none !important;
                                    background: transparent !important;
                                    box-shadow: none !important;
                                    padding: 0 !important;
                                    margin: 0 !important;
                                }
                                .ReactTags__tag:hover {
                                    transform: translateY(-3px) scale(1.06) !important;
                                    border-color: #39ff14 !important;
                                    background: rgba(0, 245, 212, 0.3) !important;
                                    box-shadow: 0 0 18px rgba(57, 255, 20, 0.55) !important;
                                }
                                .ReactTags__remove {
                                    color: #00f5d4 !important;
                                    margin-left: 6px !important;
                                    cursor: pointer !important;
                                    border: none !important;
                                    background: transparent !important;
                                }
                                .ReactTags__tagInput input {
                                    font-family: 'JetBrains Mono', monospace !important;
                                    background: transparent !important;
                                    color: #00f5d4 !important;
                                    border: none !important;
                                    outline: none !important;
                                }
                            `;
                            frameDoc.head.appendChild(styleEl);
                        }

                        // Stagger each skill pill one-by-one
                        const tags = frameDoc.querySelectorAll('.ReactTags__tag');
                        tags.forEach((t, i) => {
                            if (!t.dataset.staggeredV2) {
                                t.dataset.staggeredV2 = 'true';
                                t.style.animationDelay = `${i * 0.08}s`;
                            }
                        });

                        // Auto-resize iframe height so skills & recommendations are NEVER cut off
                        const neededHeight = tagContainer.scrollHeight + 24;
                        if (neededHeight > 60 && Math.abs(frame.clientHeight - neededHeight) > 6) {
                            frame.style.height = neededHeight + 'px';
                            frame.height = neededHeight;
                        }
                    }
                } catch (e) {}
            });

            // =========================================================================
            // C. ANIMATE PLOTLY GAUGE NUMBER (0 -> 80) & RUBRIC BARS ONE-BY-ONE
            // =========================================================================
            // 1. Stagger Rubric Breakdown Bars one by one
            const rubricBars = parentDoc.querySelectorAll('.js-plotly-plot .plot .bars .point path');
            rubricBars.forEach((bar, idx) => {
                if (!bar.dataset.rubricAnimated) {
                    bar.dataset.rubricAnimated = 'true';
                    bar.style.animationDelay = `${idx * 0.12}s, ${1.3 + idx * 0.12}s`;
                }
            });

            // 2. Count up Plotly Gauge "Overall Profile Health" Score (e.g. 0 -> 80)
            const gaugeNumbers = parentDoc.querySelectorAll('.js-plotly-plot .indicatorlayer text.numbers');
            gaugeNumbers.forEach((numEl) => {
                const rawText = numEl.textContent.trim();
                const targetVal = parseFloat(rawText);
                if (!isNaN(targetVal) && targetVal > 0 && !numEl.dataset.countedUp) {
                    numEl.dataset.countedUp = 'true';
                    let start = null;
                    const duration = 1600;
                    function stepGauge(ts) {
                        if (!start) start = ts;
                        const prog = Math.min((ts - start) / duration, 1);
                        const eased = 1 - Math.pow(1 - prog, 3);
                        numEl.textContent = Math.round(eased * targetVal);
                        if (prog < 1) {
                            parentWin.requestAnimationFrame(stepGauge);
                        } else {
                            numEl.textContent = rawText;
                        }
                    }
                    parentWin.requestAnimationFrame(stepGauge);
                }
            });

            // 3. Count up Executive ATS Metric Cards (e.g. "80/100", "12 Items", "2 Page(s)")
            const metricValues = parentDoc.querySelectorAll('[data-testid="stMetricValue"] div');
            metricValues.forEach((el) => {
                const text = el.textContent.trim();
                const match = text.match(/^(\\d+)(.*)$/);
                if (match && !el.dataset.countedUp) {
                    el.dataset.countedUp = 'true';
                    const target = parseInt(match[1], 10);
                    const suffix = match[2]; // e.g., "/100" or " Items"
                    let start = null;
                    const duration = 1400;
                    function stepMetric(ts) {
                        if (!start) start = ts;
                        const prog = Math.min((ts - start) / duration, 1);
                        const eased = 1 - Math.pow(1 - prog, 3);
                        el.textContent = Math.round(eased * target) + suffix;
                        if (prog < 1) {
                            parentWin.requestAnimationFrame(stepMetric);
                        } else {
                            el.textContent = text;
                        }
                    }
                    parentWin.requestAnimationFrame(stepMetric);
                }
            });
        }

        fixSkillsAndAnimateDashboard();
        if (parentWin.__cyberFixInterval) clearInterval(parentWin.__cyberFixInterval);
        parentWin.__cyberFixInterval = setInterval(fixSkillsAndAnimateDashboard, 500);
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
        @keyframes spinSlow { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes pulseRing {
            0%, 100% { filter: drop-shadow(0 0 6px #00f5d4); }
            50% { filter: drop-shadow(0 0 16px #39ff14); }
        }
    </style>

    <div id="hud-container" style="
        background: linear-gradient(135deg, rgba(12, 19, 31, 0.85), rgba(7, 11, 18, 0.92));
        backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 245, 212, 0.4);
        border-radius: 16px;
        padding: 18px 24px;
        color: #e0fbfc;
        font-family: 'JetBrains Mono', monospace;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.5);
        position: relative;
        overflow: hidden;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap;">
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

            <div style="position: relative; width: 135px; height: 135px; display: flex; align-items: center; justify-content: center;">
                <svg width="135" height="135" style="position: absolute; top: 0; left: 0; animation: spinSlow 14s linear infinite;">
                    <circle cx="67.5" cy="67.5" r="61" fill="none" stroke="rgba(0, 245, 212, 0.35)" stroke-width="2" stroke-dasharray="10 6" />
                </svg>
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
        const targetScore = Math.max(0, Math.min(100, Number(SCORE_VAL) || 80));
        const counterEl = document.getElementById('scoreCounter');
        const arcEl = document.getElementById('scoreArc');
        const circumference = 2 * Math.PI * 50;

        let startTime = null;
        const duration = 1800;

        function animateCounter(timestamp) {
            if (!startTime) startTime = timestamp;
            const progress = Math.min((timestamp - startTime) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const currentVal = Math.round(eased * targetScore);

            counterEl.innerText = currentVal + '%';
            arcEl.style.strokeDashoffset = circumference - (eased * targetScore / 100) * circumference;

            if (progress < 1) {
                requestAnimationFrame(animateCounter);
            } else {
                setInterval(() => {
                    const jitter = (Math.random() - 0.5) * 1.8;
                    const dynamicScore = Math.min(100, Math.max(0, targetScore + jitter));
                    arcEl.style.strokeDashoffset = circumference - (dynamicScore / 100) * circumference;
                }, 180);
            }
        }
        requestAnimationFrame(animateCounter);

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

            ctx.strokeStyle = 'rgba(0, 245, 212, 0.08)';
            ctx.lineWidth = 1;
            for (let x = 0; x < canvas.width; x += 28) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
            }
            for (let y = 0; y < canvas.height; y += 24) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
            }

            const barCount = 32;
            const barWidth = (canvas.width / barCount) - 4;
            for (let i = 0; i < barCount; i++) {
                const barH = 12 + Math.abs(Math.sin(phase * 0.8 + i * 0.35)) * (canvas.height * 0.45 * (targetScore / 100));
                ctx.fillStyle = 'rgba(0, 245, 212, 0.12)';
                ctx.fillRect(i * (barWidth + 4), canvas.height - barH, barWidth, barH);
            }

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