from potassium import Potassium, Request, Response

import whisper

app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    #medium, large-v1, large-v2
    model_name = "large-v2"
    model = whisper.load_model(model_name)   
    context = {
        "model": model
    }

    return context

# @app.handler runs for every call
@app.handler()
def handler(context: dict, request: Request) -> Response:
    mp3BytesString = request.json.get("mp3BytesString")
    model = context.get("model")

    # download the audio file from mp3 string
    mp3Bytes = BytesIO(base64.b64decode(mp3BytesString.encode("ISO-8859-1")))
    with open('input.mp3','wb') as file:
        file.write(mp3Bytes.getbuffer())
    
    # Run the model
    result = model.transcribe("input.mp3")
    output = result["text"]


    return Response(
        json = {"text": output}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()