import random
import smtplib
import pandas as pd
import datetime


my_email="amadornatalyyoseth@gmail.com"
my_password="XXX"

global letter_choose, new_letter, email



##################### Extra Hard Starting Project ######################

today=datetime.datetime.now()
list=["letter_1.txt","letter_2.txt","letter_3.txt"]
letter_choose= random.choice(list)

##read the csv
birthdays_csv= pd.read_csv("birthdays.csv")

#new_dict={new_key: newvalue for (index,data_row) in data.iterrows}
new_dict={(row["month"],row["day"]):(row["name"],row["email"],row["year"],row["month"],row["day"] )for (index,row) in birthdays_csv.iterrows()}

for key, value in new_dict.items():
    month,day=key
    name,email,year,_,_= value

    if(month==today.month and day==today.day):
        with open(f"letter_templates/{letter_choose}") as file:
            letter_file = file.read()
            new_letter=str(letter_file).replace("[NAME]",name)
            email=email
    break


with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=email,
                        msg=f"Subject:Happy Birthday\n\n{new_letter}")



