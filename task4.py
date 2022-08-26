from bs4 import BeautifulSoup
import json,requests
with open("imdb_first_task.json","r") as fh:
   data=json.load(fh)
   link=[]
   i=0
   while i<len(data):
      print(i+1,"-",data[i]["name"])
      link.append(data[i]["url"])
      i+=1
   # print(link)
   user=int(input("enter the no: "))-1
   x=link[user]
   a=requests.get(x)
   soup=BeautifulSoup(a.text,"html.parser")
   b=soup.find("script",type="application/ld+json").text
   c=json.loads(b)
   # print(c)
   with open("fourth_task.json","w") as fh:
      json.dump(c,fh,indent=5)
   with open("fourth_task.json","r") as f:
      fouth=json.load(f)
   # print(fouth)
   dict={}
   for j in fouth:
      dict["name"]=fouth["name"]
      dict["director"]=[fouth["director"][0]["name"]]
      dict["image"]=fouth["image"]
      dict["description"]=fouth["description"]
      dict["language"]=fouth["review"]["inLanguage"]
      dict["genre"]=fouth["genre"]
      dict["runtime"]=fouth["duration"]
      dict['country']='india'
   with open("imdb_fouth_task.json","w") as fh:
      json.dump(dict,fh,indent=5)
   print(fouth)



   
      