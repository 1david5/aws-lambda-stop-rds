import botocore
import boto3
from botocore.exceptions import ClientError

def lambda_handler():
  rds_client = boto3.client('rds')

  # Variable definitions

  instances = rds_client.describe_db_instances()

  for instance in instances['DBInstances']:
    instance_arn = instance['DBInstanceArn']
    instance_identifier = instance['DBInstanceIdentifier']
    # print(instance_arn)
    # print(instance_identifier)
    # Getting RDS tags

    try:
      instance_tags = rds_client.list_tags_for_resource(ResourceName = instance_arn)
    except ClientError as e:
      print('Problem retreving tags for %instance_identifier: %s' %instance_identifier %e)
      return
    # print(instance_tags['TagList'])

    for tag in instance_tags['TagList']:
      if tag['Key'] == 'Decired-state' and tag['Value'] == 'stopped':
        print('Decired-state tag found with stopped value for instance %s' %instance_identifier)
        try:
          print('Stopping %s RDS instance' %instance_identifier)
          # stopping = rds_client.stop_db_instance(DBInstanceIdentifier = instance_identifier)
          # print(stopping)
          print('Instance stopped successfully')
          break
        except ClientError as e:
          print('Stopping %s instance failed: %s' %instance_identifier %e)
          return
      else:
        print('None Decired-state tag found with stopped value for %s instance' %instance_identifier)

lambda_handler()