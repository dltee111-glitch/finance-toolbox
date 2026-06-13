import streamlit as st
import pandas as pd

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
        # 버튼 텍스트를 간결하게 수정
        if st.button("📉 대출 상환 계산기", use_container_width=True):
            st.session_state.page = "loan"; st.rerun()
        st.caption("이자 및 예상 상환액 확인")
    with col2:
        if st.button("📊 DSR 계산기", use_container_width=True):
            st.session_state.page = "dsr"; st.rerun()
        st.caption("총부채원리금상환비율 확인")
    with col3:
        if st.button("💰 청약 증거금 계산기", use_container_width=True):
            st.session_state.page = "ipo"; st.rerun()
        st.caption("공모주 청약 필요 금액")
            
    show_blog_banner()

# 2. 계산기 로직
def go_back_button():
    if st.button("← 메인으로 돌아가기"):
        st.session_state.page = "main"; st.rerun()

if st.session_state.page == "loan":
    st.header("📉 대출 이자 및 상환 예상 금액 계산")
    go_back_button()
    
    amount = st.number_input("대출 원금 (원)", value=10000000, step=1000000)
    rate = st.number_input("연 금리 (%)", value=5.0, step=0.1) / 100
    months = st.number_input("대출 기간 (개월)", value=12, step=1)
    
    if st.button("상환 스케줄 계산"):
        m_rate = rate / 12
        monthly_payment = amount * (m_rate * (1 + m_rate) ** months) / ((1 + m_rate) ** months - 1)
        
        schedule = []
        balance = amount
        for i in range(1, months + 1):
            interest = balance * m_rate
            principal = monthly_payment - interest
            balance -= principal
            schedule.append([i, int(principal), int(interest), int(max(0, balance))])
            
        df = pd.DataFrame(schedule, columns=["회차", "상환 원금", "이자", "잔금"])
        st.write("### 상환 스케줄 상세")
        st.dataframe(df, use_container_width=True)
        
    show_blog_banner()

elif st.session_state.page == "dsr":
    st.header("📊 DSR(총부채원리금상환비율) 계산기")
    go_back_button()
    income = st.number_input("연 소득 (원)", value=50000000)
    existing_debt = st.number_input("기존 부채 원리금 (원)", value=10000000)
    new_loan = st.number_input("신규 대출 원리금 (원)", value=5000000)
    if st.button("계산"):
        dsr = ((existing_debt + new_loan) / income) * 100
        st.metric("예상 DSR", f"{dsr:.2f} %")
    show_blog_banner()

elif st.session_state.page == "ipo":
    st.header("💰 공모주 청약 증거금 계산기")
    go_back_button()
    price = st.number_input("확정 공모가 (원)", value=27000)
    count = st.number_input("청약 수량 (주)", value=10)
    margin_rate = st.radio("증거금율", [50, 100])
    if st.button("계산"):
        total = price * count * (margin_rate / 100)
        st.metric("필요 증거금", f"{int(total):,} 원")
    show_blog_banner()
