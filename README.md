# Python Banking System

An object-oriented command-line banking application built in Python. This project simulates core banking operations, account security controls, and transaction tracking.

## 🎯 Why I Built This

I built this project to deepen my understanding of Object-Oriented Programming (OOP), state management, and class interactions in Python. Specifically, I wanted to practice:
- Designing multi-class architectures where objects interact with one another (`User`, `Account`, `Transaction`).
- Managing state, data validation, and conditional business logic (e.g., preventing overdrafts or negative deposits).
- Passing object references between classes to handle inter-account fund transfers.
- Tracking history by generating timestamped records using Python's `datetime` module.

## 🚀 Key Features

- **Object-Oriented Design:** Clean separation of responsibilities across `User`, `Account`, and `Transaction` classes.
- **Core Banking Operations:** Safe deposit, withdrawal, and fund transfer methods with built-in validation rules and balance checking.
- **Transaction Audit Logging:** Automatically instantiates and logs timestamped transaction records detailing senders, receivers, amounts, and operation types.
- **Account Security:** Includes account-freezing capabilities to manage security states.
- **Interactive CLI Menu:** Robust command-line interface loop allowing users to navigate through banking options smoothly.

## ⚙️ How to Run

1. Clone the repository and navigate into the directory:
   ```bash
   git clone [https://github.com/john-fafunmi/python-banking-system.git](https://github.com/john-fafunmi/python-banking-system.git)
   cd python-banking-system
