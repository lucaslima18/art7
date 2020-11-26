import requests

BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = "c842b85a03654d6905748eb0d88b9ae2"
LANGUAGE = "pt-BR"

def get_top_lists_data(path):
    url = f'{BASE_URL}{path}?api_key={API_KEY}&language={LANGUAGE}&page=1'
    print(url)
    response = requests.get(url)
    response_json = response.json()

    results = []
    count = 0

    for item in response_json["results"]:
        if count <= 8:
            count += 1
            title = item["title"]
            vote_average = str(item["vote_average"])
            results.append(f"{count}° Lugar: {title}, (nota: {vote_average}%)")

    return results

def get_trending_lists_data(path):
    url = f'{BASE_URL}{path}?api_key={API_KEY}&language={LANGUAGE}&page=1'
    print(url)
    response = requests.get(url)
    response_json = response.json()

    results = []
    count = 0

    for item in response_json["results"]:
        count += 1
        if count <= 8:
            try:
                title = item["title"]

            except:
                title = "Título desconhecido"
            vote_average = str(item["vote_average"])
            results.append(f"{count}° Lugar: {title}, (nota: {vote_average}%)")

    return results

def get_lists_data(path):
    url = f'{BASE_URL}{path}?api_key={API_KEY}&language={LANGUAGE}&page=1'
    print(url)
    response = requests.get(url)
    response_json = response.json()


    results = []
    count = 0

    for item in response_json["results"]:
        count += 1

        if count <= 8:
            title = item["title"]
            vote_average = str(item["vote_average"])
            results.append(f"- {title}, (nota: {vote_average}%)")

    return results

def get_search(path, search):
    response = requests.get(f'{BASE_URL}{path}?api_key={API_KEY}&language={LANGUAGE}&query={search}&page=1')
    response_json = response.json()

    return response_json["results"]


class BestMovies():
    #Lista de nomes
    #results.title
    def __init__(self):
        self.public_path = "movie/popular"
        self.public_results = get_top_lists_data(self.public_path)
        self.critic_path = "movie/top_rated"
        self.critic_results = get_top_lists_data(self.critic_path)
        self.soon_path = "movie/upcoming"
        self.soon_results = get_lists_data(self.soon_path)
        self.trendings_path = "trending/all/day"
        self.trendings_results = get_trending_lists_data(self.trendings_path)



class Search():
    def __init__(self, search_text):
        self.path = "search/multi"
        self.results = get_search(self.path, search_text)

    pass


if __name__ == "__main__":
    teste = BestMovies()
    print(teste)
