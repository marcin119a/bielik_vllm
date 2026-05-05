#!/bin/bash

# Set HUGGING_FACE_HUB_TOKEN in your environment before running this script
: "${HUGGING_FACE_HUB_TOKEN:?HUGGING_FACE_HUB_TOKEN is not set}"

uv run vllm serve "speakleash/Bielik-4.5B-v3.0-Instruct" \
  --enable-auto-tool-choice \
  --tool-parser-plugin ./bielik-tools/tools/bielik_vllm_tool_parser.py \
  --tool-call-parser bielik \
  --chat-template ./bielik-tools/tools/bielik_advanced_chat_template.jinja \
  --port 8000 \
  --host 0.0.0.0 \
  --max-num-batched-tokens 8192 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.85 \
  --quantization bitsandbytes
