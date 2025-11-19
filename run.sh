#!/bin/bash

# CatAlert Backend Start Script

echo "🚀 Starting CatAlert Backend..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

# Run the server
echo "✅ Starting FastAPI server on http://127.0.0.1:8000"
echo "📚 API Documentation: http://127.0.0.1:8000/docs"
echo "Press CTRL+C to stop the server"
echo ""

python -m uvicorn app.main:app --reload --port 8000
