import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add project root to path

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
