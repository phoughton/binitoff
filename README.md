# Bin It Off

A simple service that can be used dump image data to a file. So you can read it back later.

Allows you to take screen shots of your app and save them to this service. Then you can use the service to get the image data back.

## Getting started
```bash
# Create your virtual env etc, then...
python -m pip install -r requirements.txt

# Start the service
python binitoff.py
```


## Example usage
```bash
# Upload the example image eg_1.png (We are using curl but you could do this in Java, Python or NodeJS etc.)
curl -X POST -F "file=@eg_1.png" http://0.0.0.0:5000/upload
{"filename":"891a7e08-4065-4b01-97f1-d07836bf35a8.png","url":"http://181d0b217754:5000/image/891a7e08-4065-4b01-97f1-d07836bf35a8.png"}

# This should download the imeage to your local machine  
curl -O http://181d0b217754:5000/image/891a7e08-4065-4b01-97f1-d07836bf35a8.png"

# This will list all images currently stores in the service
curl http://0.0.0.0:5000/images
```

## Debugger
The `launch.json` file includes the necessary config to support using the vscode python debugger with pytest.


# Docker Container used in this repo
Here is the [Dockerfile](https://github.com/phoughton/python_dev_container) used for this  repo.
