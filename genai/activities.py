from agent.react_agent import Agent
from .prompts import activities_prompt
import re
import json

# get transportation details
def get_activities(location, duration):

    agent = Agent(react_prompt=activities_prompt)

    prompt = f"Find me all activities and attractions available in {location} for a {duration} trip."
    activities = agent(prompt)

    json_fence_pattern = r"```json(.*?)```"
    matches = re.findall(json_fence_pattern, activities, re.DOTALL)
    final_details = json.loads(matches[0])
    return final_details