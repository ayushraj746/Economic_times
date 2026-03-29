import streamlit as st
from graph import graph

st.set_page_config(
    page_title="AI Story Arc Tracker",
    layout="wide",
    page_icon="🧠"
)

# -------------------- STYLES --------------------
st.markdown("""
<style>
body { background-color: #0E1117; }

.title {
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(90deg, #00C6FF, #0072FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 16px;
    color: #9aa0a6;
    margin-bottom: 20px;
}

.card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #30363d;
    margin-bottom: 18px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #00C6FF;
}

.timeline-box {
    padding: 12px;
    border-radius: 10px;
    background: #1c2430;
    border: 1px solid #2f3b4a;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="title">AI Story Arc Tracker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Turn breaking news into structured intelligence</div>', unsafe_allow_html=True)

# -------------------- CONTROLS --------------------
perspective = st.selectbox(
    "Select Perspective",
    ["General", "Investor", "Founder", "Student"]
)

mode = st.radio("Mode", ["Single Article", "Story Evolution"])

# -------------------- INPUT --------------------
if mode == "Single Article":
    text = st.text_area("Paste News Article", height=180)

    input_payload = {
        "input_text": text,
        "perspective": perspective
    }

else:
    if "updates" not in st.session_state:
        st.session_state.updates = [""]

    for i in range(len(st.session_state.updates)):
        st.session_state.updates[i] = st.text_area(
            f"Update {i+1}",
            value=st.session_state.updates[i],
            key=f"update_{i}"
        )

    if st.button("Add Update"):
        st.session_state.updates.append("")

    input_payload = {
        "input_texts": st.session_state.updates,
        "perspective": perspective
    }

generate = st.button("Generate", use_container_width=True)

# -------------------- OUTPUT --------------------
if generate:

    try:
        with st.spinner("Analyzing..."):
            result = graph.invoke(input_payload)
            output = result["output"]

    except Exception:
        output = {
            "summary": ["Fallback"],
            "insights": [],
            "timeline": {},
            "questions": [],
            "why_it_matters": "",
            "meta_analysis": {},
            "story_evolution": {}
        }

    st.markdown("## Briefing")

    # 🔥 WHY THIS MATTERS (highlighted)
    if output.get("why_it_matters"):
        st.markdown("### Why this matters")
        st.success(output.get("why_it_matters"))

    # ---------------- SUMMARY ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    for s in output.get("summary", []):
        st.markdown(f"- {s}")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- INSIGHTS + QUESTIONS ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Insights**")

        for i in output.get("insights", []):
            # fix dict issue
            if isinstance(i, dict):
                st.markdown(f"- {i.get('implication', '')}")
            else:
                st.markdown(f"- {i}")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Questions**")

        for q in output.get("questions", []):
            st.markdown(f"- {q}")

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TIMELINE ----------------
    if output.get("timeline"):
        timeline = output.get("timeline")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("Past")
            st.markdown(f"<div class='timeline-box'>{timeline.get('past','')}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("Present")
            st.markdown(f"<div class='timeline-box'>{timeline.get('present','')}</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("Future")
            st.markdown(f"<div class='timeline-box'>{timeline.get('future','')}</div>", unsafe_allow_html=True)

    # ---------------- STORY EVOLUTION ----------------
    evolution = output.get("story_evolution", {})

    if evolution:
        st.markdown("## Story Evolution")
        st.markdown('<div class="card">', unsafe_allow_html=True)

        for i, phase in enumerate(evolution.get("phases", []), 1):

            if isinstance(phase, dict):
                title = phase.get("phase", "")
                events = ", ".join(phase.get("events", []))
                st.markdown(f"**Phase {i}: {title}**")
                st.markdown(f"- {events}")
            else:
                st.markdown(f"**Phase {i}:** {phase}")

        st.markdown("**Shift:**")
        st.write(evolution.get("shift"))

        st.markdown("**Trend:**")
        st.write(evolution.get("trend"))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- META ----------------
    meta = output.get("meta_analysis", {})

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(f"**Type:** {meta.get('story_type')}")
    st.markdown(f"**Impact:** {meta.get('impact_level')}")

    st.markdown("**Winners:**")
    for w in meta.get("stakeholders", {}).get("winners", []):
        st.markdown(f"- {w}")

    st.markdown("**Losers:**")
    for l in meta.get("stakeholders", {}).get("losers", []):
        st.markdown(f"- {l}")

    st.markdown(f"**Signal:** {meta.get('signal_strength')}")

    st.markdown('</div>', unsafe_allow_html=True)