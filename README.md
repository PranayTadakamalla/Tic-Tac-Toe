# Tic-Tac-Toe
Using Django a simple Tic-Tac-Toe game

## Overview
Tic-Tac-Toe is a classic two-player game built with Django. The players take turns marking a space in a 3x3 grid, aiming to get three of their marks in a row—horizontally, vertically, or diagonally.

## Features
- Two-player gameplay
- Simple and interactive UI
- Responsive design

## Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
- Python 3.x
- Django

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PranayTadakamalla/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```

2. **Install Dependencies**
   It's a good idea to use a virtual environment. If you don't have `virtualenv`, you can install it using:
   ```bash
   pip install virtualenv
   ```
   Then create and activate a virtual environment:
   ```bash
   virtualenv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Required Packages**
   Install Django and other dependencies:
   ```bash
   pip install django
   ```

4. **Run Migrations**
   Prepare the database:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

6. **Access the Game**
   Open your web browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## How to Play
1. Players will alternate turns clicking on the grid to place their marks (X or O).
2. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) wins the game.
3. If the grid fills up and no player has three in a row, the game ends in a draw.

## License
This project is licensed under the MIT License.

## Author
Tadakamalla Sai Pranay


Github: https://github.com/PranayTadakamalla


Linkedin: https://in.linkedin.com/in/sai-pranay-tadakamalla-7570bb1a6
