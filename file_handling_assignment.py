from pathlib import Path

f = open("OneDrive\\Desktop\\file_handling_assignment\\my_file.txt", "w")
f.write("My name is Eutycus Wanjohi.\n" )
f.write("I am 27 years old\n")
f.write("Im from Kirinyaga county\n")
f = open("OneDrive\\Desktop\\file_handling_assignment\\my_file.txt", "r")
print(f.read())
f = open("OneDrive\\Desktop\\file_handling_assignment\\my_file.txt", "a")
f.write("Software engineering is one of best career to undertake\n ")
f.write("python is among the programming languages used in web applications\n")
f.write("Data analytics and machine learning are also practised using python among other languages\n")
f = open("OneDrive\\Desktop\\file_handling_assignment\\my_file.txt", "r")
print(f.read())
try:
    f = open("OneDrive\\Desktop\\file_handling_assignment\\ doc.txt", "r")
except:
    print("file not found")

