from agent.react_agent import Agent
from .prompts import travel_plan_prompt
import re
import json
import asyncio

async def get_travel_plan(from_location, to_location, budget, duration, accommodation, transportation, activities):

    agent = Agent(react_prompt=travel_plan_prompt)

    prompt = (
        f"Create a detailed travel plan for a trip from **{from_location}** to **{to_location}**. "
        f"Please consider the following preferences and constraints:\n\n"
        f"**Duration**: {duration}\n"
        f"**Budget**: {budget}\n"
        f"**Accommodations**: {accommodation}\n"
        f"**Transportation**: {transportation}\n"
        f"**Activities**: {activities}\n\n"
    )
    plan = await asyncio.to_thread(agent, prompt)

    json_fence_pattern = r"```json(.*?)```"
    matches = re.findall(json_fence_pattern, plan, re.DOTALL)
    final_details = json.loads(matches[0])
    return final_details
