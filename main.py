import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="집가고싶다 🏠",
    page_icon="🏠",
    layout="centered"
)

# CSS 스타일 적용
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
    }
    .title {
        font-size: 60px;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        animation: bounce 1s infinite alternate;
    }
    .subtitle {
        font-size: 30px;
        text-align: center;
        color: #4ECDC4;
        margin-top: 10px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-top: 20px;
        text-align: center;
    }
    @keyframes bounce {
        from { transform: translateY(0px); }
        to   { transform: translateY(-10px); }
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<div class="title">🏠 집 가고싶다...</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">안녕하세요!!! 🐱👻</div>', unsafe_allow_html=True)

st.divider()

# 카드 섹션
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 😩 지금 내 상태")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🏠 집까지 거리", value="999km", delta="멀다")
with col2:
    st.metric(label="😴 피곤함 지수", value="100%", delta="최고조")
with col3:
    st.metric(label="⏰ 하교까지", value="3시간", delta="-빨리가라")

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 버튼
st.markdown("### 🎮 지금 기분이 어때?")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("😭 너무 힘들어"):
        st.snow()
        st.error("😭 조금만 더 힘내자...!! 집에 가면 침대가 기다려!")
with col2:
    if st.button("😐 그냥저냥"):
        st.warning("😐 그래도 버티는 중! 대단한걸?")
with col3:
    if st.button("😊 사실 괜찮아"):
        st.balloons()
        st.success("🎉 역시 멋진 당곡인!")

st.divider()

# 집에서 하고싶은 것 체크리스트
st.markdown("### 📋 집 가면 할 것들 (버킷리스트)")

things = {
    "🛋️ 소파에 눕기": False,
    "🍕 치킨 시키기": False,
    "📱 유튜브 보기": False,
    "😴 낮잠 자기": False,
    "🎮 게임하기": False,
    "🛁 뜨끈한 샤워": False,
}

checked_count = 0
for thing, default in things.items():
    if st.checkbox(thing, value=default):
        checked_count += 1

st.progress(checked_count / len(things))
st.caption(f"총 {len(things)}개 중 {checked_count}개 계획 완료! 🎯")

st.divider()

# 명언 섹션
import random
quotes = [
    "🌟 끝나지 않는 수업은 없다!",
    "🏠 집은 언제나 널 기다리고 있어!",
    "💪 조금만 더! 넌 할 수 있어!",
    "🎯 오늘 하루만 버티면 내일은 달라!",
    "😎 당곡인은 강하다!",
]

st.markdown("### 💬 오늘의 명언")
if st.button("🔄 명언 뽑기!"):
    st.info(random.choice(quotes))

st.divider()
st.caption("🏫 당곡고등학교 | 오늘도 수고했어요! 🎉")
