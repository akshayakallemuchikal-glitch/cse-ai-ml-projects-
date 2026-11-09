import streamlit as st
import google.generativeai as genai
import urllib.parse

st.title("🚀 AI Learning Path Generator")
st.write("Enter any skill and get a complete AI-made day-wise plan with videos.")

# AI KEY
api_key = st.text_input("Paste your Gemini API Key (free from aistudio.google.com)", type="password")
topic = st.text_input("What do you want to learn?", placeholder="e.g. Python, UI Design, Video Editing")
level = st.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
days = st.slider("How many days?", 3, 30, 7)
hours = st.slider("Hours per day?", 1, 8, 3)

if st.button("Generate Learning Plan"):
    if not topic:
        st.warning("Please enter a topic first!")
    elif not api_key:
        st.warning("Please paste your Gemini API Key first!")
    else:
        with st.spinner("AI is making your plan + videos... Please wait..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"Make a {days}-day learning plan to master {topic} for a {level} learner who studies {hours} hours per day. For each day give: Title, What to Learn (3 points), Practice Task. Keep it simple and clear."
                response = model.generate_content(prompt)
                plan = response.text

                st.success(f"Your {days}-Day AI Plan to Master {topic} ({level})")
                st.write(plan)

                st.divider()
                st.subheader("🎥 Watch on YouTube - Day-wise Videos")

                # 1. YOUTUBE LINKS FOR EACH DAY
                for day in range(1, days + 1):
                    search = f"{topic} Day {day} tutorial for {level}"
                    link = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(search)
                    with st.expander(f"Day {day} - Videos"):
                        st.write(f"📺 Watch: {search}")
                        st.link_button(f"▶️ Watch Day {day} on YouTube", link)
                        st.write(f"Task: Practice Day {day} topic for {hours} hours")

                # 2. DOWNLOAD BUTTON
                full_text = f"LEARNING PLAN: {topic}\nLevel: {level}\nDays: {days} | Hours: {hours}/day\n\n{plan}\n\nYOUTUBE LINKS:\n"
                for day in range(1, days + 1):
                    full_text += f"Day {day}: https://www.youtube.com/results?search_query={topic} Day {day} tutorial\n"

                st.download_button(
                    label="📥 Download My Full Plan (with YouTube Links)",
                    data=full_text,
                    file_name=f"{topic}_AI_Learning_Plan.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}. Check your API key.")
