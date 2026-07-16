import random
import streamlit as st

st.set_page_config(page_title="에이핑크 팬 인증 게임", page_icon="💗", layout="centered")

st.title("💗 에이핑크 팬 인증 게임")
st.write("에이핑크를 얼마나 잘 아는지 확인하는 팬 인증 게임입니다. 문제를 풀고 바로 정답 여부를 확인해보세요!")

QUESTIONS = [
    {
        "question": "에이핑크 데뷔 연도는 언제일까요?",
        "choices": ["2010년", "2011년", "2012년", "2013년"],
        "answer": "2011년",
    },
    {
        "question": "에이핑크 정은지의 생일은 언제일까요?",
        "choices": ["1990년 8월 18일", "1991년 1월 18일", "1992년 9월 18일", "1993년 3월 18일"],
        "answer": "1993년 8월 18일",
    },
    {
        "question": "에이핑크의 데뷔 날짜는 언제일까요?",
        "choices": ["2011년 4월 19일", "2011년 5월 21일", "2012년 3월 17일", "2010년 5월 26일"],
        "answer": "2011년 4월 19일",
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
        "question": "에이핑크 정은지가 출연하지 않은 작품은?",
        "choices": ["응답하라 1997", "당신이 잠든 사이에", "마이 디어 프렌즈", "나의 아저씨"],
        "answer": "나의 아저씨",
    },
    {
        "question": "에이핑크 정은지가 OST를 부른 드라마는?",
        "choices": ["고교처세왕", "천일의 약속", "혼술남녀", "푸른 바다의 전설"],
        "answer": "고교처세왕",
    },
    {
        "question": "에이핑크가 데뷔할 때 발표한 첫 번째 앨범 이름은?",
        "choices": ["Seven Springs of Apink", "Pink Blossom", "Secret Garden", "Pink Memory"],
        "answer": "Seven Springs of Apink",
    },
    {
        "question": "에이핑크의 데뷔 타이틀 곡은 무엇인가요?",
        "choices": ["몰라요", "NoNoNo", "Mr. Chu", "LUV"],
        "answer": "몰라요",
    },
    {
        "question": "에이핑크 정은지가 솔로로 발표한 곡은 무엇일까요?",
        "choices": ["하늘바라기", "러브 레터", "너란 봄", "아마도 그건"],
        "answer": "하늘바라기",
    },
    {
        "question": "에이핑크의 곡 'NoNoNo'가 수록된 앨범은 무엇일까요?",
        "choices": ["Pink Blossom", "Secret Garden", "Pink Memory", "Snow Pink"],
        "answer": "Pink Blossom",
    },
    {
        "question": "에이핑크 그룹 이름의 영어 표기는 무엇일까요?",
        "choices": ["Apink", "A Pink", "Pink A", "A-pink"],
        "answer": "Apink",
    },
    {
        "question": "에이핑크가 소속된 회사는 어디일까요?",
        "choices": ["YG 엔터테인먼트", "SM 엔터테인먼트", "플레디스 엔터테인먼트", "JYP 엔터테인먼트"],
        "answer": "플레디스 엔터테인먼트",
    },
    {
        "question": "에이핑크 멤버 수는 몇 명일까요?",
        "choices": ["4명", "5명", "6명", "7명"],
        "answer": "6명",
    },
    {
        "question": "에이핑크 멤버 중 '초롱이'라는 별명을 가진 사람은?",
        "choices": ["박초롱", "윤보미", "정은지", "오하영"],
        "answer": "박초롱",
    },
    {
        "question": "에이핑크 멤버 중 '남주'라는 이름이 들어간 사람은?",
        "choices": ["김남주", "윤보미", "손나은", "정은지"],
        "answer": "김남주",
    },
    {
        "question": "에이핑크 멤버 중 '하영'이라는 이름이 들어간 사람은?",
        "choices": ["오하영", "박초롱", "정은지", "김남주"],
        "answer": "오하영",
    },
    {
        "question": "에이핑크의 팬덤 이름은 무엇일까요?",
        "choices": ["Pink Panda", "Pink Star", "Pink Berry", "Pink Love"],
        "answer": "Pink Panda",
    },
    {
        "question": "에이핑크의 공식 그룹 색상은 무엇일까요?",
        "choices": ["파란색", "초록색", "핑크", "보라색"],
        "answer": "핑크",
    },
    {
        "question": "에이핑크 멤버 중 '나은'이라는 이름이 들어간 사람은?",
        "choices": ["손나은", "김남주", "윤보미", "오하영"],
        "answer": "손나은",
    },
]

if "current" not in st.session_state:
    st.session_state.current = None
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""
    st.session_state.selected = None

if st.session_state.current is None:
    st.session_state.current = random.choice(QUESTIONS)

st.markdown("**게임 방법**")
st.write(
    "1. 보기를 보고 정답을 선택합니다.\n"
    "2. 선택하면 바로 정답 여부가 나옵니다.\n"
    "3. `다음 문제`로 새로운 문제를 풀어보세요."
)

col1, col2 = st.columns([2, 1])
with col2:
    st.metric("맞은 문제", st.session_state.score, delta=f"/ {st.session_state.total}")

st.divider()

st.subheader("문제")
st.write(f"**{st.session_state.current['question']}**")

selected = st.radio("보기 중에서 선택하세요", st.session_state.current["choices"], index=0)

if selected != st.session_state.selected:
    st.session_state.selected = selected
    st.session_state.total += 1
    if st.session_state.selected == st.session_state.current["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = "🎉 정답입니다! 당신은 진짜 에이핑크 팬이에요."
    else:
        st.session_state.feedback = f"❌ 아쉽습니다. 정답은 `{st.session_state.current['answer']}` 입니다."

if st.button("다음 문제"):
    st.session_state.current = random.choice(QUESTIONS)
    st.session_state.selected = None
    st.session_state.feedback = ""

if st.session_state.feedback:
    st.info(st.session_state.feedback)

st.divider()

st.write("---")
st.write("### 에이핑크 팬 인증 퀴즈에 도전해보세요!")
st.write("- 데뷔 연도, 멤버, 팬클럽 이름 등 기본 상식을 테스트합니다.")
st.write("- 더 많은 문제를 추가하면 팬 인증 난이도를 높일 수 있어요.")
