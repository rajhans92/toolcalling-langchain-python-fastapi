from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messgaeables import HumanMessage
from app.agents.tools import get_weather, get_aqi, get_cost_of_living


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def toolCallingAi(question: str) -> str:
    try:
        tools = [get_weather, get_aqi, get_cost_of_living]

        agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt="You are a city information assistant."
        )

        result = agent.invoke({"messages": [HumanMessage(content=question)]})

        print(result["messages"][-1].content)

        return result["messages"][-1].content
    except Exception as e:
        raise Exception(f"Error in toolCallingAi: {str(e)}") from e