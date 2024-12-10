# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


from dotenv import load_dotenv
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def caption_image_file():
    # Load environment variables from .env
    load_dotenv()

    # Get the endpoint and key
    endpoint = os.getenv("AI_SERVICE_ENDPOINT")
    key = os.getenv("AI_SERVICE_KEY")

    if not endpoint or not key:
        print("Missing environment variables. Make sure to set them in the .env file.")
        exit()

    # Create an Image Analysis client for synchronous operations
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # Load image to analyze into a 'bytes' object
    with open("./Data/street.jpg", "rb") as f:
        image_data = f.read()

    # Get a caption for the image
    result = client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.CAPTION],
        gender_neutral_caption=True,  # Optional (default is False)
    )

    # Print caption results to the console
    print("Image analysis results:")
    print(" Caption:")
    if result.caption is not None:
        print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")
    print(f" Image height: {result.metadata.height}")
    print(f" Image width: {result.metadata.width}")
    print(f" Model version: {result.model_version}")


if __name__ == "__main__":
    caption_image_file()
