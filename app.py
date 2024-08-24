import fastapi
from transformers import pipeline
from pydantic import BaseModel

# Initialize the classifier pipeline
classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion')

# Initialize FastAPI
app = fastapi.FastAPI()

# Define the input data model
class Input(BaseModel):
    input_text: str

# Define the prediction endpoint
@app.post("/predict")
async def predict(input: Input):
    # Get predictions from the classifier
    predictions = classifier(input.input_text)
    
    # Extract the label with the highest score
    # highest_score = max(predictions[0], key=lambda x: x['score'])
    emotion = predictions[0]['label']
    
    # Return the prediction as a list (per your requirement)
    return {'prediction': [emotion]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='localhost', port=4098)
