import subprocess

# Define the commands to start each FastAPI service
commands = [
    "uvicorn llm_service.ollama:app --host 0.0.0.0 --port 8001",
    "uvicorn master_service.server:app --host 0.0.0.0 --port 8000",
    "streamlit run frontend/app.py"
]

# Start each service in a separate subprocess
processes = [subprocess.Popen(command, shell=True) for command in commands]

# Optionally wait for all processes to complete (they won't, since these are servers)
for process in processes:
    process.wait()