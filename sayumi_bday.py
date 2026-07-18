import streamlit as st
from datetime import datetime, date
import math

st.set_page_config(
    page_title="Happy Birthday Sayumi 🎂",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

* { font-family: 'DM Sans', sans-serif; box-sizing: border-box; }

.stApp {
    background: linear-gradient(135deg, #fff0f5 0%, #fef9ff 40%, #f0f4ff 100%);
    overflow-x: hidden;
}

/* ---- CONFETTI CANVAS ---- */
#confetti-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 9999;
}

/* ---- FLOATING HEARTS BG ---- */
.hearts-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.heart-float {
    position: absolute;
    font-size: 1.2rem;
    animation: floatUp linear infinite;
    opacity: 0;
}

@keyframes floatUp {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 0.6; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}

/* ---- HERO ---- */
.hero {
    text-align: center;
    padding: 3rem 1rem 1rem;
    position: relative;
    z-index: 1;
    animation: fadeSlideDown 1s ease both;
}

@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

.hero-tag {
    font-size: 0.7rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #c084a0;
    margin-bottom: 1rem;
    font-weight: 500;
    animation: fadeIn 1.5s ease both;
}

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 10vw, 6rem);
    font-weight: 900;
    background: linear-gradient(135deg, #e879a0, #a78bfa, #60a5fa);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    animation: gradientShift 4s ease infinite, fadeSlideDown 1s ease both;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.hero-sub {
    font-size: 1.1rem;
    color: #9d6b8a;
    font-weight: 300;
    animation: fadeIn 2s ease both;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* ---- COUNTDOWN ---- */
.countdown-wrap {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 2rem 0;
    flex-wrap: wrap;
    animation: fadeSlideUp 1.2s ease both;
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.cd-box {
    background: white;
    border-radius: 20px;
    padding: 1.2rem 1.5rem;
    min-width: 80px;
    text-align: center;
    box-shadow: 0 4px 24px rgba(232, 121, 160, 0.15);
    border: 1px solid rgba(232, 121, 160, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: default;
}

.cd-box:hover {
    transform: translateY(-6px) scale(1.05);
    box-shadow: 0 12px 40px rgba(232, 121, 160, 0.25);
}

.cd-num {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #e879a0;
    line-height: 1;
    display: block;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.04); }
}

.cd-label {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #c084a0;
    margin-top: 4px;
    display: block;
}

/* ---- EMOJI ROW ---- */
.emoji-row {
    text-align: center;
    font-size: 1.8rem;
    letter-spacing: 8px;
    margin: 1.5rem 0;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

/* ---- PHOTO GRID ---- */
.photo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin: 2rem 0;
    animation: fadeSlideUp 1.5s ease both;
}

.photo-placeholder {
    aspect-ratio: 1;
    background: linear-gradient(135deg, #fce7f0, #ede9fe);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    border: 2px dashed rgba(232, 121, 160, 0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.photo-placeholder:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 0 8px 30px rgba(232, 121, 160, 0.2);
}

/* ---- MESSAGE CARD ---- */
.msg-card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 40px rgba(167, 139, 250, 0.12);
    border: 1px solid rgba(167, 139, 250, 0.15);
    position: relative;
    z-index: 1;
    animation: fadeSlideUp 1.8s ease both;
    transition: box-shadow 0.3s ease;
}

.msg-card:hover {
    box-shadow: 0 16px 60px rgba(167, 139, 250, 0.2);
}

.msg-quote {
    font-size: 4rem;
    color: #f0abca;
    font-family: 'Playfair Display', serif;
    line-height: 0.5;
    margin-bottom: 1rem;
}

.msg-text {
    font-size: 0.95rem;
    line-height: 1.9;
    color: #6b4f6b;
    font-weight: 300;
}

.msg-sign {
    margin-top: 1.5rem;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #c084a0;
    font-size: 1rem;
}

/* ---- SPECIAL BUTTONS ---- */
.btn-row {
    display: flex;
    gap: 12px;
    justify-content: center;
    flex-wrap: wrap;
    margin: 2rem 0;
    position: relative;
    z-index: 1;
}

.special-btn {
    background: linear-gradient(135deg, #e879a0, #a78bfa);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 0.8rem 1.8rem;
    font-size: 0.85rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 4px 20px rgba(232, 121, 160, 0.3);
    letter-spacing: 0.5px;
}

.special-btn:hover {
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 8px 30px rgba(232, 121, 160, 0.4);
}

.special-btn:active {
    transform: scale(0.97);
}

.special-btn.outline {
    background: white;
    color: #e879a0;
    border: 2px solid #e879a0;
    box-shadow: none;
}

.special-btn.outline:hover {
    background: #fff0f5;
    box-shadow: 0 4px 20px rgba(232, 121, 160, 0.15);
}

/* ---- FUN FACTS CARD ---- */
.fact-card {
    background: linear-gradient(135deg, #fdf2f8, #faf5ff);
    border-radius: 20px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
    text-align: center;
    border: 1px solid rgba(232, 121, 160, 0.15);
    animation: fadeIn 0.5s ease both;
    transition: transform 0.3s ease;
    position: relative;
    z-index: 1;
}

.fact-card:hover { transform: scale(1.01); }

.fact-emoji { font-size: 2.5rem; margin-bottom: 0.5rem; }
.fact-text { color: #6b4f6b; font-size: 0.95rem; line-height: 1.7; }

/* ---- BIRTHDAY BANNER ---- */
.bday-banner {
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #fce7f0, #ede9fe, #dbeafe);
    border-radius: 24px;
    margin: 2rem 0;
    animation: shimmer 3s ease-in-out infinite;
    position: relative;
    z-index: 1;
}

@keyframes shimmer {
    0%, 100% { box-shadow: 0 0 30px rgba(232, 121, 160, 0.2); }
    50% { box-shadow: 0 0 60px rgba(167, 139, 250, 0.4); }
}

.bday-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    background: linear-gradient(135deg, #e879a0, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: float 2s ease-in-out infinite;
}

/* ---- FOOTER ---- */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    color: #c084a0;
    font-size: 0.75rem;
    letter-spacing: 1px;
    position: relative;
    z-index: 1;
}

/* ---- SPARKLE ---- */
.sparkle {
    display: inline-block;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 680px; }
</style>

<!-- Floating hearts background -->
<div class="hearts-bg" id="hearts-bg"></div>

<!-- Confetti canvas -->
<canvas id="confetti-canvas"></canvas>

<script>
// ---- FLOATING HEARTS ----
const heartsBg = document.getElementById('hearts-bg');
const heartEmojis = ['💗','🌸','💜','✨','🎀','💕','🌷','💫'];
for (let i = 0; i < 18; i++) {
    const h = document.createElement('div');
    h.className = 'heart-float';
    h.textContent = heartEmojis[Math.floor(Math.random() * heartEmojis.length)];
    h.style.left = Math.random() * 100 + 'vw';
    h.style.animationDuration = (6 + Math.random() * 10) + 's';
    h.style.animationDelay = (Math.random() * 8) + 's';
    h.style.fontSize = (0.8 + Math.random() * 1.2) + 'rem';
    heartsBg.appendChild(h);
}

// ---- CONFETTI ----
const canvas = document.getElementById('confetti-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let confettiPieces = [];
let confettiActive = false;

function createConfetti() {
    confettiPieces = [];
    const colors = ['#e879a0','#a78bfa','#60a5fa','#fbbf24','#34d399','#f472b6'];
    for (let i = 0; i < 150; i++) {
        confettiPieces.push({
            x: Math.random() * canvas.width,
            y: -10,
            w: 6 + Math.random() * 8,
            h: 10 + Math.random() * 8,
            color: colors[Math.floor(Math.random() * colors.length)],
            speed: 2 + Math.random() * 4,
            drift: (Math.random() - 0.5) * 2,
            spin: Math.random() * 0.2,
            angle: 0,
            opacity: 0.8 + Math.random() * 0.2
        });
    }
    confettiActive = true;
    animateConfetti();
}

function animateConfetti() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let alive = false;
    confettiPieces.forEach(p => {
        if (p.y < canvas.height + 20) {
            alive = true;
            p.y += p.speed;
            p.x += p.drift;
            p.angle += p.spin;
            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate(p.angle);
            ctx.globalAlpha = p.opacity;
            ctx.fillStyle = p.color;
            ctx.fillRect(-p.w/2, -p.h/2, p.w, p.h);
            ctx.restore();
        }
    });
    if (alive) requestAnimationFrame(animateConfetti);
    else { ctx.clearRect(0, 0, canvas.width, canvas.height); confettiActive = false; }
}

window.launchConfetti = createConfetti;
window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });
</script>
""", unsafe_allow_html=True)

# --- COUNTDOWN LOGIC ---
today = date.today()
birthday_2026 = date(2026, 8, 6)
if today > birthday_2026:
    birthday_2026 = date(2027, 8, 6)

delta = birthday_2026 - today
days_left = delta.days
weeks_left = days_left // 7
days_remaining = days_left % 7
hours_left = days_left * 24
is_birthday = (today.month == 8 and today.day == 6)

# --- HERO ---
st.markdown("""
<div class="hero">
    <div class="hero-tag">✦ a little something for you ✦</div>
    <div class="hero-name">Sayumi</div>
    <div class="hero-sub">turning 14 · august 6th <span class="sparkle">✨</span></div>
</div>
""", unsafe_allow_html=True)

# --- COUNTDOWN or BIRTHDAY ---
if is_birthday:
    st.markdown("""
    <div class="bday-banner">
        <div class="bday-title">🎂 IT'S YOUR DAY!! 🎂</div>
        <p style="color:#9d6b8a; margin-top:1rem; font-size:1rem;">Happy Birthday Sayumi 💗 hope it's the most amazing one yet</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div style="text-align:center; margin-bottom: 0.5rem; position:relative; z-index:1;">
        <span style="font-size:0.7rem; letter-spacing:3px; text-transform:uppercase; color:#c084a0;">countdown to the big day 🎀</span>
    </div>
    <div class="countdown-wrap">
        <div class="cd-box">
            <span class="cd-num">{days_left}</span>
            <span class="cd-label">Days</span>
        </div>
        <div class="cd-box">
            <span class="cd-num">{weeks_left}</span>
            <span class="cd-label">Weeks</span>
        </div>
        <div class="cd-box">
            <span class="cd-num">{days_remaining}</span>
            <span class="cd-label">Extra days</span>
        </div>
        <div class="cd-box">
            <span class="cd-num">{hours_left:,}</span>
            <span class="cd-label">Hours</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- EMOJI ROW ---
st.markdown('<div class="emoji-row">🎂 💗 🎉 🫶 🥹</div>', unsafe_allow_html=True)

# --- BUTTONS ---
st.markdown("""
<div class="btn-row">
    <button class="special-btn" onclick="launchConfetti()">🎉 Launch Confetti!</button>
    <button class="special-btn outline" onclick="toggleMessage()">💌 Read Message</button>
    <button class="special-btn" onclick="makeItRain()">💗 Heart Shower</button>
</div>

<script>
function toggleMessage() {
    const msg = document.getElementById('msg-card-reveal');
    if (msg) {
        msg.style.display = msg.style.display === 'none' ? 'block' : 'none';
    }
}

function makeItRain() {
    const heartsBg = document.getElementById('hearts-bg');
    for (let i = 0; i < 20; i++) {
        setTimeout(() => {
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.textContent = ['💗','💜','💕','🌸','✨'][Math.floor(Math.random()*5)];
            h.style.left = Math.random() * 100 + 'vw';
            h.style.animationDuration = (2 + Math.random() * 3) + 's';
            h.style.animationDelay = '0s';
            h.style.fontSize = (1.5 + Math.random() * 2) + 'rem';
            heartsBg.appendChild(h);
            setTimeout(() => h.remove(), 5000);
        }, i * 100);
    }
}
</script>
""", unsafe_allow_html=True)

# --- FUN FACTS ---
st.markdown("""
<div style="text-align:center; margin: 1.5rem 0 0.5rem; position:relative; z-index:1;">
    <span style="font-size:0.7rem; letter-spacing:3px; text-transform:uppercase; color:#c084a0;">reasons ur actually the worst 😭</span>
</div>
""", unsafe_allow_html=True)

facts = [
    ("😭", "threatens to slap me literally every other day and has never once apologized"),
    ("📝", "wrote 4 whole pages for absolutely no reason and thinks tht's normal"),
    ("💀", "crashes out completely every time geenuka gets mentioned"),
    ("🖤", "wears black like it's a personality trait and honestly fair enough"),
    ("🧠", "was the quietest nerd in cambridge 6 and now won't stop talking"),
]

if 'fact_idx' not in st.session_state:
    st.session_state.fact_idx = 0

emoji, text = facts[st.session_state.fact_idx]
st.markdown(f"""
<div class="fact-card">
    <div class="fact-emoji">{emoji}</div>
    <div class="fact-text">{text}</div>
    <div style="color:#c084a0; font-size:0.7rem; margin-top:0.8rem;">{st.session_state.fact_idx + 1} / {len(facts)}</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("next roast 😂", use_container_width=True):
        st.session_state.fact_idx = (st.session_state.fact_idx + 1) % len(facts)
        st.rerun()

# --- PHOTO GRID ---
st.markdown("""
<div style="text-align:center; margin: 1.5rem 0 0.5rem; position:relative; z-index:1;">
    <span style="font-size:0.7rem; letter-spacing:3px; text-transform:uppercase; color:#c084a0;">some memories 🎀</span>
</div>
<div class="photo-grid">
    <div class="photo-placeholder">📸</div>
    <div class="photo-placeholder">🌸</div>
    <div class="photo-placeholder">📸</div>
    <div class="photo-placeholder">🌺</div>
    <div class="photo-placeholder">📸</div>
    <div class="photo-placeholder">🌷</div>
</div>
""", unsafe_allow_html=True)

# --- MESSAGE ---
st.markdown("""
<div class="msg-card" id="msg-card-reveal">
    <div class="msg-quote">"</div>
    <div class="msg-text">
        happy birthday sayumi 💗🎂 ur officially old now and i hope ur enjoying the slow descent into ancient history lmao. i still remember cambridge 6, the quiet nerd in the corner who wouldn't say a word to anyone, BUT NOT NOW OKK?? now she threatens to slap me on a daily basis and somehow tht's become one of my favorite things about her 😭<br><br>
        and listen ik i've been a bit distant lately and i already apologized for tht, but i need u to know tht has never once changed how much u mean to me. u wrote me 4 whole pages once for jz no reason and i think about tht more than u know, cuz tht's jz the kind of person u are. u give so much without even thinking about it and i genuinely don't say this enough but i'm so grateful to have u in my life. like actually grateful, not jz saying it. u've been there through sm and i don't take tht lightly 🥹<br><br>
        the kind of bsf tht checks on u, roasts u, threatens to physically assault u, and somehow still makes u feel like the luckiest person in the room 😂🫶<br><br>
        have the best birthday okay. wear black obviously. eat way too much cake. and for the love of everything please jz talk to geenuka already ur going to give yourself a heart attack every time i mention his name 😭💙<br><br>
        cheers to u being a bit older, more unbothered and still living in the same era as me 🎂🫶🥹
    </div>
    <div class="msg-sign">— ur bsf, always 💗</div>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div class="footer">made with 💗 · for sayumi · august 6th 2026</div>', unsafe_allow_html=True)
