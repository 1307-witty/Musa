import streamlit as st
import os
os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

# Page configuration
st.set_page_config(
    page_title="Musa – Your AI Creative Muse", 
    page_icon="🎨",
    layout="wide"
)

# Initialize session state
if 'roadmap_generated' not in st.session_state:
    st.session_state.roadmap_generated = False
if 'critique_generated' not in st.session_state:
    st.session_state.critique_generated = False

# Main title
st.title("🎨 Musa – Your AI Creative Muse")
st.write("Welcome! I'm Musa, your creative learning companion.")

# Navigation sidebar
st.sidebar.title("Navigation")
selected = st.sidebar.radio("Choose a feature", ["Pathfinder", "Critique Studio"])

# ---------------- PATHFINDER ----------------
if selected == "Pathfinder":
    st.header("🧭 Pathfinder")
    st.write("Get a personalized 3-week learning roadmap tailored to your creative goals.")

    st.subheader("💡 Example Goals")
    examples = [
        "Learn digital illustration with Procreate",
        "Master watercolor painting techniques",
        "Develop photography composition skills",
        "Create character designs for animation",
        "Learn calligraphy and hand lettering"
    ]

    cols = st.columns(3)
    for i, example in enumerate(examples):
        if cols[i % 3].button(f"📝 {example}", key=f"example_{i}"):
            st.session_state.goal_input = example

    goal = st.text_input(
        "What creative skill do you want to master?", 
        placeholder="e.g., Learn Procreate Illustration",
        value=st.session_state.get('goal_input', ''),
        key="goal_input"
    )

    experience = st.selectbox(
        "What's your current experience level?",
        ["Complete Beginner", "Some Experience", "Intermediate", "Advanced"]
    )

    time_commitment = st.selectbox(
        "How much time can you dedicate daily?",
        ["30 minutes", "1 hour", "2 hours", "3+ hours"]
    )

    if st.button("🚀 Generate My Learning Roadmap", type="primary"):
        if goal.strip():
            with st.spinner("🎨 Musa is crafting your personalized learning journey..."):
                roadmap = {
                    "week1": f"📘 Week 1 - Foundation: Learn the basic concepts and tools for {goal.lower()}.",
                    "week2": f"🎨 Week 2 - Development: Apply intermediate techniques in daily mini-projects.",
                    "week3": f"🌟 Week 3 - Mastery: Create a capstone project using your new {goal.lower()} skills.",
                    "tips": "🌱 Stay consistent. Reflect on each task. Ask for feedback often.",
                    "resources": "- Domestika course: Intro to Digital Art\n- YouTube: Procreate Basics\n- Blog: Top 10 Tips for Creatives"
                }
                st.session_state.current_roadmap = roadmap
                st.session_state.roadmap_generated = True
        else:
            st.warning("⚠️ Please enter a creative skill you'd like to learn!")

    if st.session_state.roadmap_generated and 'current_roadmap' in st.session_state:
        roadmap = st.session_state.current_roadmap
        st.subheader("📅 Your Personalized 3-Week Learning Roadmap")
        st.markdown("### 🌱 Week 1: Foundation")
        st.markdown(roadmap['week1'])
        st.markdown("### 🌿 Week 2: Development")
        st.markdown(roadmap['week2'])
        st.markdown("### 🌳 Week 3: Mastery")
        st.markdown(roadmap['week3'])
        st.markdown("### 💡 Pro Tips")
        st.markdown(roadmap['tips'])
        st.markdown("### 📚 Recommended Resources")
        st.markdown(roadmap['resources'])

# ---------------- CRITIQUE STUDIO ----------------
elif selected == "Critique Studio":
    st.header("🖌️ Critique Studio")
    st.write("Get detailed AI feedback on your artwork to improve your creative skills.")

    st.subheader("💡 Example Artwork Descriptions")
    critique_examples = [
        "A pencil sketch of a fantasy creature in a dark forest",
        "Digital portrait painting with dramatic lighting",
        "Watercolor landscape of mountains at sunset",
        "Character design for a sci-fi story",
        "Abstract acrylic painting with bold colors"
    ]

    cols = st.columns(3)
    for i, example in enumerate(critique_examples):
        if cols[i % 3].button(f"🎨 {example}", key=f"critique_example_{i}"):
            st.session_state.artwork_input = example

    artwork_desc = st.text_area(
        "Describe your artwork in detail", 
        placeholder="e.g., A pencil sketch of a fantasy creature in a dark forest...",
        height=100,
        value=st.session_state.get('artwork_input', ''),
        key="artwork_input"
    )

    medium = st.selectbox(
        "What medium did you use?",
        ["Pencil/Graphite", "Digital Art", "Watercolor", "Acrylic", "Oil Paint", "Ink", "Mixed Media", "Other"]
    )

    st.subheader("🎯 What would you like feedback on?")
    feedback_areas = []

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.checkbox("Composition", value=True):
            feedback_areas.append("composition")
        if st.checkbox("Color Theory"):
            feedback_areas.append("color theory")
        if st.checkbox("Lighting"):
            feedback_areas.append("lighting")
    with col2:
        if st.checkbox("Proportions"):
            feedback_areas.append("proportions")
        if st.checkbox("Technique"):
            feedback_areas.append("technique")
        if st.checkbox("Perspective"):
            feedback_areas.append("perspective")
    with col3:
        if st.checkbox("Style"):
            feedback_areas.append("style")
        if st.checkbox("Mood/Atmosphere"):
            feedback_areas.append("mood and atmosphere")
        if st.checkbox("Overall Impact"):
            feedback_areas.append("overall impact")

    if st.button("🔍 Get AI Critique", type="primary"):
        if artwork_desc.strip():
            with st.spinner("🎨 Musa is analyzing your artwork..."):
                critique = {
                    "strengths": "Your use of contrast and shadow adds a lot of depth. Great emotion in the composition.",
                    "improvements": "Work on consistent perspective in background elements. Try balancing the color tones.",
                    "techniques": "- Rule of thirds for composition\n- Layering brushes for lighting\n- Reference anatomy guides",
                    "next_steps": "Redo the piece focusing on light and depth. Compare versions for improvement.",
                    "encouragement": "You're developing a strong artistic voice. Keep pushing your boundaries!"
                }
                st.session_state.current_critique = critique
                st.session_state.critique_generated = True
        else:
            st.warning("⚠️ Please describe your artwork to get feedback!")

    if st.session_state.critique_generated and 'current_critique' in st.session_state:
        critique = st.session_state.current_critique
        st.subheader("💬 Musa's Detailed Feedback")
        st.markdown("### ✨ What's Working Well")
        st.success(critique['strengths'])
        st.markdown("### 🌈 Areas for Growth")
        st.info(critique['improvements'])
        st.markdown("### 🎯 Specific Techniques to Try")
        st.markdown(critique['techniques'])
        st.markdown("### 🚀 Next Steps")
        st.markdown(critique['next_steps'])
        st.markdown("### 💪 Keep Going!")
        st.markdown(critique['encouragement'])

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🎨 **Musa** - Your AI Creative Muse | Empowering artists and creators worldwide")
