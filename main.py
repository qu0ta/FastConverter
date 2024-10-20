from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/converter")
async def converter_base():
    return RedirectResponse(url="/converter/length", status_code=302)


@app.get("/converter/length")
async def converter_length(request: Request):
    return templates.TemplateResponse(request=request, name="length.html")