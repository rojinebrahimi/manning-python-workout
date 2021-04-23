def name_triangle():
    name = input("Enter your name: ")
    
    if name.isalpha:
        for index, char in enumerate(name):
            for j in range(index+1):
                print(name[j])
            print()


name_triangle()