import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🎮 나와 닮은 강아지 찾기!", layout="centered")

# 질문 리스트 (왼쪽 0점 / 오른쪽 1점)
questions = [
    ("🧘 혼자 있는 게 편해요", "👯 사람들과 어울리는 게 좋아요"),
    ("📅 계획적인 게 좋아요", "🎲 즉흥적인 게 좋아요"),
    ("🤫 조용하고 차분해요", "🎉 시끄럽고 활발해요"),
    ("🏡 익숙한 게 좋아요", "✈️ 새로운 걸 좋아해요"),
    ("🧠 이성적으로 판단해요", "💖 감정적으로 판단해요"),
    ("🦁 리더가 되고 싶어요", "🐑 따라가는 게 편해요"),
    ("📚 집콕이 좋아요", "🚴 밖이 좋아요")
]

# 결과 매핑 함수
def get_result(score):
    if score <= 1:
        return {
            "dog": "🐕 진돗개",
            "desc": "조용하고 충직한 당신은 진돗개 스타일! 🧘‍♂️ 묵묵히 자기 길을 가는 타입이에요.",
            "img": "https://images.unsplash.com/photo-1635086458566-c801e760c01d"
        }
    elif score == 2:
        return {
            "dog": "🦊 시바 이누",
            "desc": "귀여움 💕 + 시크함 😎 의 조화! 자기주관 뚜렷한 당신은 시바 이누!",
            "img": "https://images.unsplash.com/photo-1601758123927-1961a6b0e1c3"
        }
    elif score == 3:
        return {
            "dog": "🎨 푸들",
            "desc": "지적이고 감성적인 당신은 예술혼 넘치는 푸들과 잘 어울려요!",
            "img": "https://images.unsplash.com/photo-1612531386535-d9f69a6fa5b5"
        }
    elif score == 4:
        return {
            "dog": "💛 골든 리트리버",
            "desc": "누구에게나 친절한 당신! 사랑받는 인기쟁이 골든 리트리버 타입이에요 🐾",
            "img": "https://images.unsplash.com/photo-1583511655826-05700d52f4db"
        }
    elif score == 5:
        return {
            "dog": "🌟 말티즈",
            "desc": "애교 만점 귀염둥이 💕 언제나 사랑받는 당신은 말티즈 스타일!",
            "img": "https://images.unsplash.com/photo-1593328124028-406a6ff0847c"
        }
    elif score == 6:
        return {
            "dog": "😄 비숑 프리제",
            "desc": "활기차고 긍정적인 에너지 폭발! 모두를 웃게 만드는 당신은 비숑 🐩",
            "img": "https://images.unsplash.com/photo-1583337130417-3346a1a4a3c9"
        }
    else:
        return {
            "dog": "🔥 포메라니안",
            "desc": "작지만 강한 존재감! 자신감 넘치는 당신은 포메라니안 ✨",
            "img": "https://images.unsplash.com/photo-1619983081563-430f63627307"
        }

# 세션 상태 초기화
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0

index = st.session_state.q_index

# 제목
st.markdown("<h1 style='text-align: center;'>🎮 성격 테스트: 나와 닮은 강아지는? 🐶</h1>", unsafe_allow_html=True)
st.markdown("🐾 7가지 질문에 답하고, 당신과 찰떡궁합인 강아지를 알아보세요! 🎉")

# 진행 표시
st.progress(index / len(questions))

# 질문 진행
if index < len(questions):
    left, right = questions[index]
    
    st.markdown(f"<h3>❓ Q{index + 1}</h3>", unsafe_allow_html=True)
    choice = st.radio("👇 당신의 선택은?", [left, right], key=index)

    if st.button("➡️ 다음 질문"):
        if choice == right:
            st.session_state.score += 1
        st.session_state.q_index += 1
        st.rerun()

# 결과 페이지
else:
    result = get_result(st.session_state.score)
    st.balloons()  # 🎈 풍선 애니메이션 효과
    st.markdown(f"<h2 style='text-align: center;'>✨ 당신은 <span style='color:#FF6F61'>{result['dog']}</span> 타입!</h2>", unsafe_allow_html=True)
    st.image(result["img"], use_column_width=True)
    st.markdown(f"<p style='font-size:20px; text-align:center;'>{result['desc']}</p>", unsafe_allow_html=True)

    # 다시하기 버튼
    if st.button("🔄 다시 테스트하기"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.rerun()
