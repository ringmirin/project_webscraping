import json
with open("imdb_first_task.json","r") as fh:
   movies=json.load(fh)
def arrange_by_year():
   dict={}
   for i in movies:
      list=[]
      year=i["year"]
      if year not in dict:
         for j in movies:
           if year==j["year"]:
              list.append(j)
         dict[year]=list
   with open("imdb_second_task.json","w")as fh:
      json.dump(dict,fh, indent=5, sort_keys=True) 
arrange_by_year()
         