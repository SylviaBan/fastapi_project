# 1. Library imports
import uvicorn
from fastapi import FastAPI
from typing import Optional
from joblib import load
from Tweets import Tweet

vector = load("vectors")
model = load("model")

# 2. Create the app object
app = FastAPI()


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Bienvenue dans l\'application < Détecter le Bad Buzz > (P7) !'}


# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Tweet

@app.post('/prediction')
def get_prediction(data:Tweet):
    text = [data.review]

    vec = vector.transform(text)
    prediction = model.predict(vec)
    prediction = int(prediction)
    if(prediction > 0 ):
        prediction="The sentiment is positive :-)"
    else:
        prediction="The sentiment is negative :-("
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


#uvicorn app:app --reload