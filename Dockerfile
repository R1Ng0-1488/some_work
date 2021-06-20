FROM python:3.9.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# Set work directory
WORKDIR /work

# install dependencies
COPY requirements.txt /work/
RUN pip install -r requirements.txt

# Copy project
COPY . /work/