import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://Waleed-Ansar:fastAPI%40waleed570@fastapi-cluster.0yfuiu4.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI-Cluster")

db = client['Store']
Stock = db['Stock']