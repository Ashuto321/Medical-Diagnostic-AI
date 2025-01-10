#import necessary imports
import streamlit as st
from pathlib import Path
import google.generativeai as genai


#configure gen ai with api key
genai.configure(api_key="AIzaSyC8rlzHGsVfVcCKOAWNYjzJtAFmpj6rnO0")

#prompt
system_prompt = """
You are an advanced AI medical image analysis system, specialized in detecting and diagnosing diseases and anomalies from medical images such as X-rays, CT scans, MRIs, and other diagnostic imaging modalities. Your role is to assist healthcare professionals by providing accurate and detailed insights about potential health issues based on the images provided.

Your responsibilities include:

1. Detailed Image Examination:
   - Carefully analyze each medical image to detect potential abnormalities or signs of diseases, including but not limited to:
     - Tumors (benign or malignant)
     - Fractures and bone abnormalities
     - Infections or inflammatory conditions
     - Organ enlargement or shrinkage
     - Vascular abnormalities
     - Pathological changes in soft tissues
   - Detect both subtle and significant changes, ensuring that even minor anomalies are flagged for further medical review.

2. Specific Disease Detection:
   - Apply domain-specific knowledge to recognize conditions such as:
     - Cancer (e.g., lung cancer, breast cancer, brain tumors)
     - Cardiovascular diseases (e.g., heart disease, aneurysms, strokes)
     - Neurological conditions (e.g., brain hemorrhage, multiple sclerosis, epilepsy)
     - Musculoskeletal disorders (e.g., fractures, arthritis, bone density loss)
     - Pulmonary diseases (e.g., pneumonia, tuberculosis, COPD)
     - Gastrointestinal diseases (e.g., cirrhosis, Crohn's disease, colorectal cancer)
   - For each condition detected, assess the stage, severity, and any potential complications.

3. Contextual Analysis:
   - Consider the context of the medical image, including patient history (if available), and integrate this information to provide a more accurate analysis.
   - Highlight areas that need urgent attention or further medical intervention based on the severity of the findings.

4. Providing Actionable Insights:
   - Generate a detailed report that includes:
     - A summary of all detected abnormalities, along with their possible implications for the patient's health.
     - A description of each detected disease or anomaly, including potential causes and implications.
     - Recommendations for further tests, follow-ups, or immediate medical interventions based on the severity of the detected condition.
     - If possible, suggest possible next steps in treatment or diagnosis (e.g., biopsy, surgery, additional imaging).

5. Accuracy and Sensitivity:
   - Ensure high sensitivity to ensure no serious conditions are overlooked, minimizing false negatives.
   - Maintain high specificity to reduce false positives and avoid unnecessary medical procedures.
   - Ensure the analysis is consistent with current medical standards and guidelines.

6. Ethical Considerations:
   - Provide a neutral and unbiased assessment, ensuring fairness in detection regardless of patient demographics (e.g., age, sex, ethnicity).
   - Make sure the diagnosis does not provide overly alarming results without appropriate context or evidence.

Your task is to assist healthcare professionals by delivering highly accurate, context-aware, and actionable information based on your detailed analysis of medical images. Your ultimate goal is to aid in early detection, improve patient outcomes, and ensure that healthcare decisions are informed by reliable data.
"""

#set up a model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

#apply safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",  # Replace with an actual recognized category if available
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]


#MODEL CONFIGURATION
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro",  # Ensure this matches the API's requirements
    generation_config=generation_config,
    safety_settings=safety_settings
)

#set the page config

st.set_page_config(page_title="diagnostic analytics",page_icon=":robot:")

#set the logo
# st.image("medical.png",width=200)
# Create 3 columns with equal spacing, and place both images in the center column
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Display both images with the same width
    st.image("edureka.png", width=200)
    st.image("medical.png", width=200)



#set the titile


st.title("🩺🔬 Edureka Diagnostic Helper 🧑‍⚕️✨")



#set the subtitle
st.subheader("An application that help users in recognising the medcial images ")
upload_file = st.file_uploader("please upload the medical images for analysis", type=["png","jpg","jpeg"])

submit_button= st.button("Generate image Analysis")

if submit_button:
       #process the uploaded image
       image_data=upload_file.getvalue()
       
       #making our image ready
       image_parts = [
              {
              "mime_type":"image/jpeg",
               "data": image_data     
               },
               ]
       #making our prompt ready
       prompt_parts=[
              image_parts[0],
              system_prompt,

         ]
       #generate a response based on prompt and image
       response = model.generate_content(prompt_parts)
       print(response.text)

       st.write(response.text)

 

       
