import streamlit as st

st.set_page_config(page_title="광고 성과 브리핑 자동화 툴", page_icon="📊")

st.title("📊 광고 성과 브리핑 자동화 툴")
st.write("성과 데이터를 입력하면 기간별 맞춤 브리핑 문구가 생성됩니다.")

# 입력 섹션
with st.sidebar:
    st.header("⚙️ 설정 및 데이터 입력")
    client = st.text_input("광고주명", "아이카")
    
    # 기간 선택 기능 추가
    period = st.selectbox("보고 기간 선택", ["일일 (Yesterday)", "주간 (Last 7 Days)", "월간 (Last Month)"])
    
    st.divider()
    
    spend = st.number_input(f"{period} 지출액 (원)", value=150000, step=1000)
    roas = st.number_input(f"{period} ROAS (%)", value=320, step=10)
    cpc = st.number_input(f"{period} CPC (원)", value=450, step=10)
    
    st.divider()
    mode = st.radio("문구 스타일", ["격식 보고형", "캐주얼 카톡형"])

st.subheader(f"✨ [{period} / {mode}] 브리핑 결과")

# 기간별 명칭 설정
period_label = "어제자" if "일일" in period else "지난 한 주간" if "주간" in period else "지난 한 달간"

# 문구 로직
if mode == "격식 보고형":
    msg = f"""[성과 브리핑] - {client} ({period})
    
안녕하세요, {client} 담당 AE입니다. {period_label} 성과 요약 공유드립니다.

- 총 지출액: {format(spend, ',')}원
- 평균 ROAS: {roas}%
- 평균 CPC: {cpc}원

{period_label} 성과를 검토한 결과, 전반적으로 목표 수치 내에서 안정적인 흐름을 보이고 있습니다. 세부 지표 분석을 통해 최적화 작업을 지속 진행하겠습니다."""

else:
    msg = f"""{client} 대표님 안녕하세요! 
    
{period_label} 성과 정리해서 전달드립니다. 😊

{period_label} 지출은 {format(spend, ',')}원, ROAS는 {roas}%로 마감되었습니다! 
CPC도 {cpc}원 수준으로 잘 유지되고 있어, 현재 효율 좋은 소재 위주로 예산 집중하며 운영 중입니다. 

데이터 확인해 보시고 궁금하신 점은 언제든 말씀해 주세요!"""

st.code(msg, language="text")
st.info("복사 버튼을 눌러 광고주님께 바로 전달하세요!")
