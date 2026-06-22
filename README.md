# 🐍 Python Mini Projects

A collection of two beginner-friendly Python mini projects: a **Password Manager** and a **Student Result Manager**. Both projects are console-based and demonstrate core Python concepts such as file handling, data structures, and user input validation.

---

## 📁 Project Structure

```
python-mini-projects/
│
├── password_manager.py
├── student_result_manager.py
└── README.md
```

---

## 🔐 Password Manager (`password_manager.py`)

A simple command-line password manager that allows users to securely store, retrieve, and manage passwords for different accounts.

### Features

- Save a password for any account
- View all saved account passwords
- Generate a strong random password
- Exit the application

### How to Run

```bash
python password_manager.py
```

### Usage Example

```
===== Password Manager =====
1. Save Password
2. View Passwords
3. Generate Password
4. Exit

Enter your choice: 1
Enter account name: Gmail
Enter password: mySecret123
✅ Password saved successfully!

Enter your choice: 3
🔑 Generated Password: Xk@9mLqZ#2Rp
```

### Requirements

- Python 3.x
- No external libraries required (uses built-in `json` and `os` modules)

---

## 🎓 Student Result Manager (`student_result_manager.py`)

A console-based student result management system that allows users to record, display, and analyse student grades and results.

### Features

- Add a new student with their name and marks
- View all students and their records
- Check result for a specific student (total, average, and grade)
- Exit the application

### Grade Scale

| Grade | Percentage     |
|-------|----------------|
| A     | 80% and above  |
| B     | 70% – 79%      |
| C     | 60% – 69%      |
| D     | 50% – 59%      |
| F     | Below 50%      |

### How to Run

```bash
python student_result_manager.py
```

### Usage Example

```
===== Student Result Manager =====
1. Add Student
2. View All Students
3. Check Result
4. Exit

Enter your choice: 1
Enter student name: Alice
Enter marks for Math: 85
Enter marks for English: 78
Enter marks for Science: 90
✅ Student added successfully!

Enter your choice: 3
Enter student name: Alice

📋 Result for Alice:
  Math    : 85
  English : 78
  Science : 90
  Total   : 253 / 300
  Average : 84.33%
  Grade   : A
```

### Requirements

- Python 3.x
- No external libraries required (uses built-in `json` and `os` modules)

---

## 🚀 Getting Started

1. **Clone or download** the repository to your local machine.

2. **Navigate** to the project folder:
   ```bash
   cd python-mini-projects
   ```

3. **Run** either project directly with Python:
   ```bash
   python password_manager.py
   # or
   python student_result_manager.py
   ```

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Modules:** `json`, `os`
- **Interface:** Command-line (CLI)

---

## 💡 Concepts Demonstrated

- Functions and modular code
- Dictionaries and lists
- File handling with JSON
- User input and validation
- Loops and conditionals
- Basic arithmetic and string formatting

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## 👤 Author

> Created as part of a Python mini project series for beginners.
