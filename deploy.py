import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'manu-908877777778', 'index.html')
