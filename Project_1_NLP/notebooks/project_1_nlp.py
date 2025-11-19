import nlpcloud 

class NLPapp: 
    def __init__(self): 
        self.__database={} 
        self.__first_menu() 
        
    def get_data(self): 
        return self.__database 
        
    def __first_menu(self): 
        user_input=int(input(
            """ Hi, How would you like to proceed 
                1. Not a member? Register 
                2. Already a member? Login 
                3. Exit """))
        
        if user_input==1: 
            self.__register() 
        elif user_input==2: 
            self.__login() 
        else: exit

    def __register(self): 
        user_name=input("Please enter your name: ") 
        user_email=input("Please enter your email: ") 
        user_pass=input("Please enter you pass") 
        
        if user_email in self.__database: 
            print("Already Existed") 
        else: 
            self.__database[user_email]=[user_name,user_pass] 
            print("Successfully Register") 
            self.__first_menu()

    def __login(self): 
        user_email=input("Please enter your email: ") 
        user_pass=input("Please enter you pass") 
        if user_email in self.__database: 
            if user_pass==self.__database[user_email][1]: 
                print("Log-In Successfully") 
                self.__second_menu() 
            else: 
                print("Wrong Password") 
                self.__login() 
        else: 
            print("You are not registered! Please register first") 
            self.__register()
            
    def __second_menu(self): 
        user_input=int(input(
            """ Hi, How would you like to proceed 
                1. NER 
                2. Language Detection 
                3. Sentiment Analysis 
                4. Logout """)) 
        
        if user_input==1: 
            self.__ner() 
        elif user_input==2: 
            self.__lang_detection() 
        elif user_input==3: 
            self.__sentiment_analysis() 
        else: 
            print("Logged out Successfully") 
            self.__first_menu()

    def __ner(self): 
        para=input("Please enter the paragraph") 
        search_=input("Enter the word you want to search") 
        client = nlpcloud.Client("gpt-oss-120b", "Your-Token", gpu=True) 
        response = client.entities(para,searched_entity=search_) 
        
        print(response)

    def __lang_detection(self): 
        para=input("Please enter the paragraph") 
        client = nlpcloud.Client("python-langdetect", "Your-Token", gpu=False) 
        response = client.langdetection(para)
        d = response 
        
        print(list(map(lambda x:x,d["languages"][0])))

    def __sentiment_analysis(self): 
        para=input("Please enter the paragraph") 
        client = nlpcloud.Client("gpt-oss-120b", "Your-Token", gpu=True) 
        response = client.sentiment(para,target="NLP Cloud") 
        d = response 
        
        print(d["scored_labels"][0]["label"],"-",d["scored_labels"][1]["label"].upper())


if __name__ == "__main__":
    obj = NLPapp()