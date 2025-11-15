import streamlit as st

# 1. 앱 제목 설정
st.title("버튼 클릭 카운터 앱 🖱️")

# 2. 세션 상태 초기화
# 'count'라는 변수가 세션 상태에 없으면, 0으로 초기화합니다.
if 'count' not in st.session_state:
    st.session_state.count = 0

# 3. 버튼 클릭 시 호출될 함수 정의
def increment_counter():
    # 버튼이 클릭되면 'count' 값을 1 증가시킵니다.
    st.session_state.count += 1

# 4. 버튼 위젯 생성
# on_click 인수에 위에서 정의한 함수를 연결합니다.
st.button("숫자 증가시키기", on_click=increment_counter)

# 5. 현재 카운트 값 출력
st.header(f"현재 카운트: **{st.session_state.count}**")

st.markdown("---")
st.write("*버튼을 누르면 위에 있는 숫자가 실시간으로 증가합니다.*")
