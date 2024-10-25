names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_term = input("Enter a name to search for (press Enter to search for 'Sam'): ")

if search_term.strip() == "":
    search_term = "Sam"

if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")
