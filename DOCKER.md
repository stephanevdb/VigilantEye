
# VigilantEye Docker Compose Usage

This Docker Compose configuration provides services for both the VigilantEye master and worker.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Usage

1. Create a Docker Compose file named `docker-compose.yml` with the following content:

```yaml
version: '3.1'

services:
  master:
    image: stephanevdb/vigilanteye-master:latest
    restart: unless-stopped
    ports:
      - "8666:8666"
      - "8666:8666/tcp6"

  worker:
    image: stephanevdb/vigilanteye-worker:latest
    restart: unless-stopped
    ports:
      - "8667:8667"
      - "8667:8667/tcp6"
    depends_on:
      - master
```

2. Run the following command in the same directory as the `docker-compose.yml` file:

```bash
docker-compose up -d
```

3. Access the VigilantEye Web GUI at http://localhost:8666.

**Note:** Ensure that communication between the master and worker is allowed on ports 8666 and 8667.

## License
[GPL License](LICENSE)