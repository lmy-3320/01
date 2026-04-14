import streamlit as st

st.set_page_config(page_title="AD-Message Generator", page_icon="📝")

st.title("🚀 광고주 브리핑 문구 생성기")
st.write("어제 성과 지표를 입력하면 보고용 문구가 자동으로 생성됩니다.")

# 입력 섹션
with st.sidebar:
    st.header("📊 데이터 입력")
    client_name = st.text_input("광고주명", "코베아")
    spend = st.number_input("어제 지출 비용 (원)", value=100000, step=1000)
    roas = st.number_input("어제 ROAS (%)", value=250, step=10)
    status = st.selectbox("전반적인 성과 느낌", ["상승/양호", "보합/유지", "하락/점검필요"])

# 로직 및 문구 생성
st.subheader(f"✨ {client_name}님 보고 문구")

if status == "상승/양호":
    msg = f"안녕하세요 {client_name} 광고주님! 어제는 전일 대비 효율이 개선되어 지출액 {format(spend, ',')}원 기준 ROAS {roas}%로 기분 좋게 마무리되었습니다. 현재 흐름 유지하며 모니터링하겠습니다."
elif status == "보합/유지":
    msg = f"안녕하세요 {client_name} 광고주님. 어제는 지출액 {format(spend, ',')}원, ROAS {roas}%로 목표 범위 내에서 안정적인 수치를 보였습니다. 오늘 특이사항 있는지 지속 체크하겠습니다."
else:
    msg = f"안녕하세요 {client_name} 광고주님. 어제는 지출액 {format(spend, ',')}원 대비 ROAS가 {roas}%로 다소 정체되었습니다. 소재 피로도나 매체 입찰가를 점검하여 보고드리겠습니다."

st.code(msg, language="text")
