import streamlit as st

st.set_page_config(page_title="성격으로 알아보는 강아지 유형", layout="centered")

st.title("🐾 당신은 어떤 강아지와 닮았을까요?")
st.write("7가지 밸런스 게임을 통해 당신의 성격을 알아보고, 닮은 강아지 품종을 알려드릴게요!")

# 질문 목록
questions = [
    ("혼자 있는 게 편해요", "사람들과 어울리는 게 좋아요"),
    ("계획적인 걸 좋아해요", "즉흥적인 걸 좋아해요"),
    ("활발하고 에너지가 넘쳐요", "조용하고 차분한 편이에요"),
    ("새로운 걸 시도하는 걸 좋아해요", "익숙한 걸 더 선호해요"),
    ("감정보다 이성을 우선해요", "이성보다 감정을 우선해요"),
    ("리더십 있는 스타일이에요", "서포트 역할이 편해요"),
    ("책보다 운동이 좋아요", "운동보다 책이 좋아요")
]

# 점수 저장
score = 0

# 질문별 응답
for idx, (opt1, opt2) in enumerate(questions):
    choice = st.radio(f"Q{idx+1}.", [opt1, opt2], key=idx)
    if choice == opt2:
        score += 1  # 우측 선택지일수록 외향적 성향이라고 가정

# 결과 계산
if st.button("🐶 결과 보기"):
    if score <= 2:
        dog = "시바 이누"
        desc = "조용하고 독립적인 성격을 가진 당신은 시바 이누와 닮았어요!"
        img_url = "https://images.unsplash.com/photo-1601758123927-1961a6b0e1c3"
    elif score <= 4:
        dog = "푸들"
        desc = "밝고 감성적인 당신! 푸들과 잘 어울려요!"
        img_url = "https://images.unsplash.com/photo-1612531386535-d9f69a6fa5b5"
    elif score <= 5:
        dog = "골든 리트리버"
        desc = "친절하고 에너지 넘치는 성격! 골든 리트리버와 꼭 닮았어요!"
        img_url = "https://images.unsplash.com/photo-1583511655826-05700d52f4db"
    else:
        dog = "보더 콜리"
        desc = "똑똑하고 활동적인 당신은 보더 콜리와 닮았어요!"
        img_url = "https://images.unsplash.com/photo-1596495577886-d920f1fb7238"

    st.subheader(f"🐕 당신은 {dog}!")
    st.write(desc)
    st.image(img_url, use_column_width=True)
