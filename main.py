
from fastapi import FastAPI

from model.lifespan_model import start_app
from routers.invoice_router import inv_router
from routers.get_router import get_router


app = FastAPI(lifespan=start_app)

app.include_router(router=get_router)
app.include_router(router=inv_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=1500, reload=True)