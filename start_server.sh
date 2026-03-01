#!/bin/bash

PORT=5000

echo "===================================="
echo "   STARTING CMAD WEB SERVER + NGROK"
echo "===================================="

# --------------------------------------------------------
# 1. AUTO-KILL ANY PROCESS USING PORT 5000
# --------------------------------------------------------
PID=$(lsof -t -i :$PORT)

if [ ! -z "$PID" ]; then
    echo "[0/3] Port $PORT is in use by PID $PID — killing..."
    kill -9 $PID
    echo "    → Successfully freed port $PORT."
else
    echo "[0/3] Port $PORT is free."
fi

# --------------------------------------------------------
# 2. START FLASK ONLY ONCE
# --------------------------------------------------------
echo "[1/3] Starting Flask server (single instance)..."

# IMPORTANT: only ONE Flask run
python app.py &
sleep 3

if ! lsof -i :$PORT >/dev/null; then
    echo "ERROR: Flask could not bind to port $PORT."
    exit 1
fi

# --------------------------------------------------------
# 3. START NGROK
# --------------------------------------------------------
echo "[2/3] Starting ngrok tunnel..."
ngrok http $PORT > /dev/null 2>&1 &
sleep 3

# --------------------------------------------------------
# 4. GET PUBLIC URL
# --------------------------------------------------------
echo "[3/3] Fetching public URL..."
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o '"public_url":"[^"]*' | sed 's/"public_url":"//')

echo ""
echo "========================================"
echo "   CMAD WEBSITE IS LIVE!"
echo "   Public URL: $NGROK_URL"
echo "========================================"
echo ""
echo "Press CTRL+C to stop everything."
