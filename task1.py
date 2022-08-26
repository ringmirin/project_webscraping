from bs4 import BeautifulSoup
import json, requests
import pprint
source=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
source.raise_for_status()

soup=BeautifulSoup(source.text,"html.parser")

movies=soup.find("tbody",class_="lister-list").find_all("tr")
# print(movies)
# print(len(movies))
movie_rank=[]
movie_name=[]
year_of_release=[]
movie_urls=[]
movie_ratings=[]
for movie in movies:
   name=movie.find("td",class_="titleColumn").a.text
   post=movie.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
   year=movie.find("td",class_="titleColumn").span.text.strip("()")
   ratings=movie.find("td",class_="ratingColumn imdbRating").strong.text
   link=movie.find("td",class_="titleColumn").a["href"]
   movie_link="https://www.imdb.com"+link
   
   movie_rank.append(post)
   movie_name.append(name)
   year_of_release.append(year)
   movie_ratings.append(ratings)
   movie_urls.append(movie_link)

list_of_top_movies=[]
# print(movie_name)
require={"position":"","name":"","year":"","rating":"","url":""}
i=0
while i<len(movie_rank):
   require["position"]=(movie_rank[i])
   require["name"]=str(movie_name[i])
   year_of_release[i]=year_of_release[i]
   require["year"]=int(year_of_release[i])
   require["rating"]=float(movie_ratings[i])
   require["url"]=movie_urls[i]
   list_of_top_movies.append(require.copy())
   i+=1
with open("imdb_first_task.json","w") as fh:
   json.dump(list_of_top_movies,fh,indent=4)
pprint.pprint
