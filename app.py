
import streamlit as st
from openai import OpenAI
st.write(st.secrets)
# 🔐 API KEY (OPENAI_API_KEY)
client = OpenAI(api_key="OPENAI_API_KEY")

# =========================
# GPT 기반 교정 함수
# =========================
def correct_korean(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "너는 한국어 맞춤법과 띄어쓰기를 교정하는 전문가야. 의미를 유지하면서 자연스럽게 수정해줘."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content


# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Korean AI Correction System")

st.title("🇰🇷 AI 한국어 맞춤법 교정기 (GPT 기반)")
st.write("GPT를 활용한 문장 자동 교정 웹앱입니다.")

# 입력창
text = st.text_area("문장을 입력하세요")

# 버튼
col1, col2 = st.columns(2)

with col1:
    run = st.button("교정하기")

with col2:
    example = st.button("예시 입력")

# 예시
if example:
    text = "나는밥을먹엇다그리고학교에갓다"

# 실행
if run:
    if text.strip() == "":
        st.warning("문장을 입력해주세요")
    else:
        result = correct_korean(text)

        st.subheader("입력")
        st.info(text)

        st.subheader("교정 결과")
        st.success(result)
