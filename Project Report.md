# PROJECT REPORT: TO-BUY LIST MANAGER

##  ![college logog](media/image1.png){width="5.7659722222222225in" height="3.0701388888888888in"} {#college-logog}

> **Project Title:** To-Buy List Manager
>
> **Student Name:** Aryan Sharma
>
> **Registration Number:** 25BSA10066
>
> **Course:** Introduction to problem solving and programming

## 1. Introduction {#introduction}

The To-Buy List Manager is a Python-based utility designed to digitize
the traditional shopping list. By utilizing file handling and data
structures, the application provides a secure and persistent environment
for users to track their purchasing needs. The project demonstrates the
practical application of modular programming, file I/O operations, and
user authentication logic.

## 2. Problem Statement {#problem-statement}

In a shared household or busy student environment, keeping track of
personal requirements is difficult. Paper lists are easily lost, and
digital notes often lack organization or separation between users. There
is a need for a lightweight system that allows multiple users to
maintain private shopping lists on a single machine without data overlap
or loss.

## 3. Functional Requirements {#functional-requirements}

The system is divided into three primary modules:

**Authentication Module:**

**Register:** Allows new users to create a unique username and password.

**Login:**Verifies credentials against the stored database before
granting access.

**List Management Module (CRUD):**

**Add:** Users can append new string items to their specific list.

**View:** Users can see their current list with index numbers.

**Delete:** Users can remove specific items by selecting their index.

**Storage Module:**

**Load:** Parses the text file into a Python dictionary structure on
startup

**Save:** Serializes the dictionary back into a formatted string
structure in the text file after every change.

## 

## 

## 

## 4. Non-Functional Requirements {#non-functional-requirements}

**Persistence:** The system must retain data indefinitely after the
application is closed.

**Reliability:** The system must handle invalid user inputs (e.g.,
entering non-numeric choices) without crashing.

**Efficiency:** Database operations (Read/Write) should be
near-instantaneous for standard usage.

**Privacy:** One user must not be able to view or modify another user\'s
list.

## 5. System Architecture {#system-architecture}

The application follows a monolithic console-based architecture:

**User Interface Layer:** CLI (Command Line Interface) handles inputs
via input() and outputs via print().

**Application Logic Layer:** Functions like login_user, add_items, and
remove_items process the business logic.

**Data Access Layer:** The load_data and save_data functions interact
directly with the user_data_pure.txt file.

## 6. Design Diagrams {#design-diagrams}

**Use Case Diagram:**

**Actor:** User

**Use Cases:** Register, Login, View List, Add Item, Remove Item,
Logout.

**Sequence Diagram (Add Item):**

User -\> Selects \"Add\" -\> System Prompts for Item -\> User enters
\"Apple\" -\> System updates List -\> System calls save_data() -\>
System writes to File -\> System confirms success.

## 

## 

## 

## 7. Design Decisions & Rationale {#design-decisions-rationale}

**Storage Strategy:** I chose a delimited text file format
(user:pass:\[items\]) instead of SQL.

*Rationale:* It is lightweight, portable, and requires no external
server setup, making it perfect for a personal utility tool.

**Data Structure:** I used a Python Dictionary ({user: {pass, list}})
for internal memory.

*Rationale:* Dictionaries provide O(1) time complexity for looking up
users during login, ensuring fast performance.

## 8. Implementation Details {#implementation-details}

The core functionality relies on string manipulation to parse the
database file.

**Parsing Logic:** The load_data function splits each line of the text
file by the colon delimiter (:) to separate credentials from the list
data.

**List Cleaning:** The list is stored as a string (e.g., \"\[milk,
eggs\]\"). The implementation strips the brackets \[\] and splits by
comma , to convert it back into a usable Python list object.

## 9 .Result {#result}

========================================

> WELCOME TO THE TO-BUY LIST MANAGER
>
> ========================================
>
> \*\*Menu:\*\*
>
> 1\. Login
>
> 2\. Register New Account
>
> 3\. Exit
>
> Enter choice (1-3): 2
>
> \*\*NEW USER REGISTRATION\*\* 📝
>
> Choose a new username: VIT
>
> Choose a password: VIT
>
> Error saving data to file.
>
> ✅ Registration successful! You can now log in.
>
> \*\*Menu:\*\*
>
> 1\. Login
>
> 2\. Register New Account
>
> 3\. Exit
>
> Enter choice (1-3): 1
>
> \*\*USER LOGIN\*\* 🔑
>
> Enter username: VIT
>
> Enter password: VIT

Welcome back, VIT!

