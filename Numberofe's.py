#Richard Deegan
#This program reads in a text file and outputs the number of e's it contains.
x = str("e)")

with open ("es.py moby-dick.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')
    print(data)
    freq = 0
    for char in data:
        if char == x:
            freq = freq + 1
    print(freq)

