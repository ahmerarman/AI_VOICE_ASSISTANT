import enum
import logging
from typing import Annotated
from livekit.agents import llm
import requests # type: ignore

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)
MAX_QUERY_LENGTH = 100  # Limit query length to 100 characters

class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

class AssistantFunc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()
        
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }
    
    @llm.ai_callable(description="get the temperature in a specific room")
    def get_temperature(self, zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")]):
        logger.info("get temp - zone %s", zone)
        temp = self._temperature[Zone(zone)]
        return f"The temperature in the {zone} is {temp}C"
    
    @llm.ai_callable(description="set temerature in a specific room")
    def set_temerature(self, zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")], temp: Annotated[int, llm.TypeInfo(description="The temperature to set")]):
        logger.info("set temp - zone %s", zone, temp)
        self._temperature[Zone(zone)] = temp
        return f"The temperature in the {zone} is now {temp}C"
    
    @llm.ai_callable(description="call a custom GPT CNAI tutorial to answer user queries")
    def call_cnai_gpt(self, query: Annotated[str, llm.TypeInfo(description="The user query for the CNAI tutorial")]):
#        query = query[:MAX_QUERY_LENGTH] # Trim the query if it's too long
        logger.info("call cnai_gpt - query: %s", query)
        url = "https://chatgpt.com/g/g-rHbs9yqoG-cnai-tutorial"
        response = requests.post(url, json={"query": query})
#        print(response)
        if response.status_code == 200:
            return response.json().get("answer", "No answer provided")
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    @llm.ai_callable(description="call a custom GPT Kubernetes Tutorial to answer user queries")
    def call_kubernetes_gpt(self, query: Annotated[str, llm.TypeInfo(description="The user query for the Kubernetes Tutorial")]):
        logger.info("call kubernetes_gpt - query: %s", query)
        url = "https://chatgpt.com/g/g-LVKfisAVB-kubernetes-tutorial"
        response = requests.post(url, json={"query": query})
#        print(response)
        if response.status_code == 200:
            return response.json().get("answer", "No answer provided")
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    @llm.ai_callable(description="call a custom GPT Fast API to answer user queries")
    def call_fastAPI_gpt(self, query: Annotated[str, llm.TypeInfo(description="The user query for the Fast API")]):
        logger.info("call fastAPI_gpt - query: %s", query)
        url = "https://chatgpt.com/g/g-rxSEGF2Ve-fast-api"
        response = requests.post(url, json={"query": query})
#        print(response)
        if response.status_code == 200:
            return response.json().get("answer", "No answer provided")
        else:
            return f"Error: {response.status_code} - {response.text}"

    @llm.ai_callable(description="call a custom GPT GenAI Foundations and Prompt Engineering to answer user queries")
    def call_genai_gpt(self, query: Annotated[str, llm.TypeInfo(description="The user query for the GenAI Foundations and Prompt Engineering")]):
        logger.info("call genai_gpt - query: %s", query)
        url = "https://chatgpt.com/g/g-i1I6jGn8J-genai-foundations-and-prompt-engineering"
        response = requests.post(url, json={"query": query})
#        print(response)
        if response.status_code == 200:
            return response.json().get("answer", "No answer provided")
        else:
            return f"Error: {response.status_code} - {response.text}"

    @llm.ai_callable(description="call a custom GPT Kong Tutorial to answer user queries")
    def call_kong_gpt(self, query: Annotated[str, llm.TypeInfo(description="The user query for the Kong Tutorial")]):
        logger.info("call kong_gpt - query: %s", query)
        url = "https://chatgpt.com/g/g-epC3RBzMK-kong-tutorial"
        response = requests.post(url, json={"query": query})
#        print(response)
        if response.status_code == 200:
            return response.json().get("answer", "No answer provided")
        else:
            return f"Error: {response.status_code} - {response.text}"
