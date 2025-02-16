## How to deploy and use using docker

#### Clone Repostiory
```bash
git clone https://github.com/akbln/en_fr_translation_test_deployment/
```
#### Navigate to the repository
```bash
cd ./en_fr_translation_test_deployment/
```
#### Build the docker image
```bash
docker build -t en-fr-translator-app .
```
#### Run the docker image
```bash
docker run -p 5000:5000 en-fr-translator-app
```

### Use the application
#### Navigate to your browser and enter 127.0.0.1:5000 in the URL bar
