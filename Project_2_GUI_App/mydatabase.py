import json

class Database:

    def add_data(self,first_name,last_name,email,password):

        with open("db.json","r") as rf:
            data=json.load(rf)

        if email in data:
            return 0
        else:
            data[email]=[first_name,last_name,password]
            with open("db.json","w") as wf:
                json.dump(data,wf)
            return 1

    def search_data(self,email,password):
        with open("db.json","r") as rf:
            data=json.load(rf)

        if email in data:
            if data[email][2]==password:
                return 1
            else:
                return -1
        else:
            return 0