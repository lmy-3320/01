import streamlit as st

st.set_page_config(page_title="AE 실전 문구 생성기", page_icon="📱")

st.title("📱 AE 실전 브리핑 문구 생성기")
st.write("실제로 광고주 카톡/메일에 바로 복사해서 쓸 수 있는 문구입니다.")

# 입력 섹션
with st.sidebar:
    st.header("📊 데이터 입력")
    client = st.text_input("광고주명", "아이카")
    spend = st.number_input("지출액", value=150000, step=1000)
    roas = st.number_input("ROAS (%)", value=320, step=10)
    cpc = st.number_input("CPC (원)", value=450, step=10)
    
    st.divider()
    mode = st.radio("문구 스타일 선택", ["격식 보고형", "캐주얼 카톡형", "성과 부진(방어)형"])

st.subheader(f"✨ [{mode}] 생성 결과")

# 문구 로직
if mode == "격식 보고형":
    msg = f"""[일일 성과 브리핑] - {client}
    
안녕하세요, {client} 담당 AE입니다. 어제자 성과 요약 공유드립니다.

- 지출액: {format(spend, ',')}원
- ROAS: {roas}%
- CPC: {cpc}원

어제는 목표 ROAS 내에서 안정적으로 운영되었습니다. 클릭당 비용(CPC)도 적정 수준 유지 중이며, 금일 오전 중으로 소재별 효율 다시 체크하여 특이사항 있을 시 공유드리겠습니다."""

elif mode == "캐주얼 카톡형":
    msg = f"""{client} 대표님 안녕하세요! 
    
어제 성과 지표 전달드립니다. 😊
비용 {format(spend, ',')}원 지출되었고, ROAS는 {roas}%로 마감됐습니다!

CPC도 {cpc}원대로 잘 방어되고 있어서 현재 세팅 그대로 유지하면서 효율 계속 모니터링하겠습니다. 오늘 하루도 화이팅하세요!"""

else:
    msg = f"""안녕하세요 {client}님, 어제자 성과 공유드립니다.

- 지출액: {format(spend, ',')}원
- ROAS: {roas}%

어제는 전일 대비 ROAS가 다소 정체된 모습이 보입니다. 소재 피로도가 올라간 것으로 판단되어, 오늘 중으로 신규 소재 교체 및 타겟 조정을 검토할 예정입니다. 분석 결과 나오는 대로 다시 보고드리겠습니다."""

st.code(msg, language="text")
st.info("위 박스 오른쪽의 복사 버튼을 눌러 바로 사용하세요!")
