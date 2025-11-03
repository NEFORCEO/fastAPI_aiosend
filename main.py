
from fastapi import FastAPI

from model.lifespan_model import start_app
from routers.check_router import check_router
from routers.invoice_router import inv_router
from routers.get_router import get_router
from client.Config.app_config import main_app, host, port, reload

app = FastAPI(lifespan=start_app)

app.include_router(router=get_router)
app.include_router(router=inv_router)
app.include_router(router=check_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host=host, port=port, reload=reload)