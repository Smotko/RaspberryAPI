import asyncio
import logging
from enum import Enum
from typing import Optional
from shlex import quote

from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI(
    title="🍓 API",
    description="API endpoints for my Raspberry Pi",
    version="v2021.4.25",
    openapi_tags=[
        {
            "name": "speach",
        }
    ],
)


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs")


class Language(str, Enum):
    en = "en"
    en_us = "en-us"
    pt = "pt"
    pt_pt = "pt-pt"


class Speach(BaseModel):
    text: str = "Hello World!"
    language: Optional[Language] = Language.en


class SpeachResponse(BaseModel):
    result = "I have spoken"


async def speak(speach: Speach):
    proc = await asyncio.create_subprocess_shell(
        f'espeak -v{quote(speach.language)} --stdout "{quote(speach.text)}" | aplay',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()


@app.post("/api/v1/speach", tags=["speach"], response_model=SpeachResponse)
async def speach(
    speach: Speach,
    background_tasks: BackgroundTasks,
):
    logger.info("Saying `%s` in language %s", speach.text, speach.language)
    background_tasks.add_task(speak, speach=speach)
    return SpeachResponse()
