#!/usr/bin/python3
import logging
import boto3
import botocore
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='default')
s3 = session.client('s3')
ses = session.client('ses')

def upload_file(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    try:
        s3.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_file(bucket_name, object_name, file_name):
    try:
        s3.download_file(bucket_name, object_name, file_name)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def website_config(bucket_name, index_file, error_file):
    website_configuration = {
        'ErrorDocument': {'Key': error_file},
        'IndexDocument': {'Suffix': index_file},
    }
    s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

def delete_website_config(bucket_name):
    s3.delete_bucket_website(Bucket=bucket_name)

def create_bucket(bucket_name, location='us-west-2'):
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': location})

def delete_bucket(bucket_name):
    bucket = s3.Bucket(bucket_name)
    bucket.objects.all().delete()

def create_email_template(template_name, subject, text, html):
    response = ses.create_template(
        Template={
            'TemplateName': template_name,
            'SubjectPart': subject,
            'TextPart': text,
            'HtmlPart': html
        }
    )
    print(response)

def get_email_template(template_name):
    response = ses.get_template(
        TemplateName=template_name
    )
    print(response)

def send_email(sender_email, receiver_email, subject, message, attachment):
    ses.send_raw_email(
        Destinations=[],
        FromArn='',
        RawMessage={
            'Data': 'From:' + sender_email + ' \nTo: ' + receiver_email + ' \nSubject:' + subject + '\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary="NextPart"\n\n--NextPart\nContent-Type: text/plain\n\n' + message + '\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename=' + attachment + '',
        },
        ReturnPathArn='',
        Source='',
        SourceArn='',
    )

