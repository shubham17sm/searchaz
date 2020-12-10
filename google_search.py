'''
Required Function and its parameters

search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
query : query string that we want to search for.
tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
lang : lang stands for language.
num : Number of results we want.
start : First result to retrieve.
stop : Last result to retrieve. Use None to keep searching forever.
pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

'''

from googlesearch import search

# def main():
#     try:
#         query_search = input("Enter the query you want to search for: ")

#         if query_search == "":
#             print("You haven't entered anything to search for")
#             query_search = input("Enter the query you want to search for: ")
#         else:
#             print("Getting results for your query from google....")


#         for i in search(query_search, tld='com', num=10, stop=10, pause=2):
#             print(i)
#     except:
#         print("Something is wrong...")


# if __name__ == "__main__":
#     main()


'''
classed based same program
'''

class GoogleSearchPro:
    def __init__(self, query):
        self.query = query


    def search_for(self):
        try:

            if self.query == "":
                print("You haven't entered anything to search for")
                return
                
            for i in search(self.query, tld='com', num=10, stop=10, pause=2):
                print(i)
        except:
            print("Something is wrong")

    

def main():
    keyword = input("Enter the query you want to search for: ")

    obj1 = GoogleSearchPro(keyword)

    obj1.search_for()


if __name__ == "__main__":
    main()