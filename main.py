import streamlit as st

# 페이지 초기 설정
st.set_page_config(page_title="🐶 나와 닮은 강아지 찾기", layout="centered")

# 질문과 선택지 리스트 (왼쪽 0점, 오른쪽 1점)
questions = [
    ("🧘 혼자 있는 게 편해요", "👯 사람들과 어울리는 게 좋아요"),
    ("📅 계획적인 게 좋아요", "🎲 즉흥적인 게 좋아요"),
    ("🔇 차분하고 조용한 편이에요", "🎉 활발하고 시끄러운 편이에요"),
    ("🏡 익숙한 게 좋아요", "🛫 새로운 걸 도전하는 게 좋아요"),
    ("🧠 이성적으로 판단해요", "💖 감정적으로 판단해요"),
    ("👑 주도적인 스타일이에요", "🧸 따라가는 걸 더 좋아해요"),
    ("📚 집에서 쉬는 게 좋아요", "🚴 밖에서 활동하는 게 좋아요")
]

# 소형견 위주의 결과 매핑
def get_result(score):
    if score <= 1:
        return {
            "dog": "🐕 진돗개",
            "desc": "조용하고 충직한 당신은 진돗개 스타일! 묵묵히 자기 길을 가는 타입이에요.",
            "img": "https://images.unsplash.com/photo-1635086458566-c801e760c01d"
        }
    elif score == 2:
        return {
            "dog": "🐶 시바 이누",
            "desc": "귀여움+시크함 모두 갖춘 시바 이누! 자기 주관이 뚜렷한 당신에게 딱이에요.",
            "img": "https://images.unsplash.com/photo-1601758123927-1961a6b0e1c3"
        }
    elif score == 3:
        return {
            "dog": "🐩 푸들",
            "desc": "지적이고 예술적 감성이 풍부한 당신은 푸들과 찰떡궁합!",
            "img": "https://images.unsplash.com/photo-1612531386535-d9f69a6fa5b5"
        }
    elif score == 4:
        return {
            "dog": "🦮 골든 리트리버",
            "desc": "다정하고 배려 깊은 성격의 당신은 골든 리트리버처럼 모두에게 인기만점이에요!",
            "img": "https://images.unsplash.com/photo-1583511655826-05700d52f4db"
        }
    elif score == 5:
        return {
            "dog": "🐶 말티즈",
            "desc": "귀엽고 애교 만점! 말티즈처럼 사랑스러운 매력을 가진 당신 💖",
            "img": "https://images.unsplash.com/photo-1593328124028-406a6ff0847c"
        }
    elif score == 6:
        return {
            "dog": "🐕 비숑 프리제",
            "desc": "활발하고 긍정적인 당신! 비숑 프리제처럼 주변을 행복하게 해요 😊",
            "img": "https://images.unsplash.com/photo-1583337130417-3346a1a4a3c9"
        }
    else:
        return {
            "dog": "🐾 포메라니안",
            "desc": "자신감 뿜뿜! 포메라니안처럼 작지만 에너지 넘치는 당신 ✨",
            "img": "https://images.unsplash.com/photo-1619983081563-430f63627307"
        }

# 세션 상태 초기화
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0

# 현재 인덱스
index = st.session_state.q_index

# 앱 제목
st.title("🐾 나와 닮은 강아지를 찾아보자!")
st.markdown("재미있는 7개의 질문을 통해 당신과 닮은 귀여운 강아지를 알려드릴게요 🐶")

# 질문 진행
if index < len(questions):
    left, right = questions[index]

    st.markdown(f"### Q{index+1}.")
    choice = st.radio("당신의 선택은?", [left, right], key=index)

    if st.button("다음 ➡️"):
        # 오른쪽 선택 시 1점
        if choice == right:
            st.session_state.score += 1
        st.session_state.q_index += 1
        st.experimental_rerun()

# 결과 출력
else:
    result = get_result(st.session_state.score)
    st.subheader(f"✨ 당신은 {result['dog']}!")
    st.write(result["desc"])
    st.image(result["img"], use_column_width=True)

    # 다시 시작 버튼
    if st.button("🔄 다시 테스트하기"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.experimental_rerun()
