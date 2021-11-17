import uvicorn
import os
## UVICORN = ASGI = Async Server Gateway Interface == NODEJS


if __name__ == "__main__":
    port = int(os.getenv('PORT')) if os.getenv('PORT') else 8000
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True,
                log_level="debug")
