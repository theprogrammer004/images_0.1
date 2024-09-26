from fastapi import FastAPI, WebSocket
import os

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()  # Receiving image as bytes
        # Here you can save the received image to a file if needed
        with open("received_image.jpg", "wb") as file:
            file.write(data)
        # You can send a confirmation message back to the client
        await websocket.send_text("Image received")
