import requests
from bs4 import BeautifulSoup
from googlesearch import search
from fake_useragent import UserAgent
import time


def search_title_url(query_search, number):
    urls = []
    try:
        if query_search == "":
            print("You haven't entered anything to search for")
            return

        for i in search(query_search, tld='com', num=number, stop=number, pause=0):
            urls.append(i)

        # print(urls)

        user_agent = UserAgent()

        for url in urls:
            r = requests.get(url, headers={"user_agent": user_agent.chrome})
            htmlcontent = r.content

            soup = BeautifulSoup(htmlcontent, "lxml")
            # print(soup.prettify)

            rows = soup.find_all('html')

            for row in rows:
                title = row.find('title').get_text()

                context = {
                    'title': title,
                    'url': url
                }

                print(context)

    except Exception as e:
        print("Something is wrong...", type(e).__name__)


def main():
    query_search = input("Enter the query you want to search for: ")

    try:
        number = int(input("Enter the number of result you want(Int): "))
    except ValueError:
        print("Error: You have given string input, Please enter the number.")
        number = int(input("Enter the number of result you want(Int): "))

    print("Getting results for '", query_search, "' from Google......")

    time1 = time.time()

    search_title_url(query_search, number)

    print("Time taken to execute this program: ", time.time()-time1)


if __name__ == "__main__":
    main()
