import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()


print(" postlarimiz:\n")

for post in data[:5]:
     print(f"ID :   {post [ 'id']   } ")
     print(f"Title: {post ['title'] } ")
     print(f"Body:  {post ['body']  }\n ")
     print("-"*40)

