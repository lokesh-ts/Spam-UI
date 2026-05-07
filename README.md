# Spam Classifier UI 

Interactive frontend UI for the Spam Classifier Machine Learning application built using Streamlit.

##  Overview

This project provides a user-friendly web interface for testing spam message predictions.
The frontend communicates with a deployed FastAPI backend hosted on Render.

---

## Tech Stack

* Python
* Streamlit
* Requests
* FastAPI Backend Integration

---

## Project Structure

```bash
Spam-UI/
│
├── app_ui.py
├── requirements.txt
└── README.md
```

---

## Features

* Interactive text input
* Real-time spam prediction
* API integration with FastAPI
* Cloud deployment using Streamlit Community Cloud
* Simple and clean UI

---

## Live Demo

Frontend App:
https://spam-ui-flj7wlziby2urjbg4sydyq.streamlit.app/

Backend API:
https://spam-classifier-api-3hos.onrender.com/docs

---

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit app

```bash
streamlit run app_ui.py
```

---

## Workflow

```text
User → Streamlit UI → FastAPI API → ML Model → Prediction
```

---

## Author

T S LOKESH
