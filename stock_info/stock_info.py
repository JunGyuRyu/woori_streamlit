import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import pandas as pd
from io import BytesIO

def get_stock_info():
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
    method = "download"
    url = "{0}?method={1}".format(base_url, method)   
    df = pd.read_html(url, header=0, encoding='cp949')[0]
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")     
    df = df[['회사명','종목코드']]
    return df

def get_ticker_symbol(company_name):     
    df = get_stock_info()
    code = df[df['회사명']==company_name]['종목코드'].values    
    ticker_symbol = code[0]
    return ticker_symbol

today = datetime.datetime.now()
pre_year = today.year - 1
jan_1 = datetime.date(pre_year, 1, 1)
dec_31 = datetime.date(pre_year, 12, 31)

with st.sidebar:
    st.header("회사 이름과 기간을 입력하세요")
    stock_name = st.text_input('회사 이름', '삼성전자')
    date_range = st.date_input('시작일 - 종료일', 
                                   (datetime.date(pre_year, 1, 1), today),
                                   format='YYYY/MM/DD')
    btn = st.button("주가 데이터 확인")

st.header("무슨 주식을 사야 부자가 되려나...")

if btn:
    try:
        ticker_symbol = get_ticker_symbol(stock_name)
    except:
        st.write("회사명 입력 바람.")  
    start_p = date_range[0]               
    end_p = date_range[1] + datetime.timedelta(days=1) 
    df = fdr.DataReader(ticker_symbol, start_p, end_p, exchange="KRX")
    df.index = df.index.date
    st.subheader(f"[{stock_name}] 주가 데이터")
    st.dataframe(df.head())
    st.line_chart(df)
    
    def df_csv(df):
        return df.to_csv().encode('utf-8')

    col1, col2 = st.columns([1, 1])

    # buffer setting
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    
    col1.download_button("CSV 파일 다운로드", df_csv(df), 'df.csv')
    col2.download_button('Excel 파일 다운로드',
                            data=excel_buffer.getvalue(),
                            file_name='df.xlsx',
                            key='excel_download')

