# Hackathon Education Solutions

![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)  

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Folder Structure](#folder-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Technologies Used](#technologies-used)
7. [Contribution Guidelines](#contribution-guidelines)
9. [Contact Information](#contact-information)

---

## Project Overview

This repository includes three educational solutions developed during a hackathon:

1. **Machine Learning Prediction of Students Exam Scores**  
   A predictive model that estimates students' exam performance based on multiple factors, aiding educational stakeholders in optimizing student success.
   
2. **System for Data Collection**  
   An incomplete system designed to securely collect and store student data for schools.

3. **AI Examiner**  
   An AI-powered solution that generates unique exam questions based on study materials, providing students with immediate grading and feedback to improve their learning habits.

---

## Key Features

- **Machine Learning Prediction of Exam Scores**: A machine learning model that uses various student data points to predict the probability of passing or failing exams.
  
- **System for Data Collection**: Intended to store comprehensive student data securely, though this project is not yet complete.
  
- **AI Examiner**: A fully functional AI-based exam tool that generates questions and provides instant feedback. Built with Flask (backend) and HTML (frontend).

---

## Folder Structure

The repository contains three main projects, each with its own directory:

### 1. Machine Learning Prediction Of Students Exam Score

```bash
Machine_Learning_Prediction_Of_Students_Exam_Score/
│
├── /data_generation          # Code for generating the necessary datasets
│
├── /ETL                      # Extract, Transform, Load operations
│
├── test.ipynb                # Jupyter notebook with testing and evaluation
```

### 2. System for Data Collection
```bash
/student_performance_app
│
├── /app
│   ├── /static               # Frontend static files (e.g., CSS, JS)
│   ├── /templates            # HTML templates for the frontend
│   ├── /routes               # API routes for data handling
│   │   ├── students.py       # Route for student-related data
│   │   ├── parents.py        # Route for parent-related data
│   │   ├── academic.py       # Route for academic history data
│   ├── /models               # Database models (students, parents, etc.)
│   │   ├── students.py       # SQLAlchemy model for students
│   │   ├── parents.py        # SQLAlchemy model for parents
│   │   ├── academic_history.py  # SQLAlchemy model for academic history
│   ├── /utils                # Helper functions (e.g., ETL, data processing)
│   │   ├── etl.py            # Extract, Transform, Load functions
│   ├── /ml                   # Machine learning code
│   │   ├── train_model.py     # Code for training models
│   ├── init.py               # App initialization file
│   ├── config.py             # Configuration settings (e.g., DB connection)
│   ├── app.py                # Main application entry point
│
├── /env                      # Virtual environment folder (ignore in git)
│
├── requirements.txt          # List of required packages
├── .gitignore                # Ignore unnecessary files like /env
```

### 3. AI Examiner
```bash
AI_Examiner/
│
├── /templates                # HTML templates for the frontend
│
├── /static                   # CSS and JS files for the frontend
│
├── app.py                    # Main application file (Flask backend)
│
├── requirements.txt          # Required Python packages
├── .gitignore                # Ignore unnecessary files like /env
```
## Installation

### Prerequisites
You will need Python 3.x installed on your machine. For the **AI Examiner** project, you will also need an OpenAI API key.

### Steps to Install the AI Examiner

1. Clone the repository:

    ```bash
    git clone https://github.com/Onyeocha-Keside/DataFest-Africa-Hackathon-2024.git
    ```

2. Navigate to the `AI_Examiner` directory:

    ```bash
    cd AI_Examiner
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key in the environment variables:

    ```bash
    export OPENAI_API_KEY="your-api-key"
    ```

5. Run the application:

    ```bash
    python app.py
    ```

### Additional Project Setup

- For the **Machine Learning Prediction of Students Exam Scores**, navigate to the corresponding directory, install any required dependencies, and follow the instructions in the `test.ipynb` to run the model.

- For the **System for Data Collection**, note that the system is incomplete, but the initial code and structure for student, parent, and academic data handling can be explored.

---

## Usage

### AI Examiner

To use the AI Examiner:

1. Access the application via your web browser at `http://localhost:5000`.
2. Upload study materials or use existing data to generate exam questions.
3. Answer the questions, receive immediate feedback, and view the correct answers.

The project leverages OpenAI's GPT models to generate unique questions based on the provided content.

---

## Technologies Used

- **Python**: Core language for all three projects.
- **Flask**: Used in the backend of the AI Examiner.
- **HTML/CSS**: For the front-end interface of the AI Examiner.
- **SQLAlchemy**: Database modeling for the System for Data Collection.
- **OpenAI API**: For generating exam questions in the AI Examiner.
- **Machine Learning**: Applied in the Prediction of Students Exam Scores project using libraries such as `scikit-learn`.

---

## Contribution Guidelines

We welcome contributions from the open-source community! To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature-branch
    ```

3. Make your changes and commit them:

    ```bash
    git commit -m "Added a new feature"
    ```

4. Push to your branch:

    ```bash
    git push origin feature-branch
    ```

5. Submit a pull request.

---

## Contact Information

For any inquiries or feedback, feel free to reach out:

- **Email**: [onyeocha.keside@gmail.com](mailto:onyeocha.keside@gmail.com)
