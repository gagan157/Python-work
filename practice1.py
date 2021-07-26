
user_age=input("Enter your Age Or Birth Year : ")
future_year=2090
current_year=2021
def calculate_age():
    lenght=len(user_age)

    if lenght==4:
        converts=int(user_age)
        print(f"you will be 100 years old in {converts + 100}")
        if converts<1990:
            print(f"Sorry you no more in {future_year}")
        elif converts>current_year:
            print("You are not yet born")    
        else:            
            total_age=future_year-converts
            print(f"your age in 2090 is {total_age}years old")
            
    elif lenght<=2:
        convert=int(user_age)
        print(f"you will be 100 years old in {current_year + 100 - convert}")
        if convert>30:
            print(f"Sorry you no more in {future_year}")
        elif convert<1:
            print("You are not yet born")    
        else:    
            total_year=future_year-current_year
            total_age=convert+total_year
            print(f"your age in 2090 is {total_age}years old")
    else:
        print("Please Enter valid age or years")  

calculate_age()    