import boto3
import time

role_arn = "arn:aws:iam::255327957245:role/IoTAccessRole"
session_name = "test-session"

def assume_role():
    sts_client = boto3.client(
        'sts',
        aws_access_key_id='AKIATW4V3OD6TAERHQUI',        
        aws_secret_access_key='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', 
        region_name='us-east-1'                         
    )

    start_time = time.time()
    response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
    end_time = time.time()

    creds = response['Credentials']
    duration = end_time - start_time
    print(f"Assumed role in {duration:.3f} seconds")
    print("Access Key:", creds['AccessKeyId'])
    print("Secret Key:", creds['SecretAccessKey'])
    print("Session Token:", creds['SessionToken'])

    return creds, duration

if __name__ == "__main__":
    assume_role()


