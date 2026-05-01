"""
app.py — PyForge Academy (Cloudflare / stlite Wasm version)
All features: 8 lessons, pro editor with autocomplete, sandbox, download, progress tracker.
"""
import streamlit as st
from executor import run_code
from curriculum import LESSONS

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PyForge Academy",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Try Ace editor (autocomplete), fall back gracefully ───────────────────────
try:
    from streamlit_ace import st_ace
    HAS_ACE = True
except Exception:
    HAS_ACE = False

# ── Theme ──────────────────────────────────────────────────────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono&display=swap');
:root{--bg:#0d1117;--bg2:#161b22;--card:#1c2128;--blue:#58a6ff;--green:#3fb950;--purple:#bc8cff;--orange:#ffa657;--red:#f85149;--text:#e6edf3;--muted:#8b949e;--border:#30363d;}
html,body,[class*="css"]{font-family:'Inter',sans-serif!important;background:var(--bg)!important;color:var(--text)!important;}
.main{background:var(--bg)!important;}
[data-testid="stSidebar"]{background:var(--bg2)!important;border-right:1px solid var(--border)!important;}
.stButton>button{background:linear-gradient(135deg,#1f6feb,#388bfd)!important;color:#fff!important;border:none!important;border-radius:8px!important;font-weight:600!important;transition:all .2s!important;}
.stButton>button:hover{transform:translateY(-1px)!important;box-shadow:0 4px 16px rgba(56,139,253,.5)!important;}
[data-testid="stDownloadButton"]>button{background:linear-gradient(135deg,#2ea043,#3fb950)!important;color:#fff!important;border:none!important;border-radius:8px!important;font-weight:600!important;}
.theory-box{background:var(--card);padding:1.5rem;border-radius:12px;border:1px solid var(--border);line-height:1.75;overflow-y:auto;max-height:480px;}
.theory-box h2{color:var(--blue);font-size:1.1rem;margin-top:0;}
.theory-box h3{color:var(--orange);font-size:.95rem;margin-top:1rem;}
.theory-box pre{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:.9rem;overflow-x:auto;}
.theory-box code{font-family:'JetBrains Mono',monospace;color:var(--purple);background:rgba(188,140,255,.1);padding:1px 5px;border-radius:4px;}
.theory-box pre code{background:transparent;color:var(--text);}
.theory-box table{width:100%;border-collapse:collapse;font-size:.875rem;}
.theory-box th{background:var(--bg);color:var(--blue);padding:6px 10px;text-align:left;border-bottom:1px solid var(--border);}
.theory-box td{padding:6px 10px;border-bottom:1px solid var(--border);color:var(--muted);}
.challenge-box{background:rgba(188,140,255,.06);border:1px solid rgba(188,140,255,.25);border-radius:10px;padding:1rem 1.2rem;margin-top:.75rem;}
.output-panel{background:#000;padding:1rem 1.2rem;border-radius:10px;border:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:.85rem;margin-top:.75rem;animation:fadeIn .3s ease;}
.output-panel.ok{border-color:rgba(63,185,80,.35);box-shadow:0 0 16px rgba(63,185,80,.1);}
.output-panel.err{border-color:rgba(248,81,73,.35);box-shadow:0 0 16px rgba(248,81,73,.1);}
.prog-bar{height:5px;background:var(--border);border-radius:3px;overflow:hidden;margin:6px 0 12px;}
.prog-fill{height:100%;background:linear-gradient(90deg,var(--blue),var(--green));transition:width .4s;}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:translateY(0)}}
#MainMenu,footer,header{visibility:hidden;}
</style>""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "idx" not in st.session_state:   st.session_state.idx = 0
if "done" not in st.session_state:  st.session_state.done = set()
if "sb" not in st.session_state:
    st.session_state.sb = (
        "# 🧪 Sandbox — experiment freely!\n\n"
        "for i in range(1, 6):\n"
        '    print(f"Line {i}: " + "★" * i)\n'
    )

# ── Helpers ────────────────────────────────────────────────────────────────────
def editor(key, value, height=380):
    """Ace editor with autocomplete, or plain text_area fallback."""
    if HAS_ACE:
        return st_ace(
            value=value,
            language="python",
            theme="monokai",
            key=key,
            height=height,
            font_size=14,
            tab_size=4,
            show_gutter=True,
            auto_update=True,
            enable_basic_autocomplete=True,   # Tab-to-complete keywords
            enable_live_autocomplete=True,    # Live suggestions as you type
            enable_snippets=True,             # Code snippet templates
        )
    return st.text_area("Code", value=value, height=height, key=key, label_visibility="collapsed")


def show_output(res):
    cls  = "err" if res.error else "ok"
    icon = "❌" if res.error else "✅"
    body = f'<pre style="color:{"#f85149" if res.error else "#e6edf3"};margin:0;white-space:pre-wrap">' \
           f'{res.error or res.output or "(no output)"}</pre>'
    st.markdown(
        f'<div class="output-panel {cls}">'
        f'<span style="font-size:.75rem;font-weight:700;color:{"#f85149" if res.error else "#3fb950"}">'
        f'{icon} {"ERROR" if res.error else "OUTPUT"}</span><br>{body}'
        f'<div style="font-size:.7rem;color:#484f58;margin-top:.4rem;border-top:1px solid #30363d;padding-top:.3rem">'
        f'⏱ {res.exec_time*1000:.1f} ms</div></div>',
        unsafe_allow_html=True,
    )

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<h2 style="color:#58a6ff;margin:0;font-size:1.2rem">🐍 PyForge Academy</h2>'
                '<p style="color:#8b949e;font-size:.8rem;margin:2px 0 12px">Interactive Python Learning</p>',
                unsafe_allow_html=True)

    n_done, n_total = len(st.session_state.done), len(LESSONS)
    pct = int(n_done / n_total * 100)
    st.markdown(
        f'<div style="font-size:.78rem;color:#8b949e">Progress: {n_done}/{n_total} lessons</div>'
        f'<div class="prog-bar"><div class="prog-fill" style="width:{pct}%"></div></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div style="font-size:.7rem;font-weight:700;color:#484f58;text-transform:uppercase;'
                'letter-spacing:1px;margin-bottom:4px">Curriculum</div>', unsafe_allow_html=True)

    for i, lsn in enumerate(LESSONS):
        mark = " ✓" if i in st.session_state.done else ""
        label = f"{lsn['icon']} {lsn['title']}{mark}"
        if st.button(label, key=f"nav_{i}", use_container_width=True,
                     type="primary" if st.session_state.idx == i else "secondary"):
            st.session_state.idx = i
            st.rerun()

    st.markdown("<hr><div style='font-size:.72rem;color:#484f58;text-align:center'>"
                "Built with ❤️ &nbsp;·&nbsp; PyForge Academy</div>", unsafe_allow_html=True)

# ── Main ───────────────────────────────────────────────────────────────────────
st.markdown('<div style="background:linear-gradient(135deg,#161b22,#1c2128);padding:1.2rem 1.5rem;'
            'border-radius:12px;border:1px solid #30363d;margin-bottom:1rem;position:relative;overflow:hidden">'
            '<div style="position:absolute;top:0;left:0;right:0;height:2px;'
            'background:linear-gradient(90deg,#58a6ff,#bc8cff,#3fb950)"></div>'
            '<h1 style="margin:0;font-size:1.7rem;font-weight:800;background:linear-gradient(135deg,#58a6ff,#bc8cff);'
            '-webkit-background-clip:text;-webkit-text-fill-color:transparent">🐍 PyForge Academy</h1>'
            '<p style="margin:4px 0 0;color:#8b949e;font-size:.9rem">Master Python through interactive lessons and live code execution.</p>'
            '</div>', unsafe_allow_html=True)

tab_lessons, tab_sandbox = st.tabs(["📚  Lessons", "🧪  Sandbox"])

# ── Lessons Tab ────────────────────────────────────────────────────────────────
with tab_lessons:
    lsn = LESSONS[st.session_state.idx]

    st.markdown(
        f'<div style="background:#1c2128;padding:1rem 1.3rem;border-radius:10px;'
        f'border:1px solid #30363d;border-left:3px solid #58a6ff;margin-bottom:1rem">'
        f'<div style="display:flex;align-items:center;gap:10px">'
        f'<span style="font-size:1.8rem">{lsn["icon"]}</span>'
        f'<div><h2 style="margin:0;font-size:1.25rem">Lesson {st.session_state.idx+1}: {lsn["title"]}</h2>'
        f'<span style="background:rgba(63,185,80,.1);border:1px solid rgba(63,185,80,.25);'
        f'color:#3fb950;padding:2px 10px;border-radius:100px;font-size:.75rem">🎯 {lsn["objective"]}</span>'
        f'</div></div></div>',
        unsafe_allow_html=True,
    )

    col_theory, col_editor = st.columns([1, 1], gap="medium")

    with col_theory:
        st.markdown(f'<div class="theory-box">{lsn["theory"]}</div>', unsafe_allow_html=True)
        if lsn.get("challenge"):
            st.markdown(
                f'<div class="challenge-box">'
                f'<div style="font-size:.78rem;font-weight:700;color:#bc8cff;text-transform:uppercase;'
                f'letter-spacing:1px;margin-bottom:.4rem">💡 Challenge</div>'
                f'<p style="margin:0;color:#8b949e;font-size:.9rem">{lsn["challenge"]}</p></div>',
                unsafe_allow_html=True,
            )

    with col_editor:
        st.markdown('<div style="font-size:.75rem;font-weight:700;color:#8b949e;text-transform:uppercase;'
                    'letter-spacing:1px;margin-bottom:4px">⌨️ Python Editor'
                    + (' · <span style="color:#ffa657">Autocomplete ON (Tab)</span>' if HAS_ACE else '') +
                    '</div>', unsafe_allow_html=True)

        ed_key = f"ed_{lsn['id']}"
        if ed_key not in st.session_state:
            st.session_state[ed_key] = lsn["starter_code"]

        code = editor(ed_key, st.session_state[ed_key])

        btn_run, btn_reset = st.columns([3, 1])
        with btn_run:
            if st.button("▶  Run Code", key=f"run_{lsn['id']}", use_container_width=True):
                res = run_code(code or "")
                show_output(res)
                if not res.error:
                    st.session_state.done.add(st.session_state.idx)
        with btn_reset:
            if st.button("↺ Reset", key=f"rst_{lsn['id']}", use_container_width=True):
                st.session_state[ed_key] = lsn["starter_code"]
                st.rerun()

        nav_prev, nav_next = st.columns(2)
        with nav_prev:
            if st.session_state.idx > 0:
                if st.button("← Prev", key=f"prev_{lsn['id']}", use_container_width=True):
                    st.session_state.idx -= 1
                    st.rerun()
        with nav_next:
            if st.session_state.idx < len(LESSONS) - 1:
                if st.button("Next →", key=f"nxt_{lsn['id']}", use_container_width=True):
                    st.session_state.idx += 1
                    st.rerun()
            else:
                st.success("🎓 All lessons complete!")

# ── Sandbox Tab ────────────────────────────────────────────────────────────────
with tab_sandbox:
    st.markdown('<h3 style="margin:0 0 .5rem">🧪 Sandbox</h3>'
                '<p style="color:#8b949e;font-size:.85rem;margin:0 0 1rem">'
                'Free Python playground. '
                + ('Autocomplete is ON — type and hit <kbd>Tab</kbd>.' if HAS_ACE else 'Type freely.')
                + '</p>', unsafe_allow_html=True)

    sb_code = editor("sb_ed", st.session_state.sb, height=460)
    if sb_code is not None:
        st.session_state.sb = sb_code

    col_r, col_d, col_c = st.columns([2, 2, 1])
    with col_r:
        if st.button("▶  Run", key="sb_run", use_container_width=True):
            res = run_code(sb_code or st.session_state.sb)
            show_output(res)
    with col_d:
        st.download_button(
            "⬇  Download .py",
            data=sb_code or st.session_state.sb,
            file_name="pyforge_script.py",
            mime="text/plain",
            use_container_width=True,
        )
    with col_c:
        if st.button("✕ Clear", key="sb_clr", use_container_width=True):
            st.session_state.sb = "# Start fresh!\n"
            st.rerun()
