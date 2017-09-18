#!/usr/bin/python
from bioblend import galaxy

g = galaxy.GalaxyInstance(url='http://127.0.0.1:8080', key='0b3e517e52601dfb4a866f0688110679')
g.histories.get_histories()


# you already have history ids in a text file -->> 
# purge = True, deleted = True

#loop to delete all histories for all given ids in a text file
with open ("/Users/axa677/Desktop/history_ids.txt", "r") as IdsFile:
    for history_id in IdsFile:
        if len(history_id.strip()) == 16:
            try:
                g.histories.delete_history(history_id.strip(), purge = True) #The histories might be deleted but the id will be kept so when we perform a deletion again for the same id, it is not going to print (not found!)
            except:
                print "Not found in the Galaxy instance!: ", history_id
        else: 
            print 'Invalid History ID! (Length != 16): ', history_id
