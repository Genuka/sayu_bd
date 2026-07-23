<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday Sayumi 🎂</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'DM Sans', sans-serif;
    background: linear-gradient(135deg, #fff0f5 0%, #fef9ff 40%, #f0f4ff 100%);
    min-height: 100vh;
    overflow-x: hidden;
}

#confetti-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 9999;
}

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
    animation: floatUp linear infinite;
    opacity: 0;
}

@keyframes floatUp {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 0.7; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}

.container {
    max-width: 680px;
    margin: 0 auto;
    padding: 2rem 1.2rem 4rem;
    position: relative;
    z-index: 1;
}

/* HERO */
.hero {
    text-align: center;
    padding: 3rem 1rem 1.5rem;
    animation: fadeSlideDown 1s ease both;
}

.hero-tag {
    font-size: 0.7rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #c084a0;
    margin-bottom: 1rem;
}

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3.5rem, 12vw, 6.5rem);
    font-weight: 900;
    background: linear-gradient(135deg, #e879a0, #a78bfa, #60a5fa, #e879a0);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    animation: gradientShift 4s ease infinite, fadeSlideDown 1s ease both;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.hero-sub {
    font-size: 1.05rem;
    color: #9d6b8a;
    font-weight: 300;
    margin-top: 0.5rem;
}

/* COUNTDOWN */
.section-label {
    text-align: center;
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #c084a0;
    margin: 2rem 0 0.8rem;
}

.countdown-wrap {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    animation: fadeSlideUp 1.2s ease both;
}

