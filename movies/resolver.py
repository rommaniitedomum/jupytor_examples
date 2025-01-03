import pandas as pd 
import sys
import json 
import re 


item_fname = 'data/movie_final.csv'
columns = ['movieId', 'title', 'genres', 'imdbId', 'tmdbId', 'url', 'rating_count','rating_avg', 'poster_path']


def random_items(n):
    movies_df = pd.read_csv(item_fname)
    movies_df = movies_df.fillna('') #결측치 공백처리 
    result_items = movies_df.sample(n=n).to_dict('records')
    return result_items

def latest_items(n):
    movies_df = pd.read_csv(item_frame)
    movies_df = movies_df.fillna('') #결측치 공백 처리 
    
    # 영화 제목에서 연도를 추출하는 함수 (예: "squid game(2021)" -> 2021)
    def extract_year(title):
        match = re.search(r'\((\d{4})\)', title)
        if match:
            return int(match.group(1))  # return match.group(1) # 정규 표현식에서 만든 객체중 첫 값만 출력 
        return None # 연도가 없으면 none 반환 
    
    # 연도 정보를 추출해서 새로운 'year' 컬럼에 추가 
    movies_df['year'] = movies_df['title'].apply(extract_year)
    
    # 연도를 기준으로 내림차순으로 정렬하고 최신 n개 항목 선택 
    latest_movie_df = movies_df.sort_values(by='year', ascending=False).head(n) # year 칼럼 기준으로 내림차순 (ascending=False)
    
    # 5개의 latest movie return
    result_items = latest_movie_df.to_dict('records')
    return result_items

if __name__ == '__main__':
    print(random_items(3))