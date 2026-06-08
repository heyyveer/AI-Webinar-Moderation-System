import asyncio
import websockets
import pandas as pd
import random
import json
print("Simulation Started")
DATASET_PATH = "dataset/webinar_moderation_nlp_dataset.csv"

async def simulate_attendee(message):

    async with websockets.connect(
        "ws://127.0.0.1:8000/ws"
    ) as ws:

        await ws.send(message)

        response = await ws.recv()

        result = json.loads(response)

        print(
            f"[USER] {message}"
        )

        print(
            f"[AI] {result['priority']} | "
            f"{result['cluster_name']} | "
            f"{result['users_affected']} users"
        )

        print("-" * 50)


async def main():

    df = pd.read_csv(DATASET_PATH)

    messages = df["message"].tolist()

    tasks = []

    for _ in range(50):

        msg = random.choice(messages)

        tasks.append(
            simulate_attendee(msg)
        )

    await asyncio.gather(*tasks)


asyncio.run(main())