.cd-box {
    background: white;
    border-radius: 20px;
    padding: 1.2rem 1.4rem;
    min-width: 75px;
    text-align: center;
    box-shadow: 0 4px 24px rgba(232,121,160,0.15);
    border: 1px solid rgba(232,121,160,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: default;
}

.cd-box:hover {
    transform: translateY(-6px) scale(1.06);
    box-shadow: 0 12px 40px rgba(232,121,160,0.28);
}

.cd-num {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #e879a0;
    line-height: 1;
    display: block;
    transition: transform 0.15s ease;
}

.cd-num.bump {
    transform: scale(1.2);
    color: #a78bfa;
}

.cd-label {
    font-size: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #c084a0;
    margin-top: 4px;
    display: block;
}

/* EMOJI ROW */
.emoji-row {
    text-align: center;
    font-size: 1.6rem;
    letter-spacing: 8px;
    margin: 1.8rem 0;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

/* BUTTONS */
.btn-row {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
    margin: 1.5rem 0;
}

.btn {
    border: none;
    border-radius: 50px;
    padding: 0.75rem 1.6rem;
    font-size: 0.82rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    letter-spacing: 0.3px;
}

.btn-primary {
    background: linear-gradient(135deg, #e879a0, #a78bfa);
    color: white;
    box-shadow: 0 4px 20px rgba(232,121,160,0.3);
}

.btn-primary:hover {
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 8px 30px rgba(232,121,160,0.4);
}

.btn-primary:active { transform: scale(0.96); }

.btn-outline {
    background: white;
    color: #e879a0;
    border: 2px solid #e879a0;
}

.btn-outline:hover {
    background: #fff0f5;
    transform: translateY(-3px);
    box-shadow: 0 4px 20px rgba(232,121,160,0.15);
}

.btn-dev {
    background: #1e1e2e;
    color: #a78bfa;
    border: 1px dashed #a78bfa55;
    font-size: 0.72rem;
    padding: 0.6rem 1.2rem;
}

.btn-dev:hover {
    background: #2a2440;
    transform: translateY(-2px);
}

/* ROAST CARD */
.fact-card {
    background: linear-gradient(135deg, #fdf2f8, #faf5ff);
    border-radius: 20px;
    padding: 1.5rem 2rem;
    text-align: center;
    border: 1px solid rgba(232,121,160,0.15);
    transition: transform 0.3s ease, opacity 0.3s ease;
    min-height: 120px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.fact-card.switching {
    opacity: 0;
    transform: scale(0.95);
}

.fact-emoji { font-size: 2.2rem; }
.fact-text { color: #6b4f6b; font-size: 0.92rem; line-height: 1.7; }
.fact-counter { color: #c084a0; font-size: 0.65rem; letter-spacing: 1px; margin-top: 4px; }

/* GAME */
.game-card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 8px 40px rgba(232,121,160,0.12);
    border: 1px solid rgba(232,121,160,0.18);
    margin: 1rem 0;
    min-height: 160px;
    position: relative;
    overflow: visible;
}

.game-question {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: #6b4f6b;
    margin-bottom: 0.4rem;
}

.game-sub {
    font-size: 0.75rem;
    color: #c084a0;
    letter-spacing: 1px;
    margin-bottom: 1.5rem;
}

.game-btn-wrap {
    display: flex;
    gap: 16px;
    justify-content: center;
    align-items: center;
    position: relative;
    min-height: 48px;
}

.game-yes {
    flex-shrink: 0;
}

.btn-no {
    background: white;
    color: #9d6b8a;
    border: 2px solid #e0b4c8;
    border-radius: 50px;
    padding: 0.75rem 1.6rem;
    font-size: 0.82rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    cursor: pointer;
    position: absolute;
    transition: font-size 0.2s ease;
    white-space: nowrap;
}

.game-result {
    font-size: 1.1rem;
    color: #e879a0;
    font-family: 'Playfair Display', serif;
    margin-top: 1rem;
    animation: fadeSlideUp 0.5s ease both;
}

.photo-img {
    aspect-ratio: 1;
    object-fit: cover;
    border-radius: 16px;
    width: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.photo-img:hover {
    transform: scale(1.06) rotate(2deg);
    box-shadow: 0 8px 30px rgba(232,121,160,0.2);
}

/* PHOTO GRID */
.photo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin: 1rem 0;
}

.photo-placeholder {
    aspect-ratio: 1;
    background: linear-gradient(135deg, #fce7f0, #ede9fe);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    border: 2px dashed rgba(232,121,160,0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.photo-placeholder:hover {
    transform: scale(1.06) rotate(2deg);
    box-shadow: 0 8px 30px rgba(232,121,160,0.2);
}

/* MESSAGE */
.msg-card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 40px rgba(167,139,250,0.12);
    border: 1px solid rgba(167,139,250,0.18);
    transition: box-shadow 0.3s ease, max-height 0.6s ease, opacity 0.4s ease;
    overflow: hidden;
}

.msg-card:hover {
    box-shadow: 0 16px 60px rgba(167,139,250,0.22);
}

.msg-card.hidden {
    max-height: 0;
    opacity: 0;
    padding: 0;
    margin: 0;
    border: none;
}

.msg-card.visible {
    max-height: 2000px;
    opacity: 1;
}

.msg-quote {
    font-size: 4rem;
    color: #f0abca;
    font-family: 'Playfair Display', serif;
    line-height: 0.5;
    margin-bottom: 1rem;
}

.msg-text {
    font-size: 0.93rem;
    line-height: 1.95;
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

/* BIRTHDAY BANNER */
.bday-banner {
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #fce7f0, #ede9fe, #dbeafe);
    border-radius: 24px;
    animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { box-shadow: 0 0 30px rgba(232,121,160,0.2); }
    50% { box-shadow: 0 0 60px rgba(167,139,250,0.4); }
}

.bday-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    background: linear-gradient(135deg, #e879a0, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: float 2s ease-in-out infinite;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 2.5rem 0 1rem;
    color: #c084a0;
    font-size: 0.72rem;
    letter-spacing: 1px;
}

/* DEV BADGE */
.dev-badge {
    display: inline-block;
    background: #1e1e2e;
    color: #a78bfa;
    font-size: 0.6rem;
    font-family: monospace;
    padding: 2px 8px;
    border-radius: 4px;
    margin-left: 6px;
    vertical-align: middle;
    border: 1px solid #a78bfa44;
}

@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
</head>
<body>

<canvas id="confetti-canvas"></canvas>
<div class="hearts-bg" id="hearts-bg"></div>

<div class="container">

    <!-- HERO -->
    <div class="hero">
        <div class="hero-tag">✦ a little something for you ✦</div>
        <div class="hero-name">Sayumi</div>
        <div class="hero-sub">turning 14 · august 6th ✨</div>
    </div>

    <!-- COUNTDOWN / BIRTHDAY -->
    <div id="countdown-section">
        <div class="section-label">countdown to the big day 🎀</div>
        <div class="countdown-wrap">
            <div class="cd-box"><span class="cd-num" id="cd-days">--</span><span class="cd-label">Days</span></div>
            <div class="cd-box"><span class="cd-num" id="cd-hours">--</span><span class="cd-label">Hours</span></div>
            <div class="cd-box"><span class="cd-num" id="cd-mins">--</span><span class="cd-label">Minutes</span></div>
            <div class="cd-box"><span class="cd-num" id="cd-secs">--</span><span class="cd-label">Seconds</span></div>
        </div>
    </div>

    <div id="bday-section" style="display:none;">
        <div class="bday-banner">
            <div class="bday-title">🎂 IT'S YOUR DAY!! 🎂</div>
            <p style="color:#9d6b8a; margin-top:1rem;">Happy Birthday Sayumi 💗 hope it's the most amazing one yet</p>
        </div>
    </div>

    <!-- EMOJI ROW -->
    <div class="emoji-row">🎂 💗 🎉 🫶 🥹</div>

    <!-- BUTTONS -->
    <div class="btn-row">
        <button class="btn btn-primary" onclick="launchConfetti()">🎉 Confetti!</button>
        <button class="btn btn-outline" onclick="toggleMessage()">💌 Read Message</button>
        <button class="btn btn-primary" onclick="heartShower()">💗 Heart Shower</button>
    </div>
    <div class="btn-row">
        <button class="btn btn-dev" onclick="devMode()">⚙️ dev: reset to 10s <span class="dev-badge">DEV</span></button>
    </div>

    <!-- ROAST CAROUSEL -->
    <div class="section-label">reasons ur actually the worst 😭</div>
    <div class="fact-card" id="fact-card">
        <div class="fact-emoji" id="fact-emoji">😭</div>
        <div class="fact-text" id="fact-text">threatens to slap me literally every other day and has never once apologized</div>
        <div class="fact-counter" id="fact-counter">1 / 5</div>
    </div>
    <div class="btn-row" style="margin-top:10px;">
        <button class="btn btn-outline" onclick="nextRoast()">next roast 😂</button>
    </div>

    <!-- PHOTO GRID -->
    <div class="section-label">ur camera roll era 📸</div>
    <div class="photo-grid" id="photo-grid">
        <div class="photo-placeholder">📸</div>
        <div class="photo-placeholder">🌸</div>
        <div class="photo-placeholder">📸</div>
        <div class="photo-placeholder">🌺</div>
        <div class="photo-placeholder">🌷</div>
        <div class="photo-placeholder">💗</div>
    </div>

    <!-- FLEEING NO BUTTON GAME -->
    <div class="section-label">one important question 🎀</div>
    <div class="game-card" id="game-card">
        <div class="game-question" id="game-question">are you the best bsf in the world? 🥺</div>
        <div class="game-sub" id="game-sub">choose wisely</div>
        <div class="game-btn-wrap" id="game-btn-wrap">
            <button class="btn btn-primary game-yes" onclick="yesClicked()">yes 💗</button>
            <button class="btn btn-no" id="no-btn" onmouseover="runAway()" ontouchstart="runAway()">no</button>
        </div>
        <div class="game-result" id="game-result" style="display:none"></div>
    </div>

    <!-- MESSAGE -->
    <div class="msg-card hidden" id="msg-card">
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

    <div class="footer">made with 💗 · for sayumi · august 6th 2026</div>
</div>

<script>
// ---- FLOATING HEARTS BG ----
const heartsBg = document.getElementById('hearts-bg');
const heartEmojis = ['💗','🌸','💜','✨','🎀','💕','🌷','💫'];
for (let i = 0; i < 16; i++) {
    spawnHeart(heartsBg, true);
}

function spawnHeart(container, initial) {
    const h = document.createElement('div');
    h.className = 'heart-float';
    h.textContent = heartEmojis[Math.floor(Math.random() * heartEmojis.length)];
    h.style.left = Math.random() * 100 + 'vw';
    const dur = 7 + Math.random() * 10;
    h.style.animationDuration = dur + 's';
    h.style.animationDelay = (initial ? Math.random() * 8 : 0) + 's';
    h.style.fontSize = (0.8 + Math.random() * 1.2) + 'rem';
    container.appendChild(h);
    setTimeout(() => { h.remove(); spawnHeart(container, false); }, (dur + (initial ? Math.random()*8 : 0)) * 1000);
}

// ---- CONFETTI ----
const canvas = document.getElementById('confetti-canvas');
const ctx = canvas.getContext('2d');
function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

let pieces = [];
let animId = null;
let confettiFadeTimer = null;

function launchConfetti() {
    // Clear any existing fade timer
    if (confettiFadeTimer) { clearTimeout(confettiFadeTimer); confettiFadeTimer = null; }

    const colors = ['#e879a0','#a78bfa','#60a5fa','#fbbf24','#34d399','#f472b6','#fb923c'];
    for (let i = 0; i < 180; i++) {
        pieces.push({
            x: Math.random() * canvas.width,
            y: -20 - Math.random() * 100,
            w: 6 + Math.random() * 8,
            h: 10 + Math.random() * 8,
            color: colors[Math.floor(Math.random() * colors.length)],
            speed: 2 + Math.random() * 4,
            drift: (Math.random() - 0.5) * 2,
            spin: (Math.random() - 0.5) * 0.15,
            angle: Math.random() * Math.PI * 2,
            opacity: 0.85,
            fading: false
        });
    }
    if (!animId) animateConfetti();

    // Start fading after 4 seconds
    confettiFadeTimer = setTimeout(() => {
        pieces.forEach(p => p.fading = true);
    }, 4000);
}

function animateConfetti() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pieces = pieces.filter(p => p.opacity > 0.01 && p.y < canvas.height + 30);
    pieces.forEach(p => {
        p.y += p.speed;
        p.x += p.drift;
        p.angle += p.spin;
        if (p.fading) p.opacity = Math.max(0, p.opacity - 0.025);
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(p.angle);
        ctx.globalAlpha = p.opacity;
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.w/2, -p.h/2, p.w, p.h);
        ctx.restore();
    });
    if (pieces.length > 0) {
        animId = requestAnimationFrame(animateConfetti);
    } else {
        animId = null;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
}

// ---- HEART SHOWER ----
function heartShower() {
    for (let i = 0; i < 25; i++) {
        setTimeout(() => spawnHeart(heartsBg, false), i * 80);
    }
}

// ---- TOGGLE MESSAGE ----
let msgVisible = false;
function toggleMessage() {
    const card = document.getElementById('msg-card');
    msgVisible = !msgVisible;
    if (msgVisible) {
        card.classList.remove('hidden');
        card.classList.add('visible');
        card.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
        card.classList.remove('visible');
        card.classList.add('hidden');
    }
}

// ---- ROAST CAROUSEL ----
const roasts = [
    { emoji: '😭', text: 'threatens to slap me literally every other day and has never once apologized' },
    { emoji: '📝', text: 'wrote 4 whole pages for absolutely no reason and thinks tht\'s normal behaviour' },
    { emoji: '💀', text: 'crashes out completely every single time geenuka gets mentioned. every. single. time.' },
    { emoji: '🖤', text: 'wears black like it\'s a full personality and honestly? fair enough. it works.' },
    { emoji: '🧠', text: 'was the quietest nerd in cambridge 6 and now genuinely won\'t stop talking or threatening me' },
];
let roastIdx = 0;

function nextRoast() {
    const card = document.getElementById('fact-card');
    card.classList.add('switching');
    setTimeout(() => {
        roastIdx = (roastIdx + 1) % roasts.length;
        document.getElementById('fact-emoji').textContent = roasts[roastIdx].emoji;
        document.getElementById('fact-text').textContent = roasts[roastIdx].text;
        document.getElementById('fact-counter').textContent = `${roastIdx + 1} / ${roasts.length}`;
        card.classList.remove('switching');
    }, 250);
}

// ---- COUNTDOWN ----
let devOffset = 0;
let devActive = false;

function devMode() {
    const now = new Date();
    const bday = getNextBirthday();
    const normalDiff = Math.floor((bday - now) / 1000);
    devOffset = normalDiff - 10;
    devActive = true;
    bdayTriggered = false;
    updateCountdown();
}

function getNextBirthday() {
    const now = new Date();
    let bday = new Date(now.getFullYear(), 7, 6, 0, 0, 0); // Aug 6
    if (now >= bday) bday.setFullYear(bday.getFullYear() + 1);
    return bday;
}

let bdayTriggered = false;

function updateCountdown() {
    const now = new Date();
    const bday = getNextBirthday();
    let diff = Math.floor((bday - now) / 1000) - (devActive ? devOffset : 0);

    if (diff <= 0) {
        document.getElementById('countdown-section').style.display = 'none';
        document.getElementById('bday-section').style.display = 'block';
        if (!bdayTriggered) {
            bdayTriggered = true;
            launchConfetti();
            setTimeout(() => launchConfetti(), 600);
        }
        return;
    }

    bdayTriggered = false;

    document.getElementById('countdown-section').style.display = 'block';
    document.getElementById('bday-section').style.display = 'none';

    const days = Math.floor(diff / 86400);
    const hours = Math.floor((diff % 86400) / 3600);
    const mins = Math.floor((diff % 3600) / 60);
    const secs = diff % 60;

    setNum('cd-days', days);
    setNum('cd-hours', hours);
    setNum('cd-mins', mins);
    setNum('cd-secs', secs);
}

let prevVals = {};
function setNum(id, val) {
    const el = document.getElementById(id);
    const str = String(val).padStart(2, '0');
    if (prevVals[id] !== str) {
        el.classList.add('bump');
        setTimeout(() => el.classList.remove('bump'), 150);
        prevVals[id] = str;
    }
    el.textContent = str;
}

updateCountdown();
setInterval(updateCountdown, 1000);

// ---- PHOTO LOADER ----
const photoFiles = ['photo1.jpg','photo2.jpg','photo3.jpg','photo4.jpg'];
const grid = document.getElementById('photo-grid');
grid.innerHTML = '';
photoFiles.forEach(f => {
    const img = document.createElement('img');
    img.src = f;
    img.className = 'photo-img';
    img.alt = 'selfie 📸';
    const placeholder = document.createElement('div');
    placeholder.className = 'photo-placeholder';
    placeholder.textContent = '📸';
    placeholder.style.display = 'none';
    img.onerror = () => { img.style.display = 'none'; placeholder.style.display = 'flex'; };
    grid.appendChild(img);
    grid.appendChild(placeholder);
});
// fill remaining slots
const loaded = photoFiles.length;
const extras = ['🌸','💗'];
extras.forEach(e => {
    const d = document.createElement('div');
    d.className = 'photo-placeholder';
    d.textContent = e;
    grid.appendChild(d);
});

// ---- FLEEING NO BUTTON GAME ----
const questions = [
    { q: 'are you the best bsf in the world? 🥺', win: 'obviously YES!! 💗 correct answer lol' },
    { q: 'do u think ur funny? 😭', win: 'she said yes 😭💗 ur actually so funny ugh' },
    { q: 'is geenuka kinda cute tho? 👀', win: 'SHE SAID YES 😭💗 go talk to him!!' },
    { q: 'do i deserve a slap rn? 🫣', win: 'she said yes 💀 fair enough honestly' },
    { q: 'are u having the best bday ever? 🎂', win: 'she said yes!! 💗 good. as it should be 🎂' },
];
let qIdx = 0;
let noEscapes = 0;
let gameWon = false;

const noBtn = document.getElementById('no-btn');
const gameCard = document.getElementById('game-card');

function runAway() {
    if (gameWon) return;
    noEscapes++;

    // shrink no button text over time
    const size = Math.max(0.5, 0.82 - noEscapes * 0.04);
    noBtn.style.fontSize = size + 'rem';
    noBtn.style.padding = `${Math.max(0.3, 0.75 - noEscapes*0.04)}rem ${Math.max(0.6, 1.6 - noEscapes*0.08)}rem`;

    // find a random position within the game card that doesn't overlap yes button
    const cardRect = gameCard.getBoundingClientRect();
    const noBtnRect = noBtn.getBoundingClientRect();
    const maxX = cardRect.width - noBtnRect.width - 20;
    const maxY = cardRect.height - noBtnRect.height - 10;

    let newX, newY, attempts = 0;
    do {
        newX = 10 + Math.random() * Math.max(10, maxX);
        newY = 80 + Math.random() * Math.max(10, maxY - 80);
        attempts++;
    } while (attempts < 20);

    noBtn.style.position = 'absolute';
    noBtn.style.left = newX + 'px';
    noBtn.style.top = newY + 'px';
    noBtn.style.transition = 'left 0.15s ease, top 0.15s ease, font-size 0.2s ease';

    if (noEscapes >= 5) {
        noBtn.textContent = 'noooo 😭';
    } else if (noEscapes >= 3) {
        noBtn.textContent = 'no... 🫣';
    }
}

function yesClicked() {
    if (gameWon) return;
    const result = document.getElementById('game-result');
    const wrap = document.getElementById('game-btn-wrap');
    const sub = document.getElementById('game-sub');

    gameWon = true;
    wrap.style.display = 'none';
    sub.style.display = 'none';
    result.style.display = 'block';
    result.textContent = questions[qIdx].win;
    heartShower();

    // after 2.5s go to next question
    setTimeout(() => {
        qIdx = (qIdx + 1) % questions.length;
        gameWon = false;
        noEscapes = 0;
        noBtn.textContent = 'no';
        noBtn.style.fontSize = '0.82rem';
        noBtn.style.padding = '0.75rem 1.6rem';
        noBtn.style.position = 'absolute';
        noBtn.style.left = '';
        noBtn.style.top = '';
        noBtn.style.transition = 'none';
        document.getElementById('game-question').textContent = questions[qIdx].q;
        sub.style.display = 'block';
        sub.textContent = 'choose wisely';
        wrap.style.display = 'flex';
        result.style.display = 'none';

        // reset no btn position
        setTimeout(() => {
            noBtn.style.position = 'relative';
            noBtn.style.left = 'auto';
            noBtn.style.top = 'auto';
        }, 50);
    }, 2500);
}
</script>
</body>
</html>
