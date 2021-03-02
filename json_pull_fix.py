import regex as re
import json
from pprint import pprint     

f = open("dweets.json", "r")
a = f.read()

a = re.sub("}]}{", "}]}, {")


data = json.load(a)

pprint(data[0])                          
                        
best_dweets = []                                          
for chunk in data:                       
      for dweet in chunk['results']:       
          if dweet['awesome_count'] > 9:   
              best_dweets.append(dweet)    
pprint(best_dweets[0])