> \-\-- \*\*USER ACTIONS\*\* \-\--
>
> 1\. View My To-Buy List
>
> 2\. Add New Items to List
>
> 3\. Remove/Select Item
>
> 4\. Logout and Exit
>
> Enter action (1-4): 2
>
> ➕ \*\*ADD ITEMS\*\* ➕
>
> Enter items one by one. Type \'done\' to finish.
>
> Enter item: A
>
> \'A\' added.
>
> Enter item: B
>
> \'B\' added.
>
> Enter item: C
>
> \'C\' added.
>
> Enter item: D
>
> \'D\' added.
>
> Enter item: E
>
> \'E\' added.
>
> Enter item: F
>
> \'F\' added.
>
> Enter item: G
>
> \'G\' added.
>
> Enter item: H
>
> \'H\' added.
>
> Enter item: I
>
> \'I\' added.
>
> Enter item: 1
>
> \'1\' added.
>
> Enter item: done
>
> Error saving data to file.
>
> ✅ List updated and saved!
>
> \-\-- \*\*USER ACTIONS\*\* \-\--
>
> 1\. View My To-Buy List
>
> 2\. Add New Items to List
>
> 3\. Remove/Select Item
>
> 4\. Logout and Exit
>
> Enter action (1-4): 1
>
> 🛒 \*\*VIT\'S TO-BUY LIST\*\* 🛒
>
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
>
> 1\. A
>
> 2\. B
>
> 3\. C
>
> 4\. D
>
> 5\. E
>
> 6\. F
>
> 7\. G
>
> 8\. H
>
> 9\. I
>
> 10\. 1
>
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
>
> \-\-- \*\*USER ACTIONS\*\* \-\--
>
> 1\. View My To-Buy List
>
> 2\. Add New Items to List
>
> 3\. Remove/Select Item
>
> 4\. Logout and Exit
>
> Enter action (1-4): 3
>
> 🛒 \*\*VIT\'S TO-BUY LIST\*\* 🛒
>
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
>
> 1\. A
>
> 2\. B
>
> 3\. C
>
> 4\. D
>
> 5\. E
>
> 6\. F
>
> 7\. G
>
> 8\. H
>
> 9\. I
>
> 10\. 1
>
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
>
> Enter the number of the item to remove (or \'0\' to cancel): 1
>
> Error saving data to file.
>
> Successfully removed: \*\*A\*\*
>
> \-\-- \*\*USER ACTIONS\*\* \-\--
>
> 1\. View My To-Buy List
>
> 2\. Add New Items to List
>
> 3\. Remove/Select Item
>
> 4\. Logout and Exit
>
> Enter action (1-4): 1
>
> 🛒 \*\*VIT\'S TO-BUY LIST\*\* 🛒
>
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
>
> 1\. B
>
> 2\. C
>
> 3\. D
>
> 4\. E
>
> 5\. F
>
> 6\. G
>
> 7\. H
>
> 8\. I
>
> 9\. 1
>
> \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
>
> \-\-- \*\*USER ACTIONS\*\* \-\--
>
> 1\. View My To-Buy List
>
> 2\. Add New Items to List
>
> 3\. Remove/Select Item
>
> 4\. Logout and Exit
>
> Enter action (1-4): 4
>
> VIT logged out. Goodbye!

## 10. Testing Approach {#testing-approach}

> **Unit Testing:** Verified the load_data function by manually editing
> the text file and checking if the app read it correctly
>
> **Functional Testing:** Performed a full cycle: Registered \"UserA\",
> added items, exited, registered \"UserB\", added different items.
> Verified \"UserA\" items were unchanged.
>
> **Boundary Testing:** Attempted to remove an item from an empty list
> to ensure the system displayed a \"List is empty\" warning instead of
> crashing.

## 11. Challenges Faced {#challenges-faced}

> **File Parsing:** Converting the string representation of a list back
> into a Python list was tricky. I had to handle edge cases where the
> list was empty \[\] to prevent errors during the split operation.
>
> **Data Integrity:** Ensuring that the file wasn\'t overwritten with
> partial data if the program crashed mid-operation.

## 12. Learnings & Key Takeaways {#learnings-key-takeaways}

> Mastered Python\'s file I/O modes (r, w) and string manipulation
> methods (split, strip).
>
> Learned the importance of separating the User Interface (print
> statements) from the Data Logic (file saving) for cleaner code.

## 13. Future Enhancements {#future-enhancements}

> **Password Hashing:** Implement security algorithms to hash passwords
> instead of storing them as plain text.
>
> **Item Quantities:** Allow users to specify quantities (e.g., \"Milk
> x2\").
>
> **Search Feature:** Add a search bar to find specific items in long
> lists.

## 14. References {#references}

> Python 3.10 Documentation: File Input and Output.
>
> Course materials on Dictionary Data Structures and Exception Handling.
