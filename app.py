import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Karis 금융 계산기 포털", layout="centered")

# 페이지 상태 관리
if 'page' not in st.session_state:
    st.session_state.page = "main"

# 공통 블로그 배너 함수
def show_blog_banner():
    st.markdown("---")
    st.markdown("""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 30px; text-align: center;">
            <h4 style="color: #333; margin-bottom: 10px;">✍️ Karis의 테크 & 재테크 블로그</h4>
            <p style="color: #555; margin-bottom: 15px;">최신 공모주 상세 분석, IPO 청약 일정 및 재테크 꿀팁을 놓치지 마세요!</p>
            <a href="https://blog.naver.com/karis_official" target="_blank" style="text-decoration: none; color: #ffffff; background-color: #00c73c; padding: 10px 20px; border-radius: 5px; font-weight: bold;">블로그 바로가기</a>
        </div>
    """, unsafe_allow_html=True)

# 1. 메인 화면
if st.session_state.page == "main":
    st.title("💰 Karis 금융 계산기 포털")
    st.subheader("원하시는 계산기를 선택하세요")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📉 대출 이자 계산기", use_container_width=True):
            st.session_state.page = "loan"; st.rerun()
    with col2:
        if st.button("📊 DSR 계산기", use_container_width=True):
            st.session_state.page = "dsr"; st.rerun()
    with col3:
        if st.button("💰 공모주 청약 증거금 계산기", use_container_width=True):
            st.session_state.page = "ipo"; st.rerun()
            
    show_blog_banner()

# 2. 계산기 로직
def go_back_button():
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = "main"; st.rerun()

if st.session_state.page == "loan":
    st.header("📉 대출 이자 계산기")
    go_back_button()
    # (여기에 기존 대출 계산기 로직 삽입)
    show_blog_banner()

elif st.session_state.page == "dsr":
    st.header("📊 DSR(총부채원리금상환비율) 계산기")
    go_back_button()
    income = st.number_input("연 소득 (원)", value=50000000)
    # ... (DSR 로직)
    show_blog_banner()

elif st.session_state.page == "ipo":
    st.header("💰 공모주 청약 증거금 계산기")
    go_back_button()
    price = st.number_input("확정 공모가 (원)", value=27000)
    count = st.number_input("청약 수량 (주)", value=10)
    # ... (IPO 로직)
    show_blog_banner()
