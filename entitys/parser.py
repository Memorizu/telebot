import requests
from bs4 import BeautifulSoup as bs

from fake_useragent import UserAgent

class Request:

    __genre_for_url = 'anime'
    __url_genres = 'https://www.kinopoisk.ru/lists/categories/movies/8/'
    __url_movies = 'https://www.kinopoisk.ru/lists/movies/?b=top&sort=rating'

    __url_genres_interactive = f'https://www.kinopoisk.ru/lists/movies/genre--{__genre_for_url}/year--2023/?b=top&b=released&sort=date'

    @property
    def __agent(self):
        __ua = UserAgent(browsers=['edge', 'chrome'])
        __agent = __ua.random

        __headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7.',
            'User-Agent': __agent,
            'cookie': 'yuidss=1574675431672830487; yandex_login=kaidohmaru1989; i=S8BqyH/8SNCFHpPPHnG0Idxk6nBY8PcJH6w5kuqs9LZUFS4Lr3krJ5qWAwiRjLgLDyABhB6GY8ko/j44OobTm7MU6Ik=; yandexuid=1574675431672830487; location=1; _ym_uid=1679516246875610869; gdpr=0; _ym_isad=1; yp=1680470367.yu.1574675431672830487; ymex=1682975967.oyu.1574675431672830487; L=BhdnAlt7dnBkDGNfaAR8cQBKXlxaQmN5BVUxLA09AzRFEX5AAEw=.1674333432.15229.314292.5114e81a1166b919445347bd64022b1b; crookie=3tH9tK+VU4fUIbe9foGo4A8oU9sOWmu/5rSURFhfkuVa33ojTu+/Sj8Zt1SgS1CiSz10NJhPvqSXISGqqpFr0QBC5Us=; cmtchd=MTY4MDM4Mzk3MTQxMw==; coockoos=4; _yasc=5Gga6aCn9xNBB6HrBkWnyz607gwWBYgMttvBkfrcANSMXXbgDzXIuvtQ6eo=; _csrf=S6qTOzY4VexLj2AInrhVhMZb; desktop_session_key=1c8d7750340ec496e3ae4bfd218cb44156a00ff7a67221e6e8b5d3f5d754d60964e52b1a3bfc84d4d3de3ff5068ad98e40316eb5a6372a814e21407942771be6cbd544b85e71f6fbfa5f05c916a6c75a34a44f695e7438b008aba3b43aa4012e; desktop_session_key.sig=uU8_SlceFV61sCFiSHWu1tqYvU8; disable_server_sso_redirect=1; ya_sess_id=3:1680430268.5.0.1674333431994:7Mu0Xg:33.1.2:1|1016153197.0.2|30:10214956.119920.S1VxU9OjAXOgOw4rdhBpArexrhE; ys=udn.cDprYWlkb2htYXJ1MTk4OQ==#c_chck.1553039654; mda2_beacon=1680430269007; sso_status=sso.passport.yandex.ru:synchronized; _ym_d=1680430269'
        }
        return __headers

    def genres_list(self):

        r = requests.get(self.__url_genres, headers=self.__agent)

        soup = bs(r.content, 'lxml')
        genres = soup.find('div', class_='styles_content__2mO6X').find_all('a')
        genres_list = [genre.text for genre in genres]
        return genres_list

# Надо переделать в топ 250
    def movies_top(self):

        r = requests.get(self.__url_movies, headers=self.__agent)

        soup = bs(r.content, 'lxml')
        movies = soup.find('div', class_='styles_contentSlot__h_lSN').find_all(
            'span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj')
        movies_list = [movie.text for movie in movies]
        return movies_list

    def movies_by_genres(self):
        r = requests.get(self.__url_genres_interactive, headers=self.__agent)

        soup = bs(r.content, 'lxml')
        movies_row = soup.find('div', class_='styles_contentSlot__h_lSN').find_all('div', class_='styles_root__ti07r')
        movies_list = [movie.find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
                       for movie in movies_row]
        return movies_list


request = Request()
# print(request.movies_by_genres())
# print(request.genres_list())
print(request.movies_top())

