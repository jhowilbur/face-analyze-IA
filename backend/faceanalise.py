import boto3
import json


boto3.setup_default_session(profile_name='terraform_from_ni_notebook') # when send to AWS are necessary comment
s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def detecta_faces():
    faces_detectadas = client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],  # you can choose others, like smile
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': 'fa-imagens-lambda-model',
                'Name': '_analise.png'
            }
        }
    )
    # print(json.dumps(faces_detectadas, indent=4))
    return faces_detectadas


def cria_lista_faceId_detectadas(faces_detectadas):
    faceId_detectadas = []
    for imagens in range(len(faces_detectadas['FaceRecords'])):
        faceId_detectadas.append(faces_detectadas['FaceRecords'][imagens]['Face']['FaceId'])
    # print(faceId_detectadas)
    return faceId_detectadas


def compara_imagens(faceId_detectadas):
    resultado_comparacao = []
    for ids in faceId_detectadas:
        resultado_comparacao.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=ids,
                FaceMatchThreshold=80,
                MaxFaces=10,
            )
        )
    print(json.dumps(resultado_comparacao, indent=4))
    return resultado_comparacao


def gera_dados_json(resultado_comparacao):
    dados_json = []
    for face_matches in resultado_comparacao:
        if(len(face_matches.get('FaceMatches'))) >= 1:
            perfil = dict(nome=face_matches['FaceMatches'][1]['Face']['ExternalImageId'],
                          faceMatch=round(face_matches['FaceMatches'][1]['Similarity'], 2))
            dados_json.append(perfil)
    return dados_json


def publica_dados(dados_json):
    arquivo = s3.Object('fa-site-lambda-model', 'dados.json')
    arquivo.put(Body=json.dumps(dados_json))


def exclui_imagem_colecao(faceId_detectadas):
    client.delete_faces(
        CollectionId='faces',
        FaceIds=faceId_detectadas,
    )


def main(event, context):
    faces_detectadas = detecta_faces()
    faceId_detectadas = cria_lista_faceId_detectadas(faces_detectadas)
    resultado_comparacao = compara_imagens(faceId_detectadas)
    dados_json = gera_dados_json(resultado_comparacao)
    publica_dados(dados_json)
    exclui_imagem_colecao(faceId_detectadas)
    print(json.dumps(dados_json, indent=4))