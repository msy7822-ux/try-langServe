from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

from rag_opensearch import chain as rag_opensearch_chain
from vertexai_chuck_norris.chain import chain as vertexai_chuck_norris_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, rag_opensearch_chain, path="/rag-opensearch")
add_routes(app, vertexai_chuck_norris_chain, path="/vertexai-chuck-norris")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
