
DATA_FILE = 'user_data_pure.txt'

def load_data():
    """
    Loads user data from the text file using pure file I/O.
    
    Data format in file: username:password:[item1,item2,item3]
    
    Returns a dictionary: {'user1': {'password': 'pwd', 'list': ['item1', 'item2']}, ...}
    """
    user_data = {}
    try:
        f = open(DATA_FILE, 'r')
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(':', 2) 
            
            if len(parts) == 3:
                username, password, list_str = parts
                
                item_list = []
                if list_str.startswith('[') and list_str.endswith(']'):
                    content = list_str[1:-1]
                    if content:
                        item_list = [item.strip() for item in content.split(',')]
                
                user_data[username] = {'password': password, 'list': item_list}
        f.close()
    except IOError:
        pass 
        
    return user_data

def save_data(data):
    """Saves user data back to the text file in the raw format."""
    lines = []
    for username, user_info in data.items():
        password = user_info['password']
        item_list = user_info['list']
        list_str = '[' + ','.join(item_list) + ']'
        line = f"{username}:{password}:{list_str}\n"
        lines.append(line)

    try:
        f = open(DATA_FILE, 'w')
        f.writelines(lines)
        f.close()
    except IOError:
        print("Error saving data to file.")



def register_user(user_data):
    """Prompts for new username and password and saves the new user."""
    print("\n📝 **NEW USER REGISTRATION** 📝")
    while True:
        username = input("Choose a new username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue
        if username in user_data:
            print(f"Username '{username}' already exists. Please choose another.")
        else:
            break
            
    password = input("Choose a password: ").strip()
    if not password:
        print("Password cannot be empty. Registration failed.")
        return False
        
    user_data[username] = {'password': password, 'list': []}
    save_data(user_data)
    print("✅ Registration successful! You can now log in.")
    return True

def login_user(user_data):
    """Handles the login process and returns the username if successful."""
    print("\n🔑 **USER LOGIN** 🔑")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in user_data and user_data[username]['password'] == password:
        print(f"\nWelcome back, {username}!")
        return username
    else:
        print("\n❌ Login failed. Invalid username or password. ❌")
        return None


def view_list(user_data, current_user):
    """Displays the current user's to-buy list."""
    print(f"\n🛒 **{current_user.upper()}'S TO-BUY LIST** 🛒")
    user_list = user_data[current_user]['list']
    
    if not user_list:
        print("Your list is currently empty.")
        return

    print("-" * 30)
    for i, item in enumerate(user_list, 1):
        print(f"{i:2}. {item}") 
    print("-" * 30)

def add_items(user_data, current_user):
    """Allows the user to add new items to their list."""
    print("\n➕ **ADD ITEMS** ➕")
    print("Enter items one by one. Type 'done' to finish.")
    
    while True:
        item = input("Enter item: ").strip()
        if item.lower() == 'done':
            break
        
        if item:
            user_data[current_user]['list'].append(item)
            print(f"'{item}' added.")
        else:
            print("Item cannot be empty.")
            
    save_data(user_data)
    print("\n✅ List updated and saved!")

def remove_item(user_data, current_user):
    """Allows the user to select and remove an item by its number."""
    user_list = user_data[current_user]['list']

    if not user_list:
        print("\nYour list is empty. Nothing to remove.")
        return

    view_list(user_data, current_user)
    
    while True:
        try:
            choice = input("Enter the number of the item to remove (or '0' to cancel): ").strip()
            
            if choice == '0':
                print("Removal cancelled.")
                return
            item_index = int(choice) - 1 
            
            if 0 <= item_index < len(user_list):
                removed_item = user_list.pop(item_index)
                save_data(user_data)
                print(f"🗑️ Successfully removed: **{removed_item}**")
                break
            else:
                print(f"Invalid number. Please enter a number between 1 and {len(user_list)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_app():
    """The main entry point of the application."""
    user_data = load_data()
    current_user = None

    print("=" * 40)
    print("    WELCOME TO THE TO-BUY LIST MANAGER")
    print("=" * 40)
    while current_user is None:
        print("\n**Menu:**")
        print("1. Login")
        print("2. Register New Account")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            current_user = login_user(user_data)
        elif choice == '2':
            register_user(user_data)
        elif choice == '3':
            print("👋 Goodbye!")
            return 
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    while True:
        print("\n--- **USER ACTIONS** ---")
        print("1. View My To-Buy List")
        print("2. Add New Items to List")
        print("3. Remove/Select Item")
        print("4. Logout and Exit")
        
        action = input("Enter action (1-4): ").strip()
        
        if action == '1':
            view_list(user_data, current_user)
        elif action == '2':
            add_items(user_data, current_user)
        elif action == '3':
            remove_item(user_data, current_user)
        elif action == '4':
            print(f"👋 {current_user} logged out. Goodbye!")
            save_data(user_data)
            break 
        else:
            print("Invalid action. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    run_app()

input("Press enter to exit")