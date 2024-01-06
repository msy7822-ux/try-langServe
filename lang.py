from langchain.chat_models import ChatVertexAI
from langchain.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_template(
    "Tell me a joke about Chuck Norris and {text}"
)
_model = ChatVertexAI()

chain = _prompt | _model

chain.invoke({"text": "Cannelloni"})
# Chuck Norris とカネロニに関するジョークは次のとおりです。
# Chuck Norris はカネロニを食べません。食べるのは缶です。"
