# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

import whisper

def download_model():
    #medium, large-v1, large-v2
    model_name = "large"
    model = whisper.load_model(model_name)

if __name__ == "__main__":
    download_model()