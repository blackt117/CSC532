import random

import pandas as pd
from Tools.scripts.dutree import display
from sklearn.neighbors import NearestNeighbors
from random import randint
from sklearn.metrics import mean_absolute_error

ratings = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv('movies.csv', usecols=['movieId', 'title'])
ratings2 = pd.merge(ratings, movies, how='inner', on='movieId')

df = ratings2.pivot_table(index='title', columns='userId', values='rating').fillna(0)
df1 = df.copy()



def recommend_movies(user, num_recommended_movies):
    print('The list of the Movies {} Has Watched \n'.format(user))

    for m in df[df[user] > 0][user].index.tolist():
        print(m)

    print('\n')

    recommended_movies = []
    recommended_movies_real = []
    for m in df[df[user] == 0].index.tolist():
        index_df = df.index.tolist().index(m)
        predicted_rating = df1.iloc[index_df, df1.columns.tolist().index(user)]
        recommended_movies.append((m, predicted_rating))
        recommended_movies_real.append([m,random.randint(1,5)])


    sorted_rm = sorted(recommended_movies, key=lambda x: x[1], reverse=True)

    pred_ratings =[]
    real_ratings =[]
    print('The list of the Recommended Movies \n')
    rank = 1
    for recommended_movie in sorted_rm[:num_recommended_movies]:
        print('{}: {} - predicted rating:{}'.format(rank, recommended_movie[0], recommended_movie[1]))
        rank = rank + 1
        pred_ratings.append(recommended_movie[1])
        for i in recommended_movies_real:
            if recommended_movie[0] == i[0]:
                real_ratings.append(i[1])
                print('{} - predicted rating:{}'.format(i[0], i[1]))


    print()
    print()
    print(pred_ratings)
    print(real_ratings)
    return(pred_ratings,real_ratings)


def movie_recommender(user, num_neighbors, num_recommendation):
    number_neighbors = num_neighbors

    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(df.values)
    distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

    user_index = df.columns.tolist().index(user)

    for m, t in list(enumerate(df.index)):
        if df.iloc[m, user_index] == 0:
            sim_movies = indices[m].tolist()
            movie_distances = distances[m].tolist()

            if m in sim_movies:
                id_movie = sim_movies.index(m)
                sim_movies.remove(m)
                movie_distances.pop(id_movie)

            else:
                sim_movies = sim_movies[:num_neighbors - 1]
                movie_distances = movie_distances[:num_neighbors - 1]

            movie_similarity = [1 - x for x in movie_distances]
            movie_similarity_copy = movie_similarity.copy()
            nominator = 0

            for s in range(0, len(movie_similarity)):
                if df.iloc[sim_movies[s], user_index] == 0:
                    if len(movie_similarity_copy) == (number_neighbors - 1):
                        movie_similarity_copy.pop(s)

                    else:
                        movie_similarity_copy.pop(s - (len(movie_similarity) - len(movie_similarity_copy)))

                else:
                    nominator = nominator + movie_similarity[s] * df.iloc[sim_movies[s], user_index]

            if len(movie_similarity_copy) > 0:
                if sum(movie_similarity_copy) > 0:
                    predicted_r = nominator / sum(movie_similarity_copy)

                else:
                    predicted_r = 0

            else:
                predicted_r = 0

            df1.iloc[m, user_index] = predicted_r
    pred, real = recommend_movies(user, num_recommendation)
    return (pred,real)


mae_list = []
for i in range(1,16):
    pred, real = movie_recommender(i, 10, 10)
    mae = mean_absolute_error(real,pred)
    mae_list.append(mae)

print(sum(mae_list)/15)


