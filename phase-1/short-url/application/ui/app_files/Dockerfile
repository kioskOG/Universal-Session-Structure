# Stage 1: Builder Stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install necessary system dependencies for building grpcio and others
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libc-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python dependencies into a separate install directory
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt


ENV PATH="/install/bin:$PATH"
ENV PYTHONPATH="/install/lib/python3.11/site-packages"
# RUN opentelemetry-bootstrap --action=install

# Stage 2: Final Slim Image
FROM python:3.11-slim AS runtime

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libffi8 \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*



ENV OTEL_SERVICE_NAME=flask-ui \
    OTEL_RESOURCE_ATTRIBUTES=service.name=flask-ui \
    OTEL_EXPORTER_OTLP_PROTOCOL=grpc \
    OTEL_EXPORTER_OTLP_ENDPOINT=http://signoz-otel-collector.signoz.svc.cluster.local:4317
# Copy only installed Python packages
COPY --from=builder /install /usr/local

# Copy application code
COPY  templates/ /app/templates/
COPY app.py .

RUN opentelemetry-bootstrap --action=install

# Expose Flask app port
EXPOSE 5000

CMD ["opentelemetry-instrument", "gunicorn", "-b", "0.0.0.0:5000", "app:app"]
