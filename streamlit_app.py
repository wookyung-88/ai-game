import random
import streamlit as st

st.set_page_config(page_title="중학생 영어 단어 게임", page_icon="📚", layout="centered")

st.title("📘 중학생 영어 단어 게임")
st.write("중학생 수준의 영어 단어를 재미있게 공부해 보세요. 문제를 풀고 `다음 문제` 버튼을 눌러 보세요.")

WORDS = [
    {"english": "apple", "korean": "사과"},
    {"english": "school", "korean": "학교"},
    {"english": "family", "korean": "가족"},
    {"english": "friend", "korean": "친구"},
    {"english": "book", "korean": "책"},
    {"english": "teacher", "korean": "선생님"},
    {"english": "class", "korean": "수업"},
    {"english": "music", "korean": "음악"},
    {"english": "dance", "korean": "춤"},
    {"english": "happy", "korean": "행복한"},
    {"english": "summer", "korean": "여름"},
    {"english": "winter", "korean": "겨울"},
    {"english": "water", "korean": "물"},
    {"english": "apple", "korean": "사과"},
    {"english": "sports", "korean": "운동"},
    {"english": "movie", "korean": "영화"},
    {"english": "travel", "korean": "여행"},
    {"english": "computer", "korean": "컴퓨터"},
    {"english": "animal", "korean": "동물"},
    {"english": "happy", "korean": "행복한"},
    {"english": "family", "korean": "가족"},
    {"english": "study", "korean": "공부하다"},
    {"english": "mountain", "korean": "산"},
    {"english": "river", "korean": "강"},
    {"english": "ocean", "korean": "바다"},
    {"english": "food", "korean": "음식"},
    {"english": "market", "korean": "시장"},
    {"english": "picture", "korean": "그림"},
    {"english": "happy", "korean": "행복한"},
]

if "question" not in st.session_state:
    st.session_state.question = None
    st.session_state.correct_answer = None
    st.session_state.options = []
    st.session_state.mode = "영단어 → 뜻"
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""

mode = st.radio("게임 모드 선택", ["영단어 → 뜻", "뜻 → 영단어"], index=0)

if mode != st.session_state.mode:
    st.session_state.mode = mode
    st.session_state.question = None
    st.session_state.feedback = ""

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("**게임 방법**")
    st.write(
        "1. 문제를 보고 네 가지 보기 중에서 정답을 선택합니다.\n"
        "2. `정답 확인` 버튼을 누르면 맞았는지 확인합니다.\n"
        "3. `다음 문제` 버튼으로 새로운 문제를 풀어보세요."
    )
with col2:
    st.metric("정답", st.session_state.score, delta=f"/ {st.session_state.total}")

st.divider()

if st.session_state.question is None:
    st.session_state.question = random.choice(WORDS)

def make_options(question, mode):
    items = WORDS.copy()
    random.shuffle(items)
    if mode == "영단어 → 뜻":
        correct = question["korean"]
        choices = [item["korean"] for item in items if item["korean"] != correct][:3]
    else:
        correct = question["english"]
        choices = [item["english"] for item in items if item["english"] != correct][:3]
    choices.append(correct)
    random.shuffle(choices)
    return correct, choices

if not st.session_state.options:
    st.session_state.correct_answer, st.session_state.options = make_options(st.session_state.question, st.session_state.mode)

st.subheader("문제")
if st.session_state.mode == "영단어 → 뜻":
    st.write(f"**{st.session_state.question['english']}** 의 뜻은 무엇일까요?")
else:
    st.write(f"**{st.session_state.question['korean']}** 에 해당하는 영어 단어는 무엇일까요?")

answer = st.radio("보기 중에서 선택하세요", st.session_state.options)
solve = st.button("정답 확인")
next_q = st.button("다음 문제")

if solve:
    st.session_state.total += 1
    if answer == st.session_state.correct_answer:
        st.session_state.score += 1
        st.session_state.feedback = "🎉 정답입니다! 잘했어요."
    else:
        st.session_state.feedback = f"❌ 틀렸어요. 정답은 `{st.session_state.correct_answer}` 입니다."

if st.session_state.feedback:
    st.success(st.session_state.feedback)

if next_q:
    st.session_state.question = random.choice(WORDS)
    st.session_state.correct_answer, st.session_state.options = make_options(st.session_state.question, st.session_state.mode)
    st.session_state.feedback = ""

st.divider()

st.write("---")
st.write("### 단어 목록 예시")
example_words = random.sample(WORDS, min(6, len(WORDS)))
for item in example_words:
    st.write(f"- {item['english']} : {item['korean']}")
