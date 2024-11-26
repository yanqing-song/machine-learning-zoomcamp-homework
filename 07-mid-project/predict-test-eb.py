import requests

host = 'heart-failure-predict-env.eba-qhajbtg2.us-west-2.elasticbeanstalk.com'
url = f'http://{host}/predict'
patient = {
    'age': 65,
    'anaemia': False,
    'creatinine_phosphokinase': 1688,
    'diabetes': False,
    'ejection_fraction': 38,
    'high_blood_pressure': False,
    'platelets': 263360,
    'serum_creatinine': 1.1,
    'serum_sodium': 138,
    'sex': 'man',
    'smoking': True,
    'time': 250,
}
response = requests.post(url, json=patient).json()
print(response)


if response['death_event']:
    print('The patient may not survive')
else:
    print('The patient may survive')
