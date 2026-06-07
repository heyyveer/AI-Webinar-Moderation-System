from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from process_message import process_message

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    try:

        while True:

            message = await websocket.receive_text()

            result = process_message(message)

            await websocket.send_json(result)

    except WebSocketDisconnect:

        print("Client disconnected")