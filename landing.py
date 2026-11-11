def render_futuristic_landing_page():
    """Renders a full-screen, heavy-animation 3D cyberpunk landing page for ResumeIQ."""
    
    # Hide the sidebar on the landing page for a true full-screen web experience
    st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none !important;
        }
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            max-width: 1250px !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Inject the Interactive 3D Canvas, Glitch Hero, Live Terminal & 3D Tilt Cards
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@500;600;700&display=swap');

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: transparent;
            color: #e6f1ff;
            font-family: 'Rajdhani', sans-serif;
            overflow-x: hidden;
            user-select: none;
        }

        .landing-wrapper {
            position: relative;
            width: 100%;
            min-height: 760px;
            border-radius: 24px;
            border: 1px solid rgba(0, 245, 212, 0.35);
            background: radial-gradient(circle at 50% 25%, rgba(0, 245, 212, 0.12), rgba(5, 8, 15, 0.94) 75%);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.75), inset 0 0 40px rgba(0, 245, 212, 0.08);
            overflow: hidden;
            padding: 36px 28px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* 3D Interactive Canvas Background */
        #heroCanvas {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 1;
            pointer-events: none;
        }

        /* Top HUD Status Bar */
        .hud-topbar {
            position: relative;
            z-index: 3;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(0, 245, 212, 0.25);
            padding-bottom: 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            color: #00f5d4;
            letter-spacing: 2px;
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 245, 212, 0.1);
            border: 1px solid rgba(0, 245, 212, 0.45);
            padding: 5px 14px;
            border-radius: 20px;
            color: #39ff14;
            box-shadow: 0 0 15px rgba(57, 255, 20, 0.25);
        }

        .pulse-dot {
            width: 8px; height: 8px;
            background: #39ff14;
            border-radius: 50%;
            box-shadow: 0 0 10px #39ff14;
            animation: blink 1.2s infinite;
        }

        @keyframes blink { 0%, 100% { opacity: 0.2; } 50% { opacity: 1; } }

        /* Center Hero Section */
        .hero-center {
            position: relative;
            z-index: 3;
            text-align: center;
            margin: 28px auto 20px auto;
            max-width: 880px;
        }

        .cyber-badge {
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            color: #00f5d4;
            background: rgba(0, 173, 181, 0.14);
            border: 1px solid #00f5d4;
            padding: 6px 18px;
            border-radius: 4px;
            letter-spacing: 3px;
            margin-bottom: 16px;
            box-shadow: 0 0 20px rgba(0, 245, 212, 0.25);
            animation: floatBadge 3s ease-in-out infinite;
        }

        @keyframes floatBadge {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
        }

        .glitch-title {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(2.8rem, 6vw, 4.8rem);
            font-weight: 900;
            letter-spacing: 10px;
            color: #ffffff;
            text-transform: uppercase;
            text-shadow: 0 0 25px rgba(0, 245, 212, 0.8), 0 0 55px rgba(0, 173, 181, 0.4);
            position: relative;
            margin-bottom: 10px;
        }

        .glitch-title span {
            color: #00f5d4;
            text-shadow: 0 0 30px #00f5d4, 0 0 60px #39ff14;
        }

        /* Typewriter Terminal Box */
        .terminal-box {
            display: inline-block;
            background: rgba(6, 11, 19, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 245, 212, 0.35);
            border-left: 4px solid #39ff14;
            border-radius: 8px;
            padding: 10px 22px;
            margin: 12px 0 24px 0;
            font-family: 'JetBrains Mono', monospace;
            font-size: 14px;
            color: #39ff14;
            letter-spacing: 1.5px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        }

        .cursor-blink {
            display: inline-block;
            width: 8px;
            height: 15px;
            background: #39ff14;
            vertical-align: middle;
            margin-left: 4px;
            animation: blink 0.8s infinite;
        }

        /* Live Stats Strip */
        .stats-strip {
            display: flex;
            justify-content: center;
            gap: 36px;
            flex-wrap: wrap;
            margin-bottom: 28px;
        }

        .stat-item {
            text-align: center;
            background: rgba(12, 20, 32, 0.55);
            border: 1px solid rgba(0, 245, 212, 0.25);
            padding: 10px 24px;
            border-radius: 12px;
            backdrop-filter: blur(8px);
            transition: all 0.3s ease;
        }

        .stat-item:hover {
            border-color: #00f5d4;
            transform: translateY(-4px);
            box-shadow: 0 0 25px rgba(0, 245, 212, 0.3);
        }

        .stat-num {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.7rem;
            font-weight: 800;
            color: #00f5d4;
            text-shadow: 0 0 12px rgba(0, 245, 212, 0.5);
        }

        .stat-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            color: #94a3b8;
            letter-spacing: 1.5px;
            margin-top: 2px;
        }

        /* 3D Interactive Feature Cards Grid */
        .cards-grid {
            position: relative;
            z-index: 3;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 20px;
            margin-top: 10px;
            perspective: 1000px;
        }

        .tilt-card {
            background: linear-gradient(145deg, rgba(16, 25, 40, 0.72), rgba(8, 13, 22, 0.88));
            backdrop-filter: blur(16px);
            border: 1px solid rgba(0, 245, 212, 0.3);
            border-radius: 16px;
            padding: 22px;
            transition: transform 0.15s ease-out, border-color 0.3s ease, box-shadow 0.3s ease;
            transform-style: preserve-3d;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }

        .tilt-card::before {
            content: "";
            position: absolute;
            top: 0; left: -100%;
            width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, #00f5d4, #39ff14, transparent);
            animation: scanBar 3.5s linear infinite;
        }

        @keyframes scanBar {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .tilt-card:hover {
            border-color: #00f5d4;
            box-shadow: 0 15px 35px rgba(0, 245, 212, 0.28), inset 0 0 20px rgba(0, 245, 212, 0.1);
        }

        .card-icon {
            font-size: 26px;
            margin-bottom: 10px;
            display: inline-block;
            background: rgba(0, 245, 212, 0.12);
            border: 1px solid rgba(0, 245, 212, 0.4);
            padding: 8px 12px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 245, 212, 0.2);
        }

        .card-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
        }

        .card-desc {
            font-size: 0.98rem;
            color: #b0c4de;
            line-height: 1.45;
        }
    </style>
    </head>
    <body>
        <div class="landing-wrapper" id="landingWrapper">
            <canvas id="heroCanvas"></canvas>

            <!-- Top HUD Bar -->
            <div class="hud-topbar">
                <div>SYS_CORE // RESUME_IQ_V4.2</div>
                <div class="status-pill">
                    <span class="pulse-dot"></span> NEURAL ENGINE READY
                </div>
                <div id="coordsDisplay">GRID_SYNC: 00.00 // 00.00</div>
            </div>

            <!-- Hero Center Content -->
            <div class="hero-center">
                <div class="cyber-badge">⚡ NEXT-GEN AI CAREER & ATS INTELLIGENCE</div>
                <h1 class="glitch-title">RESUME<span>IQ</span></h1>
                
                <div class="terminal-box">
                    <span id="typewriterText"></span><span class="cursor-blink"></span>
                </div>

                <!-- Animated Counter Strip -->
                <div class="stats-strip">
                    <div class="stat-item">
                        <div class="stat-num" data-target="99.4" data-suffix="%">0%</div>
                        <div class="stat-label">ATS PARSING PRECISION</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-num" data-target="50" data-suffix="+">0+</div>
                        <div class="stat-label">NEURAL RUBRIC VECTORS</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-num" data-target="100" data-suffix="%">0%</div>
                        <div class="stat-label">REAL-TIME TELEMETRY</div>
                    </div>
                </div>
            </div>

            <!-- 3D Tilt Feature Cards -->
            <div class="cards-grid">
                <div class="tilt-card">
                    <div class="card-icon">📊</div>
                    <div class="card-title">EXECUTIVE ATS TELEMETRY</div>
                    <div class="card-desc">
                        Real-time 0-to-100 profile health scoring with multi-axis rubric breakdowns across Experience, Projects, Skills, and Certifications.
                    </div>
                </div>

                <div class="tilt-card">
                    <div class="card-icon">🎯</div>
                    <div class="card-title">JD MATCHER & IMPACT AUDIT</div>
                    <div class="card-desc">
                        Deep semantic alignment against target job descriptions to uncover missing keywords, weak action verbs, and quantifiable impact gaps.
                    </div>
                </div>

                <div class="tilt-card">
                    <div class="card-icon">🧠</div>
                    <div class="card-title">AI SKILL & CAREER MATRIX</div>
                    <div class="card-desc">
                        Automated skill extraction paired with personalized role predictions, curated course roadmaps, and interview preparation modules.
                    </div>
                </div>
            </div>
        </div>

        <script>
        (function() {
            // 1. TYPEWRITER BOOT SEQUENCE
            const phrases = [
                ">> INITIALIZING NEURAL RESUME PARSER...",
                ">> CALIBRATING EXECUTIVE ATS RUBRIC WEIGHTS...",
                ">> LOADING JD SEMANTIC MATCHING ENGINE...",
                ">> SYSTEM ONLINE: CLICK 'ENTER NEURAL DASHBOARD' BELOW"
            ];
            let pIdx = 0, cIdx = 0, deleting = false;
            const twEl = document.getElementById('typewriterText');

            function typeLoop() {
                const current = phrases[pIdx];
                if (!deleting) {
                    twEl.textContent = current.substring(0, cIdx + 1);
                    cIdx++;
                    if (cIdx === current.length) {
                        deleting = true;
                        setTimeout(typeLoop, 2200);
                        return;
                    }
                    setTimeout(typeLoop, 38);
                } else {
                    twEl.textContent = current.substring(0, cIdx - 1);
                    cIdx--;
                    if (cIdx === 0) {
                        deleting = false;
                        pIdx = (pIdx + 1) % phrases.length;
                    }
                    setTimeout(typeLoop, 18);
                }
            }
            typeLoop();

            // 2. SMOOTH NUMBER COUNTERS
            document.querySelectorAll('.stat-num').forEach((el) => {
                const target = parseFloat(el.dataset.target);
                const suffix = el.dataset.suffix || '';
                const isFloat = String(el.dataset.target).includes('.');
                let start = null;
                function step(ts) {
                    if (!start) start = ts;
                    const p = Math.min((ts - start) / 1600, 1);
                    const val = (1 - Math.pow(1 - p, 3)) * target;
                    el.textContent = (isFloat ? val.toFixed(1) : Math.round(val)) + suffix;
                    if (p < 1) requestAnimationFrame(step);
                }
                requestAnimationFrame(step);
            });

            // 3. 3D TILT PHYSICS ON FEATURE CARDS
            document.querySelectorAll('.tilt-card').forEach((card) => {
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const rotY = ((x / rect.width) - 0.5) * 18;
                    const rotX = ((0.5 - (y / rect.height))) * 18;
                    card.style.transform = `perspective(900px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-6px) scale(1.02)`;
                });
                card.addEventListener('mouseleave', () => {
                    card.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg) translateY(0px) scale(1)';
                });
            });

            // 4. 3D ROTATING NEURAL SPHERE & PERSPECTIVE GRID CANVAS
            const canvas = document.getElementById('heroCanvas');
            const wrapper = document.getElementById('landingWrapper');
            const coordsEl = document.getElementById('coordsDisplay');
            const ctx = canvas.getContext('2d');

            function resize() {
                canvas.width = wrapper.clientWidth;
                canvas.height = wrapper.clientHeight;
            }
            resize();
            window.addEventListener('resize', resize);

            let mouseX = 0, mouseY = 0;
            wrapper.addEventListener('mousemove', (e) => {
                const r = wrapper.getBoundingClientRect();
                mouseX = ((e.clientX - r.left) / r.width - 0.5) * 2;
                mouseY = ((e.clientY - r.top) / r.height - 0.5) * 2;
                coordsEl.textContent = `GRID_SYNC: ${(mouseX * 90).toFixed(1)} // ${(mouseY * 90).toFixed(1)}`;
            });

            // Create 3D sphere points
            const numPoints = 95;
            const spherePoints = [];
            for (let i = 0; i < numPoints; i++) {
                const phi = Math.acos(1 - 2 * (i + 0.5) / numPoints);
                const theta = Math.PI * (1 + Math.sqrt(5)) * i;
                spherePoints.push({
                    x: Math.cos(theta) * Math.sin(phi),
                    y: Math.sin(theta) * Math.sin(phi),
                    z: Math.cos(phi)
                });
            }

            let angleY = 0;
            let angleX = 0;

            function animateCanvas() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                const cx = canvas.width / 2;
                const cy = canvas.height * 0.42;
                const radius = Math.min(canvas.width, canvas.height) * 0.34;

                angleY += 0.007 + mouseX * 0.015;
                angleX += 0.003 + mouseY * 0.015;

                const projected = spherePoints.map((p) => {
                    // Rotate around Y
                    let x1 = p.x * Math.cos(angleY) - p.z * Math.sin(angleY);
                    let z1 = p.z * Math.cos(angleY) + p.x * Math.sin(angleY);
                    // Rotate around X
                    let y2 = p.y * Math.cos(angleX) - z1 * Math.sin(angleX);
                    let z2 = z1 * Math.cos(angleX) + p.y * Math.sin(angleX);

                    const scale = 320 / (320 + z2 * radius * 0.5);
                    return {
                        x: cx + x1 * radius * scale,
                        y: cy + y2 * radius * scale,
                        z: z2,
                        scale: scale
                    };
                });

                // Draw neural connections on 3D globe
                for (let i = 0; i < projected.length; i++) {
                    for (let j = i + 1; j < projected.length; j++) {
                        const d = Math.hypot(projected[i].x - projected[j].x, projected[i].y - projected[j].y);
                        if (d < 78) {
                            ctx.beginPath();
                            ctx.moveTo(projected[i].x, projected[i].y);
                            ctx.lineTo(projected[j].x, projected[j].y);
                            ctx.strokeStyle = `rgba(0, 245, 212, ${(1 - d / 78) * 0.25})`;
                            ctx.lineWidth = 0.9;
                            ctx.stroke();
                        }
                    }
                }

                // Draw glowing 3D nodes
                projected.forEach((p) => {
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, Math.max(1.2, 2.8 * p.scale), 0, Math.PI * 2);
                    ctx.fillStyle = p.z > 0 ? '#00f5d4' : 'rgba(0, 173, 181, 0.45)';
                    ctx.fill();
                });

                requestAnimationFrame(animateCanvas);
            }
            animateCanvas();
        })();
        </script>
    </body>
    </html>
    """, height=780)