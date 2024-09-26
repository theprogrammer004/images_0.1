from fastapi import FastAPI, WebSocket
import os

app = FastAPI()

# WebSocket endpoint for receiving and forwarding images
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connection established.")
    
    try:
        while True:
            # Receive image as bytes
            data = await websocket.receive_bytes()
            image_size = len(data)  # Calculate image size in bytes
            
            # Save the received image to a file (optional)
            with open("received_image.jpg", "wb") as file:
                file.write(data)
            print(f"Image received ({image_size} bytes).")
            
            # Acknowledge receipt of the image and send its size back to the client
            await websocket.send_text(f"Image received. Size: {image_size} bytes")
    except Exception as e:
        print(f"Connection closed with error: {e}")
    finally:
        print("WebSocket connection closed.")
