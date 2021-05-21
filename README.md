# Artificial intelligence for images
# AWS Lambda project

## Applied technologies
AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers, creating cluster sizing logic with workload recognition, maintaining event integrations or managing run times. With Lambda, you can run the code for almost any type of application or back-end service, all without administration.

Boto3 makes it easy to integrate your Python application, library or script with AWS services, including Amazon S3, Amazon EC2 and Amazon DynamoDB, among others.

## How Works
You can put imagens in folder "imagens" and after you need run index.py for making a Rekognition indices...

After you can put a _analise.png photo with a group of people, where having one or more people when exists in folder imagens.

Well for finish you can run faceanalise.py for get a comparison and have answered if have recognition any person in _analise.png

#### usually commands
- to get profiles from aws cli
```
aws configure list-profiles
```

- synchronize folder in S3
```
aws s3 sync . s3://fa-imagens-lambda-model --profile 
```

- see collections on rekognition
```
aws rekognition list-collections --profile
```