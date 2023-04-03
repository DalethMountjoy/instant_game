import json

with open("results.json", "r") as f:
    data = json.load(f)

setting = data["setting"]
plot = data["plot"]

print("Setting: ", setting["Your setting"])
print("Setting tone: ", setting["Setting tone"])

print("Opposition: ", plot["Here is your main opposition"])
print("Prompt 1:", plot["Here are some prompts"])