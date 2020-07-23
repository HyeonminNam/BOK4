# edaily, infomax df_pre_processing
from ekonlpy.sentiment import MPCK
from ekonlpy.tag import Mecab
import numpy as np
import pandas as pd
import csv
from ekonlpy.tag import Mecab


df = pd.read_csv(r'C:\NHM\scrapy\edaily_crawling\news2013-2017.csv', encoding='euc-kr')


def multi_pre_processing(df, doc_name) : 
    test_list = [[1,2,3,4,5,6]]
    df_pre_processing = pd.DataFrame(test_list,columns =['date', 'title', 'content','tokens', 'ngrams', 'callLabel'])
    
    mecab = Mecab()
    mpck = MPCK()
    max = 10 # 전체 개수 +1
    for i in range(max) :
        print('{}/{}'.format(i, max))
        text = str(df['d_content'][i])
        date = str(df['a_date'][i])
        date = '{}-{}-{}'.format(date[:4], date[4:6], date[6:])
        title = str(df['c_title'][i])

        tokens = mpck.tokenize(text)

    # #멀티프로세싱해서 돌리기

        ngrams = mpck.ngramize(tokens)
        df_pre_processing.loc[i] = [date, title, text, tokens, ngrams, 0]

    df_pre_processing.to_csv('{}.csv'.format(doc_name)) #맞게 고치기

multi_pre_processing(df, 'edaily_2013-2017')

# 확인
df_test = pd.read_csv(r'edaily_2013-2017.csv')

df_test
