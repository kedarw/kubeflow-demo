From python:3.9

# Get all security updates, clean cache and remove updates to save space

#RUN apt-get update

# Copy requirements.txt from repo into docker image
COPY requirements.txt /tmp/requirements.txt

# Install requirements into docker
RUN pip install -r /tmp/requirements.txt

# TODO: For security purposed I would recommend to create user(if this was private repo), for now I am not going to do that

# Copy source code
COPY src /opt/src

COPY data /opt/data