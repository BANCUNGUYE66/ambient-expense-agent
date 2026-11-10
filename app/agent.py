from google.adk import Agent
from google.adk.apps import App

# Define your root agent
root_agent = Agent(
    name="ambient_expense_agent",
    model="gemini-3.5-flash-lite",
    instruction=(
        "You are an ambient expense tracking agent. "
        "Extract the amount, category, and vendor from expense claims, "
        "and route them for auto-approval if under $500 or human review if $500 and above."
    )
)

app = App(
    root_agent=root_agent,
    name="ambient_expense_agent"
)