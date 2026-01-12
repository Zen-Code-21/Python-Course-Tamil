#Create a file called "rohit_sharma.txt", and it is going to contain inforamtion about rohit sharma


f = open("rohit_sharma.txt", "w")

info = '''
Rohit sharma is the captain of Indian Cricket Team.
He has also captained Mumbai Indians in the IPL
His favorite shot is pull shot
He has won the champions trophy and t20 world cup
'''

f.write(info)
f.close()