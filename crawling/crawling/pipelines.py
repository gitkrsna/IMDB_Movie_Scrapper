
from movie.models import Movie

def clean_title(param):
    return param

def clean_year(param):
    return param

def clean_rating(param):
    return param

def clean_duration(param):
    return param.strip()

def clean_genres(param):
    s = param[5:]
    listToStr = ' '.join([str(elem) for elem in s]) 
    return listToStr

def clean_director(param):
    return param


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        year = clean_year(item['year'])
        rating = clean_rating(item['rating'])
        duration = clean_duration(item['duration'])
        genres = clean_genres(item['genres'])
        director = clean_director(item['director'])

        Movie.objects.create(
            title=title,
            year=year,
            rating=rating,
            duration=duration,
            genres=genres,
            director=director,
        )

        return item


        




        