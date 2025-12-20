import os
from Recommendation_system.pipline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()
# from Recommendation_system.components.Prediction import app
# server.py


# if __name__ == "__main__":
#     app.run(debug=True)

# # file_path=r"Recommendation_system\notebooks\similarity.pkl"
# # obj=Prediction(filepath=file_path)
# # obj.get_input()
