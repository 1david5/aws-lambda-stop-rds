import botocore
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
  rds_client = boto3.client('rds')

  # Variable definitions

  instance_identifier = event['detail']['SourceIdentifier']
  instance_arn = event['detail']['SourceArn']
  instance_state = event['detail']['Message'].split(' ')[-1]
  print ('The instace %s is in %s state' %(instance_identifier,instance_state))

  # Getting RDS tags
  try:
    state_tag = rds_client.list_tags_for_resource(
      ResourceName = instance_arn,
    )
  except ClientError as e:
    print('Problem retreving tags: %s' %e)
    return

  for tag in state_tag['TagList']:
    if tag['Key'] == 'Decired-state' and tag['Value'] ==   'stopped':
      print("Decired-state tag found")
      try:
        print('Stopping %s RDS instance' %instance_identifier)
        stopping = rds_client.stop_db_instance(
              DBInstanceIdentifier=instance_identifier
          )
        print(stopping)
        print('Instance stopped successfully')
        return
      except ClientError as e:
        print('Stopping instance failed: %s' %e)
        return
  return