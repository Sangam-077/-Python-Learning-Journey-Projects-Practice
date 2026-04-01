contacts={}
def add_contact(contacts,name,phn_number,email):
    if name in contacts:
        print("name already exists")
        return
    contacts[name]={"phone":phn_number, "email":email}
    print(f"{name} added in the contact")

def search_contact(contacts,name):
    result=contacts.get(name)
    if result:
        print(f"Name: {name} | Phone: {result['phone']} | Email: {result['email']}")
    else:
        print("name not in the contact")
    
def delete_name(contacts,name):
    if name not in contacts:
        print(f"{name} not found")
        return
    del contacts[name]
    print(f"{name} deleted")

def list_all(contacts):
    if not  contacts:
        print("no any names in contacts")
        return
    for name in sorted(contacts):
        info = contacts[name]
        print(f"{name}: {info['phone']} | {info['email']}")

        
    
    


    
def menu():
    while True:
        print(" 1. Add contact ")
        print(" 2. Search contact ")
        print(" 3. Delete Contact ")
        print(" 4. List all contact ")
        print(" 5. Quit")
    
        choice=input("\nselect an option ").strip()

        if choice=="1":
            name=input("Name: ").strip()
            phn_number=input("Phone number: ").strip()
            email=input("Email: ").strip()
            add_contact(contacts,name,phn_number,email)
        
        elif choice=="2":
            name=input("Search name: ").strip()
            search_contact(contacts,name)
        
        elif choice=="3":
            name=input("Delete name: ").strip()
            delete_name(contacts,name)
        
        elif choice=="4":
            list_all(contacts)
        
        elif choice=="5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid Option! Enter a valid number")

if __name__=="__main__":
    menu()
            
        
