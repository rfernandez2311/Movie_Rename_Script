from pickle import FALSE
import requests
import pprint
import os
import re

movie_set = []

def get_movies():
    os.chdir('/Volumes/Plex_Movies')

                   
    for files_server in os.listdir():

        if files_server != ".DS_Store" and files_server != "#recycle":
            
            match = re.match(r'.*([1-3][0-9]{3})', files_server)
            if match is None:
                movie_set.append(files_server)
                 
    pprint.pprint(movie_set)
    print("*****************")
    print("")


def movies_rename():
    ranemd_movie = "" 
while len(movie_set) > 0:
    for movie in movie_set:
        file_name, file_ext = os.path.splitext(movie)
        
        response = requests.get("https://api.themoviedb.org/3/search/movie?query="+file_name+"&api_key=e25abcda54aa6b0a579e7bd6d10d6139")
        data = response.json()

        movie_data = data['results']
        for date in movie_data:

                data_api = re.sub('\W+','', date["original_title"]).lower()
                file_ = re.sub('\W+','', file_name).lower()
                if file_ == data_api:
                    print(file_name)
                    
                    year = "("+date["release_date"][0:4]+")"    
                    new_name = '{} {}{}'.format(file_name, year, file_ext)
                    
                    if movie != ranemd_movie:
                        ranemd_movie = movie
                        print('{} {}{}'.format(file_name, year, file_ext))
                        os.rename(movie, new_name)
                        movie_set.remove(movie)

        

def main():
   get_movies()
   if len(movie_set) > 0:
        movies_rename()

    
main()