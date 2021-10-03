from bs4 import BeautifulSoup
import requests

URL = "https://www.georgefox.edu/library/explore-contribute/collections/afi-top100-films.html"

page_movies = requests.get(URL).text
soup = BeautifulSoup(page_movies, "html.parser")

extract = soup.find_all(name="a", rel="noopener", target="_blank")

movie_titles = [movie.getText().title() for movie in extract]
final_list = movie_titles[14:114]

with open(file="movies_list.txt", mode="w") as file:
    for movie in final_list:
        file.write(f"{movie}\n")
