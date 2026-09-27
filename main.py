from tabulate import tabulate
#FUNCTION TO ADD BOOKS IN THE LIBRARY 
all_book=[]
def add_book():
    print("===== ADD BOOKS =====")
    entry=int(input("Enter no of books to be added: ")) #TO ADD MULTIPLE BOOKS
    for i in range(entry):
        print("=====||=====")
        print(f"ENTRY of BOOK #{i+1}")
        while True:  #GETTING ONLY INTEGER INPUT
            book_id=input("Enter Book ID: ")
            if book_id.isdigit():
              break
            else:
               print("invalid input,try again!")
        book_name=input("Enter Book name: ").upper()
        author_name=input("Enter Author name: ").upper()
        while True:    #CHECK AVAILABILITY OF BOOK
            avbly=['ISSUED','AVAILABLE']
            m=input("ISSUED--> 0 || AVAILABLE--> 1\n CHOOSE: ")
            if m.isdigit():
                m1=int(m)
                if 0<= m1 <len(avbly):
                    availability=(avbly[m1])
                    break
                else:
                    print("Enter valid option")
            else:
                print("Invalid input")
                 
        book_data=[book_id,book_name,author_name,availability]
        all_book.append(book_data)

    
#TO DISPLAY ALL THE BOOKS ADDED
def display():   
    print(tabulate(all_book,headers=['BOOK ID','BOOK NAME','AUTHOR NAME','STATUS'],tablefmt='fancy_grid'))
    
#TO CHECK AND DISPLAY THE DETAILS OF BOOKS
def search_book():    
    print("""
    ===== SEARCH BOOK =====
    1.Search by ID
    2.Search by Name
    3.Search by Author
    4.Exit
    """)
    while True:
        n=input("Enter your Search action(1,2,3,4): ")
        if n=='4':
            break
        if n not in ['1','2','3']:
            print("invalid choice,try again!")
            continue
        choice=input("Enter your search value: ").upper()
        found=False
        for book in all_book:
            if n=='1' and book[0]==choice:
                print("BOOK FOUND!")
                found=True
            elif n=='2' and book[1]==choice:
                print("BOOK FOUND!")
                found=True
            elif n=='3' and book[2]==choice:
                print("BOOK FOUND!")
                found=True

            if found:
                print(tabulate([book],headers=['BOOK ID','BOOK NAME','BOOK AUTHOR','AVAILABILITY'],tablefmt='fancy_grid'))
                break
        else:
            print("Book not found!")

#TO ISSUE THE BOOK FROM THE LIBRARY
def issue_book():   
    n=input("Enter book name or id to issue: ").upper()
    for i in all_book:
        if i[0]==n or i[1]==n:
            if(i[3]=='ISSUED'):
                print(f"{i[1]} already issued")
            elif(i[3]=='AVAILABLE'):
             i[3]='ISSUED'
             print("Book issued successfully")
            else:
              print("Book not available in library")


#TO RETURN THE BOOK TO LIBRARY
def return_book():   
    n=input("Enter Book ID or Name to return: ").upper()
    for book in all_book:
        if book[0]==n or book[1]==n:
            if book[3]=='ISSUED':
                book[3]='AVAILABLE'
                print("Book is successfully returned")
            elif book[3]=='AVAILABLE':
                print("Already available")
            else:
                print("Not available in library")


#TO REMOVE THE BOOK FROM THE LIBRARY
def delete_book():
    found=False
    n=input("Enter Book ID or Name to delete from collection: ").upper()
    for book in all_book:
        if n==book[0] or book[1]==n:
            all_book.remove(book)
            print("Book removed successfully from the collection".upper())
            found=True
            break
    else:
        print("BOOK NOT FOUND!")

def statistics():
    total=len(all_book)
    count_avbl=0
    count_issue=0
    for book in all_book:
        if book[3]=='AVAILABLE':
            count_avbl+=1
        elif book[3]=='ISSUED':
            count_issue+=1
    print(f"""
    ===== LIBRARY STATISTICS =====
            TOTAL BOOKS = {total}
            AVAILABLE BOOKS = {count_avbl}
            ISSUED BOOK = {count_issue}
           """)
    

            #PROGRAM TO CALL THE NEEDED FUNCTION
functions=[add_book,display,search_book,issue_book,return_book,delete_book,statistics]
while True:
     print("""
=====> MAIN MENU <=====
 ADD BOOKS--> 0
 DISPLAY BOOKS--> 1 
 SEARCH BOOK--> 2
 ISSUE BOOK--> 3 
 RETURN BOOK--> 4 
 DELETE BOOK--> 5
 LIBRARY STATISTICS--> 6 
 EXIT--> 7""")
     choice=input("Enter your action(0-6): ")
     if choice.isdigit():
          user_input=int(choice)
          if user_input == len(functions):
            print("program ended!".upper())
            break
          elif 0<=user_input<len(functions):
              functions[user_input]()
          else:
              print("invalid choice")
     else:
         print("Invalid input, enter a valid text number")