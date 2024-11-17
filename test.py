import google.generativeai as genai
class NLPModel:
    def get_model(self):
        genai.configur(api_key="AIzaSyCfq9PeM1zIFUyLh8we8OqPkwzmU_-PiGs")
        model = genai.GenerativeModel("gemini-pro")
        return model
#all the functions in this class
class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.__first_menu()  

    def __first_menu(self):
        first_input = input("""
        Hi! Would you like to proceed?
        1. Not a member? Register
        2. Already a member? Login
        3. Exit
        """)
        
        if first_input == '1':
            self.__register()
        elif first_input == '2':
            self.__login()
        else:
            exit()
    #as
    def __second_menu(self):
        second_input = input("""
        Hi! Would you like to proceed?
        1. sentimental analysis
        2. language translaton
        3. Language detection
        """)
        
        if second_input == '1':
            self.__statement_analysis()
            pass
        elif second_input == '2':
            self.___language_translation()
        elif second_input == '3':
            
            self.__language_detection()
        
#functions for registeration
    def __register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.__database:
            print("E-mail already exists. Please try again.")
        else:
            self.__database[email] = [name, password]
            print("Registration successful.")
            print(self.__database)
            self.__first_menu() 
        

    def __login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.__database and self.__database[email][1] == password:
            print("Login successful.")
            self.__second_menu()
        else:
            print("Invalid email or password. Please try again.")
            self.__first_menu()

    def __statement_analysis(self):
        user_text2= input("Enter your text: ")
        model = super().get_model()
        response= model.generate_content(f"Give me the sentiment of the given sentance{user_text2}")
        result = response.text
        print(result)
        self.__second_menu()

#lang translation model using appi
    def ___language_translation(self):   
        user_text= input("Enter your text: ")
        response = model.generate_content(f"Give me hindi traslation of this sentance:{user_text}")
        result = response.text
        print(result)
        self.__second_menu()

    def __language_detection(self):
     user_test1=input("Enter your text:")
     response = model.generate_content(f"Detect the language of the sentance:{user_test1}")
     self.__second_menu()
     
#here the main code ends 

# To start the application, create an instance of NLPApp.
app = NLPApp()
.
