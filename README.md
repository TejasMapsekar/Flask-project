# Flask User Management Application

## Project Description
A Flask-based user management application with a MySQL database for storing user data, including CRUD operations and HTML templates for user interaction.

## Setup Instructions

### Prerequisites
- Python 3.x
- MySQL

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone <your_repository_url>
    cd <repository_name>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```bash
    pip install flask mysql-connector-python
    ```

5. **Set up the MySQL database**:
    ```sql
    CREATE DATABASE users;

    USE users;

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        role VARCHAR(255)
    );

    INSERT INTO users (name, email, role) VALUES
    ('John Doe', 'john@example.com', 'admin'),
    ('Jane Doe', 'jane@example.com', 'user');
    ```

6. **Run the Flask application**:
    ```bash
    python app.py
    ```

7. **Access the application**:
    - Open a web browser and go to `http://127.0.0.1:5000/hello` to see "Hello, World!".
    - Visit `http://127.0.0.1:5000/users` to see the list of users.
    - Visit `http://127.0.0.1:5000/new_user` to add a new user.

## Git Workflow

1. **Initialize a new Git repository**:
    ```bash
    git init
    ```

2. **Add all files to the staging area**:
    ```bash
    git add .
    ```

3. **Create the initial commit**:
    ```bash
    git commit -m "Initial commit"
    ```

4. **Create a new branch**:
    ```bash
    git branch flask_project
    ```

5. **Switch to the new branch**:
    ```bash
    git checkout flask_project
    ```

6. **Add the remote repository**:
    ```bash
    git remote add origin <your_repository_url>
    ```

7. **Push the new branch to the remote repository**:
    ```bash
    git push -u origin flask_project
    ```

8. **Create a pull request**:
    - Go to your Git hosting service (e.g., GitHub, GitLab).
    - Find the `flask_project` branch.
    - Create a pull request to the `main` branch.

## Dependencies

- Flask
- MySQL Connector for Python

## Database Schema

```sql
CREATE DATABASE users;

USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(255)
);

INSERT INTO users (name, email, role) VALUES
('John Doe', 'john@example.com', 'admin'),
('Jane Doe', 'jane@example.com', 'user');
