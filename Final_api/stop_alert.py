from fastapi import FastAPI, Request, Response
import json
import requests
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/end_point1")
async def end_point1(request: Request):

    try:
        body = await request.body()
        list_items = json.loads(body)
        values_list = list_items.split(',')
        for value in values_list:
            # header1 = {
            #     "Content-Type": "application/json",
            #     "Authorization": "Bearer a44f5d93-4f06-4d6f-873b-e96d7945e48f"
            # }
            # data = {
            #     "userId": str(item['id']),
            #     "eventName": "stop_alert_sent",
            #     "eventData": {}
            # }
            # response = requests.post('https://api.webengage.com/v1/accounts/~2024b707/events', headers=header1, json=data)

            print(value)
            # print(response)

        return {"message": "API is working successfully"}

    except Exception as ep1_exc:
        print("Exception: " + str(ep1_exc))



