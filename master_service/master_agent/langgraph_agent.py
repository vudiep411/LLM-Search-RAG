
from langgraph.graph import Graph, END
from .agents import PriceAgent, SearchAgent, FilterAgent, AnalysisAgent
from langgraph.checkpoint import MemorySaver
from concurrent.futures import ThreadPoolExecutor



class MasterAgent:
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.memory = MemorySaver()

    def check_ticker(self, state):
        return "search" if state.get("price", 0) > 0 else "end"

    def end(self, state: dict):
        return state

    def run(self):
        # Creating Agent
        price_agent = PriceAgent()
        search_agent = SearchAgent()
        filter_agent = FilterAgent()
        analysis_agent = AnalysisAgent()

        # Nodes
        workflow = Graph()
        workflow.add_node("price", price_agent.run)
        workflow.add_node("search", search_agent.run)
        workflow.add_node("filter", filter_agent.run)
        workflow.add_node("analysis", analysis_agent.run)
        workflow.add_node("end", self.end)
        
        # Edges
        workflow.add_conditional_edges(
            'price',
            self.check_ticker,
            {"search": "search", "end": "end"}
        )
        workflow.add_edge("search", "filter")
        workflow.add_edge("filter", "analysis")
        workflow.add_edge("analysis", "end")
        
        # Compile the graph
        workflow.set_entry_point("price")
        chain = workflow.compile(checkpointer=self.memory)

        # Run the graph
        thread = {"configurable" : {"thread_id": "2"}}
        chain.invoke({"ticker": self.ticker}, thread)

        return chain.get_state(thread).values["end"]