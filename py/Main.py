try:
    import json, os
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from time import sleep

    print("Auto Webhook Send || Made by WhiteKJ#0001 || Copyright 2020. WhiteKJ. All right reserved.\n")
    with open(f"{os.getcwd()}/../data/config.json", 'r', encoding="UTF8") as config:
        json_data = json.load(config)
        value = json_data
        i = 0
        while True:
            f = open("../webhook/list.txt", "r")
            line = f.readlines()
            result = []
            for item in line:
                temp_item = item.replace("\n", "")
                result.append(temp_item)
            
            webhook = DiscordWebhook(url=result, content=value["send"]["msg"], username=value["embed"]["username"])
            embed = DiscordEmbed(title=value["embed"]["title"], description=value["embed"]["description"])#, color=value["embed"]["color"]
            embed.set_thumbnail(url=value["embed"]["thumbnail"])
            embed.set_author(username=value["embed"]["username"])
            embed.set_footer(text=value["embed"]["footer"]+"\nAuto Webhook Sender - Made by WhiteKJ#0001")
            embed.set_timestamp()
            webhook.add_embed(embed)

            i += 1
            response = webhook.execute()
            print(f"현재 전송 횟수 : {i}")
            sleep(int(value["send"]["interval"]))
except ImportError as error:
    print("json, sys, DiscordWebhook, 이 셋중 한가지 모듈이 설치되어있지 않습니다.\n\npy -m pip install <모듈명> 을 입력하여 설치할 수 있습니다.\n오류 : {}".format(error))