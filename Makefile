# Variables
IMAGE_NAME=tariffrisk-app
CONTAINER_NAME=tariffq-test
PYTHONPATH=app

# Install dependencies locally
install:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

# Run FastAPI app locally
dev:
	. .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
	
# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run tests locally
test-local:
PYTHONPATH=app pytest tests/

# Run tests inside Docker
test:
	docker run --rm \
		-e PYTHONPATH=/app \
		-v $$(pwd):/app \
		$(IMAGE_NAME) \
		pytest tests/

# Run FastAPI server (inside Docker)
run:
	docker run --rm -p 8000:8000 \
		-e PYTHONPATH=/app \
		-v $$(pwd):/app \
		$(IMAGE_NAME)

# Enter interactive shell in container
bash:
	docker run --rm -it \
		-e PYTHONPATH=/app \
		-v $$(pwd):/app \
		$(IMAGE_NAME) \
		bash

# Clean up image
clean:
	docker rmi $(IMAGE_NAME)
