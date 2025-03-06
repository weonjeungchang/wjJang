import streamlit as st

# Streamlit UI
st.set_page_config(page_title="wjjang_career", layout="wide")
st.subheader("📄 [장원증] 소프트웨어 학사, 경제학(인공지능경제) 석사")
st.caption(":rainbow[ 📜 This page was developed with Python Streamlit.]")

# 탭 생성
tabPage01, tabPage02, tabPage03, tabPage04, tabPage05 = st.tabs(["인공지능", "분석/설계/기획", "프로젝트(개발)", "학력/이력/자격", "개인프로젝트"])

with tabPage01:
    st.success("📌 FinancialDataSystem : 신탁계약 약관 챗봇 :orange[진행중]")
    contents_text = """
    """
    st.markdown(contents_text)

    st.success("📌 FinancialDataSystem : OCR기반 문서 데이터화 :orange[진행중]")
    contents_text = """이미지 파일을 :red[OCR(tesseract)] 기법으로 문자화하여  
    검수(승인결재) 단계를 걸쳐 :red[ollama]를 이용하여 :red[Llama3.1:8B] 모델로 정재하여  
    특정 데이터를 선별하여 기존 데이터베이스(Oracle)에 insert하는 로직  
    :red[Flask]로 시각화"""
    st.markdown(contents_text)

    st.success("📌 FnDataLab : 퇴직연금가이드포털(B2C) :orange[상품화X]")
    contents_text = """PDF/Excel파일을 읽어들여 : fitz(PyMuPDF), pandas, openpyxl  
    시간가중수익률을 구하는 배치성 프로그램 code-Interpreter : :red[Python]  
    :red[Chroma] 벡터DB에 인서트하여 :red[LangChain]으로 :red[RAG] 구현  
    LLM : :red[OpenAI-o3]와 :red[Llama2.0] 모델의 평균값으로 응답 생성  
    :red[Highcharts] 컴포넌트 import 시키고, :red[streamlit]으로 시각화"""
    st.markdown(contents_text)

    st.success("📌 글로벌금융자산 자산배분(Deep Momentum) :orange[한양대 산업공학과 산학연구과제 협업]")
    contents_text = """:red[python] :blue[Deep Momentum] 모델 구현  
    2000년부터 10년씩 :red[롤링 강화학습] :blue[fine-tuning] (글로벌주식, 글로벌채권, 글로벌ETF 등)  
    현시점 이후 자산배분 예측치 생성"""
    st.markdown(contents_text)

    st.success("📌 FnDataLab : 금융자산 위험군 클러스터링 :orange[한양대 산업공학과 산학연구과제 협업]")
    contents_text = """(글로벌주식, 글로벌채권, 글로벌ETF 등) return 기반 risk지표 25가지 :red[python]으로 생성  
    :blue[k-means, contrastive learning] 으로 6군집으로 클러스터링하여 비교 분석 (sharp ratio 비교)"""
    st.markdown(contents_text)

    st.success("📌 FnDataLab : 고객문의 챗봇")
    contents_text = """:red[Python, GPTo3]  
    :red[Chroma] 벡터DB에 사내 자료 인서트하여 :red[LangChain]으로 :red[RAG] 구현  
    :red[streamlit] 으로 시각화"""
    st.markdown(contents_text)

    st.success("📌 FnGuide : 기관컨설팅 제안서작성 챗봇")
    contents_text = """:red[Python, GPTo1]  
    :red[Chroma] 벡터DB에 인서트하여 :red[LangChain]으로 :red[RAG] 구현  
    :red[Highcharts] 컴포넌트 import 시키고, :red[streamlit]으로 시각화"""
    st.markdown(contents_text)

    st.success("📌 서민금융진흥원 : 신용평가 예측 모형 :orange[연구시연]")
    contents_text = """:red[Python]  
    상장폐지된 종목들을 찾아, 상장될 시기에 비슷한 재무구조였던 기업들을 찾아, 상폐여부를 :blue[labeling]  
    상폐여부에 영향을 미친 재무적 feature :blue[OLS] 통계적 분석  
    분석된 feature들에 결정요인 :blue[randomforest] 적용  
    feature들에 가중치를 부여하여 :blue[LSTM]으로 예측치 생성하여 신용지표로 사용"""
    st.markdown(contents_text)

    st.success("📌 웰컴저축은행 : AML 위험의심거래 감지 :orange[연구시연]")
    contents_text = """:red[Python]  
    AML(Anti-Money Laundering) 자금세탁방지 의심거래 추출
    과거 거래내역에서 의심거래여부 :blue[labeling]  
    :blue[KNN]모델 통한 학습을 통해 의심거래판별 모델 생성하여 새로운 거래가 발생할때마다 의심거래여부 판별"""
    st.markdown(contents_text)

