import scrapy
from jobscraper.items import JobscraperItem

class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["web3.career"]
    start_urls = ["https://web3.career/remote-jobs"]

    def parse(self, response):
        
        data = JobscraperItem()

        jobs = response.css("table tbody tr")
        for job in jobs:
            data["job_position"] = job.css("h2::text").get()
            data["company"] = job.css("h3::text").get()
            data["salary"] = job.xpath("td[5]/p/text()").get()

            yield data

        next_button = response.css("li.next a::attr('href')").get()

        next_page = "https://web3.career" + next_button

        yield response.follow(next_page, callback=self.parse)
