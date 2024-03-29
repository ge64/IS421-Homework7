# IS 421-002 - Homework 7 
# Scalability and Cloud Computing
### Repo link:
![myRepoQRCode](/images/myRepo.png)

## Instructions
### Clone repo
`git clone https://github.com/ge64/homework7`

### Install requirements
`pip install -r requirements.txt`

### Build the Docker image
`docker build -t qrcode-generator .`

### Run the Docker container
`docker-compose up`

### To run with a different link
`docker run -e QR_CODE_DEFAULT_URL=https://[yourLinkHere].com -e QR_CODE_IMAGE_DIRECTORY=images -e QR_CODE_DEFAULT_FILE_NAME='[yourFileNameHere].png' -v ${pwd}:/home/myuser qrcode`