# Use ARM-compatible Python image for Apple Silicon
FROM --platform=linux/arm64 python:3.12-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy dependency file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create folders and set permissions
RUN useradd -m myuser && mkdir logs qr_codes && chown myuser:myuser logs qr_codes

# Copy app files
COPY --chown=myuser:myuser . .

# Use non-root user
USER myuser

# Default run command
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "http://github.com/kaw393939"]

