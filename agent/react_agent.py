from typing import Any
import openai
from .react_prompt import react_prompt as rp
from vyzeai.tools.base_tool import handle_tool_calls
import json
import re
import os

class Agent:
    def __init__(self, api_key=None, model_name = 'gpt-4o-mini', tools=None, max_iterations=25, react_prompt=None ) -> None:

        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        
        if not self.api_key:
            raise ValueError("API key must be provided either via argument or 'OPENAI_API_KEY' environment variable.")
        
        self.model_name = model_name
        self.tools = tools
        self.max_iterations = max_iterations
        self.messages = []

        if react_prompt:
            self.react_prompt = react_prompt
        else:
            self.react_prompt = rp

        self._update_system_message(self.react_prompt)

    def __call__(self, prompt) -> Any:
        response = self._execute(prompt)
        return response

    def _execute(self, prompt):

        i = 0
        self._add_user_query(prompt)

        while i<self.max_iterations:
            i += 1

            response = self._run_gpt()
            self._add_response(response)

            last_message = self.messages[-1]['content']
            print(last_message)

            if '**Answer**:' in last_message:
                return self.messages[-1]['content']
            
    def _run_gpt(self):
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            tools= self.tools,
        )
        # print(response.choices[0].message.content)

        return response

    def _update_system_message(self, content):
        if self.messages and self.messages[0]['role'] == 'system':
            self.messages[0]['content'] = content
        else:
            self.messages.insert(0, {'role': 'system', 'content': content})

    def _add_response(self, response):
        parsed_responses = self._parse_response(response)

        for parsed_response in parsed_responses:

            if parsed_response['finish_reason'] == 'stop':
                self._add_llm_response(parsed_response['content'])
            
            if parsed_response['finish_reason'] == 'tool_calls':
                tool_outputs = handle_tool_calls(response)
                contents = [{'function_name': tool_call.function.name, 'arguments':tool_call.function.arguments, 'output': json.dumps(tool_outputs[i])} for i, tool_call in enumerate(parsed_response['tool_calls'])]
                tool_call_ids = [tool_call.id for tool_call in parsed_response['tool_calls']]
                self.messages.append(response.choices[0].message)
                for i, id in enumerate(tool_call_ids):                    
                    self._add_tool_output(json.dumps(contents[i]), id)

    def _add_user_query(self, query):
        self.messages.append({'role': 'user', 'content': query})

    def _add_llm_response(self, response):
        self.messages.append({'role': 'assistant', 'content': response})

    def _add_tool_output(self, tool_output, id):
        self.messages.append({'role': 'tool', 'content': tool_output, 'tool_call_id':id})

    def _parse_response(self, response):
        return [
            {
                'finish_reason': choice.finish_reason,
                'role': choice.message.role,
                'content': choice.message.content,
                'function_call': choice.message.function_call,
                'tool_calls': choice.message.tool_calls,
                'refusal': choice.message.refusal
            }
            for choice in response.choices
        ]
    

                