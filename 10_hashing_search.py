
LABSHEET10

n = int(input("enter the number of input")) 
fruits = set()
for i in range(0,n): 
    a = input("enter the fruits") 
    fruits.add(a) 
q = int(input("enter the number of items to search"))
result = []
for i in range(0,q): 
    search = input("enter the fruits to search")  
    if search in fruits:
        result.append("found")
    else:
        result.append("Not found")
for i in result:
    print(i)



n = int(input("Enter the number of books: ")) 
books_db = {} 
for i in range(n): 
    name = input(f"Enter name for book {i+1}: ") 
    book_id = input(f"Enter ID for {name}: ")
    books_db[name] = book_id 
q = int(input("\nEnter the number of items to search: "))
results = []
for i in range(q): 
    search_term = input("Enter the book name to search: ") 
    if search_term in books_db:
        results.append(books_db[search_term]) # Append the ID
    else:
        results.append("Book not found")
for res in results:
    print(res)

