# Anteambulo
An AI assistant to clear your debugging pathig tu

# Steps
1. Make a python virtual env
python3 -m venv .venv
source .venv/bin/activate
2. To install python packages run the following command
pip3 install -r requirements. txt 
3. Run the flask app
flask run

# Curl to get response for issues
curl --location 'http://localhost:5000/getAll

# Curl to get the response 
curl --location 'http://localhost:5000/getAnswer?selected_option=<selected_option>>'

