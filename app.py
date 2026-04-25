import streamlit as st

st.title("🇰🇷 한국어 음절 구조 분석기")
st.write("한글 단어를 입력하면 초성/중성/종성으로 분해합니다.")

# -------------------------
# 한글 분해 함수
# -------------------------
def decompose_hangul(text):
    result = []

    for char in text:
        if '가' <= char <= '힣':
            base = ord(char) - ord('가')

            cho = base // 588
            jung = (base % 588) // 28
            jong = base % 28

            cho_list = [
                "ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ",
                "ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
            ]

            jung_list = [
                "ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ",
                "ㅗ","ㅘ","ㅙ","ㅚ","ㅛ",
                "ㅜ","ㅝ","ㅞ","ㅟ","ㅠ",
                "ㅡ","ㅢ","ㅣ"
            ]

            jong_list = [
                "∅","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ",
                "ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ",
                "ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
            ]

            result.append(f"{char} = {cho_list[cho]} + {jung_list[jung]} + {jong_list[jong]}")
        else:
            result.append(f"{char} = (한글 아님)")

    return "\n".join(result)


# -------------------------
# UI
# -------------------------
text = st.text_input("단어를 입력하세요")

if st.button("분석하기"):
    if text.strip() == "":
        st.warning("문장을 입력해주세요!")
    else:
        output = decompose_hangul(text)

        st.subheader("🔍 분석 결과")
        st.text(output)
