import streamlit as st
import pandas as pd
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="Karis 금융 계산기 포털", layout="centered")

# 2. 사이드바 메뉴
st.sidebar.title("💰 Karis 금융 툴박스")
menu = st.sidebar.radio(
    "계산기 선택",
    ["📉 대출 이자 계산기", "📈 마이너스 통장 계산기", "💰 공모주 청약 계산기"]
)

# 3. 각 계산기 함수 정의

def loan_calculator():
    st.header("📉 대출 이자 계산기")
    st.write("원리금/원금 균등 상환 방식을 계산합니다.")
    # 여기에 가지고 계신 기존 대출 계산기 코드를 그대로 붙여넣으세요.
    # 예시: 
    # principal = st.number_input("대출 원금")
    # rate = st.number_input("금리")
    # ... 계산 로직 ...

def minus_account_calculator():
    st.header("📈 마이너스 통장 계산기")
    st.write("사용한 금액과 기간만큼만 계산하는 스마트한 일할 계산기입니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        total_limit = st.number_input("마통 전체 한도 (원)", min_value=0, value=50000000, step=1000000)
    with col2:
        amount = st.number_input("현재 사용 금액 (원)", min_value=0, value=10000000, step=1000000)

    rate = st.number_input("연 금리 (%)", min_value=0.0, value=5.5, step=0.1)

    c1, c2 = st.columns(2)
    with c1:
        start_date = st.date_input("대출 시작일", date.today())
    with c2:
        end_date = st.date_input("상환 예정일", date.today())

    days = (end_date - start_date).days

    if days > 0:
        interest = amount * (rate / 100) * (days / 365)
        usage_rate = (amount / total_limit) * 100 if total_limit > 0 else 0
        
        st.markdown("---")
        m1, m2 = st.columns(2)
        m1.metric("총 사용 일수", f"{days}일")
        m2.metric("예상 발생 이자", f"{int(interest):,} 원")
        
        st.write(f"**한도 사용률: {usage_rate:.1f}%**")
        st.progress(min(usage_rate/100, 1.0))
    else:
        st.warning("상환 예정일을 시작일 이후로 설정해주세요.")

def ipo_calculator():
    st.header("📊 Karis의 공모주 청약 증거금 계산기")
    st.caption("공모가와 원하는 청약 수량을 입력하시면 필요한 총 증거금을 실시간으로 계산해 드립니다.")
    st.divider()

    price = st.number_input("1. 확정 공모가를 입력하세요 (원)", min_value=0, value=27000, step=500)
    count = st.number_input("2. 청약하고자 하는 수량을 입력하세요 (주)", min_value=0, value=10, step=10)
    margin_rate = st.radio("3. 증거금율을 선택하세요", [50, 100], index=0)

    total_money = price * count
    required_margin = total_money * (margin_rate / 100)

    st.divider()
    st.subheader("🧮 청약 준비금 계산 결과")
    st.metric(label="계좌에 필요한 총 증거금", value=f"{int(required_margin):,} 원")
    st.info(f"총 청약 금액 {int(total_money):,} 원 중 {margin_rate}%에 해당하는 증거금입니다.")
    st.link_button("🚀 Karis 블로그 방문하기", "https://blog.naver.com/karis_official")

# 4. 메뉴 선택 실행
if menu == "📉 대출 이자 계산기":
    loan_calculator()
elif menu == "📈 마이너스 통장 계산기":
    minus_account_calculator()
elif menu == "💰 공모주 청약 계산기":
    ipo_calculator()