with tabPage02:
    st.warning("📌 프로젝트 분석/설계/기획")

    contents_text = """✔️ UI 및 컨텐츠 기획
    LLM을 통한 자연어 처리
    연령대별, 퇴직 예상시기별, 연봉대별, 직군/직종별 자산배분 통계를 통한 비교/분석
    퇴직연금제도에 대한 전반적인 질의 응답"""
    st.text_area("◽ FnDataLab : 퇴직연금가이드포털(B2C) - :red[상품화X]", contents_text, height=130, disabled=False)

    contents_text = """✔️ 테이블(Oracle) 모델링
    퇴직연금 DC형 및 IRP형 가입자 자산배분 가이드"""
    st.text_area("◽ FnDataLab : 퇴직연금포털 - www.korpension.com", contents_text, height=80, disabled=False)

    contents_text = """✔️ 자산배분 로직정리/모델링/구현
    MVO - Mean Variance Optimizer
    Black Litermman
✔️ 성과요인분해 로직정리/모델링/구현
    🔹주식성과평가
    - BHB(Brinson, Hood and Beebower)
    - Bottom-Up 
    🔹채권성과평가
    - 8-factor 모형
    - Lehmann 모형
    - Campisi in :green[R-script] (Nelson-Siegel)
    🔹TimeSeries-Smoothing (Multi-period Attribution) 기법
    - Carino
    - Laker"""
    st.text_area("◽ FnGuide : 펀드위탁평가 - www.pfguide.co.kr", contents_text, height=350, disabled=False)

    contents_text = """✔️ IRR 패키지 로직정리/모델링/구현
    캐시플로우를 통한 내부수익률
    IRR, Net-IRR, Gross-IRR"""
    st.text_area("◽ FnGuide : 대체자산평가 - www.fnaims.co.kr", contents_text, height=100, disabled=False)

    contents_text = """✔️ 학습/습득, 모델링, 구현
    STOCK multi-factor
    BOND multi-factor"""
    st.text_area("◽ FnGuide : 멀티팩터 모형", contents_text, height=100, disabled=False)

    contents_text = """✔️ UI기획, 모델링, 구현"""
    st.text_area("◽ FnGuide : 배치프로그램 스케쥴링/모니터링", contents_text, height=68, disabled=False)

    contents_text = """✔️ UI기획, 모델링, 구현"""
    st.text_area("◽ FnPricing : 메타시스템", contents_text, height=68, disabled=False)

    contents_text = """✔️ UI기획, 모델링, 구현"""
    st.text_area("◽ FnGuide : 인사시스템", contents_text, height=68, disabled=False)

with tabPage03:
    st.info("📌 금융권 프로젝트")
    st.write("◽ 2024.04 ~ 2024.11 | FnDataLab - 한국퇴직연금포털 | :blue[Python, Shell, Oracle Package(Procedure)]")
    st.write("◽ 2023.12 ~ 2024.05 | FnDataLab - 국민연금 주거래은행 프로젝트 | :blue[spotfire(BI), Oracle, Pro*C, Nexacro, proframe]")
    st.write("◽ 2023.02 ~ 2023.12 | FnDataLab - 디폴트옵션 분석 | :blue[Python, Shell, Oracle, Pro*C]")
    st.write("◽ 2020.02 ~ 2023.01 | FnGuide - PFGuide 위탁펀드평가시스템 | :blue[Oracle, Pro*C, Python, R, Shell, spotfire]")
    st.write("◽ 2020.02 ~ 2023.01 | FnGuide - PFGuide 대체자산분석시스템 | :blue[Oracle, Pro*C, R, Shell]")
    st.write("◽ 2017.12 ~ 2020.01 | FnGuide - 국민연금 정보분석 고도화 | :blue[Xplatform, Proframe(C), RD(Report Designer)]")
    st.write("◽ 2017.09 ~ 2019.05 | FnPricing - 기금운용시스템 | :blue[Nexacro, JAVA, spring, Oracle, MongoDB, spotfire, C#, PL-SQL)]")
    st.write("◽ 2016.03 ~ 2017.08 | FnPricing - 한국투자증권 성과요인분해 | :blue[Xplatform, JAVA, Oracle Package, PL-SQL)]")
    st.write("◽ 2015.09 ~ 2016.03 | 신한아이타스 - 차세대 프로젝트")
    st.write("◽ 2015.05 ~ 2015.07 | 신한아이타스 - 트레이딩 지원 시스템")
    st.write("◽ 2014.10 ~ 2015.02 | 국민건강보험공단 - 통합금여시스템 (의료조사/급여, 이의신청)")
    st.write("◽ 2013.10 ~ 2013.11 | 경남은행 - 차세대 프로젝트 (마케팅허브)")
    st.write("◽ 2013.04 ~ 2013.07 | 미래에셋증권 - 정보계 리뉴얼(펀드 집계)")
    st.write("◽ 2013.02 ~ 2013.03 | 현대증권 - 해외채권매매시스템")
    st.write("◽ 2012.08 ~ 2012.11 | 코스콤 - 영업지원, 실적집계")
    st.write("◽ 2011.11 ~ 2012.04 | 미래에셋증권 - 자산관리/포트폴리오")
    st.write("◽ 2011.04 ~ 2011.10 | 미래에셋증권 - 섹터집계/영업관리 시스템")
    st.write("◽ 2010.10 ~ 2011.03 | 미래에셋증권 - 컴플라이언스 시스템")
    st.write("◽ 2010.01 ~ 2010.09 | 미래에셋증권 - AML(자금세탁방지)")
    st.write("◽ 2009.02 ~ 2009.12 | 미래에셋증권 - 고객관리/영업관리 시스템")
    st.write("◽ 2008.08 ~ 2009.01 | 한국투자증권 - CMA 소액결제 전문조립")

    st.info("📌 비금융권 프로젝트")
    st.write("◽ 2017.08 ~ 2017.09 | FnPricing - 메타시스템 | :blue[Nexacro, JAVA, Oracle]")
    st.write("◽ 2017.08 ~ 2017.09 | FnPricing - 인사시스템 | :blue[JSP, JAVA, Oracle]")
    st.write("◽ 2015.07 ~ 2015.08 | S oil - PRM (파트너쉽관리시스템) | :blue[Xplatform]")
    st.write("◽ 2015.02 ~ 2015.05 | SK Telecom - 빌링시스템 (부가서비스 요금청구) | :blue[Pro*C]")
    st.write("◽ 2014.05 ~ 2014.09 | 한국스마트카드 - 통합단말,모바일 시외버스 발권시스템 | :blue[Pro*C]")
    st.write("◽ 2007.08 ~ 2008.07 | TCO Solution - IT자산관리/보안시스템/헬프데스크 SM | :blue[기술지원, Web]")
    st.write("◽ 2004.08 ~ 2005.07 | LG Telecom - 영업관리 및 개통시스템 SM | :blue[MFC, C++]")

