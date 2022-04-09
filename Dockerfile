FROM docker.io/python:3.9.7

# Set Working Directory
WORKDIR /usr/src/app

# Install Python Dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Run Python Script
COPY analysis.py ./
COPY data.csv ./
CMD python analysis.py

### Usage Instructions ########################################################
# Using Docker (in same directory as Dockerfile), build the images with:
# > docker build --tag macs30200 .
# Replicate analysis in docker container and reproduce figures:
# > docker run --volume $(pwd):/figures/ macs30200
# Figures are saved to same directory as Dockerfile
