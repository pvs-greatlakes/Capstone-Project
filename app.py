from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Model.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Hospital_region_code -----------------------------------------------------------------------------------

        hrc = request.form['Hospital_region_code']

        if(hrc == 'Y'):
            hrc_Y = 1
            hrc_Z = 0

        elif(hrc == 'Z'):
            hrc_Y = 0
            hrc_Z = 1

        else:
            hrc_Y = 0
            hrc_Z = 0

        # City_Code_Hospital ---------------------------------------------------------------------------------------

        cch = request.form['City_Code_Hospital']

        if(cch == '2'):
            cch_2 = 1
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '3'):
            cch_2 = 0
            cch_3 = 1
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '4'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 1
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '5'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 1
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '6'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 1
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '7'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 1
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '9'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 1
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        elif(cch == '10'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 1
            cch_11 = 0
            cch_13 = 0

        elif(cch == '11'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 1
            cch_13 = 0

        elif(cch == '13'):
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 1

        else:
            cch_2 = 0
            cch_3 = 0
            cch_4 = 0
            cch_5 = 0
            cch_6 = 0
            cch_7 = 0
            cch_9 = 0
            cch_10 = 0
            cch_11 = 0
            cch_13 = 0

        # Hospital_code --------------------------------------------------------------------------------

        hc = request.form['Hospital_code']

        if(hc == '2'):
            hc_2 = 1
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif(hc == '3'):
            hc_2 = 0
            hc_3 = 1
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif(hc == '4'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 1
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif(hc == '5'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 1
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif(hc == '6'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 1
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif(hc == '7'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 1
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif(hc == '8'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 1
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '9'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 1
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '10'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 1
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '11'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 1
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '12'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 1
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '13'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 1
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '14'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 1
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '15'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 1
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '16'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 1
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '17'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 1
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '18'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 1
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '19'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 1
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '20'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 1
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '21'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 1
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '22'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 1
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '23'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 1
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '24'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 1
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '25'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 1
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '26'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 1
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '27'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 1
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '28'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 1
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '29'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 1
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        elif (hc == '30'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 1
            hc_31 = 0
            hc_32 = 0

        elif (hc == '31'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 1
            hc_32 = 0

        elif (hc == '32'):
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 1

        else:
            hc_2 = 0
            hc_3 = 0
            hc_4 = 0
            hc_5 = 0
            hc_6 = 0
            hc_7 = 0
            hc_8 = 0
            hc_9 = 0
            hc_10 = 0
            hc_11 = 0
            hc_12 = 0
            hc_13 = 0
            hc_14 = 0
            hc_15 = 0
            hc_16 = 0
            hc_17 = 0
            hc_18 = 0
            hc_19 = 0
            hc_20 = 0
            hc_21 = 0
            hc_22 = 0
            hc_23 = 0
            hc_24 = 0
            hc_25 = 0
            hc_26 = 0
            hc_27 = 0
            hc_28 = 0
            hc_29 = 0
            hc_30 = 0
            hc_31 = 0
            hc_32 = 0

        # Hospital_type_code -----------------------------------------------------------------------------------

        htc = request.form['Hospital_type_code']

        if (htc == 'b'):
            htc_b = 1
            htc_c = 0
            htc_d = 0
            htc_e = 0
            htc_f = 0
            htc_g = 0

        elif (htc == 'c'):
            htc_b = 0
            htc_c = 1
            htc_d = 0
            htc_e = 0
            htc_f = 0
            htc_g = 0

        elif (htc == 'd'):
            htc_b = 0
            htc_c = 0
            htc_d = 1
            htc_e = 0
            htc_f = 0
            htc_g = 0

        elif (htc == 'e'):
            htc_b = 0
            htc_c = 0
            htc_d = 0
            htc_e = 1
            htc_f = 0
            htc_g = 0

        elif (htc == 'f'):
            htc_b = 0
            htc_c = 0
            htc_d = 0
            htc_e = 0
            htc_f = 1
            htc_g = 0

        elif (htc == 'g'):
            htc_b = 0
            htc_c = 0
            htc_d = 0
            htc_e = 0
            htc_f = 0
            htc_g = 1

        else:
            htc_b = 0
            htc_c = 0
            htc_d = 0
            htc_e = 0
            htc_f = 0
            htc_g = 0

        # City_code_patient ----------------------------------------------------------------

        ccp = request.form['City_Code_Patient']

        if (ccp == '2'):
            ccp_2 = 0
            ccp_3 = 1
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '3'):
            ccp_2 = 0
            ccp_3 = 1
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif(ccp == '4'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 1
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif(ccp == '5'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 1
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif(ccp == '6'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 1
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '7'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 1
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '8'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 1
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '9'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 1
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '10'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 1
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '11'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 1
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '12'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 1
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '13'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 1
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '14'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 1
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '15'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 1
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '16'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 1
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '18'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 1
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '19'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 1
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '20'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 1
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '21'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 1
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '22'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 1
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '23'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 1
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '24'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 1
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '25'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 1
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '26'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 1
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '27'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 1
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '28'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 1
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '29'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 1
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '30'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 1
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '31'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 1
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '32'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 1
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '33'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 1
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '34'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 1
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '35'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 1
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '36'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 1
            ccp_37 = 0
            ccp_38 = 0

        elif (ccp == '37'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 1
            ccp_38 = 0

        elif (ccp == '38'):
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 1

        else:
            ccp_2 = 0
            ccp_3 = 0
            ccp_4 = 0
            ccp_5 = 0
            ccp_6 = 0
            ccp_7 = 0
            ccp_8 = 0
            ccp_9 = 0
            ccp_10 = 0
            ccp_11 = 0
            ccp_12 = 0
            ccp_13 = 0
            ccp_14 = 0
            ccp_15 = 0
            ccp_16 = 0
            ccp_18 = 0
            ccp_19 = 0
            ccp_20 = 0
            ccp_21 = 0
            ccp_22 = 0
            ccp_23 = 0
            ccp_24 = 0
            ccp_25 = 0
            ccp_26 = 0
            ccp_27 = 0
            ccp_28 = 0
            ccp_29 = 0
            ccp_30 = 0
            ccp_31 = 0
            ccp_32 = 0
            ccp_33 = 0
            ccp_34 = 0
            ccp_35 = 0
            ccp_36 = 0
            ccp_37 = 0
            ccp_38 = 0

        # Department ---------------------------

        d = request.form['Department']

        if(d == 'anesthesia'):
            d_anesthesia = 1
            d_gynecology = 0
            d_radiotherapy = 0
            d_surgery = 0

        elif(d == 'gynecology'):
            d_anesthesia = 0
            d_gynecology = 1
            d_radiotherapy = 0
            d_surgery = 0

        elif(d == 'radiotherapy'):
            d_anesthesia = 0
            d_gynecology = 0
            d_radiotherapy = 1
            d_surgery = 0

        elif(d == 'surgery'):
            d_anesthesia = 0
            d_gynecology = 0
            d_radiotherapy = 0
            d_surgery = 1

        else:
            d_anesthesia = 0
            d_gynecology = 0
            d_radiotherapy = 0
            d_surgery = 0

        # Type of Admission ------------------------------------------------------------------------

        ta = request.form['Type_of_Admission']
        
        if (ta == 'Trauma'):
            ta = 1

        elif (ta == 'Urgent'):
            ta = 2

        elif (ta == 'Emergency'):
            ta = 3

        # Severity of Illness -----------------------------------------------------------------------

        si = request.form['Severity_of_Illness']

        if (si == 'Minor'):
            si = 1

        elif (si == 'Moderate'):
            si = 2

        elif (si == 'Extreme'):
            si = 3

        # Ward type ---------------------------------------------------------------------------------

        wt = request.form['Ward_Type']

        if(wt == 'Q'):
            wt_Q = 1
            wt_R = 0
            wt_S = 0
            wt_T = 0
            wt_U = 0

        elif(wt == 'R'):
            wt_Q = 0
            wt_R = 1
            wt_S = 0
            wt_T = 0
            wt_U = 0

        elif(wt == 'S'):
            wt_Q = 0
            wt_R = 0
            wt_S = 1
            wt_T = 0
            wt_U = 0

        elif(wt == 'Q'):
            wt_Q = 0
            wt_R = 0
            wt_S = 0
            wt_T = 1
            wt_U = 0

        elif(wt == 'U'):
            wt_Q = 0
            wt_R = 0
            wt_S = 0
            wt_T = 0
            wt_U = 1

        else:
            wt_Q = 0
            wt_R = 0
            wt_S = 0
            wt_T = 0
            wt_U = 0

        # Ward_Facility_Code ------------------------------------------------------------

        wfc = request.form['Ward_Facility_Code']

        if(wfc == 'B'):
            wfc_B = 1
            wfc_C = 0
            wfc_D = 0
            wfc_E = 0
            wfc_F = 0

        elif(wfc == 'C'):
            wfc_B = 0
            wfc_C = 1
            wfc_D = 0
            wfc_E = 0
            wfc_F = 0

        elif(wfc == 'D'):
            wfc_B = 0
            wfc_C = 0
            wfc_D = 1
            wfc_E = 0
            wfc_F = 0

        elif(wfc == 'E'):
            wfc_B = 0
            wfc_C = 0
            wfc_D = 0
            wfc_E = 1
            wfc_F = 0

        elif(wfc == 'F'):
            wfc_B = 0
            wfc_C = 0
            wfc_D = 0
            wfc_E = 0
            wfc_F = 1

        else:
            wfc_B = 0
            wfc_C = 0
            wfc_D = 0
            wfc_E = 0
            wfc_F = 0

        # Bed Grade --------------------------------------------------------------------------------
        bg = request.form['Bed_Grade']

        if(bg == '2'):
            bg_2 = 1
            bg_3 = 0
            bg_4 = 0

        elif(bg == '3'):
            bg_2 = 0
            bg_3 = 1
            bg_4 = 0

        elif(bg == '4'):
            bg_2 = 0
            bg_3 = 0
            bg_4 = 1

        else:
            bg_2 = 0
            bg_3 = 0
            bg_4 = 0

        # Age -------------------------------------------------------------------------------

        age = request.form['Age']

        if (age == '0-10'):
            age = 10

        elif (age == '11-20'):
            age = 20

        elif (age == '21-30'):
            age = 30

        elif (age == '31-40'):
            age = 40

        elif (age == '41-50'):
            age = 50

        elif (age == '51-60'):
            age = 60

        elif (age == '61-70'):
            age = 70

        elif (age == '71-80'):
            age = 80

        elif (age == '81-90'):
            age = 90

        elif (age == '91-100'):
            age = 100

        # Numerical Columns ------------------------------------------------------------------------------

        Available_Extra_Rooms = int(request.form["Available_Extra_Rooms"])
        Visitors_with_Patient = int(request.form["Visitors_with_Patient"])
        Admission_Deposit = int(request.form["Admission_Deposit"])

        # Prediction -------------------------------------------------------------------------------------

        prediction = model.predict([[
            Available_Extra_Rooms,
            ta,
            si,
            Visitors_with_Patient,
            Admission_Deposit,
            age,
            hc_2,
            hc_3,
            hc_4,
            hc_5,
            hc_6,
            hc_7,
            hc_8,
            hc_9,
            hc_10,
            hc_11,
            hc_12,
            hc_13,
            hc_14,
            hc_15,
            hc_16,
            hc_17,
            hc_18,
            hc_19,
            hc_20,
            hc_21,
            hc_22,
            hc_23,
            hc_24,
            hc_25,
            hc_26,
            hc_27,
            hc_28,
            hc_29,
            hc_30,
            hc_31,
            hc_32,
            htc_b,
            htc_c,
            htc_d,
            htc_e,
            htc_f,
            htc_g,
            cch_2,
            cch_3,
            cch_4,
            cch_5,
            cch_6,
            cch_7,
            cch_9,
            cch_10,
            cch_11,
            cch_13,
            hrc_Y,
            hrc_Z,
            d_anesthesia,
            d_gynecology,
            d_radiotherapy,
            d_surgery,
            wt_Q,
            wt_R,
            wt_S,
            wt_T,
            wt_U,
            wfc_B,
            wfc_C,
            wfc_D,
            wfc_E,
            wfc_F,
            ccp_2,
            ccp_3,
            ccp_4,
            ccp_5,
            ccp_6,
            ccp_7,
            ccp_8,
            ccp_9,
            ccp_10,
            ccp_11,
            ccp_12,
            ccp_13,
            ccp_14,
            ccp_15,
            ccp_16,
            ccp_18,
            ccp_19,
            ccp_20,
            ccp_21,
            ccp_22,
            ccp_23,
            ccp_24,
            ccp_25,
            ccp_26,
            ccp_27,
            ccp_28,
            ccp_29,
            ccp_30,
            ccp_31,
            ccp_32,
            ccp_33,
            ccp_34,
            ccp_35,
            ccp_36,
            ccp_37,
            ccp_38,
            bg_2,
            bg_3,
            bg_4
        ]])
    
    
        if (prediction==1):
            output = '0-10'
        elif (prediction==2):
            output = '11-20'
        elif (prediction==3):
            output = '21-30'
        elif (prediction==4):
            output = '31-40'
        elif (prediction==5):
            output = '41-50'
        elif (prediction==6):
            output = '51-60'
        elif (prediction==7):
            output = '61-70'
        elif (prediction==8):
            output = '71-80'
        elif (prediction==9):
            output = '81-90'
        elif (prediction==10):
            output = '91-100'
        elif (prediction==11):
            output = '100+'
            
        return render_template('result.html', prediction_text="LOS = {} days".format(output))

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
