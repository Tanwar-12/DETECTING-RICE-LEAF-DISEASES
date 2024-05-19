from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
from io import BytesIO
import numpy as np

app = Flask(__name__)
model = load_model('leaf.keras')

cols = ['Bacterial leaf blight', 'Brown spot', 'Leaf sum', 'class4', 'class5']  # replace with your actual class labels

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    if file:
        img = load_img(BytesIO(file.read()), target_size=(224, 224))
        img = img_to_array(img)
        img = img/255
        img = np.expand_dims(img, axis=0)
        proba = model.predict(img)
        prob_img = np.argsort(proba[0])[:-4:-1]
        return jsonify({'prediction': cols[prob_img[0]]})

@app.route('/')
def upload_file():
   return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)