FROM python:3.10-slim

ARG ROOT_PATH=/
ENV ROOT_PATH=${ROOT_PATH}

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir agenta openai python-dotenv uvicorn "litellm>=1.0,<2.0" google-generativeai

# Add agenta-cli to PYTHONPATH so it can find the local agenta package
ENV PYTHONPATH=/agenta-cli:$PYTHONPATH

EXPOSE 80

CMD ["python", "main.py"]
