Here’s the updated version of the `README.md` without symbols like `#`, `---`, `*`, etc.:

---

AnalysisVision4

Overview  
AnalysisVision4 is a Python application that leverages Azure's AI Vision API, inspired by Microsoft's sample_caption_image_file.py. The project enhances the sample by introducing a .env file to securely manage sensitive information without hardcoding and uses Docker for containerization. It generates captions for images, providing human-readable descriptions along with metadata such as image dimensions and confidence scores.

Features  
- Generate captions for images using Azure Vision AI  
- Supports containerization with Docker for streamlined deployment  
- Securely manages sensitive data with .env files  

Prerequisites  
- Python 3.10 or later (for local development)  
- Docker (for containerized deployment)  
- Azure Vision AI Resource  
  - Endpoint: Your Azure Cognitive Services endpoint  
  - Key: Your Azure Cognitive Services API key  

Setup and Usage  

Local Development  
1. Clone the Repository  
   git clone https://github.com/nqd-u/analysisVision4.git  
   cd analysisVision4  

2. Set Up Environment Variables  
   Create a .env file in the project directory with the following content:  
   AI_SERVICE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/  
   AI_SERVICE_KEY=your-azure-key  

3. Create a Virtual Environment  
   python -m venv venv  
   source ./venv/Scripts/activate  (On Windows)  
   source ./venv/bin/activate  (On macOS/Linux)  

4. Install Dependencies  
   pip install -r requirements.txt  

5. Run the Script  
   Ensure sample.jpg is in the ./Data directory and run:  
   python caption-image1.py  

Containerized Deployment with Docker  

1. Build the Docker Image  
   docker build -t analysis-vision .  

2. Run the Docker Container  
   Provide the .env file to the container:  
   docker run --env-file .env analysis-vision  

3. Output  
   The container will process the sample.jpg image and print results to the console:  
   Image analysis results:  
    Caption:  
      'a person walking a dog on a leash on a street', Confidence 0.8207  
    Image height: 533  
    Image width: 800  
    Model version: 2023-10-01  

Project Structure  

analysisVision4  
Data (Directory for input images)  
  sample.jpg (Example input image)  
caption-image1.py (Main Python script)  
Dockerfile (Docker configuration)  
requirements.txt (Python dependencies)  
.env.example (Example .env file)  
README.md (Project documentation)  
LICENSE (License file)  
.gitignore (Git ignore rules)  

Troubleshooting  

Common Issues with Containers  

1. Error: Missing .env File  
   Ensure the .env file is correctly configured and passed during runtime:  
   docker run --env-file .env analysis-vision  

2. Docker Build Issues  
   Make sure Docker is installed and running.  
   Verify the Dockerfile syntax and context.  

3. Azure Authentication Errors  
   Ensure your AI_SERVICE_ENDPOINT and AI_SERVICE_KEY in the .env file are correct.  

License  
This project is licensed under the MIT License. See the LICENSE file for details.  

Acknowledgments  
Azure AI Vision API  

---
