# 📝 To-Do App (Flask + Docker)
A simple and clean to-do list web app built using Flask (Python), styled with CSS, and containerized using Docker for seamless deployment.

## 🔧 Features
- Add tasks with a clean UI
- Delete tasks instantly
- Responsive layout with modern styling
- Material Design icons for a polished look
- Fully Dockerized for consistent deployment

## 🚀 Getting Started
1. Clone the Repository  
git clone https://github.com/your-username/to-do_app.git  
cd to-do_app

2. Build the Docker Image  
docker build -t todo-flask-app .

3. Run the App in Docker  
docker run -d -p 5000:5000 todo-flask-app  
Visit http://localhost:5000 to use the app!

## 📁 Project Structure

to-do_app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── Dockerfile

## 📦 Tech Stack
- Python + Flask
- HTML + CSS
- Docker
- Google Material Icons