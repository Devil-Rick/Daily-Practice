import smtplib as smt
import datetime as dt
import random as rn

my_mail = "saptarshidhibar424@gmail.com"
password = "wxetfrpzzlqgvmxo"
today = dt.datetime.now()

with open("quotes.txt", "r") as data:
    data_file = data.readlines()
    quote_of_day = rn.choice(data_file)

if today.weekday() == 0:
    with smt.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # tls = Transfer Layer Security
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs="testing793@yahoo.com",
                            msg=f"Subject:'MONDAY QUOTES'\n\n{quote_of_day}")
