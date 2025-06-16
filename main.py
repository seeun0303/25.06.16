import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🐶 강아지 성격 테스트", layout="centered")

# 세션 상태 초기화
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

# 질문 리스트 (왼쪽 = 0점, 오른쪽 = 1점)
questions = [
    ("🧘 혼자 있는 게 편해요", "👯 사람들과 어울리는 게 좋아요"),
    ("🧩 계획적인 걸 좋아해요", "🎲 즉흥적인 걸 좋아해요"),
    ("⚡ 활발하고 에너지가 넘쳐요", "🌙 조용하고 차분한 편이에요"),
    ("🚀 새로운 걸 시도하는 걸 좋아해요", "🏡 익숙한 걸 더 선호해요"),
    ("🧠 감정보다 이성을 우선해요", "💖 이성보다 감정을 우선해요"),
    ("👑 리더십 있는 스타일이에요", "🛟 서포트 역할이 편해요"),
    ("📚 책보다 운동이 좋아요", "🤸 운동보다 책이 좋아요")
]

# 결과 매핑 함수 (소형견 위주 구성)
def get_dog_result(score):
    if score <= 1:
        return {
            "dog": "🐕 진돗개",
            "desc": "조용하고 단단한 당신, 진돗개의 충직하고 독립적인 성격과 닮았어요!",
            "img": "https://images.unsplash.com/photo-1635086458566-c801e760c01d"
        }
    elif score == 2:
        return {
            "dog": "🐶 시바 이누",
            "desc": "귀여운 외모 속 시크한 매력! 시바 이누처럼 자기 주관이 뚜렷한 타입이에요.",
            "img": "https://images.unsplash.com/photo-1601758123927-1961a6b0e1c3"
        }
    elif score == 3:
        return {
            "dog": "🐩 푸들",
            "desc": "센스 있고 감성적인 당신은 푸들과 찰떡! 지적이고 사교적인 성격이에요.",
            "img": "https://images.unsplash.com/photo-1612531386535-d9f69a6fa5b5"
        }
    elif score == 4:
        return {
            "dog": "🦮 골든 리트리버",
            "desc": "다정하고 따뜻한 마음씨를 가진 당신은 골든 리트리버 그 자체예요!",
            "img": "https://images.unsplash.com/photo-1583511655826-05700d52f4db"
        }
    elif score == 5:
        return {
            "dog": "🐶 말티즈",
            "desc": "귀엽고 애교 많은 당신! 말티즈처럼 모두의 사랑을 듬뿍 받아요 💕",
            "img": "https://images.unsplash.com/photo-1593328124028-406a6ff0847c"
        }
    elif score == 6:
        return {
            "dog": "🐕 비숑 프리제",
            "desc": "뽀글뽀글 외모만큼이나 발랄한 에너지! 비숑처럼 긍정적인 매력이 넘쳐요!",
            "img": "https://images.unsplash.com/photo-1583337130417-3346a1a4a3c9"
        }
    else:
        return {
            "dog": "🐾 포메라니안",
            "desc": "작지만 강한 자신감! 포메라니안처럼 자신감 넘치고 귀엽게 자기 주장하는 스타일이에요.",
            "img": "https://images.unsplash.com/photo-1619983081563-430f63627307"
        }

# 현재 질문 인덱스
idx = st.session_state.question_index

# 앱 제목
st.title("🐾 당신은 어떤 강아지와 닮았을까요?")
st.markdown("재미있는 7문제 성격 테스트로 나와 닮은 강아지를 알아보세요!")

# 질문 표시
if idx < len(questions):
    st.markdown(f"### Q{idx+1}.")
    choice = st.radio("당신의 선택은?", [questions[idx][0], questions[idx][1]], key=idx)

    if st.button("다음 ➡️"):
        if choice == questions[idx][1]:
            st.session_state.score += 1
        st.session_state.question_index += 1
        st.experimental_rerun()

# 결과 표시
else:
    result = get_dog_result(st.session_state.score)
    st.subheader(f"✨ 당신은 {result['dog']}!")
    st.write(result["desc"])
    st.image(result["img"], use_column_width=True)

    if st.button("🔁 다시 시작하기"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.experimental_rerun()
