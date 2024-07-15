from typing import TypedDict
from langgraph.graph import StateGraph, END, Graph
from langgraph.checkpoint import MemorySaver


class State(TypedDict):
    start: bool


def fn1(state: dict):
    state["fn1"] = "execute"
    return state

def fn2(state: dict):
    state["fn2"] = "execute"
    return state

def end(state: dict):
    return state

memory = MemorySaver()

workflow = Graph()
workflow.add_node("fn1", fn1)
workflow.add_node("fn2", fn2)
workflow.add_node("end", end)

workflow.add_edge("fn1", "fn2")
workflow.add_edge("fn2", "end")
workflow.set_entry_point("fn1")
chain = workflow.compile(checkpointer=memory)
thread = {"configurable" : {"thread_id": "2"}}

res = chain.invoke({"start": True}, thread, stream_mode="values")
    


print(chain.get_state(thread).values['end'])