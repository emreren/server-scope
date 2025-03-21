FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.7 /uv /uvx /bin/

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

# Presuming there is a `my_app` command provided by the project
CMD ["uv", "run", "main.py"]