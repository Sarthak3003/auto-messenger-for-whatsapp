from threading import local
from time import localtime
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')

name = input("Enter the name of user or group: ")
msg = input("Enter your message: ")
count = int(input("Enter the count: "))

input("Enter anything after scanning QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('p3_M1')

print("\nEnter year like 2022\nMonth like 2\nDay like 10\nWhere 2 means feb for month\n")

year = int(input("which year to send message? "))
month = int(input("which month to send message? "))
day = int(input("which day to send message? "))

hour = int(input("which hour of the day in 24 hrs format: "))
minu = int(input("Minute of the hour 0-59: "))
sec = int(input("Second of hour 0-59: "))

work_not_done = True
print("\nScript is running normally\n")
while work_not_done:
    if year == localtime()[0] and month == localtime()[1] and day == localtime()[2] and hour == localtime()[3] and minu == localtime()[4] and sec == localtime()[5]:
        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_3HQNh _1Ae7k')
            button.click()
