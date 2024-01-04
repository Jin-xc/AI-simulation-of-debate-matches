import os
import replicate
import datetime

os.environ["REPLICATE_API_TOKEN"] = "Your API-key"

# https://replicate.com/meta/llama-2-70b-chat
model_version = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"

# 读取背景
backgroundFile = open("background.txt", "r")
background = backgroundFile.read()
backgroundFile.close()

# log文件
logFile = open("log.txt", "r+")
logFile.seek(0)
# 清空文件内容
logFile.truncate()

# 老师提出辩题
current_time = datetime.datetime.now()
formatted_time = current_time.strftime(" --- %Y-%m-%d %H:%M:%S --- ")
logFile.write(formatted_time)
logFile.write("\nTeacher:")
for event in replicate.stream(
    model_version,
    input={
        "prompt": "Please come up with a debate topic and two aspects of the topic in short. Do not describe.",
        "system_prompt": background + "You are the teacher Ms.White. Today you are going to hold a debate for two student, you expect cultivate students' ability to think independently through this debate.",
        "max_new_tokens": 500,
    },
):
    print(str(event), end="")
    logFile.write(str(event))
logFile.write("\n")

# 学生辩论
for _ in range(5):
    # 学生1 Tony
    logFile.flush()
    logFile.seek(0)
    history = logFile.read()
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(" --- %Y-%m-%d %H:%M:%S --- ")
    logFile.write(formatted_time)
    logFile.write("\nStudent Tony:")
    for event in replicate.stream(
        model_version,
        input={
            "prompt": "Please debate, limited in two sentences. Do not repeat what you said.",
            "system_prompt": background + "History:" + history + "You are the student Tony. You are suppose to prove your argument and refute Jack's argument to win this debate.",
            "max_new_tokens": 500,
    },
        ):
        print(str(event), end="")
        logFile.write(str(event))
    logFile.write("\n")

    # 学生2 Jack
    logFile.flush()
    logFile.seek(0)
    history = logFile.read()
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(" --- %Y-%m-%d %H:%M:%S --- ")
    logFile.write(formatted_time)
    logFile.write("\nStudent Jack:")
    for event in replicate.stream(
        model_version,
        input={
            "prompt": "Please debate, limited in two sentences. Do not repeat what you said.",
            "system_prompt": background + "History:" + history + "You are the student Jack. You are suppose to prove your argument and refute Tony's argument to win this debate.",
            "max_new_tokens": 500,
    },
        ):
        print(str(event), end="")
        logFile.write(str(event))
    logFile.write("\n")

# 老师评分以及点评
logFile.flush()
logFile.seek(0)
history = logFile.read()
current_time = datetime.datetime.now()
formatted_time = current_time.strftime(" --- %Y-%m-%d %H:%M:%S --- ")
logFile.write(formatted_time)
logFile.write("\nTeacher:")
for event in replicate.stream(
    model_version,
    input={
        "prompt": "Please rating and feedback for each student.The score is 0-5 points.",
        "system_prompt": background + "History:" + history + "You are the teacher Ms.White. Today you are going to hold a debate for two student, you expect cultivate students' ability to think independently through this debate.",
        "max_new_tokens": 500,
    },
):
    print(str(event), end="")
    logFile.write(str(event))
logFile.write("\n")

logFile.flush()
logFile.close()
