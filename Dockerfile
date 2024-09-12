FROM pypy:latest

# Set working dir
WORKDIR /app

# Copy requirements into image
COPY requirements.txt /app/

# Install any needed packages in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory content to image
COPY . /app/

# Make port 8000 avaiable to the world outside the container
EXPOSE 8000

# Run the Django server when container lauches
CMD ["pypy", "manage.py", "runserver", "0.0.0.0:8000"]
