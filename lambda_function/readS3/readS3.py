import json
import boto3

# This py reads names of the S3 buckets by running a Lambda function
# Ensure that the Lambda function has the right role
## Can be editted from "Basic Seeings, Execution role, Use an existing role" 
## and select the role that has "AmazonS3FullAccess and AWSLambda Execute" Policies, for lab activities

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket_list = []
    for bucket_list in s3.buckets.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    return {
        'statusCode': 200,
        'body': bucket_list
    }