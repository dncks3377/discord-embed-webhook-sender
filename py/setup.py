import json, os, sys

print("Auto Webhook Send % Setup || Made by WhiteKJ#0001 || Copyright 2020. WhiteKJ. All right reserved.\n")
print("# 임베드 속성 설정 #\n중요: 해당 설정을 원치 않는다면 그냥 엔터만 쳐주세요.\n\n")
title = input("제목을 입력해주세요. : ")
description = input("설명을 입력해주세요. : ")
thumbnail = input("썸네일을 입력해주세요. : ")
footer = input("Footer를 입력해주세요. : ")
username = input("웹훅의 이름을 입력해주세요. : ")
msg = input("임베드와 같이 보낼 메세지를 입력해주세요. : ")
interval = input("보낼 주기를 입력해주세요. (기본단위: 초) : ")

if title == "" and description == "":
    print("제목 혹은 설명 중 하나는 입력되어야합니다.")
    sys.exit()
elif interval == "" or interval.isdigit() == False:   
    print("시간은 반드시 입력되어야하며, 숫자만 입력해야합니다.")
    sys.exit()
else:
    with open(f"{os.getcwd()}/../data/config.json", 'r', encoding="UTF8") as config:
        group = dict()
        embed = dict()
        send = dict()
        embed["title"] = title
        embed["description"] = description
        embed["thumbnail"] = thumbnail
        embed["footer"] = footer
        embed["username"] = username
        group["embed"] = embed

        send["msg"] = msg
        send["interval"] = interval
        group["send"] = send

        try:
            with open(f"{os.getcwd()}/../data/config.json", "w", encoding='UTF8') as make_file:
                json.dump(group, make_file, indent="\t")
                print("설정이 완료가 되었습니다.")
        except Exception as error:
            print(f"오류가 발생했습니다.\n\n{error}")
