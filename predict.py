import joblib

model = joblib.load("models/resume_model.pkl")

candidate = [[
    8.5,
    2,
    4,
    3,
    1,
    1,
    2,
    80
]]

prediction = model.predict(candidate)

if prediction[0] == 1:
    print("Likely to be Hired")
else:
    print("Not Likely to be Hired")