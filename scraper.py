from googlesearch import search
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


class GoogleSearchPro:
    def __init__(self, query, number):
        self.query = query
        self.number = number


    def search_for(self):
        urls = []
        try:

            if self.query == "":
                print("[Blank]You haven't entered anything to search for")
                return
                
            for i in search(self.query, tld='com', num=self.number, stop=self.number, pause=2):
                urls.append(i)

            

            user_agent = UserAgent()
            
            for url in urls:
                r = requests.get(url, headers={"user-agent": user_agent.chrome})
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

        except Exception as e:
            print("Something is wrong: ", type(e).__name__)

    

def main():
    keyword_query = input("Enter the query you want to search for: ")
    number = int(input("Enter the number of result we want(Int): "))

    print("Getting result from Google for '",keyword_query,"' query....")

    obj1 = GoogleSearchPro(keyword_query, number)

    obj1.search_for()


if __name__ == "__main__":
    main()