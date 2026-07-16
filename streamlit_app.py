import random
import streamlit as st

st.set_page_config(page_title="에이핑크 팬 인증 게임", page_icon="💗", layout="centered")

st.title("💗 에이핑크 팬 인증 게임")
st.write("에이핑크를 얼마나 잘 아는지 확인하는 팬 인증 게임입니다. 문제를 풀고 `정답 확인`을 눌러보세요!")

QUESTIONS = [
    {
        "question": "에이핑크 데뷔 연도는 언제일까요?",
        "choices": ["2010년", "2011년", "2012년", "2013년"],
        "answer": "2011년",
    },
    {
        "question": "에이핑크 리더의 이름은 무엇일까요?",
        "choices": ["보미", "정은지", "윤보미", "손나은"],
        "answer": "윤보미",
    },
    {
        "question": "다음 중 에이핑크의 곡이 아닌 것은?",
        "choices": ["Mr. Chu", "NoNoNo", "LUV", "Lion Heart"],
        "answer": "Lion Heart",
    },
    {
        "question": "에이핑크 멤버가 아닌 사람은 누구일까요?",
        "choices": ["박초롱", "김남주", "윤보미", "아이유"],
        "answer": "아이유",
    },
    {
        "question": "에이핑크의 공식 팬클럽 이름은 무엇일까요?",
        "choices": ["Pink Panda", "Pink Bubble", "Pink Candy", "Pink Star"],
        "answer": "Pink Panda",
    },
    {
        "question": "다음 중 에이핑크의 대표 색깔은 무엇인가요?",
        "choices": ["핑크", "푸른색", "노란색", "초록색"],
        "answer": "핑크",
    },
    {
        "question": "에이핑크 멤버 중 '에이핑크의 맏언니'로 불리는 사람은?",
        "choices": ["홍진영", "박초롱", "정은지", "남주"],
        "answer": "박초롱",
    },
    {
        "question": "에이핑크의 데뷔 앨범 제목은 무엇인가요?",
        "choices": ["Seven Springs of Apink", "Pink Blossom", "Remember", "Secret Garden"],
        "answer": "Seven Springs of Apink",
    },
]

if "current" not in st.session_state:
    st.session_state.current = None
    st.session_state.selected = None
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""

if st.session_state.current is None:
    st.session_state.current = random.choice(QUESTIONS)

st.markdown("**게임 방법**")
st.write(
    "1. 보기를 보고 정답을 선택합니다.\n"
    "2. `정답 확인`을 누르면 결과를 확인합니다.\n"
    "3. `다음 문제`로 새로운 문제를 풀어보세요."
)

col1, col2 = st.columns([2, 1])
with col2:
    st.metric("맞은 문제", st.session_state.score, delta=f"/ {st.session_state.total}")

st.divider()

st.subheader("문제")
st.write(f"**{st.session_state.current['question']}**")

st.session_state.selected = st.radio("보기 중에서 선택하세요", st.session_state.current["choices"], index=0)

col1, col2 = st.columns(2)
with col1:
    if st.button("정답 확인"):
        st.session_state.total += 1
        if st.session_state.selected == st.session_state.current["answer"]:
            st.session_state.score += 1
            st.session_state.feedback = "🎉 정답입니다! 당신은 진짜 에이핑크 팬이에요."
        else:
            st.session_state.feedback = f"❌ 아쉽습니다. 정답은 `{st.session_state.current['answer']}` 입니다."
with col2:
    if st.button("다음 문제"):
        st.session_state.current = random.choice(QUESTIONS)
        st.session_state.feedback = ""

if st.session_state.feedback:
    st.info(st.session_state.feedback)

st.divider()

st.write("---")
st.write("### 에이핑크 팬 인증 퀴즈에 도전해보세요!")
st.write("- 데뷔 연도, 멤버, 팬클럽 이름 등 기본 상식을 테스트합니다.")
st.write("- 더 많은 문제를 추가하면 팬 인증 난이도를 높일 수 있어요.")
