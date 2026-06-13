import streamlit as st
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="Karis 금융 계산기 포털", layout="centered")

# 2. 사이드바 메뉴 개선
st.sidebar.title("💰 Karis 금융 계산기 포털")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "메뉴 선택",
    ["🏠 대출 이자 계산기", "📊 DSR 계산기", "💰 공모주 청약 계산기"]
)

# 3. 각 계산기 함수 정의

def loan_calculator():
    st.header("🏠 대출 이자 계산기")
    # 탭을 사용하여 대출 유형 분리
    tab1, tab2, tab3 = st.tabs(["주택담보대출", "전세자금대출", "신용/마이너스"])

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
        st.write("기본 원리금 균등 상환 로직 적용")
        # 전세 대출 관련 로직 추가 공간

    with tab3:
        st.subheader("신용/마이너스 통장 계산")
        # 기존 마통 계산기 로직 삽입 가능

def dsr_calculator():
    st.header("📊 DSR(총부채원리금상환비율) 계산기")
    income = st.number_input("연 소득 (원)", value=50000000, step=1000000)
    existing_debt_repayment = st.number_input("연간 기존 부채 원리금 상환액 (원)", value=10000000, step=1000000)
    new_loan_repayment = st.number_input("연간 신규 대출 원리금 상환액 (원)", value=5000000, step=1000000)
    
    total_repayment = existing_debt_repayment + new_loan_repayment
    dsr = (total_repayment / income) * 100
    
    st.metric("예상 DSR", f"{dsr:.2f} %")
    if dsr > 40:
        st.error("DSR이 40%를 초과합니다. 대출 규제 영향권입니다.")
    else:
        st.success("DSR이 40% 이하입니다. 대출이 원활할 수 있습니다.")

def ipo_calculator():
    st.header("💰 공모주 청약 증거금 계산기")
    price = st.number_input("확정 공모가 (원)", value=27000)
    count = st.number_input("청약 수량 (주)", value=10)
    margin_rate = st.radio("증거금율", [50, 100])
    
    total = price * count * (margin_rate / 100)
    st.metric("필요 증거금", f"{int(total):,} 원")

# 4. 메뉴 실행
if menu == "🏠 대출 이자 계산기":
    loan_calculator()
elif menu == "📊 DSR 계산기":
    dsr_calculator()
elif menu == "💰 공모주 청약 계산기":
    ipo_calculator()
