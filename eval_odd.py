#these are the functions which i told about, written with 100 percent accuracy
def add(shopping, item: str):
    # Taking input at runtime
    new = str(input("Enter item to add: "))
    shopping.append(new)
    print(shopping)

def remove(shopping, item: str):
    if item in shopping:
        shopping.remove(item)
        print(shopping)
    else:
        print('NOT IN LIST')

def search(shopping, item: str):
    if item in shopping:
        print("It is in the list")
    else:
        print("Not in the list")

def display(shopping):
    print(shopping)
def binary_search(shopping, item: str):
    shopping.sort()  
    low = 0
    high = len(shopping) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if shopping[mid] == item:
            print(item[::-1]) 
            return
        elif shopping[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
            
    print("Item not found")





# only thing which i didn't knew was systax of switch case, 
***     shoping = ["apple", "banana", "kors"]
#apply switch case for add ,remove, search, display, binary_search
    
    1.add(shoping)
    
    2.remove(shoping)
    

    3.search(shoping)

***
upper code is my main, will not work




#below code is ai generated, after you checked
*** def main():
    shopping = ["apple", "banana", "kors"]
    
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Remove")
        print("3. Search")
        print("4. Display")
        print("5. Binary Search")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add(shopping, "")
        elif choice == '2':
            item_to_remove = input("Enter item to remove: ")
            remove(shopping, item_to_remove)
        elif choice == '3':
            item_to_search = input("Enter item to search: ")
            search(shopping, item_to_search)
        elif choice == '4':
            display(shopping)
        elif choice == '5':
            item_to_binary_search = input("Enter item for binary search: ")
            binary_search(shopping, item_to_binary_search)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function
if __name__ == "__main__":
    main()
***
