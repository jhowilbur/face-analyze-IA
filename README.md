# Artificial intelligence for images
# AWS Lambda project

## Applied technologies
AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers, creating cluster sizing logic with workload recognition, maintaining event integrations or managing run times. With Lambda, you can run the code for almost any type of application or back-end service, all without administration.

Boto3 makes it easy to integrate your Python application, library or script with AWS services, including Amazon S3, Amazon EC2 and Amazon DynamoDB, among others.

## http://fa-site-lambda-model.s3-website-us-east-1.amazonaws.com/

## How Works BACKEND
You can put imagens in folder "imagens" and after you need run index.py for making a Rekognition indices...

After you can put a _analise.png photo with a group of people, where having one or more people when exists in folder imagens.

Well for finish you can run faceanalise.py for get a comparison and have answered if have recognition any person in _analise.png

## How Works FRONTEND
http://fa-site-lambda-model.s3-website-us-east-1.amazonaws.com/

## Technical explain
#### looking first in BACKEND folder, and just about def in python (must answer are in JSON)
- detecta_faces
    
Here you got answer about a number of faces found
```json
{
    "FaceRecords": [
        {
            "Face": {
                "FaceId": "109c3f6a-e590-4549-951f-3dc1ea9a6dbc",
                "BoundingBox": {
                    "Width": 0.22026316821575165,
                    "Height": 0.5820565223693848,
                    "Left": 0.13230381906032562,
                    "Top": 0.1318039447069168
                },
                "ImageId": "8b7fd402-baa3-3747-beda-d22240f892a1",
                "ExternalImageId": "TEMPORARIA",
                "Confidence": 99.99578857421875
            },
            "FaceDetail": {
                "BoundingBox": {
                    "Width": 0.22026316821575165,
                    "Height": 0.5820565223693848,
                    "Left": 0.13230381906032562,
                    "Top": 0.1318039447069168
                },
                "Landmarks": [
                    {
                        "Type": "eyeLeft",
                        "X": 0.21049439907073975,
                        "Y": 0.3392156958580017
                    },
                    {
                        "Type": "eyeRight",
                        "X": 0.30272796750068665,
                        "Y": 0.32937851548194885
                    },
                    {
                        "Type": "mouthLeft",
                        "X": 0.22794485092163086,
                        "Y": 0.5349754095077515
                    },
                    {
                        "Type": "mouthRight",
                        "X": 0.30468636751174927,
                        "Y": 0.5259949564933777
                    },
                    {
                        "Type": "nose",
                        "X": 0.2861842215061188,
                        "Y": 0.4209754168987274
                    }
                ],
                "Pose": {
                    "Roll": -1.212821364402771,
                    "Yaw": 20.20708465576172,
                    "Pitch": 7.424732208251953
                },
                "Quality": {
                    "Brightness": 79.70891571044922,
                    "Sharpness": 67.22731018066406
                },
                "Confidence": 99.99578857421875
            }
        },...
```

- cria_lista_faceId_detectadas

Here you're having a list(dict) from a sequence for faces ID recognized in photo.
```json
['109c3f6a-e590-4549-951f-3dc1ea9a6dbc', '809c303e-6ee7-4eda-9cd8-b6f71965fe51']
```

- compara_imagens

Here you get a comparison from folder "imagens" with _analise.png

```json
[
    {
        "SearchedFaceId": "109c3f6a-e590-4549-951f-3dc1ea9a6dbc",
        "FaceMatches": [
            {
                "Similarity": 100.0,
                "Face": {
                    "FaceId": "3810e0bd-f849-4745-89b8-cbcba9ac3455",
                    "BoundingBox": {
                        "Width": 0.22026300430297852,
                        "Height": 0.582056999206543,
                        "Left": 0.13230399787425995,
                        "Top": 0.13180400431156158
                    },
                    "ImageId": "fef233b1-1213-38a2-ae43-f18e3050f657",
                    "ExternalImageId": "_analise",
                    "Confidence": 99.99579620361328
                }
            },
            {
                "Similarity": 99.99791717529297,
                "Face": {
                    "FaceId": "51e1f148-5233-488e-999c-efd7ca71c0ab",
                    "BoundingBox": {
                        "Width": 0.5133600234985352,
                        "Height": 0.5126010179519653,
                        "Left": 0.24783000349998474,
                        "Top": 0.13105200231075287
                    },
                    "ImageId": "e1a63c2d-a13d-38ce-a4ce-de53fd8b7e51",
                    "ExternalImageId": "rock",
                    "Confidence": 99.99849700927734
                }
            }
        ],...
```

- gera_dados_json

Return a clean JSON with content saying a persons founds in group from _analise.png image

```json
[
    {
        "nome": "rock",
        "faceMatch": 100.0
    },
    {
        "nome": "trump",
        "faceMatch": 97.17
    }
]
```

Well after this part you need create a S3 Bucket from show in FRONTEND this information


----------------------------------

### usually commands
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