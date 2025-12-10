import json

class Database:

    def add_data(self,f_name,l_name,email,password):
        with open("db.json","r") as rf:
            data=json.load(rf)

        if email in data:
            return 0
        else:
            data[email]=[f_name,l_name,password]
            with open("db.json","w") as wf:
                json.dump(data,wf)
            return 1

    def search_user(self,email,password):
        with open("db.json","r") as rf:
            data=json.load(rf)

        if email in data:
            if password in data[email]:
                return 0
            else:
                return 2
        else:
            return 1