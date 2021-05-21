import boto3


boto3.setup_default_session(profile_name='terraform_from_ni_notebook')
s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def lista_imagens():
    imagens=[]
    bucket = s3.Bucket('fa-imagens-lambda-model')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    return imagens

def indexa_colecao(imagens):
    client.delete_collection(CollectionId='faces')
    client.create_collection(CollectionId='faces')

    for i in imagens:
        response = client.index_faces(
            CollectionId = 'faces',
            DetectionAttributes = [],
            ExternalImageId = i[:-4],
            Image = {
                'S3Object': {
                    'Bucket': 'fa-imagens-lambda-model',
                    'Name': i
               }
            }
        )


imagens = lista_imagens()
indexa_colecao(imagens)