import streamlit as st

# 제목
st.title('나의 첫 Streamlit 앱')

# 텍스트
st.write("안녕하세요! 이것은 Streamlit을 이용한 간단한 웹 앱입니다.")

# 버튼 클릭 시 이벤트 처리
if st.button('클릭하세요'):
    st.write('버튼이 클릭되었습니다!')

# 숫자 입력 받기
number = st.number_input('숫자를 입력하세요', 0, 100)
st.write(f'입력한 숫자: {number}')
