import requests
from bs4 import BeautifulSoup

# Get html
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
# Filter tags.
# When h3 tag is not available get creative
soup_images = soup.find_all(name='img', class_='jsx-952983560 loading')
# Use 101 to later remove duplicate image
place = 101
movies_list = []
for image in soup_images:
    movies_list.append(f'{place}) {image.get("alt")}')
    place -= 1
# Remove the duplicate image
movies_list.pop(0)
# Reverse the order of the list
movies_list = movies_list[::-1]

with open('top_movies_to_watch.txt', mode='w') as file:
    for movie in movies_list:
        file.write(f'{movie}\n')

