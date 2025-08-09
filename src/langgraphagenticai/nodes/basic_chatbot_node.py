from src.langgraphagenticai.state.state import State



class BasicChatbotNode :
    """
    Basic chatbot login implementation
    """

    def __init__(self,model):
        self.llm = model 

# this process fun is assistant functionality
# here process fun op is dic because typeddict 
    def process(self, state:State) -> dict :
        """
        Processes the input state and generates a chatbot responses.
        """
        return {"messages": self.llm.invoke(state["messages"])}
    

