import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import loadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app() :
    """ 
    Loads and runs the LangGraph AgentiAI application with Streamlit UI. 
    This function initializes the UI, handles user input, configures the LLM model, 
    sets up the graph based on the selectedd use case, and displays the output while 
    implementing exceptions handling for robustness.
    """

    # load UI
    ui = loadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input :
        st.error("Error: Failed to load user input from the UI.")
        return 
    
    user_message = st.chat_input("enter your message: ")

    if user_message:
        try :
            # configure the LLMs
            obj_llm_config = GroqLLM(user_controls_input= user_input)
            model = obj_llm_config.get_llm_model()
            if not model :
                st.error("Error: LLM model could not be initialized.")
                return 
            
            # initialize and setup the graph based on use case 
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected.")
                return 
            
            # graph builder 
            graph_builder = GraphBuilder(model)
            try :
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e :
                st.error(f"Error: Graph setup failed- {e}")
                return 


        except Exception as e :
            st.error(f"Error: Graph setup failed- {e}")
            return 
        
        