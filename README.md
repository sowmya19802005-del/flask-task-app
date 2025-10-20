# Task Smash 2.0 - Flask Task Management App

A simple **Flask web application** to manage tasks. Users can **add, update, and delete tasks**. Built with Flask, SQLite, SQLAlchemy, and SCSS for styling.

---

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Tasks are saved in a SQLite database
* Clean UI with SCSS styling

---

## Screenshots

![Task List](screenshots/task_list.png)
![Update Task](screenshots/update_task.png)

> *Note: Add screenshots of your app here if possible.*

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/flask-task-app.git
cd flask-task-app
```

2. **Create and activate virtual environment**

```bash
python -m venv env      # create virtual environment
.\env\Scripts\activate  # Windows
# or on Mac/Linux: source env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python app.py
```

5. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Project Structure

```
MY_FLASK_APP/
│
├─ app.py                 # Main Flask application
├─ requirements.txt       # Python dependencies
├─ .gitignore             # Git ignore rules
├─ templates/             # HTML templates
│   ├─ base.html
│   ├─ index.html
│   └─ update.html
└─ static/
    └─ styles.css         # CSS/SCSS files
```

---

## Dependencies

* Flask
* Flask-SQLAlchemy
* Flask-SCSS
* SQLite3

---

## License

This project is licensed under the MIT License.

---

## Author
MOHITH VENKATESH
[GitHub Profile](https://github.com/your-username)
