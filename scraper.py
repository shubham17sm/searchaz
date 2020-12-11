import requests
from bs4 import BeautifulSoup
from googlesearch import search
from fake_useragent import UserAgent
import time


class GoogleSearchPro:
    def __init__(self, query, number):
        self.query = query
        self.number = number

    def search_title_url(self):
        urls = []
        try:
            if self.query == "":
                print("[Blank]You haven't entered anything to search for")
                return

            for i in search(self.query, tld='com', num=self.number, stop=self.number, pause=0):
                urls.append(i)

            user_agent = UserAgent()

            for url in urls:
                r = requests.get(
                    url, headers={"user-agent": user_agent.chrome})
                htmlcontent = r.content
                # print(htmlcontent)

                soup = BeautifulSoup(htmlcontent, "lxml")
                # print(soup.prettify)
                # print("-------------------------------------------------------------------\
                #       ------------------------new website--------------------------------")

                rows = soup.find_all('html')

                for row in rows:
                    title = row.find('title').get_text()

                    context = {
                        'title': title,
                        'url': url
                    }

                    print(context)

        except AttributeError:
            print("Attribute Error: Maybe we found a website which needs login")

        except Exception as e:
            print("Something is wrong: ", type(e).__name__)


def main():
    keyword_query = input("Enter the query you want to search for: ")

    try:
        number = int(input("Enter the number of result you want(Int): "))
    except ValueError:
        print("Error: You have given string input, Please enter the number.")
        number = int(input("Enter the number of result you want(Int): "))

    print("Getting result from Google for '", keyword_query, "' query....")

    time1 = time.time()

    obj1 = GoogleSearchPro(keyword_query, number)

    obj1.search_title_url()

    print("Time taken to execute this program: ", time.time()-time1)


if __name__ == "__main__":
    main()
