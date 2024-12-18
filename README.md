# S1 Coursework

This is the repository containing the code and report for my S1 Coursework.

## Repository Structure
```
eszt2/
├── data_storage/
│   ├── bootstraps/ #contains toy data and plots for MLE
│   ├── bootstraps_sweights2/ #contains toys for sWeights
│   ├── fitted_values.csv #saved values from MLE fit of 100k sample
│   ├── fitted_errors.csv #saved errors from MLE fit of 100k sample
│   ├── joint_pdf_sample_s100.csv #100k sample events
│   ├── noisy_params.csv #noisy starting params
│   └── timings.csv #time taken for part d
├── plots/ #plots for report
├── report/ #report in here
├── .dockerignore 
├── .gitignore
├── Dockerfile 
├── environment.yml #environment variables
├── s1_coursework.ipynb #notebook for parts a-e
├── S1_Coursework.pdf
└── sweights_vs_MLE.ipynb #notebook for part f (sWeights)
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone [repository-url]
cd ESZT2
```

### 2. Docker Setup

The project includes a Dockerfile for creating a reproducible environment with all necessary dependencies.
You must have Docker Desktop installed.

Build the Docker image:
```bash
docker build -t s1_coursework .
```

Run the Jupyter environment:
```bash
docker run -p 8888:8888 s1_coursework
```

### 3. Accessing Jupyter Notebooks

After running the container:
1. Look for the URL with token in the terminal output
2. Copy and paste it into your browser
3. You can now access and run the notebooks:
   - `s1_coursework.ipynb`
   - `sweights_vs_MLE.ipynb`

## Environment Details

You can also install the environment variables from the `environment.yml` file.
