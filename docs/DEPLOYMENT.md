# Deployment Guide

This guide covers various deployment options for the Rice Disease Prediction System.

## Table of Contents

1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Cloud Deployment](#cloud-deployment)
4. [Production Considerations](#production-considerations)

## Local Development

### Prerequisites

- Python 3.9+
- pip
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rice-disease-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run src/app.py
   ```

5. **Access the application**
   Open `http://localhost:8501` in your browser

## Docker Deployment

### Using Docker Compose (Recommended)

1. **Development environment**
   ```bash
   docker-compose up --build
   ```

2. **Production environment with Nginx**
   ```bash
   docker-compose --profile production up --build -d
   ```

### Using Docker directly

1. **Build the image**
   ```bash
   docker build -t rice-disease-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 rice-disease-app
   ```

### Environment Variables

Set the following environment variables for Docker deployment:

```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

## Cloud Deployment

### Heroku

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create rice-disease-prediction
   ```

4. **Set environment variables**
   ```bash
   heroku config:set STREAMLIT_SERVER_PORT=8501
   heroku config:set STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

### AWS (EC2 + Docker)

1. **Launch EC2 instance**
   - Choose Ubuntu 20.04 LTS
   - Select t3.medium or larger
   - Configure security group (port 80, 443, 22)

2. **Install Docker**
   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose
   sudo usermod -aG docker ubuntu
   ```

3. **Clone and deploy**
   ```bash
   git clone <repository-url>
   cd rice-disease-prediction
   docker-compose --profile production up -d
   ```

### Google Cloud Platform

1. **Create Cloud Run service**
   ```bash
   gcloud run deploy rice-disease-app \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

### Azure Container Instances

1. **Build and push to Azure Container Registry**
   ```bash
   az acr build --registry <registry-name> --image rice-disease-app .
   ```

2. **Deploy to Container Instances**
   ```bash
   az container create \
     --resource-group <resource-group> \
     --name rice-disease-app \
     --image <registry-name>.azurecr.io/rice-disease-app \
     --ports 8501
   ```

## Production Considerations

### Security

1. **Environment Variables**
   - Never commit secrets to version control
   - Use environment variables for sensitive data
   - Consider using a secrets management service

2. **HTTPS**
   - Always use HTTPS in production
   - Configure SSL certificates
   - Use a reverse proxy (Nginx) for SSL termination

3. **Authentication** (Optional)
   - Consider adding user authentication
   - Implement rate limiting
   - Add input validation

### Performance

1. **Caching**
   - Implement model caching
   - Use Redis for session storage
   - Cache static assets

2. **Scaling**
   - Use load balancers for multiple instances
   - Consider horizontal pod autoscaling
   - Monitor resource usage

3. **Monitoring**
   - Set up application monitoring
   - Configure logging
   - Use health checks

### Database (Optional)

If you need to store user data or predictions:

1. **PostgreSQL**
   ```yaml
   # docker-compose.yml
   services:
     db:
       image: postgres:13
       environment:
         POSTGRES_DB: rice_disease
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
   ```

2. **MongoDB**
   ```yaml
   services:
     mongodb:
       image: mongo:4.4
       environment:
         MONGO_INITDB_ROOT_USERNAME: user
         MONGO_INITDB_ROOT_PASSWORD: password
   ```

### Backup Strategy

1. **Model Backup**
   - Store model files in cloud storage
   - Version control model artifacts
   - Implement model rollback capability

2. **Data Backup**
   - Regular database backups
   - User upload backup strategy
   - Disaster recovery plan

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 8501
   lsof -i :8501
   # Kill the process
   kill -9 <PID>
   ```

2. **Docker build fails**
   - Check Dockerfile syntax
   - Ensure all files are copied correctly
   - Verify base image availability

3. **Model loading errors**
   - Check model file path
   - Verify model file exists
   - Check file permissions

4. **Memory issues**
   - Increase container memory limits
   - Optimize model loading
   - Use model quantization

### Logs

1. **Docker logs**
   ```bash
   docker logs rice-disease-prediction
   ```

2. **Streamlit logs**
   - Check browser console
   - Enable debug mode
   - Check server logs

## Monitoring and Maintenance

### Health Checks

1. **Application health**
   ```bash
   curl http://localhost:8501/_stcore/health
   ```

2. **Docker health**
   ```bash
   docker ps
   docker inspect rice-disease-prediction
   ```

### Updates

1. **Code updates**
   ```bash
   git pull origin main
   docker-compose up --build -d
   ```

2. **Model updates**
   - Replace model file
   - Restart application
   - Test predictions

### Scaling

1. **Horizontal scaling**
   ```bash
   docker-compose up --scale rice-disease-app=3
   ```

2. **Load balancer configuration**
   - Update Nginx configuration
   - Configure health checks
   - Set up SSL termination
