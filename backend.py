from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# HTML content as a string
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telegram Username</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        .username-display {
            font-size: 1.5em;
            color: #0088cc;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Telegram Web App</h1>
    <p>Your Telegram Username:</p>
    <p class="username-display" id="telegram-username">Loading...</p>

    <script>
        function getTelegramUsername() {
            if (window.Telegram && window.Telegram.WebApp) {
                const telegram = window.Telegram.WebApp;
                const username = telegram.initDataUnsafe?.user?.username || "No username available";
                document.getElementById("telegram-username").textContent = username;
            } else {
                document.getElementById("telegram-username").textContent = "Not in Telegram environment.";
            }
        }
        getTelegramUsername();
    </script>
</body>
</html>

"""

@app.get("/", response_class=HTMLResponse)
async def serve_html():
    return html_content


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=80,
        ssl_certfile="cert.pem",
        ssl_keyfile="key.pem"
    )
