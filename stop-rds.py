import botocore
import boto3
from botocore.exceptions import ClientError

rds_client = boto3.client("rds")

def lambda_handler():
  instances = rds_client.describe_db_instances()
  clusters = rds_client.describe_db_clusters()

  for cluster in clusters["DBClusters"]:
    cluster_arn = cluster["DBClusterArn"]
    cluster_identifier = cluster["DBClusterIdentifier"]
    cluster_status = cluster["Status"]
    cluster_attributes = {"arn": cluster_arn, "identifier": cluster_identifier, "status": cluster_status}

    stop_rds(cluster_attributes, "Cluster")

  for instance in instances["DBInstances"]:
    instance_arn = instance["DBInstanceArn"]
    instance_identifier = instance["DBInstanceIdentifier"]
    instance_status = instance["DBInstanceStatus"]
    instance_attributes = {"arn": instance_arn, "identifier": instance_identifier, "status": instance_status}

    stop_rds(instance_attributes, "Instance")

def stop_rds(attributes, rds_type):
  arn = attributes["arn"]
  identifier = attributes["identifier"]
  status = attributes["status"]
  stop_param = {"DB" + rds_type + "Identifier": identifier}

  try:
    rds_tags = rds_client.list_tags_for_resource(ResourceName = arn)
  except ClientError as e:
    print("Problem retreving tags for %s: %s" %(identifier,e))
    return

  no_stopped_tag_bool = True
  for tag in rds_tags["TagList"]:
    if tag["Key"].lower() == "decired-state" and tag["Value"].lower() == "stopped" and status.lower() == "available":
      print("Decired-state tag found with stopped value for %s %s" %(rds_type,identifier))
      try:
        print("Stopping %s RDS instance" %identifier)
        if rds_type == "Instance":
          rds_client.stop_db_instance(**stop_param)
        elif rds_type == "Cluster":
          rds_client.stop_db_cluster(**stop_param)
        print("%s %s stopped successfully" %(rds_type,identifier))
        no_stopped_tag_bool = True
        break
      except ClientError as e:
        print("Stopping %s failed: %s" %(identifier,e))
        return
  if no_stopped_tag_bool:
    print("%s %s isn't in 'Available' state or not 'Decired-state' tag found\n" %(identifier, rds_type))

lambda_handler()