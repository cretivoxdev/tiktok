from TikTokAPI import TikTokAPI
import requests
import re
import pandas as pd
from flask import Flask, request, jsonify, render_template


#from utils import load_json
import json
import pprint
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378'}
jsn = json.load(open("cookie.json", "r", encoding="utf-8"))
api = TikTokAPI(jsn)
counttiktok = pd.DataFrame(columns = ['Likes', 'Comment', 'Share'])

flask_app = Flask(__name__)

def truncate(num):
    return re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(num))

# @flask_app.route("/")
# def Home():
#     return render_template('index.html')


@flask_app.route("/", methods=["POST", "GET"])
def analyst():

    ## scrap data from tiktok
    #retval = api.getUserByName(user_name="cretivox")
    #user = retval['userInfo']
    # param = {
    #         "type": 1,
    #         "secUid": "",
    #         "id": user['user']['id'],
    #         "count": int(retval['userInfo']['stats']['videoCount']),
    #         "minCursor": 0,
    #         "maxCursor": 0,
    #         "shareUid": "",
    #         "lang": "",
    #         "verifyFp": "",
    #         }
    # url = 'https://www.tiktok.com/node/video/feed'
    #data = requests.get(url, params=param, headers=headers)
    #data = data.json()
    #filename = 'user.json'
    #with open(filename, 'w') as file_object:  #open the file in write mode
    #        json.dump(data, file_object)

    #DIGCOUNT = LIKES
    #COMMENTCOUNT = COMMENT
    #SHARECOUNT = SHARE
    #PLAYCOUNT = VIEWS

    print("===================================== Analytics Account Start =====================================")
    # pprint.pprint(retval, width = 1)
    file = open('user.json')
    dataTik = json.load(file)
    Like, Comment, Share, Views = [], [], [], []
    countdata = len(dataTik['body']['itemListData'])

    for i in range(28):
            Like.append(dataTik['body']['itemListData'][i]['itemInfos']['diggCount'])
            Comment.append(dataTik['body']['itemListData'][i]['itemInfos']['commentCount'])
            Share.append(dataTik['body']['itemListData'][i]['itemInfos']['shareCount'])
            Views.append(dataTik['body']['itemListData'][i]['itemInfos']['playCount'])
            #pprint.pprint(dataTik['body']['itemListData'][i]['itemInfos']['diggCount'], width = 1)


    # 100 videos
    print("Analytics for last " + str(i+1) + " videos")
    print("Like : " + str(sum(Like)))
    print("Comment : " + str(sum(Comment)))
    print("Share : " + str(sum(Share)))
    print("Views : " + str(sum(Views)))
    print("Followers : " + str(dataTik['body']['itemListData'][0]['authorStats']['followerCount']))
    print("Total Post : " + str(dataTik['body']['itemListData'][0]['authorStats']['videoCount']))
    print("evg Likes : " + str(truncate(sum(Views)/dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%")
    print("evg Comment : " + str(truncate(sum(Comment)/dataTik['body']['itemListData'][0]['authorStats']['videoCount']))+ "%")

    evglike = str(truncate(sum(Views)/dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%"
    evgCom = str(truncate(sum(Comment)/dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%"
    engfol = (sum(Like) + sum(Comment) + sum(Share))/dataTik['body']['itemListData'][0]['authorStats']['followerCount']
    engview = (sum(Like) + sum(Comment) + sum(Share))/sum(Views)

    print("engfol : " + str(truncate(engfol))+ "%" + " engview : " + str(truncate(engview))+ "%")
    #print(dataTik['body']['itemListData'][0]['authorStats']['followerCount'])
    #pprint.pprint(dataTik, width = 1)

    #output comment, share
    # pprint.pprint(retval['itemInfo']['itemStruct']['stats'], width = 1)

    #print(retval['itemInfo']['itemStruct'])
    # print(retval.get("items"))
    print("===================================== Analytics Account Finish =====================================")
    # print(retval2)

    return render_template('index.html',
                           engfol = str(truncate(engfol))+ "%",
                           engview = str(truncate(engview)) + "%",
                           like = evglike,
                           comment = evgCom)

if __name__ == "__main__":
    flask_app.run(debug=True)