with tabPage04:
    st.error("📌 근무 이력")
    st.write("◽ 現 파이넨셜데이터시스템 커스터디부문 SI사업부 수석 (:red[인공지능] 담당)")
    st.write("◽ 現 :blue[이그지표데브랩] CEO")
    # st.write("◽ 그린다에이아이:rainbow[startup] :red[CTO] 사외이사")
    st.write("◽ 에프앤데이터랩 금융사업본부 수석")
    st.write("◽ 에프앤가이드 투자플랫폼실 차장")
    st.write("◽ 에프앤자산평가 솔루션본부 :red[개발팀장] 차장")

    st.error("📌 학력 사항")
    st.write("◽ 서강대학교 경제대학원 인공지능경제. 2025.02. 졸업")
    # st.caption(" 📜 논문 : :rainbow[퇴직연금 사전지정운용제도(디폴트옵션) 활용 활성화를 위한 챗봇(chatbot) 개발에 필요한 기술 적용방안 연구]")
    st.write("◽ 한국방송통신대학교 컴퓨터과학. 2022.08. 졸업")
    # st.write("◽ 광운대학교 소프트웨어공학. 편입~중퇴")
    st.write("◽ 한성대학교 소프트웨어시스템. 중퇴")
    # st.write("◽ 전북대학교 소프트웨어공학. 입학~중퇴")

    st.error("📌 자격 사항")
    st.write("◽ 정보처리기사. [03204011308W]. 2003.12.08. 한국산업인력공단")
    st.write("◽ SQLD. [SQLD-045006984]. 2022.06.24. 한국데이터산업진흥원")

    # st.error("📌 수상 경력")
    # st.write("◽ 한국방송통신대학교 총장배 소프트웨어경진대회 은상 : 메타표준용어시스템 R-shiny")

    st.error("📌 교육/강좌 수료사항")
    st.write("◽ 자바 중급. [PRGMS_20250131_23612937552]. 2025.01.20~2025.01.31. 프로그래머스")
    st.write("◽ 자바 입문. [PRGMS_20250120_66035307109]. 2025.01.16~2025.01.20. 프로그래머스")
    st.write("◽ 웹 프로그래밍(풀스택). 부스트코스")
    st.write("◽ 인공지능을 위한 선형대수. 부스트코스")
    st.write("◽ [칸아카데미] 모두를 위한 선형대수학. 부스트코스")
    st.write("◽ 인공지능의 이해. 2022.06. 경북대학교 소프트웨어교육센터")
    st.write("◽ 빅데이터와 통계. 2022.06. 통계교육원")
    st.write("◽ 레버리지 ETP,ETF,ETN. 2021.01. 금융투자교육원")
    st.write("◽ 파생상품모의거래. 2020.08. 한국거래소")
    st.write("◽ 클라우드컴퓨팅기반 NoSQL 구축실무. 2017.12. 한국데이터진흥원")

with tabPage05:
    st.warning("📌 퇴직연금 사전지정운용제도(디폴트옵션) 자산배분 챗봇")

    st.warning("📌 자산배분-성과요인분해 cycling")

    st.warning("📌 주식 종목 분석 screening")

    st.warning("📌 주식 추천 시스템")
