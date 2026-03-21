from fastapi import FastAPI 
from .databasemodels import Base

app = FastAPi()

app.include_router(User.routers)
app.include_router(Login.routers)
app.include_router(profile.routers)
app.include_router(update.routers)
app.include_router(delete.routers)
app.include_router(delete_items.routers)
app.include_router(profile.routers)
app.include_router(admin_profile.routers)
app.include_router(updateitem.routers)
app.include_
