# Student Management & Performance Analysis System

A Python and MySQL based application for managing student details, subjects, marks, and academic performance

## Technologies Used

 - Python
 - MySQL
 - SQL
 - MySQL Connector for Python
 - Git & GitHub

## Features

### Student Management

 - Add student
 - View students
 - Search student
 - Update student
 - Delete student

### Subject Management

 - Add subject
 - View subjects
 - Update subject
 - Delete subject

### Marks Management

 - Enter marks
 - View marks
 - Update marks
 - Delete marks

### Performance Analysis

 - Total marks
 - Average marks
 - Highest mark
 - Lowest mark
 - Pass / Fail result
 - Grade calculation

### Reports

 - Individual student report
 - Class performance report
 - Subject performance report
 - Top performers

## Database

The project uses MySQL with three main tables :
 - 'STUDENT'
 - 'SUBJECT'
 - 'MARK'
 
 The 'MARK' table uses foreign keys to connect students and subjects.

## Project Structure

'''text
Student-Management-System/
|
|---main.py
|---database.py
|---student.py
|---subject.py
|---marks.py
|---performance.py
|---report.py
|---validation.py
|---README.md