from bs4 import BeautifulSoup
import requests as req


url = req.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(url.text, "html.parser")
all_links = soup.select(selector=".article-title-description__text .title")
movies = [movie.get_text() for movie in all_links]
movies = movies[::-1]

with open("movie_names.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

