# Expense Tracker (Python CLI)

A simple command-line Expense Tracker built in Python to revise core Python concepts such as functions, classes, file handling, JSON operations, loops, conditionals, and object-oriented programming.

This project is part of my Python fundamentals revision before extending it into a more production-ready backend application with PostgreSQL and an ETL pipeline.

---

## Features

- Add a new expense
- View all expenses
- Edit existing expenses
- Delete expenses
- Search expenses
- Sort expenses
- Store data persistently using JSON
- Category selection menu
- Input validation for user choices

---

## Concepts Practiced

- Functions
- Classes and Objects
- File Handling
- JSON Serialization (`json.load`, `json.dump`)
- Lists and Dictionaries
- Loops (`for`, `while`)
- Conditionals
- Exception Handling
- User Input Validation
- Enumerate
- CRUD Operations
- Modular Code Structure

---

## Project Structure

```
expense-tracker/
│
├── main.py
├── expense.py
├── storage.py
├── expenses.json
└── README.md
```

*(Modify according to your actual folder structure.)*

---

## Technologies

- Python 3
- JSON

---

## Future Improvements

This project is intentionally kept simple as a revision project. The next versions will include:

- PostgreSQL database integration
- ETL pipeline for importing bank statements (CSV/Excel)
- Data cleaning and transformation
- SQLAlchemy ORM
- Logging
- REST API using FastAPI
- Docker support
- Unit testing with Pytest
- Analytics and monthly spending reports
- Data visualization dashboard
- Export reports to CSV/PDF

---

## Learning Outcome

This project helped reinforce:

- Writing modular Python code
- Managing persistent data
- Implementing CRUD operations
- Working with collections and objects
- Designing a menu-driven CLI application

It also serves as a foundation for future backend and data engineering projects.

---

## Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project

```bash
cd expense-tracker
```

Run

```bash
python main.py
```

---

## Future Roadmap

- [x] JSON-based storage
- [x] PostgreSQL integration
- [ ] ETL pipeline
- [x] FastAPI backend
- [ ] Docker containerization
- [ ] Unit testing
- [ ] CI/CD
- [ ] Deployment

---

## License

This project is created for educational purposes and Python revision.
