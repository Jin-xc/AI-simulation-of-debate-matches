import os

os.environ["REPLICATE_API_TOKEN"] = "r8_NbU0PkakswVrdk9ZDtepXJwCcUfd47E04unFA"
import replicate
import datetime

model_version = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"

file = open("text.txt", "r")
text = file.read()
print(text)
file.close()
file = open("backup.txt", "w")

#output =
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("当前时间是：", formatted_time)
file.write(formatted_time)
file.write("--\n")

for event in replicate.stream(model_version, input={"prompt": text},):
    print(str(event), end="")
    file.write(str(event))

file.close()


#print(output)