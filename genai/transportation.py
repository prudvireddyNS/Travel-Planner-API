from agent.react_agent import Agent
from .prompts import transportation_prompt
import re
import json
import asyncio

# get transportation details
async def get_transportation(from_location, to_location, budget):

    agent = Agent(react_prompt=transportation_prompt)

    prompt = f"Find me transportation options from {from_location} to {to_location} with a {budget} budget."
    transportation = await asyncio.to_thread(agent, prompt)

    json_fence_pattern = r"```json(.*?)```"
    matches = re.findall(json_fence_pattern, transportation, re.DOTALL)
    final_details = json.loads(matches[0])
    return final_details
