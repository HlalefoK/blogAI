import PIL.Image
import google.generativeai as genai
import os
import csv

apiKey = "AIzaSyA0OBWLCYfuMRTwctEUwhn4nglSRFIfvc0"

genai.configure(api_key=apiKey)
model = genai.GenerativeModel('gemini-pro-vision')

image_folder = "images"

prompt = "Write an engaging caption about the Image."

for image_filename in os.listdir(image_folder):
    if image_filename.lower().endswith(('.png', '.jpeg', '.jpg')):
        image_path = os.path.join(image_folder, image_filename)
        img = PIL.Image.open(image_path)

        response_with_text = model.generate_content([prompt, img], stream=True)

        response_with_text.resolve()

        print(response_with_text)

        csv_filename = os.path.splitext(image_filename)[0] + '.csv'

        with open(csv_filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Image Name', 'Generated Text'])
            csvwriter.writerow([image_filename, response_with_text.text])