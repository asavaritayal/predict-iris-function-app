# predict-iris-function-app
Predict the species of an Iris flower given it's proportions.

## Requirements

- Python3.6.x
- Azure Functions Core Tools

## Get Started

### Create and activate a virtual environment

Run the following commands to create and activate a virtual environment named `.env`.

```bash
# In Bash
python3.6 -m venv env
source env/bin/activate

# In PowerShell
py -3.6 -m venv env
env\scripts\activate
```

### Setup your app

```bash
git clone https://github.com/asavaritayal/predict-iris-function-app.git
cd predict-iris-function-app
pip install -r requirements.txt
func host start
```

### Test 

```bash
curl -w '\n' 'http://localhost:7071/api/predictspecies?plen=2.0&pwid=2.0&slen=2.0&swid=2.0'
```
