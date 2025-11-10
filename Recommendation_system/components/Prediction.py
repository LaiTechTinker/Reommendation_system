from Recommendation_system.exception import RecomException
from Recommendation_system.logger import logging
import pickle
import sys
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from Recommendation_system.utils.main_utils import read_csv
from pathlib import Path
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")
ACCESS_TOKEN=os.getenv("IMDB_ACCESS_TOKEN")

app = Flask(__name__)
CORS(app)

pickle_path = r"Recommendation_system\notebooks\similarity.pkl"

class Prediction:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.fame_path = Path("artifacts/11_08_2025_21_39_04/Data_transformation/transformed_train.csv")

    def load_pickle(self):
        try:
            logging.info("Entered the pickle loading function")
            with open(self.filepath, "rb") as f:
                model = pickle.load(f)
            return model
        except Exception as e:
            raise RecomException(e, sys)
    def get_movie_poster(self, title):
    
     try:
        url = "https://api.themoviedb.org/3/search/movie"
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "accept": "application/json"
        }
        params = {"query": title}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results")
            if results:
                poster_path = results[0].get("poster_path")
                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500{poster_path}"
     except Exception as e:
        print(f"Poster fetch error for {title}: {e}")
     return None


    def Recommend_func(self, moviename):
        try:
            model = self.load_pickle()
            df = read_csv(file_path=self.fame_path)

            if moviename not in df["title"].values:
                print("Movie name not found in dataframe. enter another value")
                return None

            movie_index = df[df["title"] == moviename].index[0]
            distances = model[movie_index]
            output = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            title_list = [df.iloc[i[0]]["title"] for i in output]
            movie_id = [df.iloc[i[0]]["id"] for i in output]
            movieposter=self.get_movie_poster(moviename)
            poster_url=[self.get_movie_poster(name) for name in title_list]


            return title_list, movie_id,poster_url,movieposter
        except Exception as e:
            raise RecomException(e, sys)


@app.route("/recommend", methods=["POST"])
def Recom():
    try:
        data = request.get_json()
        moviename = data.get("name")
        obj = Prediction(filepath=pickle_path)

        if not moviename:
            return jsonify({
                "status": "fail",
                "message": "no input received"
            }), 400

        result = obj.Recommend_func(moviename)
        if not result:
            return jsonify({
                "status": "fail",
                "message": "movie not found"
            }), 404

        recommended_names, movie_ids,poster,movieposter = result
        return jsonify({
            "status": "success",
            "output": recommended_names,
            "ids": [int(i) for i in movie_ids],# Convert np.int64 → int
            "poster":poster,
            "movieposter":movieposter 
        }), 200

    except Exception as e:
        return jsonify({
            "status": "fail",
            "message": str(e)
        }), 400
