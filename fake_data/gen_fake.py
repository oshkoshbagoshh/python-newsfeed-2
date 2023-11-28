# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2023-11-28 10:31:41
# @Last Modified by:   undefined
# @Last Modified time: 2023-11-28 10:31:41
# @Description: file:///Users/aj/python-newsfeed-2/fake_data/gen_fake.py

from faker import Faker
# import User from app.models
import os 
import sys
# write fake users and fake posts to a csv file
import csv 



fake = Faker()

# data to be written row-wise in csv file
headers = ['name', 'email', 'username', 'password', 'text']


data = [fake.name(), fake.email(), fake.user_name(), fake.password(), fake.text()]

# writing to a csv file 
with open('fake_data.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    
    # writing the data rows
    csvwriter.writerow(headers)
    # csvwriter.writerows(data)

# def gen_fake_users():
#     for _ in range(10):
#         print(fake.name())
#         print(fake.email())
#         print(fake.password())
#         print(fake.text())
        
#     return fake.name(), fake.email(), fake.password(), fake.text()

# gen_fake_users()
    


# fake posts 
# def gen_fake_posts():
#     fake = Faker()
#     for _ in range(10):
#         print(fake.text())
        
#     return fake.text()

# gen_fake_posts()
