#!/bin/bash
# Quick setup script for tech-interview-generator

echo "===================================================="
echo "  Tech Interview Generator - Setup"
echo "===================================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Setup .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "Setting up .env file..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "===================================================="
    echo "  IMPORTANT: Add your OpenAI API key"
    echo "===================================================="
    echo ""
    echo "Edit the .env file and add your API key:"
    echo "  OPENAI_API_KEY=your_key_here"
    echo ""
    echo "Get your API key from: https://platform.openai.com/api-keys"
    echo ""
else
    echo "✓ .env file already exists"
fi

# Make generate_question.py executable
chmod +x generate_question.py

echo ""
echo "===================================================="
echo "  Setup Complete!"
echo "===================================================="
echo ""
echo "Next steps:"
echo "1. Add your OpenAI API key to .env file"
echo "2. Run: python generate_question.py"
echo ""
