# Use a base miniconda image
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy environment.yml
COPY environment.yml .

# Copy your notebooks and other files
COPY . .

# Create conda environment from environment.yml
RUN conda env create -f environment.yml

# Initialize conda in bash
RUN conda init bash

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "s1_coursework_env", "/bin/bash", "-c"]

# Expose the port Jupyter will run on
EXPOSE 8888

# Start Jupyter notebook - modified command
CMD ["conda", "run", "--no-capture-output", "-n", "s1_coursework_env", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]