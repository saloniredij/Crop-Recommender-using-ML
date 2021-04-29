# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# app = Flask(__name__)
# model = pickle.load(open('../model/RandomForest.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')
#     # return "<h1>hello</h1>"

# # @app.route('/predict',methods=['POST'])
# # def predict():
# #     '''
# #     For rendering results on HTML GUI
# #     '''
# #     int_features = [int(x) for x in request.form.values()]
# #     final_features = [np.array(int_features)]
# #     prediction = model.predict(final_features)

# #     output = round(prediction[0], 2)

# #     return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

# # @app.route('/predict_api',methods=['POST'])
# # def predict_api():
# #     '''
# #     For direct API calls trought request
# #     '''
# #     data = request.get_json(force=True)
# #     prediction = model.predict([np.array(list(data.values()))])

# #     output = prediction[0]
# #     return jsonify(output)

# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, render_template, request, Markup
import numpy as np
import pickle

crop_recommendation_model_path = '../model/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# model = pickle.load(open('../model/RandomForest.pkl', 'rb'))

app = Flask(__name__)

@ app.route('/')
def home():
    # title = 'crop recc'
    return render_template('index.html')

@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # state = request.form.get("stt")
        # city = request.form.get("city")

        # if weather_fetch(city) != None:
        #     temperature, humidity = weather_fetch(city)
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        return render_template('index.html', prediction=final_prediction, title=title)

        # else:

        #     return render_template('try_again.html', title=title)



if __name__ == '__main__':
    app.run(debug=True)
 #    set FLASK_APP = yourfilename.py
	# set FLASK_DEBUG = 1