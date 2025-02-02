# Database Analysis and Visualization through Natural Language

## Overview

This project is a web application that enables users to query a SQL database using natural language. The AI-powered system translates user commands into SQL queries, retrieves the relevant data, and automatically generates visualizations to present the results. The user only sees the SQL output and the corresponding graph, making it easy for non-technical users to analyze data without needing SQL expertise.

This project was developed on 2025-02-01 for the CONUHACKS IX hackathon at Concordia University.

## Setting up

Follow these steps to set up and run the application.  

#### **1. Clone the Repository**  
```bash
git clone https://github.com/MaherDissem/Text2SQL
cd Text2SQL  
```

#### **2. Get Dependencies**
```
cd frontend/  
npm install  
cd chatbot-frontend/  
npm install

cd ../..
pip install -r requirements.txt  
```

#### **3. Set parameters**
First, set the OpenAI API key: `export OPENAI_API_KEY="YOUR-API-KEY`.

Default webapp parameters, API parameters and prompts can be changed in `backend/config.py`.

#### **4. Start the App**
```
npm start  
python backend/main.py  
```

**Note:** For the purpose of the demo we use `backend/db_generator.py`, to generate dummy data.

## Demo
[Click to view the demo video.](video.mp4)
