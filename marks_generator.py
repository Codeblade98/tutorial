name = input("Enter the name of the student ")
mod_name = name + ' : '


with open('marks_list.txt', mode = 'r') as my_file:
    while True:
        str = my_file.readline()
        if str.startswith(mod_name):
            print(str)
            break

        if str == '':
            print("\nName not in list")
            break
            
    

    

   
    