
# Content-Based Recommendation System (MLOps-Oriented Project)

## Project Overview
This project is an end-to-end implementation of a **content-based movie recommendation system** with a strong focus on the **MLOps lifecycle**. The system recommends movies to users based on the similarity of movie content such as genres, overview, keywords, and other descriptive metadata.

The project demonstrates how a machine learning solution evolves from raw data collection and notebook experimentation to a modular, production-ready pipeline.

---

## Project Objectives
- Build a content-based recommendation system using movie metadata.
- Apply core machine learning and data engineering concepts.
- Follow an end-to-end MLOps lifecycle.
- Write clean, modular, and reusable code.
- Prepare the project for deployment and future scalability.

---

## MLOps Lifecycle Implementation

### 1. Data Collection
The dataset used for this project is the **IMDB Movie Dataset**, downloaded from Kaggle.

Dataset source:
https://kaggle.com/IMDBDataset

The dataset contains information such as:
- Movie titles
- Genres
- Movie overview/description
- Keywords
- Popularity and ratings

---

### 2. Notebook Experimentation
Before writing production-level code, experiments were conducted in Jupyter notebooks to understand the data and validate modeling choices.

Key experiments include:

#### a. Exploratory Data Analysis (EDA)
- Understanding dataset structure and size
- Identifying important features for recommendations
- Checking data distribution and feature relevance

#### b. Data Cleaning
- Handling missing values in critical columns
- Removing duplicates
- Standardizing text-based features

#### c. Feature Engineering and Vector Embedding Creation
- Combining relevant textual features into a single representation
- Text preprocessing (lowercasing, tokenization, stopword removal)
- Vectorization using techniques such as TF-IDF or Count Vectorizer
- Creating numerical embeddings suitable for similarity computation

---

### 3. Model Building
A **content-based filtering approach** was implemented:

- Movie similarity is computed using cosine similarity
- Recommendations are generated based on similarity scores
- The system returns top-N similar movies for a given input movie

---

### 4. Modular Code Development
After notebook validation, the project was refactored into modular Python scripts:
- Data ingestion module
- Data transformation module
-  Data validation module
- embedding creation  module
- Pipeline creation
- embedding pusher module
- Utility and helper functions

This improves:
- Maintainability
- Reusability
- Testability

---

### 5. Pipeline Design
A structured pipeline was designed to ensure:
- Clear separation of concerns
- Easy retraining and updates
- Smooth integration with deployment workflows

---

### 6. Version Control
- Git is used for tracking changes


---

### 7. Deployment Readiness
The project structure is designed to support:
- API integration ( Flask)
- CI/CD integration
- AWS model registry
- Cloud deployment in future iterations

---

## Project Structure
```
Recommendation
│__artifacts
|__config
|__flowchart
|__Logs
|__UI
|Recommendation_system/
│   ├── component/
|      data ingestion.py,datavalidation.py,model_training.py,prediction.py
│   ├── cloud storage/
|        awsstrorage
│
├── entity/
│   ├── config entity.py
│   ├── artifact entity.py
│__logger
|__notebooks
|__pipeline
|__utils  
│__excecption
├── requirements.txt
├── README.md
└── main.py
|___setup.py
|___create_files.py
```

---

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Jupyter Notebook
- Git
-mongodb
* check requirements.txt

---

## How to Run the Project
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run `demo.py` to start pipelin
4. Use the notebook files for experimentation and understanding

---

## Future Improvements
- Add collaborative filtering
- Hybrid recommendation system
- Model monitoring and logging
- API-based deployment
- User feedback loop
- Integration with cloud services

---

## Author
Ibrahim Olayiwola
