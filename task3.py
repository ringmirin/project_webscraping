import json
with open("imdb_second_task.json","r") as fh:
   data=json.load(fh)
# print(movies)
def group_by_decades():
   dict={}
   y=1950
   for x in range(y,2022,10):
      list=[]
      for j in data:
         if x<(int(j)) and int(j)<x+10:
            list.append(data[j])
            y+=10
      dict[x]=list
   with open("imdb_third_task.json","w") as fh:
      json.dump(dict, fh, indent=5, sort_keys=True)
group_by_decades()

