from tkinter import *   ##Here * means import ever class inside tkinter
from mydatabase import Database
from tkinter import messagebox
import nlpcloud

class NLPApp:

    def __init__(self):
        self.obj = Database()
        ##GUI
        self.root=Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry("360x600")
        self.root.configure(bg="#053345")

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLPApp",bg="#053345",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("Times New Roman",28,"bold"))

        heading2=Label(self.root,text="Enter Email",bg="#053345",fg="white")
        heading2.pack(pady=(5,10))
        heading2.configure(font=("Times New Roman",20,"bold"))

        self.email_input = Entry(self.root,width=40)
        self.email_input.pack(pady=(5,10),ipady=3)

        heading3=Label(self.root,text="Enter Password",bg="#053345",fg="white")
        heading3.pack(pady=(5,10))
        heading3.configure(font=("Times New Roman",20,"bold"))

        self.pass_input=Entry(self.root,width=40,show="*")
        self.pass_input.pack(pady=(5, 10), ipady=3)

        login_btn=Button(self.root,text="Login",bg="white",fg="black",command=self.perform_login)
        login_btn.pack(pady=(15,15),ipady=5)
        login_btn.configure(font=("Times New Roman",15,"bold"),width=10)

        heading4=Label(self.root,text="Not a member ?",bg="#053345",fg="white")
        heading4.pack(pady=(15,10))
        heading4.configure(font=("Times New Roman",12,"bold"))

        redirect_btn=Button(self.root,text="Register Now",command=self.register_gui)
        redirect_btn.pack(pady=(1,15))
        redirect_btn.configure(font=("Times New Roman",15,"bold"),width=20)

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg="#053345", fg="white")
        heading.pack(pady=(20, 20))
        heading.configure(font=("Times New Roman", 28, "bold"))

        heading1=Label(self.root,text="First Name",bg="#053345",fg="white")
        heading1.pack(pady=(5,5))
        heading1.configure(font=("Times New Roman", 20, "bold"))

        self.f_input=Entry(self.root,width=30)
        self.f_input.pack(pady=(5,5),ipady=4)

        heading1 = Label(self.root, text="Last Name", bg="#053345", fg="white")
        heading1.pack(pady=(5, 5))
        heading1.configure(font=("Times New Roman", 20, "bold"))

        self.l_input = Entry(self.root, width=30)
        self.l_input.pack(pady=(5, 5), ipady=4)

        heading2 = Label(self.root, text="Enter Email", bg="#053345", fg="white")
        heading2.pack(pady=(5, 5))
        heading2.configure(font=("Times New Roman", 20, "bold"))

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 5), ipady=3)

        heading3 = Label(self.root, text="Enter Password", bg="#053345", fg="white")
        heading3.pack(pady=(5, 5))
        heading3.configure(font=("Times New Roman", 20, "bold"))

        self.pass_input = Entry(self.root, width=20, show="*")
        self.pass_input.pack(pady=(5, 5), ipady=3)

        register_btn = Button(self.root, text="Register", bg="white", fg="black",command=self.perform_registration)
        register_btn.pack(pady=(15, 8), ipady=4)
        register_btn.configure(font=("Times New Roman", 15, "bold"), width=10)

        heading4 = Label(self.root, text="Already a member ?", bg="#053345", fg="white")
        heading4.pack(pady=(15, 8))
        heading4.configure(font=("Times New Roman", 12, "bold"))

        redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        redirect_btn.pack(pady=(1, 1))
        redirect_btn.configure(font=("Times New Roman", 15, "bold"), width=20)

    def perform_registration(self):
        first_name=self.f_input.get()
        last_name=self.l_input.get()
        email=self.email_input.get()
        password=self.pass_input.get()

        response = self.obj.add_data(first_name,last_name,email,password)

        if response==1:
            messagebox.showinfo("Success","You can Now login")
        else:
            messagebox.showerror("Error","Email Already Exists")

    def perform_login(self):
        email=self.email_input.get()
        password=self.pass_input.get()

        response = self.obj.search_data(email,password)
        if response==1:
            messagebox.showinfo("Success","Login Successfully")
            self.home_gui()
        elif response==-1:
            messagebox.showerror("Wrong Info","Incorrect email/password")
        else:
            messagebox.showerror("Error","User doesn't exists! Please register first")

    def home_gui(self):
        self.clear()
        logout_btn = Button(self.root, text="Logout", command=self.login_gui)
        logout_btn.pack(side="top", anchor="se", pady=(5, 5))
        logout_btn.configure(font=("Times New Roman", 12, "bold"))

        heading = Label(self.root, text="NLPApp", bg="#053345", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Times New Roman", 28, "bold"))

        language_btn = Button(self.root, text="Language Detection", bg="#053345", fg="white",command=self.language_detection)
        language_btn.pack(pady=(20, 20))
        language_btn.configure(font=("Times New Roman", 20, "bold"))

        er_btn = Button(self.root, text="Entity Extraction", bg="#053345", fg="white",command=self.entity_extraction)
        er_btn.pack(pady=(20, 20))
        er_btn.configure(font=("Times New Roman", 20, "bold"))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", bg="#053345", fg="white",command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(20, 20), ipady=5)
        sentiment_btn.configure(font=("Times New Roman", 20, "bold"))

    def language_detection(self):
        self.clear()
        go_back_btn=Button(self.root,text="Go Back",bg="white",fg="black",command=self.home_gui)
        go_back_btn.pack(side="top",anchor="w",pady=(5,5))
        go_back_btn.configure(font=("Times New Roman", 12, "bold"))

        heading = Label(self.root, text="NLPApp", bg="#053345", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Times New Roman", 30, "bold"))

        heading2 = Label(self.root, text="Language Detection", bg="#053345", fg="white")
        heading2.pack(pady=(30, 30))
        heading2.configure(font=("Times New Roman", 30, "bold"))

        heading2 = Label(self.root, text="Enter your Text", bg="#053345", fg="white")
        heading2.pack(pady=(15,1))
        heading2.configure(font=("Times New Roman", 24, "bold"))

        self.language_input=Entry(self.root,width=50)
        self.language_input.pack(pady=(20,5),ipady=4)

        detect_language_btn=Button(self.root,text="Detect Language",bg="white",fg="black",command=self.perform_detection)
        detect_language_btn.pack(pady=(30,30))
        heading2.configure(font=("Times New Roman", 25, "bold"))

        self.result_=Label(self.root,text="",bg="#053345",fg="white")
        self.result_.pack(pady=(15,15))

    def entity_extraction(self):
        self.clear()
        go_back_btn = Button(self.root, text="Go Back", bg="white", fg="black", command=self.home_gui)
        go_back_btn.pack(side="top", anchor="w", pady=(5, 5))
        go_back_btn.configure(font=("Times New Roman", 12, "bold"))

        heading = Label(self.root, text="NLPApp", bg="#053345", fg="white")
        heading.pack(pady=(30, 15))
        heading.configure(font=("Times New Roman", 30, "bold"))

        heading2 = Label(self.root, text="Entity Extraction", bg="#053345", fg="white")
        heading2.pack(pady=(10, 10))
        heading2.configure(font=("Times New Roman", 20, "bold"))

        heading3 = Label(self.root, text="Enter your Text", bg="#053345", fg="white")
        heading3.pack(pady=(10, 1))
        heading3.configure(font=("Times New Roman", 20, "bold"))

        self.para_input = Entry(self.root, width=50)
        self.para_input.pack(pady=(5, 5), ipady=4)

        heading4 = Label(self.root, text="Enter the word", bg="#053345", fg="white")
        heading4.pack(pady=(10, 1))
        heading4.configure(font=("Times New Roman", 20, "bold"))

        self.word_input = Entry(self.root, width=50)
        self.word_input.pack(pady=(5, 5), ipady=4)

        detect_entity_btn = Button(self.root, text="Launch", bg="white", fg="black",command=self.entity_detection)
        detect_entity_btn.pack(pady=(30, 30))
        detect_entity_btn.configure(font=("Times New Roman", 25, "bold"))


        self.result_1 = Label(self.root, text="",bg="#053345",fg="white")
        self.result_1.pack(pady=(15, 15))

    def sentiment_analysis(self):
        self.clear()
        go_back_btn = Button(self.root, text="Go Back", bg="white", fg="black", command=self.home_gui)
        go_back_btn.pack(side="top", anchor="w", pady=(5, 5))
        go_back_btn.configure(font=("Times New Roman", 12, "bold"))

        heading = Label(self.root, text="NLPApp", bg="#053345", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Times New Roman", 30, "bold"))

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#053345", fg="white")
        heading2.pack(pady=(30, 30))
        heading2.configure(font=("Times New Roman", 30, "bold"))

        heading3 = Label(self.root, text="Enter your Text", bg="#053345", fg="white")
        heading3.pack(pady=(15, 1))
        heading3.configure(font=("Times New Roman", 24, "bold"))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(20, 5), ipady=4)

        detect_analyze_btn = Button(self.root, text="Analyze", bg="white", fg="black", command=self.sentiment_detection)
        detect_analyze_btn.pack(pady=(30, 30))
        detect_analyze_btn.configure(font=("Times New Roman", 25, "bold"))

        self.result_2 = Label(self.root, text="",bg="#053345",fg="white")
        self.result_2.pack(pady=(15, 15))

    def perform_detection(self):

        client = nlpcloud.Client("python-langdetect", "YOUR_API_KEY", gpu=False)
        text=self.language_input.get()
        response=client.langdetection(text)
        response_result=response["languages"][0]
        self.result_.configure(text=response_result)

    def entity_detection(self):
        client = nlpcloud.Client("gpt-oss-120b", "YOUR_API_KEY", gpu=True)
        response = client.entities(
            self.para_input.get(),
            searched_entity=self.word_input.get()
        )
        entities = response.get("entities", [])
        if not entities:
            pretty = "No entities found."
        else:
            lines = []
            for e in entities:
                text = e.get("text", "")
                ent_type = e.get("type", "")
                start = e.get("start", "")
                end = e.get("end", "")
                lines.append(f"{text} ({ent_type}) [{start}:{end}]")
            pretty = "\n".join(lines)

        self.result_1.configure(text=pretty)

    def sentiment_detection(self):
        client = nlpcloud.Client("gpt-oss-120b", "YOUR_API_KEY", gpu=True)
        response = client.sentiment(
            self.sentiment_input.get(),
            target="NLP Cloud"
        )
        overall = response.get("sentiment") or response.get("label") or ""
        emotions = response.get("emotions") or response.get("labels") or []
        if isinstance(emotions, dict):
            emotions = list(emotions.values())
        if isinstance(emotions, str):
            emotions = [emotions]

        emotions_str = ", ".join(emotions) if emotions else "na"
        overall_str = overall if overall else "na"

        pretty = f"Sentiment: {overall_str}\nEmotions: {emotions_str}"

        self.result_2.configure(text=pretty)

    def clear(self):
        a = self.root.pack_slaves()
        for i in a:
            i.destroy()

if __name__=="__main__":
    nlp=NLPApp()


