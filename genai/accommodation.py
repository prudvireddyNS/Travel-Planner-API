from agent.react_agent import Agent
from .prompts import accommodation_prompt
import re
import json
import asyncio

# get accomodation details
async def get_accommodation(location, budget, duration):

    agent = Agent(react_prompt=accommodation_prompt)
    
    prompt = f"Find me accommodation options in {location} within a {budget} budget for a duration of {duration}."
    accommodation = await asyncio.to_thread(agent, prompt)

    json_fence_pattern = r"```json(.*?)```"
    matches = re.findall(json_fence_pattern, accommodation, re.DOTALL)
    final_details = json.loads(matches[0])
    return final_details

