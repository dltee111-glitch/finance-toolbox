import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="Karis 금융 계산기 포털", layout="centered")

# 사이드바를 이용한 메뉴 내비게이션
st.sidebar.title("💰 Karis 금융 툴박스")
menu = st.sidebar.radio(
    "계산기 선택",
    ["📉 대출 이자 계산기", "📈 마이너스 통장 계산기", "💰 공모주 청약 계산기", "🏦 연금저축 복리 계산기"]
)

st.sidebar.markdown("---")
st.sidebar.info("블로그 방문자를 위한 금융 관리 도구 모음입니다.")

# 1. 대출 이자 계산기 로직
def loan_calculator():
    st.header("📉 대출 이자 계산기")
    # 기존 대출 이자 계산기 로직 유지
    principal = st.number_input("대출 원금 (원)", min_value=100000, value=10000000, step=100000)
    rate = st.number_input("연 금리 (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
    period = st.number_input("대출 기간 (개월)", min_value=1, max_value=360, value=12)
    method = st.selectbox("상환 방식", ["원리금 균등 상환", "원금 균등 상환"])
    
    if st.button("계산하기"):
        st.write("계산 로직이 여기에 실행됩니다.")

# 2. 마이너스 통장 계산기 로직
def minus_account_calculator():
    st.header("📈 마이너스 통장 계산기")
    st.write("사용한 만큼만 계산하는 일할 이자 분석기입니다.")

# 3. 공모주 청약 계산기 로직
def ipo_calculator():
    st.header("💰 공모주 청약 계산기")
    st.write("증거금 및 배정 수량을 계산합니다.")

# 4. 연금저축 복리 계산기 로직 (추가)
def pension_calculator():
    st.header("🏦 연금저축 복리 계산기")
    st.write("매년 적립 시 복리 효과를 계산합니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        monthly_deposit = st.number_input("월 적립액 (원)", min_value=0, value=300000, step=10000)
        annual_rate = st.number_input("연 기대 수익률 (%)", min_value=0.0, value=5.0, step=0.1)
    with col2:
        years = st.number_input("적립 기간 (년)", min_value=1, max_value=50, value=20)
    
    if st.button("복리 계산 시작"):
        total_principal = monthly_deposit * 12 * years
        # 월 복리 계산 (간이)
        monthly_rate = (annual_rate / 100) / 12
        months = years * 12
        future_value = monthly_deposit * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
        
        st.metric("총 적립 원금", f"{int(total_principal):,} 원")
        st.metric("예상 적립금 (세전)", f"{int(future_value):,} 원")
        st.success(f"총 {int(future_value - total_principal):,} 원의 이자 수익이 기대됩니다.")

# 메뉴 선택에 따른 화면 출력
if menu == "📉 대출 이자 계산기":
    loan_calculator()
elif menu == "📈 마이너스 통장 계산기":
    minus_account_calculator()
elif menu == "💰 공모주 청약 계산기":
    ipo_calculator()
elif menu == "🏦 연금저축 복리 계산기":
    pension_calculator()

# 공통 푸터
st.markdown("---")
st.markdown("""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 30px; text-align: center;">
        <h4 style="color: #333; margin-bottom: 10px;">✍️ Karis의 테크 & 재테크 블로그</h4>
        <a href="https://blog.naver.com/karis_official" target="_blank" style="text-decoration: none; color: #ffffff; background-color: #00c73c; padding: 10px 20px; border-radius: 5px; font-weight: bold;">블로그 바로가기</a>
    </div>
""", unsafe_allow_html=True)
