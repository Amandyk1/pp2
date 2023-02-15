# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def single_score(movie):
    for m in movies:
        if m["name"] == movie and m["imdb"] > 5.5:
            imdb_score = True 
        elif m["name"] == movie and m["imdb"] < 5.5:
            imdb_score = "Sorry, score less than 5.5"
    return imdb_score

def movies_above(movies):
    movies_above = []
    for m in movies:
        if m["imdb"] > 5.5:
            movies_above.append(m["name"])
    return movies_above

movies_above(movies)

def a_score(movies_list):
    movies_scores = []
    for movie in movies_list:
        score = movie["imdb"]
        movies_scores.append(score)
    average_score = sum(movies_scores) / len(movies_scores)
    return average_score
average = a_score(movies)
print(average)

def mcategory(category):
    mcategory = []
    for m in movies:
        if m["category"] == category:
            mcategory.append(m["name"])
    return mcategory
romance = mcategory("Romance")
print(romance)
['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']