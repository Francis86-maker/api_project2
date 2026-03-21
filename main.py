from fastapi import FastAPI 
from .databasemodels import Base

app = FastAPi()
metadata.Base.create_all(bind=engine)
app.include_router(User.routers)
app.include_router(Login.routers)
app.include_router(userprofile.routers)
app.include_router(update.routers)
app.include_router(delete.routers)
app.include_router(Item.routers)
app.include_router(Item_update.routers)
app.include_router(admin_profile.routers)
app.include_router(delete_item.routers)
app.include_router(iteminfo.routers)

