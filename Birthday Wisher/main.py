import pandas as pd
import datetime as dt
import random as rn
import smtplib as smt

my_mail = "saptarshidhibar424@gmail.com"
password = "wxetfrpzzlqgvmxo"
today = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if int(row['month']) == int(today.month) and int(row['day']) == int(today.day):
        letter = rn.choice(["./letter_templates/letter_1.txt",
                            "./letter_templates/letter_2.txt",
                            "./letter_templates/letter_3.txt"])
        with open(letter, "r") as main_data:
            lines = main_data.read()
            update_lines = lines.replace("[NAME]", row["name"])
        with smt.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # tls = Transfer Layer Security
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs="testing793@yahoo.com",
                                msg=f"Subject:'HAPPY BIRTHDAY'\n\n{update_lines}")
