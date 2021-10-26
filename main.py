from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)
userDataMap = defaultdict(lambda:list)

@app.route("/sendData", methods = ['POST'])
def addData():
    sentData = request.get_json(force=True)
    # sentData["1"].replace("\n", " ")
    for key in sentData.keys():
        userDataMap[key] = sentData[key]
    # print(sentData)
    # print(userDataMap)
    return sentData
'''
function to allo fetch of data
receives the client ID and tries to match it with the data
'''
@app.route("/fetchData", methods = ['POST'])
def returnData():
    userID = request.get_json(force=True)
    # if userDataMap:
    #     # for key, value in 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7001, debug=True)