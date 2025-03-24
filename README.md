# AgentToolBuilder

`AgentToolBuilder` is a lightweight Python utility for dynamically building tool configurations for AI agents (e.g., OpenAI function calling, LangChain tools, OpenAPI schemas). It allows you to add properties on the fly, define types, descriptions, and enums, and output a clean JSON schema.

## Features

- Add properties with type, description, and optional enum
- Generate dynamic tool configuration
- Optional JSON output
- Chainable property definition
- Easily integrable with OpenAI function tools and similar

# Project Structure
```bash
agent_tool_builder/
├── agent_tool_builder.py
├── README.md
├── LICENSE
├── .gitignore
```

# Usage
```bash
from agent_tool_builder import AgentToolBuilder

tool = AgentToolBuilder(
    tool_type="function",
    tool_name="get_gold_price",
    tool_description="Get the actual gold price from the Polish National Bank"
)

tool.add_new_property("price", "string", "The current gold price")
tool.add_new_property("weight", "integer", "Gold weight in grams", prop_enum=[1, 5, 10, 50])

print(tool.build(return_json=True))
```

# Output
```json
{
  "type": "function",
  "name": "get_gold_price",
  "description": "Get the actual gold price from the Polish National Bank",
  "parameters": {
    "type": "object",
    "properties": {
      "price": {
        "type": "string",
        "description": "The current gold price"
      },
      "weight": {
        "type": "integer",
        "description": "Gold weight in grams",
        "enum": [1, 5, 10, 50]
      }
    },
    "required": ["price", "weight"]
  }
}
```

# Author
Made with ❤️ by Michał Kamiński

# License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as you wish.