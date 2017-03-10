with open("text.txt", "w") as my_file:
    my_file.write("Hello World! My Name is Muhammad Azizul Hakim.")
    
if my_file != my_file.closed:
    my_file.close()
    
status = my_file.closed
print status
