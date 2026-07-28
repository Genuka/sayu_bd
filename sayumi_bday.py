import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Happy Birthday Sayumi", page_icon="🎂", layout="centered")
st.markdown("""
<style>
#MainMenu, footer, header, .stDeployButton { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

def img_to_b64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

photos = []
for i in range(1, 5):
    for ext in ['jpg','jpeg','png','webp']:
        b64 = img_to_b64(f"photo{i}.{ext}")
        if b64:
            photos.append(f"data:image/{ext};base64,{b64}")
            break
    else:
        photos.append(None)

placeholders = ["📸","🌸","📸","🌺","🌷","💗"]
photo_tags = ""
for i, src in enumerate(photos):
    if src:
        photo_tags += f'<img src="{src}" class="photo-img" alt="selfie">'
    else:
        photo_tags += f'<div class="photo-placeholder">{placeholders[i]}</div>'
photo_tags += f'<div class="photo-placeholder">{placeholders[4]}</div>'
photo_tags += f'<div class="photo-placeholder">{placeholders[5]}</div>'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'DM Sans',sans-serif;background:linear-gradient(135deg,#fff0f5 0%,#fef9ff 40%,#f0f4ff 100%);min-height:100vh;overflow-x:hidden;}}
#confetti-canvas{{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;}}
.hearts-bg{{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;}}
.heart-float{{position:absolute;animation:floatUp linear infinite;opacity:0;}}
@keyframes floatUp{{0%{{transform:translateY(100vh) rotate(0deg);opacity:0.7;}}100%{{transform:translateY(-10vh) rotate(360deg);opacity:0;}}}}

/* ---- LOCK SCREEN ---- */
#lock-screen{{
  position:fixed;top:0;left:0;width:100%;height:100%;
  background:linear-gradient(135deg,#1a0f2e 0%,#2d1b4e 50%,#1a1035 100%);
  z-index:8000;display:flex;align-items:center;justify-content:center;
  flex-direction:column;transition:opacity 0.8s ease,transform 0.8s ease;
}}
#lock-screen.unlocking{{opacity:0;transform:scale(1.05);pointer-events:none;}}
.lock-title{{font-family:'Playfair Display',serif;font-size:1.6rem;color:#f0abca;margin-bottom:0.3rem;text-align:center;}}
.lock-sub{{font-size:0.75rem;color:#9d8fc0;letter-spacing:2px;text-transform:uppercase;margin-bottom:2rem;text-align:center;}}
.pin-display{{
  display:flex;gap:12px;margin-bottom:2rem;justify-content:center;
}}
.pin-dot{{
  width:16px;height:16px;border-radius:50%;
  border:2px solid #a78bfa;background:transparent;
  transition:background 0.2s ease,transform 0.15s ease;
}}
.pin-dot.filled{{background:#e879a0;border-color:#e879a0;transform:scale(1.2);}}
.pin-dot.error{{background:#f87171;border-color:#f87171;animation:shake 0.4s ease;}}
@keyframes shake{{0%,100%{{transform:translateX(0);}}20%{{transform:translateX(-6px);}}40%{{transform:translateX(6px);}}60%{{transform:translateX(-4px);}}80%{{transform:translateX(4px);}}}}
.keypad{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:12px;
  max-width:240px;width:100%;
}}
.key{{
  background:rgba(255,255,255,0.07);border:1px solid rgba(167,139,250,0.25);
  border-radius:16px;padding:1rem;font-size:1.4rem;font-weight:500;
  color:#e8e0f0;cursor:pointer;text-align:center;
  transition:background 0.15s ease,transform 0.1s ease,box-shadow 0.15s ease;
  font-family:'DM Sans',sans-serif;user-select:none;
}}
.key:hover{{background:rgba(167,139,250,0.15);transform:scale(1.06);box-shadow:0 4px 20px rgba(167,139,250,0.2);}}
.key:active{{transform:scale(0.93);background:rgba(232,121,160,0.2);}}
.key.del{{font-size:1rem;color:#a78bfa;}}
.key.empty{{visibility:hidden;}}
.lock-hint{{font-size:0.65rem;color:#6b5f80;margin-top:1.5rem;letter-spacing:1px;}}

/* ---- MAIN ---- */
.container{{max-width:680px;margin:0 auto;padding:2rem 1.2rem 4rem;position:relative;z-index:1;}}
.hero{{text-align:center;padding:3rem 1rem 1.5rem;animation:fadeSlideDown 1s ease both;}}
.hero-tag{{font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;color:#c084a0;margin-bottom:1rem;}}
.hero-name{{
  font-family:'Playfair Display',serif;font-size:clamp(3.5rem,12vw,6.5rem);font-weight:900;
  background:linear-gradient(135deg,#e879a0,#a78bfa,#60a5fa,#e879a0);background-size:300% 300%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;
  animation:gradientShift 4s ease infinite,fadeSlideDown 1s ease both;
}}
@keyframes gradientShift{{0%,100%{{background-position:0% 50%;}}50%{{background-position:100% 50%;}}}}
.hero-sub{{font-size:1.05rem;color:#9d6b8a;font-weight:300;margin-top:0.5rem;}}
.section-label{{text-align:center;font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;color:#c084a0;margin:2rem 0 0.8rem;}}
.countdown-wrap{{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;animation:fadeSlideUp 1.2s ease both;}}
.cd-box{{background:white;border-radius:20px;padding:1.2rem 1.4rem;min-width:75px;text-align:center;box-shadow:0 4px 24px rgba(232,121,160,0.15);border:1px solid rgba(232,121,160,0.2);transition:transform 0.3s ease,box-shadow 0.3s ease;cursor:default;}}
.cd-box:hover{{transform:translateY(-6px) scale(1.06);box-shadow:0 12px 40px rgba(232,121,160,0.28);}}
.cd-num{{font-family:'Playfair Display',serif;font-size:2.4rem;font-weight:700;color:#e879a0;line-height:1;display:block;transition:transform 0.15s ease;}}
.cd-num.bump{{transform:scale(1.2);color:#a78bfa;}}
.cd-label{{font-size:0.6rem;text-transform:uppercase;letter-spacing:2px;color:#c084a0;margin-top:4px;display:block;}}
.emoji-row{{text-align:center;font-size:1.6rem;letter-spacing:8px;margin:1.8rem 0;animation:float 3s ease-in-out infinite;}}
@keyframes float{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-8px);}}}}
.btn-row{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:1.5rem 0;}}
.btn{{border:none;border-radius:50px;padding:0.75rem 1.6rem;font-size:0.82rem;font-family:'DM Sans',sans-serif;font-weight:500;cursor:pointer;transition:transform 0.2s ease,box-shadow 0.2s ease;letter-spacing:0.3px;}}
.btn-primary{{background:linear-gradient(135deg,#e879a0,#a78bfa);color:white;box-shadow:0 4px 20px rgba(232,121,160,0.3);}}
.btn-primary:hover{{transform:translateY(-3px) scale(1.04);box-shadow:0 8px 30px rgba(232,121,160,0.4);}}
.btn-primary:active{{transform:scale(0.96);}}
.btn-outline{{background:white;color:#e879a0;border:2px solid #e879a0;}}
.btn-outline:hover{{background:#fff0f5;transform:translateY(-3px);box-shadow:0 4px 20px rgba(232,121,160,0.15);}}
.btn-dev{{background:#1e1e2e;color:#a78bfa;border:1px dashed #a78bfa55;font-size:0.72rem;padding:0.6rem 1.2rem;}}
.btn-dev:hover{{background:#2a2440;transform:translateY(-2px);}}
.dev-badge{{display:inline-block;background:#1e1e2e;color:#a78bfa;font-size:0.6rem;font-family:monospace;padding:2px 8px;border-radius:4px;margin-left:6px;border:1px solid #a78bfa44;}}
.fact-card{{background:linear-gradient(135deg,#fdf2f8,#faf5ff);border-radius:20px;padding:1.5rem 2rem;text-align:center;border:1px solid rgba(232,121,160,0.15);transition:transform 0.3s ease,opacity 0.3s ease;min-height:120px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;}}
.fact-card.switching{{opacity:0;transform:scale(0.95);}}
.fact-emoji{{font-size:2.2rem;}}
.fact-text{{color:#6b4f6b;font-size:0.92rem;line-height:1.7;}}
.fact-counter{{color:#c084a0;font-size:0.65rem;letter-spacing:1px;margin-top:4px;}}
.photo-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:1rem 0;}}
.photo-placeholder{{aspect-ratio:1;background:linear-gradient(135deg,#fce7f0,#ede9fe);border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:2rem;border:2px dashed rgba(232,121,160,0.3);transition:transform 0.3s ease,box-shadow 0.3s ease;cursor:pointer;}}
.photo-placeholder:hover{{transform:scale(1.06) rotate(2deg);box-shadow:0 8px 30px rgba(232,121,160,0.2);}}
.photo-img{{aspect-ratio:1;object-fit:cover;border-radius:16px;width:100%;transition:transform 0.3s ease,box-shadow 0.3s ease;cursor:pointer;}}
.photo-img:hover{{transform:scale(1.06) rotate(2deg);box-shadow:0 8px 30px rgba(232,121,160,0.2);}}
.msg-card{{background:white;border-radius:24px;padding:2rem;margin:1.5rem 0;box-shadow:0 8px 40px rgba(167,139,250,0.12);border:1px solid rgba(167,139,250,0.18);transition:box-shadow 0.3s ease,max-height 0.6s ease,opacity 0.4s ease;overflow:hidden;}}
.msg-card:hover{{box-shadow:0 16px 60px rgba(167,139,250,0.22);}}
.msg-card.hidden{{max-height:0;opacity:0;padding:0;margin:0;border:none;}}
.msg-card.visible{{max-height:2000px;opacity:1;}}
.msg-quote{{font-size:4rem;color:#f0abca;font-family:'Playfair Display',serif;line-height:0.5;margin-bottom:1rem;}}
.msg-text{{font-size:0.93rem;line-height:1.95;color:#6b4f6b;font-weight:300;}}
.msg-sign{{margin-top:1.5rem;font-family:'Playfair Display',serif;font-style:italic;color:#c084a0;font-size:1rem;}}
.bday-banner{{text-align:center;padding:3rem 2rem;background:linear-gradient(135deg,#fce7f0,#ede9fe,#dbeafe);border-radius:24px;animation:shimmer 3s ease-in-out infinite;}}
@keyframes shimmer{{0%,100%{{box-shadow:0 0 30px rgba(232,121,160,0.2);}}50%{{box-shadow:0 0 60px rgba(167,139,250,0.4);}}}}
.bday-title{{font-family:'Playfair Display',serif;font-size:2.8rem;background:linear-gradient(135deg,#e879a0,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:float 2s ease-in-out infinite;}}
.game-card{{background:white;border-radius:24px;padding:2rem;text-align:center;box-shadow:0 8px 40px rgba(232,121,160,0.12);border:1px solid rgba(232,121,160,0.18);margin:1rem 0;min-height:200px;position:relative;overflow:hidden;}}
.game-question{{font-family:'Playfair Display',serif;font-size:1.3rem;color:#6b4f6b;margin-bottom:0.4rem;}}
.game-sub{{font-size:0.75rem;color:#c084a0;letter-spacing:1px;margin-bottom:1.5rem;}}
.game-btn-wrap{{display:flex;gap:16px;justify-content:center;align-items:center;position:relative;min-height:80px;}}
.btn-no{{background:white;color:#9d6b8a;border:2px solid #e0b4c8;border-radius:50px;padding:0.75rem 1.6rem;font-size:0.82rem;font-family:'DM Sans',sans-serif;font-weight:500;cursor:pointer;position:absolute;transition:left 0.15s ease,top 0.15s ease,font-size 0.2s ease;white-space:nowrap;}}
.game-result{{font-size:1.1rem;color:#e879a0;font-family:'Playfair Display',serif;margin-top:1rem;animation:fadeSlideUp 0.5s ease both;}}
.footer{{text-align:center;padding:2.5rem 0 1rem;color:#c084a0;font-size:0.72rem;letter-spacing:1px;}}
@keyframes fadeSlideDown{{from{{opacity:0;transform:translateY(-30px);}}to{{opacity:1;transform:translateY(0);}}}}
@keyframes fadeSlideUp{{from{{opacity:0;transform:translateY(30px);}}to{{opacity:1;transform:translateY(0);}}}}
</style>
</head>
<body>

<!-- LOCK SCREEN -->
<div id="lock-screen">
  <div class="lock-title">&#127383; hey sayumi &#127383;</div>
  <div class="lock-sub">enter the secret code to get in</div>
  <div class="pin-display" id="pin-display">
    <div class="pin-dot" id="d0"></div>
    <div class="pin-dot" id="d1"></div>
    <div class="pin-dot" id="d2"></div>
    <div class="pin-dot" id="d3"></div>
    <div class="pin-dot" id="d4"></div>
    <div class="pin-dot" id="d5"></div>
    <div class="pin-dot" id="d6"></div>
    <div class="pin-dot" id="d7"></div>
  </div>
  <div class="keypad">
    <div class="key" onclick="pressKey('1')">1</div>
    <div class="key" onclick="pressKey('2')">2</div>
    <div class="key" onclick="pressKey('3')">3</div>
    <div class="key" onclick="pressKey('4')">4</div>
    <div class="key" onclick="pressKey('5')">5</div>
    <div class="key" onclick="pressKey('6')">6</div>
    <div class="key" onclick="pressKey('7')">7</div>
    <div class="key" onclick="pressKey('8')">8</div>
    <div class="key" onclick="pressKey('9')">9</div>
    <div class="key empty"></div>
    <div class="key" onclick="pressKey('0')">0</div>
    <div class="key del" onclick="deleteKey()">&#9003;</div>
  </div>
  <div class="lock-hint">hint: her bday &#128521;</div>
</div>

<canvas id="confetti-canvas"></canvas>
<div class="hearts-bg" id="hearts-bg"></div>

<div class="container">
  <div class="hero">
    <div class="hero-tag">&#10022; a little something for you &#10022;</div>
    <div class="hero-name">Sayumi</div>
    <div class="hero-sub">turning 14 &middot; august 6th &#10024;</div>
  </div>

  <div id="countdown-section">
    <div class="section-label">countdown to the big day &#127872;</div>
    <div class="countdown-wrap">
      <div class="cd-box"><span class="cd-num" id="cd-days">--</span><span class="cd-label">Days</span></div>
      <div class="cd-box"><span class="cd-num" id="cd-hours">--</span><span class="cd-label">Hours</span></div>
      <div class="cd-box"><span class="cd-num" id="cd-mins">--</span><span class="cd-label">Minutes</span></div>
      <div class="cd-box"><span class="cd-num" id="cd-secs">--</span><span class="cd-label">Seconds</span></div>
    </div>
  </div>

  <div id="bday-section" style="display:none;">
    <div class="bday-banner">
      <div class="bday-title">&#127874; IT'S YOUR DAY!! &#127874;</div>
      <p style="color:#9d6b8a;margin-top:1rem;">Happy Birthday Sayumi &#128151; hope it's the best one yet</p>
    </div>
  </div>

  <div class="emoji-row">&#127874; &#128151; &#127881; &#129782; &#129401;</div>

  <div class="btn-row">
    <button class="btn btn-primary" onclick="launchConfetti()">&#127881; Confetti!</button>
    <button class="btn btn-outline" onclick="toggleMessage()">&#128140; Read Message</button>
    <button class="btn btn-primary" onclick="heartShower()">&#128151; Heart Shower</button>
  </div>
  <div class="btn-row">
    <button class="btn btn-dev" onclick="devMode()">&#9881;&#65039; dev: reset to 10s <span class="dev-badge">DEV</span></button>
  </div>

  <div class="section-label">reasons ur actually the worst &#128557;</div>
  <div class="fact-card" id="fact-card">
    <div class="fact-emoji" id="fact-emoji">&#128557;</div>
    <div class="fact-text" id="fact-text">threatens to slap me literally every other day and has never said sorry once</div>
    <div class="fact-counter" id="fact-counter">1 / 5</div>
  </div>
  <div class="btn-row" style="margin-top:10px;">
    <button class="btn btn-outline" onclick="nextRoast()">next roast &#128514;</button>
  </div>

  <div class="section-label">ur camera roll era &#128248;</div>
  <div class="photo-grid">{photo_tags}</div>

  <div class="section-label">one important question &#127872;</div>
  <div class="game-card" id="game-card">
    <div class="game-question" id="game-question">are you the best bsf in the world? &#129402;</div>
    <div class="game-sub" id="game-sub">choose wisely</div>
    <div class="game-btn-wrap" id="game-btn-wrap">
      <button class="btn btn-primary game-yes" onclick="yesClicked()">yes &#128151;</button>
      <button class="btn-no" id="no-btn" onmouseover="runAway()" ontouchstart="runAway()">no</button>
    </div>
    <div class="game-result" id="game-result" style="display:none"></div>
  </div>

  <div class="msg-card hidden" id="msg-card">
    <div class="msg-quote">"</div>
    <div class="msg-text">
      happy birthday sayumi &#128151;&#127874; ur officially old now and i hope ur having the best time lmao. i still remember cambridge 6, the quiet nerd in the corner who wouldn't say a word to anyone, BUT NOT NOW OKK?? now she threatens to slap me on a daily basis and somehow tht's become one of my fav things about her &#128557;<br><br>
      ik i've been a bit quiet lately and i'm sorry for tht, but i need u to know tht never changed how much u mean to me. u wrote me 4 whole pages once for jz no reason and i still think about tht, cuz tht's jz who u are. u give so much without even thinking about it and i don't say this enough but i'm so glad to have u in my life. like actually glad, not jz saying it. u've been there through so much and i don't take tht lightly &#129401;<br><br>
      the kind of bsf tht checks on u, roasts u, threatens to hit u, and somehow still makes u feel like the luckiest person in the room &#128514;&#129782;<br><br>
      have the best birthday okay. wear black obviously. eat way too much cake. and please jz go talk to geenuka already ur going to give yourself a heart attack every time i say his name &#128557;&#128153;<br><br>
      cheers to u being a bit older, more unbothered and still living in the same era as me &#127874;&#129782;&#129401;
    </div>
    <div class="msg-sign">— ur bsf, always &#128151;</div>
  </div>

  <div class="footer">made with &#128151; &middot; for sayumi &middot; august 6th 2026</div>
</div>

<script>
// ---- LOCK ----
const PASSWORD = '06082012';
let pin = '';

function pressKey(k) {{
  if (pin.length >= 8) return;
  pin += k;
  updateDots();
  if (pin.length === 8) {{
    setTimeout(() => {{
      if (pin === PASSWORD) {{
        unlock();
      }} else {{
        wrongPin();
      }}
    }}, 150);
  }}
}}

function deleteKey() {{
  pin = pin.slice(0, -1);
  updateDots();
}}

function updateDots() {{
  for (let i = 0; i < 8; i++) {{
    const d = document.getElementById('d' + i);
    d.classList.toggle('filled', i < pin.length);
    d.classList.remove('error');
  }}
}}

function wrongPin() {{
  for (let i = 0; i < 8; i++) {{
    document.getElementById('d' + i).classList.add('error');
  }}
  setTimeout(() => {{
    pin = '';
    updateDots();
  }}, 600);
}}

function unlock() {{
  const ls = document.getElementById('lock-screen');
  ls.classList.add('unlocking');
  launchConfetti();
  setTimeout(() => {{ ls.style.display = 'none'; }}, 800);
}}

// ---- FLOATING HEARTS ----
const heartsBg = document.getElementById('hearts-bg');
const heartEmojis = ['&#128151;','&#127800;','&#128156;','&#10024;','&#127872;','&#128149;','&#127801;','&#128171;'];
for (let i = 0; i < 16; i++) spawnHeart(true);
function spawnHeart(initial) {{
  const h = document.createElement('div');
  h.className = 'heart-float';
  h.innerHTML = heartEmojis[Math.floor(Math.random() * heartEmojis.length)];
  h.style.left = Math.random() * 100 + 'vw';
  const dur = 7 + Math.random() * 10;
  h.style.animationDuration = dur + 's';
  h.style.animationDelay = (initial ? Math.random() * 8 : 0) + 's';
  h.style.fontSize = (0.8 + Math.random() * 1.2) + 'rem';
  heartsBg.appendChild(h);
  setTimeout(() => {{ h.remove(); spawnHeart(false); }}, (dur + (initial ? Math.random()*8 : 0)) * 1000);
}}

// ---- CONFETTI ----
const canvas = document.getElementById('confetti-canvas');
const ctx = canvas.getContext('2d');
function resizeCanvas() {{ canvas.width = window.innerWidth; canvas.height = window.innerHeight; }}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);
let pieces = [], animId = null, confettiFadeTimer = null;
function launchConfetti() {{
  if (confettiFadeTimer) {{ clearTimeout(confettiFadeTimer); confettiFadeTimer = null; }}
  const colors = ['#e879a0','#a78bfa','#60a5fa','#fbbf24','#34d399','#f472b6','#fb923c'];
  for (let i = 0; i < 180; i++) {{
    pieces.push({{ x:Math.random()*canvas.width, y:-20-Math.random()*100, w:6+Math.random()*8, h:10+Math.random()*8,
      color:colors[Math.floor(Math.random()*colors.length)], speed:2+Math.random()*4,
      drift:(Math.random()-0.5)*2, spin:(Math.random()-0.5)*0.15, angle:Math.random()*Math.PI*2, opacity:0.85, fading:false }});
  }}
  if (!animId) animateConfetti();
  confettiFadeTimer = setTimeout(() => {{ pieces.forEach(p => p.fading = true); }}, 4000);
}}
function animateConfetti() {{
  ctx.clearRect(0,0,canvas.width,canvas.height);
  pieces = pieces.filter(p => p.opacity > 0.01 && p.y < canvas.height+30);
  pieces.forEach(p => {{
    p.y += p.speed; p.x += p.drift; p.angle += p.spin;
    if (p.fading) p.opacity = Math.max(0, p.opacity - 0.025);
    ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.angle);
    ctx.globalAlpha = p.opacity; ctx.fillStyle = p.color;
    ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h); ctx.restore();
  }});
  if (pieces.length > 0) {{ animId = requestAnimationFrame(animateConfetti); }}
  else {{ animId = null; ctx.clearRect(0,0,canvas.width,canvas.height); }}
}}
function heartShower() {{ for (let i = 0; i < 25; i++) setTimeout(() => spawnHeart(false), i * 80); }}

// ---- MESSAGE TOGGLE ----
let msgVisible = false;
function toggleMessage() {{
  const card = document.getElementById('msg-card');
  msgVisible = !msgVisible;
  if (msgVisible) {{ card.classList.remove('hidden'); card.classList.add('visible'); card.scrollIntoView({{behavior:'smooth',block:'start'}}); }}
  else {{ card.classList.remove('visible'); card.classList.add('hidden'); }}
}}

// ---- ROASTS ----
const roasts = [
  {{ emoji:'&#128557;', text:"threatens to slap me literally every other day and has never said sorry once" }},
  {{ emoji:'&#128221;', text:"wrote 4 whole pages for no reason at all and thinks tht's totally normal" }},
  {{ emoji:'&#128128;', text:"crashes out every single time geenuka gets mentioned. every. single. time." }},
  {{ emoji:'&#129408;', text:"wears black like it's her whole thing and honestly? fair. it works." }},
  {{ emoji:'&#129504;', text:"was the quietest nerd in cambridge 6 and now won't stop talking or threatening me" }},
];
let roastIdx = 0;
function nextRoast() {{
  const card = document.getElementById('fact-card');
  card.classList.add('switching');
  setTimeout(() => {{
    roastIdx = (roastIdx + 1) % roasts.length;
    document.getElementById('fact-emoji').innerHTML = roasts[roastIdx].emoji;
    document.getElementById('fact-text').textContent = roasts[roastIdx].text;
    document.getElementById('fact-counter').textContent = (roastIdx+1) + ' / ' + roasts.length;
    card.classList.remove('switching');
  }}, 250);
}}

// ---- COUNTDOWN ----
let devOffset = 0, devActive = false, bdayTriggered = false;
function devMode() {{
  const now = new Date(); const bday = getNextBirthday();
  devOffset = Math.floor((bday - now) / 1000) - 10;
  devActive = true; bdayTriggered = false; updateCountdown();
}}
function getNextBirthday() {{
  const now = new Date();
  let bday = new Date(now.getFullYear(), 7, 6, 0, 0, 0);
  if (now >= bday) bday.setFullYear(bday.getFullYear() + 1);
  return bday;
}}
function updateCountdown() {{
  const now = new Date(); const bday = getNextBirthday();
  let diff = Math.floor((bday - now) / 1000) - (devActive ? devOffset : 0);
  if (diff <= 0) {{
    document.getElementById('countdown-section').style.display = 'none';
    document.getElementById('bday-section').style.display = 'block';
    if (!bdayTriggered) {{ bdayTriggered = true; launchConfetti(); setTimeout(() => launchConfetti(), 600); }}
    return;
  }}
  bdayTriggered = false;
  document.getElementById('countdown-section').style.display = 'block';
  document.getElementById('bday-section').style.display = 'none';
  setNum('cd-days', Math.floor(diff/86400));
  setNum('cd-hours', Math.floor((diff%86400)/3600));
  setNum('cd-mins', Math.floor((diff%3600)/60));
  setNum('cd-secs', diff%60);
}}
let prevVals = {{}};
function setNum(id, val) {{
  const el = document.getElementById(id);
  const str = String(val).padStart(2,'0');
  if (prevVals[id] !== str) {{ el.classList.add('bump'); setTimeout(() => el.classList.remove('bump'), 150); prevVals[id] = str; }}
  el.textContent = str;
}}
updateCountdown(); setInterval(updateCountdown, 1000);

// ---- GAME ----
const questions = [
  {{ q:'are you the best bsf in the world? &#129402;', win:'obviously YES!! &#128151; correct answer lol' }},
  {{ q:'do u think ur funny? &#128557;', win:'she said yes &#128557;&#128151; ur actually so funny ugh' }},
  {{ q:'is geenuka kinda cute tho? &#128064;', win:'SHE SAID YES &#128557;&#128151; go talk to him!!' }},
  {{ q:'do i deserve a slap rn? &#129767;', win:'she said yes &#128128; fair enough honestly' }},
  {{ q:'are u having the best bday ever? &#127874;', win:'she said yes!! &#128151; good. as it should be &#127874;' }},
];
let qIdx = 0, noEscapes = 0, gameWon = false;
const noBtn = document.getElementById('no-btn');
const gameCard = document.getElementById('game-card');
function runAway() {{
  if (gameWon) return;
  noEscapes++;
  const size = Math.max(0.5, 0.82 - noEscapes * 0.04);
  noBtn.style.fontSize = size + 'rem';
  noBtn.style.padding = Math.max(0.3,0.75-noEscapes*0.04)+'rem '+Math.max(0.6,1.6-noEscapes*0.08)+'rem';
  const cardRect = gameCard.getBoundingClientRect();
  noBtn.style.left = (10 + Math.random() * Math.max(10, cardRect.width - 120)) + 'px';
  noBtn.style.top = (80 + Math.random() * Math.max(10, cardRect.height - 130)) + 'px';
  if (noEscapes >= 5) noBtn.textContent = 'noooo 😭';
  else if (noEscapes >= 3) noBtn.textContent = 'no... 🫣';
}}
function yesClicked() {{
  if (gameWon) return;
  gameWon = true;
  document.getElementById('game-btn-wrap').style.display = 'none';
  document.getElementById('game-sub').style.display = 'none';
  const result = document.getElementById('game-result');
  result.style.display = 'block';
  result.innerHTML = questions[qIdx].win;
  heartShower();
  setTimeout(() => {{
    qIdx = (qIdx + 1) % questions.length;
    gameWon = false; noEscapes = 0;
    noBtn.textContent = 'no'; noBtn.style.fontSize = '0.82rem';
    noBtn.style.padding = '0.75rem 1.6rem';
    noBtn.style.left = '50%'; noBtn.style.top = '60%';
    document.getElementById('game-question').innerHTML = questions[qIdx].q;
    document.getElementById('game-sub').style.display = 'block';
    document.getElementById('game-sub').textContent = 'choose wisely';
    document.getElementById('game-btn-wrap').style.display = 'flex';
    result.style.display = 'none';
  }}, 2500);
}}
</script>
</body>
</html>"""

components.html(html, height=3400, scrolling=True)
