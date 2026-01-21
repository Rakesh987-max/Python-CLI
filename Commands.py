

users = {}        
todos = {}        

while True:
    print("\n--- MAIN MENU ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    # REGISTER
    if choice == "1":
        username = input("Enter username: ")

        if username in users:
            print(" Username already exists")
        else:
            password = input("Enter password: ")
            users[username] = password
            todos[username] = []      # empty todo list
            print(" Registration successful")

    # LOGIN
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print(" Login successful")

            # USER MENU
            while True:
                print("\n--- TODO MENU ---")
                print("1. Add Todo")
                print("2. View Todos")
                print("3. Delete Todo")
                print("4. Logout")

                option = input("Enter option: ")

                # ADD TODO
                if option == "1":
                    task = input("Enter task: ")
                    todos[username].append(task)
                    print(" Task added")

                # VIEW TODOS
                elif option == "2":
                    if not todos[username]:
                        print(" No tasks found")
                    else:
                        print("\nYour Tasks:")
                        for i, task in enumerate(todos[username], start=1):
                            print(f"{i}. {task}")

                # DELETE TODO
                elif option == "3":
                    if not todos[username]:
                        print(" No tasks to delete")
                    else:
                        for i, task in enumerate(todos[username], start=1):
                            print(f"{i}. {task}")

                        num = int(input("Enter task number: "))
                        if 1 <= num <= len(todos[username]):
                            removed = todos[username].pop(num - 1)
                            print(f" Deleted: {removed}")
                        else:
                            print(" Invalid number")

                # LOGOUT
                elif option == "4":
                    print("Logged out")
                    break

                else:
                    print("Invalid option")

        else:
            print(" Invalid username or password")

    # EXIT
    elif choice == "3":
        print(" Program exited")
        break

    else:
        print(" Invalid choice")
