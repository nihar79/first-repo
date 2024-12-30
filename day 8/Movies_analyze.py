import pandas as pd
movies_data = "movies.csv"
ratings_data = "movie_ratings.csv"

null_values = ['None']

movies_df = pd.read_csv(movies_data,na_values=null_values)
ratings_df = pd.read_csv(ratings_data,na_values=null_values)

# Extract the Year from Title Column
movies_df['year']=movies_df.title.str.extract('(\d\d\d\d)',expand=False)

movies_df['title']=movies_df.title.str.replace('(\(\d\d\d\d\))',' ')
movies_df['genres']=movies_df.genres.str.split('|')
movies_df.year.fillna(0,inplace=True)

movies_df.year = movies_df.year.astype('int16')
movies_df.movieId=movies_df.movieId.astype('int32')
movies_genres = movies_df.copy(deep=True)

a=[]
for index,row in movies_df.iterrows():
    a.append(index)
    for genre in row['genres']:
        movies_genres.at[index,genre]=1


print(len(a)) == len(movies_df)

movies_genres = movies_genres.fillna(0)

ratings_df.drop('timestamp',axis=1,inplace=True)

print(ratings_df.dtypes)
print(ratings_df.isna().sum())

new_movie_ratings = [
    {'title':'Avengers, The (1998)','ratings':4.5},
    {'title':'Avengers, The (2012)','ratings':4.8},
    {'title':'Captain America (1990)','ratings':4.9}
]
new_movie_ratings = pd.DataFrame(new_movie_ratings)


new_movie_id = movies_df[movies_df['title'].isin(new_movie_ratings['title'])]

new_movie_ratings = pd.merge(new_movie_id,new_movie_ratings)

new_movie_ratings = new_movie_ratings.drop(['genres','year'], axis=1)


new_genres_df = movies_genres[movies_genres.movieId.isin(new_movie_ratings.movieId)]

new_genres_df.reset_index(drop=True,inplace=True)

new_genres_df.drop(['movieId','title','genres','year'],axis=1,inplace=True)
new_profile = new_genres_df.T.dot(new_movie_ratings.ratings)

movies_genres = movies_genres.set_index(movies_genres.movieId)

print(new_profile)

