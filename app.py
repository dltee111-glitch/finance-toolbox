import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="Karis 금융 계산기 포털", layout="centered")

st.title("💰 Karis 금융 계산기 포털")
st.markdown("원하시는 계산기를 선택하여 금융 자산을 체계적으로 관리하세요.")
st.markdown("---")

# 상단 선택 카드 레이아웃 (텍스트를 간결하게 수정)
col1, col2, col3, col4 = st.columns(4)

# 세션 상태를 이용한 페이지 전환
if 'page' not in st.session_state:
    st.session_state.page = "메인"

with col1:
    if st.button("📉 대출이자"): st.session_state.page = "대출"
with col2:
    if st.button("📈 마통이자"): st.session_state.page = "마통"
with col3:
    if st.button("💰 공모주"): st.session_state.page = "공모주"
with col4:
    if st.button("🏦 연금복리"): st.session_state.page = "연금"

st.markdown("---")

# 1. 대출 이자 계산기
def loan_calculator():
    st.subheader("📉 대출 이자 계산기")
    principal = st.number_input("대출 원금 (원)", min_value=100000, value=10000000, step=100000)
    rate = st.number_input("연 금리 (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
    period = st.number_input("대출 기간 (개월)", min_value=1, max_value=360, value=12)
    method = st.selectbox("상환 방식", ["원리금 균등 상환", "원금 균등 상환"])
    
    if st.button("계산 실행"):
        if method == "원리금 균등 상환":
            monthly_rate = (rate / 100) / 12
            if monthly_rate == 0:
                monthly_payment = principal / period
            else:
                monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** period) / ((1 + monthly_rate) ** period - 1)
            
            st.metric("월 예상 상환액", f"{int(monthly_payment):,} 원")
            st.metric("총 상환 금액", f"{int(monthly_payment * period):,} 원")
        else:
            st.info("원금 균등 상환은 준비 중입니다.")

# 2. 마이너스 통장 계산기
def minus_account_calculator():
    st.subheader("📈 마이너스 통장 계산기")
    limit = st.number_input("대출 한도 (원)", value=50000000)
    used_amount = st.number_input("사용 금액 (원)", value=1000000)
    days = st.number_input("사용 일수 (일)", value=30)
    interest_rate = st.number_input("연 이자율 (%)", value=6.0)
    if st.button("계산 실행"):
        interest = used_amount * (interest_rate / 100) * (days / 365)
        st.metric("예상 발생 이자", f"{int(interest):,} 원")

# 3. 공모주 청약 증거금 계산기
def ipo_calculator():
    st.subheader("💰 공모주 청약 증거금 계산기")
    price = st.number_input("공모가 (원)", value=20000)
    shares = st.number_input("청약 주식 수 (주)", value=100)
    ratio = st.number_input("증거금률 (%)", value=50)
    if st.button("계산 실행"):
        deposit = price * shares * (ratio / 100)
        st.metric("필요 증거금", f"{int(deposit):,} 원")

# 4. 연금저축 복리 계산기
def pension_calculator():
    st.subheader("🏦 연금저축 복리 계산기")
    col1, col2 = st.columns(2)
    with col1:
        monthly_deposit = st.number_input("월 적립액 (원)", min_value=0, value=300000, step=10000)
        annual_rate = st.number_input("연 기대 수익률 (%)", min_value=0.0, value=5.0, step=0.1)
    with col2:
        years = st.number_input("적립 기간 (년)", min_value=1, max_value=50, value=20)
    
    if st.button("복리 계산 시작"):
        total_principal = monthly_deposit * 12 * years
        monthly_rate = (annual_rate / 100) / 12
        months = years * 12
        future_value = monthly_deposit * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
        st.metric("총 적립 원금", f"{int(total_principal):,} 원")
        st.metric("예상 적립금 (세전)", f"{int(future_value):,} 원")
        st.success(f"총 {int(future_value - total_principal):,} 원의 이자 수익이 기대됩니다.")

# 페이지 분기 처리
if st.session_state.page == "대출":
    loan_calculator()
elif st.session_state.page == "마통":
    minus_account_calculator()
elif st.session_state.page == "공모주":
    ipo_calculator()
elif st.session_state.page == "연금":
    pension_calculator()
elif st.session_state.page == "메인":
    st.info("위 메뉴에서 원하시는 금융 계산기를 선택해 주세요.")

# 푸터
st.markdown("---")
st.markdown("""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 30px; text-align: center;">
        <h4 style="color: #333; margin-bottom: 10px;">✍️ Karis의 테크 & 재테크 블로그</h4>
        <a href="https://blog.naver.com/karis_official" target="_blank" style="text-decoration: none; color: #ffffff; background-color: #00c73c; padding: 10px 20px; border-radius: 5px; font-weight: bold;">블로그 바로가기</a>
    </div>
""", unsafe_allow_html=True)
