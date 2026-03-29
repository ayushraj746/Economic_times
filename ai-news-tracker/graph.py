from typing import TypedDict, Dict, Any, List
from langgraph.graph import StateGraph
from agents import main_agent


# unified state (supports both single + evolution modes)
class State(TypedDict, total=False):
    input_text: str            # single article
    input_texts: List[str]     # multiple updates (story evolution)
    perspective: str           # user perspective
    output: Dict[str, Any]     # final structured output


# create graph
builder = StateGraph(State)

# single node (main agent handles everything)
builder.add_node("main", main_agent)

# set entry point
builder.set_entry_point("main")

# compile graph
graph = builder.compile()