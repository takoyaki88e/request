import requests

num = 1
url = "https://manage.digitalartscloud.com/command"  #アクセスするリンクを---に挿入
AccessTime = 99999999999999999999999999999999999999999999    #連続してアクセスする回数を指定
print("AccessURL-->"+str(url))

while num <= AccessTime:

    response = requests.get(url)

    if response.status_code == 200:
        print(str(num)+"th-success. request-success <" +
              str(response.status_code)+">")
    else:
        print(str(num)+"th-success. request-failure" "<" +
              str(response.status_code)+">")

    num += 1

print("Complete.")
