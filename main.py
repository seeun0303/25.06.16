def get_dog_result(score):
    if score <= 1:
        return {
            "dog": "🐕 진돗개",
            "desc": "조용하고 단단한 당신은 진돗개 스타일! 한 번 정한 건 끝까지 밀고 나가는 충직한 성격이에요.",
            "img": "https://images.unsplash.com/photo-1635086458566-c801e760c01d"
        }
    elif score == 2:
        return {
            "dog": "🐶 시바 이누",
            "desc": "귀여운 외모 속 시크한 매력! 시바 이누처럼 자기 주관이 뚜렷하고 깔끔한 스타일이에요.",
            "img": "https://images.unsplash.com/photo-1601758123927-1961a6b0e1c3"
        }
    elif score == 3:
        return {
            "dog": "🐩 푸들",
            "desc": "감성적이고 똑똑한 당신은 푸들과 찰떡! 예술적인 기질과 사교성이 매력적이에요.",
            "img": "https://images.unsplash.com/photo-1612531386535-d9f69a6fa5b5"
        }
    elif score == 4:
        return {
            "dog": "🦮 골든 리트리버",
            "desc": "누구에게나 따뜻하고 다정한 당신! 골든 리트리버처럼 배려심 넘치는 천사 같은 성격이에요.",
            "img": "https://images.unsplash.com/photo-1583511655826-05700d52f4db"
        }
    elif score == 5:
        return {
            "dog": "🐶 말티즈",
            "desc": "귀엽고 애교 넘치는 당신! 말티즈처럼 주변의 사랑을 듬뿍 받는 타입이에요.",
            "img": "https://images.unsplash.com/photo-1593328124028-406a6ff0847c"
        }
    elif score == 6:
        return {
            "dog": "🐕 비숑 프리제",
            "desc": "뽀글뽀글한 외모처럼 발랄하고 사교적인 당신! 비숑은 주변에 기분 좋은 에너지를 퍼뜨려요.",
            "img": "https://images.unsplash.com/photo-1583337130417-3346a1a4a3c9"
        }
    else:
        return {
            "dog": "🐾 포메라니안",
            "desc": "작지만 강한 에너지! 포메라니안처럼 자신감 넘치고 리더십 있는 스타일이에요.",
            "img": "https://images.unsplash.com/photo-1619983081563-430f63627307"
        }
