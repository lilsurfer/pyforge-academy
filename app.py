"""
app.py — Python Learning Academy
A premium, interactive Python learning environment built with Streamlit.
"""

import streamlit as st
from pathlib import Path

from executor import run_code
from lessons.curriculum import LESSONS

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Python Learning Academy",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load CSS ───────────────────────────────────────────────────────────────────
css_path = Path(__file__).parent / "styles" / "theme.css"
with open(css_path, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Try to import streamlit-ace ────────────────────────────────────────────────
try:
    from streamlit_ace import st_ace
    HAS_ACE = True
except ImportError:
    HAS_ACE = False

# ── Session state defaults ─────────────────────────────────────────────────────
if "selected_lesson" not in st.session_state:
    st.session_state.selected_lesson = 0
if "sandbox_code" not in st.session_state:
    st.session_state.sandbox_code = (
        '# 🧪 Sandbox — Your free coding space\n'
        '# Write any Python you like!\n\n'
        'message = "Hello from the Sandbox! 🚀"\n'
        'print(message)\n\n'
        'for i in range(1, 6):\n'
        '    print(f"  Line {i}: {"★" * i}")\n'
    )
if "completed" not in st.session_state:
    st.session_state.completed = set()


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-logo">
                <h1>🐍 Python Academy</h1>
                <p>Interactive Learning Environment</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Progress indicator
        n_done = len(st.session_state.completed)
        n_total = len(LESSONS)
        pct = int(n_done / n_total * 100)
        st.markdown(
            f"""
            <div class="progress-section">
                <div style="display:flex;justify-content:space-between;
                            font-size:0.75rem;color:var(--text-secondary);">
                    <span>Progress</span>
                    <span>{n_done}/{n_total} lessons</span>
                </div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width:{pct}%"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='font-size:0.7rem;font-weight:700;"
            "color:var(--text-muted);text-transform:uppercase;"
            "letter-spacing:1px;padding:0.5rem 0 0.3rem 0;"
            "margin-left:2px;'>Curriculum</div>",
            unsafe_allow_html=True,
        )

        for idx, lesson in enumerate(LESSONS):
            done_mark = " ✓" if idx in st.session_state.completed else ""
            label = f"{lesson['icon']} {lesson['title']}{done_mark}"
            is_active = st.session_state.selected_lesson == idx

            if st.button(
                label,
                key=f"lesson_btn_{idx}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.selected_lesson = idx
                st.rerun()

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style='font-size:0.75rem;color:var(--text-muted);
                        text-align:center;padding:0.5rem 0;'>
                Built with ❤️ using Streamlit<br>
                <span style='color:var(--accent-blue);'>Python Learning Academy</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ══════════════════════════════════════════════════════════════════════════════
# CODE EDITOR WIDGET
# ══════════════════════════════════════════════════════════════════════════════
def code_editor(key: str, value: str, height: int = 300) -> str:
    """Render a code editor — uses streamlit-ace if available, else text_area."""
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
            show_print_margin=False,
            wrap=False,
            auto_update=True,
            annotations=None,
        )
    else:
        return st.text_area(
            label="Python Code",
            value=value,
            height=height,
            key=key,
            label_visibility="collapsed",
        )


# ══════════════════════════════════════════════════════════════════════════════
# OUTPUT RENDERER
# ══════════════════════════════════════════════════════════════════════════════
def render_output(result):
    """Display execution results with styled output panel."""
    has_error = bool(result.error)
    has_output = bool(result.output)

    status = "error" if has_error else "success"
    label_text = "❌ Error" if has_error else "✅ Output"

    content_html = ""
    if has_output:
        safe = result.output.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        content_html += f'<div class="output-text">{safe}</div>'
    if has_error:
        safe_err = result.error.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        content_html += f'<div class="error-text">{safe_err}</div>'
    if not has_output and not has_error:
        content_html = '<div style="color:var(--text-muted);font-style:italic;">No output.</div>'

    meta = f"⏱ {result.exec_time * 1000:.1f} ms"
    if result.timed_out:
        meta += "  |  ⏰ Timed out"

    st.markdown(
        f"""
        <div class="output-panel {status}" style="margin-top:0.8rem;">
            <span class="output-label {status}">{label_text}</span>
            {content_html}
            <div class="output-meta">{meta}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# LESSON TAB
# ══════════════════════════════════════════════════════════════════════════════
def render_lesson_tab():
    lesson = LESSONS[st.session_state.selected_lesson]

    # Header
    st.markdown(
        f"""
        <div class="lesson-header">
            <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
                <span style="font-size:2rem;">{lesson['icon']}</span>
                <div>
                    <h2>Lesson {st.session_state.selected_lesson + 1}: {lesson['title']}</h2>
                    <span class="lesson-objective">🎯 {lesson['objective']}</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Theory + Editor columns
    col_theory, col_editor = st.columns([1, 1], gap="medium")

    with col_theory:
        st.markdown(
            f'<div class="theory-box">{_md_to_html_passthrough(lesson["theory"])}</div>',
            unsafe_allow_html=True,
        )

        # Challenge box
        if lesson.get("challenge"):
            st.markdown(
                f"""
                <div class="challenge-box">
                    <div class="challenge-title">💡 Challenge</div>
                    <p>{lesson['challenge']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_editor:
        st.markdown(
            """
            <div class="editor-label">
                <span class="editor-dot"></span> Python Editor
            </div>
            """,
            unsafe_allow_html=True,
        )

        editor_key = f"lesson_editor_{lesson['id']}"
        # Initialize with starter code on first visit
        starter_key = f"_starter_{lesson['id']}"
        if starter_key not in st.session_state:
            st.session_state[starter_key] = True
            st.session_state[editor_key] = lesson["starter_code"].strip()

        code = code_editor(
            key=editor_key,
            value=st.session_state.get(editor_key, lesson["starter_code"].strip()),
            height=360,
        )

        btn_col, reset_col = st.columns([3, 1])
        with btn_col:
            run_clicked = st.button(
                "▶  Run Code",
                key=f"run_{lesson['id']}",
                use_container_width=True,
            )
        with reset_col:
            if st.button("↺ Reset", key=f"reset_{lesson['id']}", use_container_width=True):
                st.session_state[editor_key] = lesson["starter_code"].strip()
                st.rerun()

        if run_clicked and code:
            result = run_code(code)
            render_output(result)
            # Mark lesson complete if it ran successfully
            if not result.error and not result.timed_out:
                st.session_state.completed.add(st.session_state.selected_lesson)

        # Navigation buttons
        st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
        nav_prev, nav_next = st.columns(2)
        with nav_prev:
            if st.session_state.selected_lesson > 0:
                if st.button("← Previous", key=f"prev_{lesson['id']}", use_container_width=True):
                    st.session_state.selected_lesson -= 1
                    st.rerun()
        with nav_next:
            if st.session_state.selected_lesson < len(LESSONS) - 1:
                if st.button("Next →", key=f"next_{lesson['id']}", use_container_width=True):
                    st.session_state.selected_lesson += 1
                    st.rerun()
            else:
                st.success("🎓 You've completed the curriculum!")


def _md_to_html_passthrough(markdown_text: str) -> str:
    """
    Streamlit's st.markdown renders MD, but we're inside a raw HTML div.
    We convert basic markdown to HTML manually for the theory box.
    This handles headers, code blocks, inline code, bold, tables.
    """
    import re

    text = markdown_text.strip()

    # Fenced code blocks ```...```
    def replace_code_block(m):
        code = m.group(1)
        code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<pre><code>{code}</code></pre>'
    text = re.sub(r'```(?:\w+)?\n?(.*?)```', replace_code_block, text, flags=re.DOTALL)

    # Inline code `...`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Headers
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # Bold **...**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

    # Tables — basic markdown table to HTML
    lines = text.split('\n')
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if '|' in line and i + 1 < len(lines) and re.match(r'\s*\|[\s\-|]+\|\s*$', lines[i+1]):
            # Table header
            headers = [h.strip() for h in line.strip().strip('|').split('|')]
            table_html = '<table><thead><tr>'
            for h in headers:
                table_html += f'<th>{h}</th>'
            table_html += '</tr></thead><tbody>'
            i += 2  # skip separator row
            while i < len(lines) and '|' in lines[i]:
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                table_html += '<tr>'
                for c in cells:
                    table_html += f'<td>{c}</td>'
                table_html += '</tr>'
                i += 1
            table_html += '</tbody></table>'
            result_lines.append(table_html)
            continue
        result_lines.append(line)
        i += 1
    text = '\n'.join(result_lines)

    # Paragraphs — wrap consecutive non-empty non-tag lines in <p>
    paragraphs = re.split(r'\n{2,}', text)
    html_parts = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if para.startswith('<'):
            html_parts.append(para)
        else:
            para = para.replace('\n', '<br>')
            html_parts.append(f'<p>{para}</p>')

    return '\n'.join(html_parts)


# ══════════════════════════════════════════════════════════════════════════════
# SANDBOX TAB
# ══════════════════════════════════════════════════════════════════════════════
def render_sandbox_tab():
    st.markdown(
        """
        <div class="app-header">
            <h1>🧪 Sandbox</h1>
            <p>Your unlimited Python playground — experiment freely, no lesson constraints.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="editor-label"><span class="editor-dot"></span> Python Editor</div>',
        unsafe_allow_html=True,
    )

    sandbox_code = code_editor(
        key="sandbox_editor",
        value=st.session_state.sandbox_code,
        height=480,
    )

    # Save sandbox code to session state
    if sandbox_code is not None:
        st.session_state.sandbox_code = sandbox_code

    col_run, col_download, col_clear = st.columns([2, 2, 1])

    with col_run:
        run_sandbox = st.button(
            "▶  Run Code",
            key="run_sandbox",
            use_container_width=True,
        )

    with col_download:
        code_to_download = sandbox_code or st.session_state.sandbox_code
        st.download_button(
            label="⬇  Download .py",
            data=code_to_download,
            file_name="sandbox_code.py",
            mime="text/plain",
            use_container_width=True,
            key="download_sandbox",
        )

    with col_clear:
        if st.button("✕ Clear", key="clear_sandbox", use_container_width=True):
            st.session_state.sandbox_code = "# Start fresh!\n"
            st.rerun()

    if run_sandbox:
        code_to_run = sandbox_code or st.session_state.sandbox_code
        result = run_code(code_to_run)
        render_output(result)

    # Tips
    st.markdown(
        """
        <div style="margin-top:1.5rem;padding:0.8rem 1.2rem;
                    background:rgba(88,166,255,0.06);
                    border:1px solid rgba(88,166,255,0.15);
                    border-radius:8px;font-size:0.8rem;
                    color:var(--text-secondary);">
            <strong style="color:var(--accent-blue);">💡 Sandbox Tips</strong><br>
            • Code runs in an isolated subprocess with a 5-second timeout<br>
            • <code>import</code> any standard library module freely<br>
            • Use <strong>⬇ Download .py</strong> to save your code to your Downloads folder<br>
            • Standard <code>print()</code> output and errors are both shown below
        </div>
        """,
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ══════════════════════════════════════════════════════════════════════════════
def main():
    render_sidebar()

    # App header
    st.markdown(
        """
        <div class="app-header">
            <h1>🐍 Python Learning Academy</h1>
            <p>Master Python through interactive lessons, live execution, and hands-on challenges.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Main tabs
    tab_lessons, tab_sandbox = st.tabs(["📚  Lessons", "🧪  Sandbox"])

    with tab_lessons:
        render_lesson_tab()

    with tab_sandbox:
        render_sandbox_tab()


if __name__ == "__main__":
    main()
