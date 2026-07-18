import streamlit as st
import base64
from pathlib import Path

# ============================================================
# 1. EDIT YOUR INFO HERE — this is the only section you need
#    to touch to make the page yours.
# ============================================================

PROFILE = {
    "name": "Vishal",
    "tagline": "Frames of life, strokes of imagination ✨",
    # Each item is one line in the bio. Wrap key phrases in <hl>...</hl>
    # to highlight them in the accent color.
    "bio_lines": [
        "📸 Capturing &nbsp; | &nbsp; ✏️ Sketching &nbsp; | &nbsp; ☕ Brewing &nbsp; | &nbsp; 💻 Exploring Tech",
        "A 22-year-old creator turning coffee into code and moments into memories.",
        "<hl>M.Tech in Computer Science</hl> — <hl>AI/ML/DL &amp; Data Science</hl>",
        "<hl>Full-Stack Developer</hl>",
    ],
    # Local image file — must sit in the SAME folder as this script.
    # (If you'd rather use a hosted image, put a full https:// URL here instead.)
    "avatar_path": "profile.jpg",
    "accent_color": "#7C3AED",  # change this one value to re-theme the whole page
}

LINKS = [
    {"label": "Instagram", "icon": "📷", "url": "https://www.instagram.com/vishal.pclicks/"},
    {"label": "X (Twitter)", "icon": "✖️", "url": "https://x.com/_vishal06"},
    {"label": "LinkedIn", "icon": "💼", "url": "https://www.linkedin.com/in/vishal-datascience/"},
    {"label": "GitHub", "icon": "🐙", "url": "https://github.com/VISHAL-038"},
    {"label": "Portfolio", "icon": "🌐", "url": "https://vishal-038.github.io/Portfolio__/"},
    {"label": "Shutterstock", "icon": "🖼️", "url": "https://www.shutterstock.com/g/vishal_pclicks"},
    {"label": "Lightroom", "icon": "🎞️", "url": "https://lightroom.adobe.com/u/4a318132"},
    {"label": "Threads", "icon": "🧵", "url": "https://www.threads.net/@vishal.pclicks"},
    {"label": "Snapchat", "icon": "👻", "url": "https://www.snapchat.com/@vishal.490?"},
    {"label": "Pinterest", "icon": "📌", "url": "https://in.pinterest.com/Vishal_038/"},
    {"label": "Vero", "icon": "🟢", "url": "https://vero.co/_vishal06"},
    {"label": "Email Me", "icon": "✉️", "url": "mailto:vishaal03.it@gmail.com"},
]

# ============================================================
# 2. PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title=f"{PROFILE['name']} | Links",
    page_icon="🔗",
    layout="centered",
)

# ============================================================
# 3. STYLING
# ============================================================

st.markdown(
    f"""
    <style>
        #MainMenu, footer, header {{visibility: hidden;}}

        .stApp {{
            background: radial-gradient(circle at top, #1a1a2e 0%, #0d0d15 60%, #000000 100%);
        }}

        .block-container {{
            max-width: 560px;
            padding-top: 3rem;
        }}

        .profile-card {{
            text-align: center;
            padding: 2rem 1.5rem 1.5rem 1.5rem;
        }}

        .avatar {{
            width: 130px;
            height: 130px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid {PROFILE['accent_color']};
            box-shadow: 0 0 25px {PROFILE['accent_color']}55;
            margin-bottom: 1rem;
        }}

        .name {{
            color: #ffffff;
            font-size: 1.9rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
        }}

        .tagline {{
            color: {PROFILE['accent_color']};
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 0.6rem;
        }}

        .bio {{
            color: #b8b8c8;
            font-size: 0.92rem;
            line-height: 1.6rem;
            max-width: 460px;
            margin: 0 auto 1.8rem auto;
        }}

        .bio-line {{
            margin-bottom: 0.35rem;
        }}

        .bio-line:last-child {{
            margin-bottom: 0;
        }}

        .bio hl {{
            color: {PROFILE['accent_color']};
            font-weight: 700;
            font-style: normal;
            background: {PROFILE['accent_color']}18;
            padding: 0.1rem 0.5rem;
            border-radius: 8px;
        }}

        a.link-btn {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6rem;
            width: 100%;
            padding: 0.85rem 1rem;
            margin-bottom: 0.85rem;
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.09);
            color: #ffffff !important;
            font-size: 1.02rem;
            font-weight: 600;
            text-decoration: none !important;
            transition: all 0.2s ease-in-out;
            backdrop-filter: blur(6px);
        }}

        a.link-btn:hover {{
            background: {PROFILE['accent_color']}22;
            border-color: {PROFILE['accent_color']};
            transform: translateY(-2px);
            box-shadow: 0 6px 18px {PROFILE['accent_color']}33;
        }}

        .footer-note {{
            text-align: center;
            color: #666677;
            font-size: 0.8rem;
            margin-top: 2rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 4. PAGE CONTENT
# ============================================================


def load_avatar_src(profile: dict) -> str:
    """Return an <img> src for the avatar. Reads a local file (given by
    'avatar_path') and embeds it as base64 so it works both locally and
    once deployed. Falls back to 'avatar_url' if no local file is found."""
    avatar_path = profile.get("avatar_path")
    if avatar_path and Path(avatar_path).exists():
        suffix = Path(avatar_path).suffix.lstrip(".").lower()
        mime = "jpeg" if suffix in ("jpg", "jpeg") else suffix
        encoded = base64.b64encode(Path(avatar_path).read_bytes()).decode()
        return f"data:image/{mime};base64,{encoded}"
    return profile.get("avatar_url", "")


avatar_src = load_avatar_src(PROFILE)

bio_html = "".join(
    f'<div class="bio-line">{line}</div>' for line in PROFILE["bio_lines"]
)

st.markdown(
    f"""
    <div class="profile-card">
        <img src="{avatar_src}" class="avatar">
        <div class="name">{PROFILE['name']}</div>
        <div class="tagline">{PROFILE['tagline']}</div>
        <div class="bio">{bio_html}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

links_html = "".join(
    f'<a class="link-btn" href="{link["url"]}" target="_blank">'
    f'<span>{link["icon"]}</span><span>{link["label"]}</span></a>'
    for link in LINKS
)
st.markdown(links_html, unsafe_allow_html=True)

st.markdown(
    '<div class="footer-note">Crafted with ❤️ using Streamlit</div>',
    unsafe_allow_html=True,
)