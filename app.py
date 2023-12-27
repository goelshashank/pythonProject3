from flask import Flask
import boto3
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    print("test")

    client = boto3.client('s3')

    session = boto3.Session()

    sts = session.client("sts")
    response = sts.assume_role(
        RoleArn="arn:aws:iam::xxx:role/s3-readonly-access",
        RoleSessionName="learnaws-test-session"
    )

    new_session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                                aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                                aws_session_token=response['Credentials']['SessionToken'])
    s3 = new_session.client("s3")
    s3.list_buckets()


    # Fetch the list of existing buckets
    # clientResponse = client.list_buckets()

   # print(clientResponse['Buckets'][000]['Name'])

  #  bucket='gentechworkbench-dev-us-east-1-xlab'
    # for obj in bucket.objects.all():
    #     key = obj.key
    #     body = obj.get()['Body'].read()
    # result = s3.list_objects(Bucket=bucket, Prefix='/something/')
    # for o in result.get('Contents'):
    #     data = s3.get_object(Bucket=bucket, Key=o.get('Key'))
    #     contents = data['Body'].read()
    #     print(contents.decode("utf-8"))

   # app.run(host='0.0.0.0')


