# English Learner - Quiz App

A full-stack web application designed to help users practice English grammar. The project features a **FastAPI** backend for question management and validation, paired with a responsive **Tailwind CSS** frontend that tracks user progress using local storage.

## 🚀 Features

- **Dynamic Quiz Loading**: Fetches questions and variants dynamically from the backend.
    
- **Progress Persistence**: Automatically saves your score, attempts, and completed questions to `localStorage`.
    
- **Intelligent Feedback**:
    
    - Highlights correct answers in green if guessed on the first try.
        
    - Highlights correct answers in blue if the "Reveal" feature was used.
        
- **Resume Functionality**: A "Resume" button that scrolls the user directly to their next unanswered question.
    
- **Score Tracking**: Tracks "First-try" accuracy versus "Errors" (multiple attempts).
    
- **Responsive Design**: Mobile-friendly UI built with Tailwind CSS.
    

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/ "null") (Python)
    
- **Frontend**: HTML5, JavaScript (ES6+), [Tailwind CSS](https://tailwindcss.com/ "null")
    
- **Containerization**: [Docker](https://www.docker.com/ "null") & Docker Compose
    
- **Data Handling**: Pydantic for request validation
    
- **State Management**: Browser LocalStorage
    

## 📂 Project Structure

```
.
├── main.py              # FastAPI Application & Endpoints
|── questions_provider.py # The questions themselves
├── index.html           # Frontend Application
├── core/                # Backend logic directory
│   ├── question.py      # Question class logic
├── Dockerfile           # Backend container definition
├── docker-compose.yml   # Multi-container orchestration (API: 8000, Web: 8080)
├── requirements.txt     # Python dependencies
├── .gitignore           # Python-specific git ignore file
└── README.md            # Project documentation
```

## ⚙️ Setup Instructions

### Option 1: Using Docker (Recommended)

Ensure you have Docker and Docker Compose installed.

1. **Build and start the containers**:
    
    ```
    docker-compose up --build
    ```
    
2. **Access the App**:
    
    - **Frontend**: [http://localhost:8080](http://localhost:8080)
        
    - **Backend API**: [http://localhost:8000](http://localhost:8000 "null")
        

### Option 2: Local Manual Setup

1. **Navigate to the project directory** and create a virtual environment:
    
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    
2. **Install dependencies**:
    
    ```
    pip install -r requirements.txt
    ```
    
3. **Run the server**:
    
    ```
    uvicorn main:app --reload
    ```
    
4. **Open the frontend**: Simply open `index.html` in your browser or serve it via a local static server on port 8080.
    

## 📡 API Endpoints

### `GET /questions`

Retrieves the list of grammar questions.

### `POST /validate`

Validates a user's selection based on `question_index` and `selected_index`.

## 🛡️ License

Distributed under the MIT License.