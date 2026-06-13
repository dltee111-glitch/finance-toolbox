import streamlit as st
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="Karis 금융 계산기 포털", layout="centered")

# 2. 메인 화면 구성 (대시보드 방식)
st.title("💰 Karis 금융 계산기 포털")
st.markdown("---")

# 세션 상태를 사용하여 페이지 전환 관리
if 'page' not in st.session_state:
    st.session_state.page = "main"

def go_main():
    st.session_state.page = "main"

if st.session_state.page == "main":
    st.subheader("원하시는 계산기를 선택하세요")
    
    # 카드형 UI 구현
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📉 대출 이자 계산기", use_container_width=True):
            st.session_state.page = "loan"
            st.rerun()
    with col2:
        if st.button("📊 DSR 계산기", use_container_width=True):
            st.session_state.page = "dsr"
            st.rerun()
    with col3:
        if st.button("💰 공모주 청약", use_container_width=True):
            st.session_state.page = "ipo"
            st.rerun()

# 3. 계산기 로직 페이지들

def loan_calculator():
    st.header("🏠 대출 이자 계산기")
    if st.button("← 메인으로 돌아가기"):
        go_main(); st.rerun()
        
    tab1, tab2, tab3 = st.tabs(["주택담보대출", "전세자금대출", "신용/마이너스"])
    # ... 기존 로직 동일 ...
    with tab1:
        st.subheader("주택담보대출 계산")
        p = st.number_input("대출 원금 (원)", value=300000000, step=10000000)
        y = st.number_input("대출 기간 (년)", value=30)
        r = st.number_input("연 금리 (%)", value=4.0, step=0.1)
        if st.button("주택담보 계산"):
            m_rate = (r / 100) / 12
            months = y * 12
            payment = p * (m_rate * (1 + m_rate) ** months) / ((1 + m_rate) ** months - 1)
            st.metric("월 예상 상환액", f"{int(payment):,} 원")
    with tab2:
        st.subheader("전세자금대출 계산")
        p = st.number_input("전세 대출금 (원)", value=200000000, step=10000000)
        y = st.number_input("대출 기간 (년)", value=2)
        r = st.number_input("연 금리 (%)", value=3.5, step=0.1)
        if st.button("전세자금 계산"):
            m_rate = (r / 100) / 12
            months = y * 12
            payment = p * (m_rate * (1 + m_rate) ** months) / ((1 + m_rate) ** months - 1)
            st.metric("월 예상 이자액", f"{int(payment):,} 원")
    with tab3:
        st.subheader("신용/마이너스 통장 계산")
        amount = st.number_input("사용 금액 (원)", value=10000000, step=1000000)
        r = st.number_input("연 금리 (%)", value=5.5, step=0.1)
        days = st.number_input("사용 일수 (일)", value=30)
        if st.button("이자 계산"):
            interest = amount * (r / 100) * (days / 365)
            st.metric("예상 발생 이자", f"{int(interest):,} 원")

def dsr_calculator():
    st.header("📊 DSR(총부채원리금상환비율) 계산기")
    if st.button("← 메인으로 돌아가기"):
        go_main(); st.rerun()
    income = st.number_input("연 소득 (원)", value=50000000, step=1000000)
    existing_debt_repayment = st.number_input("연간 기존 부채 원리금 상환액 (원)", value=10000000, step=1000000)
    new_loan_repayment = st.number_input("연간 신규 대출 원리금 상환액 (원)", value=5000000, step=1000000)
    total_repayment = existing_debt_repayment + new_loan_repayment
    dsr = (total_repayment / income) * 100
    st.metric("예상 DSR", f"{dsr:.2f} %")

def ipo_calculator():
    st.header("💰 공모주 청약 증거금 계산기")
    if st.button("← 메인으로 돌아가기"):
        go_main(); st.rerun()
    price = st.number_input("확정 공모가 (원)", value=27000)
    count = st.number_input("청약 수량 (주)", value=10)
    margin_rate = st.radio("증거금율", [50, 100])
    total = price * count * (margin_rate / 100)
    st.metric("필요 증거금", f"{int(total):,} 원")

# 4. 페이지 라우팅
if st.session_state.page == "loan":
    loan_calculator()
elif st.session_state.page == "dsr":
    dsr_calculator()
elif st.session_state.page == "ipo":
    ipo_calculator()
