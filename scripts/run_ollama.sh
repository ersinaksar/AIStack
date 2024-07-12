#!/bin/bash

echo "Starting Ollama server..."
ollama serve &

echo "Waiting for Ollama server to be active..."
while [ "$(ollama list | grep 'NAME')" == "" ]; do
  sleep 1
done

echo "Running the model..."
ollama run phi3
# ollama run phi3:latest
# llama2