#add information to the file "rohit_sharma.txt", add info of the years in which we won an ipl

f = open("rohit_sharma.txt", "a")

info = '''
Rohit sharma is the captain of Indian Cricket Team.
He has also captained Mumbai Indians in the IPL
His favorite shot is pull shot
He has won the champions trophy and t20 world cup
'''
additional_info = "Rohit sharma won the ipl trophy in 2013, 2015, 2017, 2019 and 2020"

f.write(additional_info)
f.close()