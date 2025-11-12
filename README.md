# 🎬 Movie Recommendation System  

An intelligent **content-based movie recommendation system** built using **Python, Flask, and machine learning**.  
Users can input any movie title, and the system suggests **five similar movies** based on content similarity (genres, cast, overview, etc.), along with movie posters fetched from **The Movie Database (TMDb) API**.

---

## 🚀 Features  

**Content-based recommendation** using similarity scores  
**Dynamic web UI** built with HTML, CSS, and pure JavaScript  
 **REST API backend** served with Flask  
 **Poster integration** via TMDb API  
 **Cloud-ready structure** for deployment (Render, Vercel, etc.)  

---

## 🧠 Tech Stack  

| Layer | Technology |
|--------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Flask (Python) |
| **Machine Learning** | scikit-learn, pandas, pickle |
| **API** | TMDb API (for movie posters) |
| **Deployment** | Render (Cloud Hosting) |

---



---

## ⚙️ Setup & Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/LaiTechTinker/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create a virtual environment  
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file  

In the root directory, add your **TMDb API access token**:

```
API_KEY=your_api_key_here
IMDB_ACCESS_TOKEN=your_access_token_here
```

You can generate this token by creating an account on [The Movie Database](https://www.themoviedb.org/).

### 5️⃣ Run the Flask server  
```bash
python demo.py
```

Your app will be live on  
👉 **http://localhost:5000/**  

---

## 🧩 How It Works  

1. The ML model was trained on a dataset of movies (titles, genres, cast, overview).  
2. A **similarity matrix** was generated and saved as `similarity.pkl`.  
3. When a user inputs a movie name:
   - Flask fetches the top 5 most similar movies.
   - The TMDb API fetches posters for each movie.
   - The results are displayed beautifully on the frontend.

---

## 🧠 Example Workflow  

1. Type: **“Inception”**  
2. Click **“Get Recommendations”**  
3. Output:  
   - Interstellar  
   - The Matrix  
   - Shutter Island  
   - The Prestige  
   - Source Code  

Each with poster images shown below the input box.

---

## 🛠️ API Endpoint  

### **POST** `/recommend`  

**Request Body**
```json
{
  "name": "Inception"
}
```

**Response**
```json
{
  "status": "success",
  "output": ["Interstellar", "The Matrix", "Shutter Island", "The Prestige", "Source Code"],
  "ids": [1234, 5678, 9101, 1121, 3141],
  "poster": ["url1", "url2", "url3", "url4", "url5"],
  "movieposter": "url_main_movie"
}
```

---

## ☁️ Deployment on Render  

Render makes deploying Flask apps super easy.

1. Push your project to GitHub  
2. Add a file named **`render.yaml`** in the root directory:  

```yaml
services:
  - type: web
    name: movie-recommender
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: python demo.py
    envVars:
      - key: FLASK_ENV
        value: production
```

<!-- 3. Go to [Render.com](https://render.com), connect your GitHub repo, and deploy 🚀   -->

---

## 🖼️ UI Preview  

**Home Page**  
```
🎬 Movie Recommendation System
Enter a movie name to get 5 similar movie suggestions.
[Input Box] [Get Recommendations]
```

**Output Section**  
Shows main movie poster and recommended movie cards below it in a grid layout.

---

## 👨‍💻 Author  

**Laitech**  
🔗 [GitHub](https://github.com/LaiTechTinker)  
💬 Passionate about Data Science, Machine Learning, and Intelligent Systems.  

---

## ⭐ Support  

If you find this project useful, consider giving it a ⭐ on GitHub!  
It helps others discover it and motivates continued improvement.  
