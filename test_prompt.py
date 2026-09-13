import os
from dotenv import load_dotenv
import anthropic
from schema_utils import get_schema_description
from prompts import SYSTEM_PROMPT_TEMPLATE

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

schema = get_schema_description()
system_prompt = SYSTEM_PROMPT_TEMPLATE.format(schema=schema)

question = "What is the average discount by category?"

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    system=system_prompt,
    messages=[
        {"role": "user", "content": question}
    ]
)

print("Question:", question)
print("Generated SQL:")
print(response.content[0].text)