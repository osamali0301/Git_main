from fastapi import FastAPI, Request, Response
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/end_point1")
async def end_point1(request: Request):
    try:
        list_items = await request.json()
        

        for i in range(len(list_items)):
            # print(i)
            print(list_items[i]['id'])

        # id_list = []
        # for id in list_items:
        #     print(id)
        #     id_list.append(id)

        
        return {
            "message" : "api is working successfully"
        }

    except Exception as ep1_exc:
        print("Exception: " + str(ep1_exc))



