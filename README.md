Twilio AI Voice Assistant

This project is a Twilio-powered AI voice assistant that connects incoming calls to OpenAI's Realtime API, allowing users to have an interactive voice conversation with an AI assistant. The AI is designed to be helpful, engaging, and humorous, with support for real-time speech recognition and audio streaming.

Features

Twilio Media Stream Integration: Streams real-time audio from Twilio to OpenAI's API.

OpenAI Realtime API: Processes speech and responds dynamically.

FastAPI Backend: Manages WebSocket connections and API routes.

Live Audio Response: Sends AI-generated responses back to Twilio for playback.

Interactive Conversation Handling: Supports interruption detection and response truncation.

Webhook Configuration: Automatically updates Twilio phone number settings.

Tech Stack

Python (FastAPI, WebSockets, Twilio, OpenAI API)

Twilio Media Streams (Real-time audio streaming)

OpenAI GPT-4o Realtime API (AI conversation processing)

Uvicorn (ASGI server for FastAPI)

Prerequisites

Before running this project, ensure you have:

A Twilio Account with an active phone number.

An OpenAI API Key for real-time AI responses.

Python 3.8+ installed.

pip install -r requirements.txt dependencies installed.

Installation & Setup

Clone the Repository

Install Dependencies

Set Up Environment Variables
Create a .env file with the following content:

Run the Server

Twilio Webhook Configuration

Run the following Python script to update your Twilio phone number webhook:

This will configure your Twilio number to route calls to your AI assistant.

API Endpoints

GET / - Health check endpoint.

POST /incoming-call - Handles incoming Twilio calls and connects them to AI.

WS /media-stream - WebSocket endpoint for real-time audio streaming.

How It Works

A user calls your Twilio number.

Twilio routes the call to /incoming-call.

The API responds with TwiML to establish a WebSocket connection.

Twilio streams real-time audio to /media-stream.

The AI processes the speech and sends responses back as audio.

The user interacts with the AI in a real-time conversation.

Future Improvements

Multi-language Support

Enhanced Speech Recognition & Sentiment Analysis

Database Logging for Conversations

User Authentication & Personalization

License

This project is licensed under the MIT License. Feel free to use and modify it!

Author

Himanshu Chelani

