# 尝试流式输出，成功！运行会给你一系列的url，是图片不断迭代的过程
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_NbU0PkakswVrdk9ZDtepXJwCcUfd47E04unFA"
import replicate

# text = open("text.txt", "rb")

iterator = replicate.run(
    "pixray/text2image:5c347a4bfa1d4523a58ae614c2194e15f2ae682b57e3797a5bb468920aa70ebf",
    input={"prompts": "robots talking to robots"},
)
for image in iterator:
    print(image)
