# AI Movie Critic - Sentiment Analysis

**Live Demo:**  https://movie-review-analyser.onrender.com

A full-stack machine learning web application that classifies English movie reviews as either positive or negative. The project includes a custom-trained Natural Language Processing model, a REST API, and a lightweight web interface.

## Overview

# AI Movie Critic - Sentiment Analysis

A full-stack machine learning web application that classifies English movie reviews as either positive or negative. The project includes a custom-trained Natural Language Processing model, a REST API, and a lightweight web interface.

## Overview

The core of this project is a Logistic Regression model trained on a dataset of movie reviews using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. The trained pipeline is serialized using Joblib and served through a FastAPI backend, allowing for real-time text analysis via a simple frontend or direct API calls.

## Tech Stack

* **Machine Learning:** Python, Scikit-Learn, Joblib
* **Backend:** FastAPI, Uvicorn, Pydantic
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Deployment:** Render

## Repository Structure

* `main.py`: The FastAPI application and endpoint definitions.
* `index.html`: The user interface and client-side logic.
* `sentiment_model.pkl`: The serialized Scikit-Learn model and TF-IDF vectorizer.
* `requirements.txt`: Python dependencies required to run the environment.

## Local Setup

1. Clone the repository:

```bash
git clone https://github.com/aidalada/movie-review-analyser.git
cd movie-review-analyser

```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate

```

3. Install the required dependencies:

```bash
pip install -r requirements.txt

```

4. Start the development server:

```bash
uvicorn main:app --reload

```

5. Open a web browser and navigate to `http://127.0.0.1:8000` to view the application.

## API Usage

The backend provides a `/predict` endpoint that accepts POST requests containing the review text.

**HTTP Request:**

```http
POST /predict
Content-Type: application/json

```

**Request Body:**

```json
{
    "text": "The cinematography was excellent and the plot kept me engaged until the very end."
}

```

**Response:**

```json
{
    "sentiment": "pos"
}

```

## Deployment Configuration

This project is configured for cloud deployment on platforms like Render.

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
