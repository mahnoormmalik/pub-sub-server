from flask import Flask, request, jsonify
from collections import defaultdict
import numpy as np
import sys

app = Flask(__name__)
userDataMap = defaultdict(lambda:list)

THRESHOLD = 30

@app.route("/sendData", methods = ['POST'])
def addData():
    sentData = request.get_json(force=True)
    # sentData["1"].replace("\n", " ")
    for key in sentData.keys():
        userDataMap[key] = sentData[key]
    return sentData

'''
function to allow fetch of data

This function computes a similarity measure (Dot Product) between the received userID 
and all the existing Data+ID enteries in the userDataMap
'''

@app.route("/fetchData", methods = ['POST'])
def returnData():
    clientID = request.get_json(force=True)
    maxRes = - sys.maxsize - 1
    mostMatchedData = None
    if userDataMap:
        for key, data in userDataMap.items():
            res = abs(np.dot(clientID["ID"], data))
            if res>maxRes:
                maxRes = res
                mostMatchedData = data
            print(res)

    if mostMatchedData and maxRes > THRESHOLD:
        return {"data": mostMatchedData}
    return {"data": None}
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7001, debug=True)