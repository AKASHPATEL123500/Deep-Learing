
def list_all_students():
    pass

def add_students(roll_no,name,subject):
    pass

def update_students(id,):
    pass

def delete_students(id):
    pass

def main():
    while True:
        print("----Enter your choice----\n")
        print("1. List All Students")
        print("2. Add students")
        print("3. Update Students")
        print("4. Delete Students")
        print("5. Exist")
        choice = input("Enter your choice")
        
        match choice:
            case "1":
                list_all_students()
            case "2":
                add_students(roll_no,name,subject)
            case "3":
                update_students()
            
            case "4":
                delete_students()
            
            case "5":
                break
            
if __name__ == "__main__":
    main()