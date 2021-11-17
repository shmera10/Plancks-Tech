from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from application.routers import router
from application.menuClass import Menu, Update_Menu
import os

app = FastAPI()
get_par = os.path.abspath('..')

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)

# Generate the Menu Singleton
menu = Menu()


@app.on_event("startup")
@repeat_every(seconds=60*60*24)  # 24 hour
def update_menu():
    global menu
    menu = Update_Menu()
