import scrapy
from ..items import DatascienceItem


class SpiderMan(scrapy.Spider):
    name = 'imdb'
    start_urls = [
        "https://www.imdb.com/search/title/?title_type=feature&count=250&ref_=adv_prv"
    ]

    sr = 1

    def parse(self, response):

        items = DatascienceItem()
        movie_data = response.css(".mode-advanced")

        for movie in movie_data:

            movie_name = movie.css(".lister-item-header a").css("::text").extract()
            imdb_score = movie.css(".ratings-imdb-rating strong").css("::text").extract()
            runtime = movie.css(".runtime::text").extract()
            genre = movie.css(".genre::text").extract()
            rating = movie.css(".certificate::text").extract()
            cast_crew = movie.css(".text-muted~ .text-muted+ p , .ratings-bar~ .text-muted+ p").css("::text").extract()
            votes = movie.css(".sort-num_votes-visible span:nth-child(2)").css("::text").extract()
            description = movie.css(".text-muted+ .text-muted , .ratings-bar+ .text-muted").css("::text").extract()
            gross = movie.css(".ghost~ .text-muted+ span").css("::text").extract()

            items['movie_name'] = movie_name
            items['imdb_score'] = imdb_score
            items['runtime'] = runtime
            items['genre'] = genre
            items['rating'] = rating
            items['cast_crew'] = cast_crew
            items['votes'] = votes
            items['description'] = description
            items['gross'] = gross

            yield items
        next_page = response.css(".next-page::attr(href)").get()
        if SpiderMan.sr <= 50:
            SpiderMan.sr += 1
            yield response.follow(next_page, self.parse)

