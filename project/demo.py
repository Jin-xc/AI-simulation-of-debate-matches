import os

os.environ["REPLICATE_API_TOKEN"] = "r8_NFb3c9LbaN50TWS39OGIbcMxlNHwq6h4WDvvY"
# "r8_NFb3c9LbaN50TWS39OGIbcMxlNHwq6h4WDvvY"
# "r8_NbU0PkakswVrdk9ZDtepXJwCcUfd47E04unFA"
import replicate

# https://replicate.com/meta/llama-2-70b-chat
model_version = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"

for event in replicate.stream(
    model_version,
    input={
        "prompt": "Please come up with a debate topic and two aspects of the topic in short. Do not describe.",
        "system_prompt": "You are a teacher. Today you are going to hold a debate for two student, you expect cultivate students' ability to think independently through this debate.",
        "max_new_tokens": 500,
    },
):
    print(str(event), end="")