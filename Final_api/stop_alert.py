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
        list_items = await request.json()
        

        for i in range(len(list_items)):
            header1 = {"Content-Type" :"application/json" ,
             "Authorization" : "Bearer a44f5d93-4f06-4d6f-873b-e96d7945e48f" 
                }
            data = data = {
                "userId":"00000186-178a-0e68-81bb-b61ea52a87cb",
                "eventName" : "stop_alert_sent",
                "eventData":
                {
                }
                }
            response = requests.post('https://api.webengage.com/v1/accounts/~2024b707/events' ,headers=header1,  json=data)
            # print(i)
            print(list_items[i]['id'])
            print(response)

        # id_list = []
        # for id in list_items:
        #     print(id)
        #     id_list.append(id)

        
        return {
            "message" : "api is working successfully"
        }

    except Exception as ep1_exc:
        print("Exception: " + str(ep1_exc))



