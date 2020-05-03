{'DBInstances': [
        {'DBInstanceIdentifier': 'b6odb30', 'DBInstanceClass': 'db.t3.xlarge', 'Engine': 'oracle-se2', 'DBInstanceStatus': 'available', 'MasterUsername': 'mysys', 'DBName': 'B6ODB30', 'Endpoint': {'Address': 'b6odb30.c6mkbuzeqxcs.us-east-1.rds.amazonaws.com', 'Port': 1521, 'HostedZoneId': 'Z2R2ITUGPM61AM'
            }, 'AllocatedStorage': 2000, 'InstanceCreateTime': datetime.datetime(2020,
            3,
            27,
            23,
            44,
            7,
            430000, tzinfo=tzutc()), 'PreferredBackupWindow': '04: 58-05: 28', 'BackupRetentionPeriod': 0, 'DBSecurityGroups': [], 'VpcSecurityGroups': [
                {'VpcSecurityGroupId': 'sg-0a59495b4957c4fc5', 'Status': 'active'
                },
                {'VpcSecurityGroupId': 'sg-0ac81693efc97d0ee', 'Status': 'active'
                }
            ], 'DBParameterGroups': [
                {'DBParameterGroupName': 'oracle-parameters-se-19-rds', 'ParameterApplyStatus': 'in-sync'
                }
            ], 'AvailabilityZone': 'us-east-1a', 'DBSubnetGroup': {'DBSubnetGroupName': 'db-subnet-group', 'DBSubnetGroupDescription': 'db-subnet-group', 'VpcId': 'vpc-0c73efa103848edbc', 'SubnetGroupStatus': 'Complete', 'Subnets': [
                    {'SubnetIdentifier': 'subnet-0b548cb1560c6df49', 'SubnetAvailabilityZone': {'Name': 'us-east-1a'
                        }, 'SubnetStatus': 'Active'
                    },
                    {'SubnetIdentifier': 'subnet-0c184d5d17abd129f', 'SubnetAvailabilityZone': {'Name': 'us-east-1b'
                        }, 'SubnetStatus': 'Active'
                    }
                ]
            }, 'PreferredMaintenanceWindow': 'sun: 04: 01-sun: 04: 31', 'PendingModifiedValues': {}, 'MultiAZ': False, 'EngineVersion': '19.0.0.0.ru-2020-01.rur-2020-01.r1', 'AutoMinorVersionUpgrade': True, 'ReadReplicaDBInstanceIdentifiers': [], 'LicenseModel': 'license-included', 'OptionGroupMemberships': [
                {'OptionGroupName': 'oracle-option-groups-se19-rds', 'Status': 'in-sync'
                }
            ], 'CharacterSetName': 'AL32UTF8', 'PubliclyAccessible': False, 'StorageType': 'gp2', 'DbInstancePort': 0, 'StorageEncrypted': True, 'KmsKeyId': 'arn:aws:kms:us-east-1: 432081807973:key/b7f85338-580a-4773-aed8-d1ccdf06b81d', 'DbiResourceId': 'db-EILGCSO2I3VGWDR2U33EH7EXCU', 'CACertificateIdentifier': 'rds-ca-2019', 'DomainMemberships': [], 'CopyTagsToSnapshot': False, 'MonitoringInterval': 60, 'EnhancedMonitoringResourceArn': 'arn:aws:logs:us-east-1: 432081807973:log-group:RDSOSMetrics:log-stream:db-EILGCSO2I3VGWDR2U33EH7EXCU', 'MonitoringRoleArn': 'arn:aws:iam: : 432081807973:role/rds-monitoring-role', 'DBInstanceArn': 'arn:aws:rds:us-east-1: 432081807973:db:b6odb30', 'IAMDatabaseAuthenticationEnabled': False, 'PerformanceInsightsEnabled': True, 'PerformanceInsightsKMSKeyId': 'arn:aws:kms:us-east-1: 432081807973:key/b7f85338-580a-4773-aed8-d1ccdf06b81d', 'EnabledCloudwatchLogsExports': ['alert', 'audit', 'listener', 'trace'
            ], 'DeletionProtection': True, 'AssociatedRoles': [
                {'RoleArn': 'arn:aws:iam: : 432081807973:role/test-role2', 'FeatureName': 'S3_INTEGRATION', 'Status': 'ACTIVE'
                }
            ]
        },
        {'DBInstanceIdentifier': 'b6odb31', 'DBInstanceClass': 'db.t3.xlarge', 'Engine': 'oracle-se2', 'DBInstanceStatus': 'available', 'MasterUsername': 'mysys', 'DBName': 'B6ODB31', 'Endpoint': {'Address': 'b6odb31.c6mkbuzeqxcs.us-east-1.rds.amazonaws.com', 'Port': 1521, 'HostedZoneId': 'Z2R2ITUGPM61AM'
            }, 'AllocatedStorage': 2499, 'InstanceCreateTime': datetime.datetime(2020,
            3,
            27,
            23,
            45,
            19,
            404000, tzinfo=tzutc()), 'PreferredBackupWindow': '08: 06-08: 36', 'BackupRetentionPeriod': 0, 'DBSecurityGroups': [], 'VpcSecurityGroups': [
                {'VpcSecurityGroupId': 'sg-0a59495b4957c4fc5', 'Status': 'active'
                },
                {'VpcSecurityGroupId': 'sg-0ac81693efc97d0ee', 'Status': 'active'
                }
            ], 'DBParameterGroups': [
                {'DBParameterGroupName': 'oracle-parameters-se-19-rds', 'ParameterApplyStatus': 'in-sync'
                }
            ], 'AvailabilityZone': 'us-east-1a', 'DBSubnetGroup': {'DBSubnetGroupName': 'db-subnet-group', 'DBSubnetGroupDescription': 'db-subnet-group', 'VpcId': 'vpc-0c73efa103848edbc', 'SubnetGroupStatus': 'Complete', 'Subnets': [
                    {'SubnetIdentifier': 'subnet-0b548cb1560c6df49', 'SubnetAvailabilityZone': {'Name': 'us-east-1a'
                        }, 'SubnetStatus': 'Active'
                    },
                    {'SubnetIdentifier': 'subnet-0c184d5d17abd129f', 'SubnetAvailabilityZone': {'Name': 'us-east-1b'
                        }, 'SubnetStatus': 'Active'
                    }
                ]
            }, 'PreferredMaintenanceWindow': 'sat: 05: 50-sat: 06: 20', 'PendingModifiedValues': {}, 'MultiAZ': False, 'EngineVersion': '19.0.0.0.ru-2020-01.rur-2020-01.r1', 'AutoMinorVersionUpgrade': True, 'ReadReplicaDBInstanceIdentifiers': [], 'LicenseModel': 'license-included', 'OptionGroupMemberships': [
                {'OptionGroupName': 'oracle-option-groups-se19-rds', 'Status': 'in-sync'
                }
            ], 'CharacterSetName': 'AL32UTF8', 'PubliclyAccessible': False, 'StorageType': 'gp2', 'DbInstancePort': 0, 'StorageEncrypted': True, 'KmsKeyId': 'arn:aws:kms:us-east-1: 432081807973:key/b7f85338-580a-4773-aed8-d1ccdf06b81d', 'DbiResourceId': 'db-LTOAXATV7MBF6FF2QLDPJDIY7I', 'CACertificateIdentifier': 'rds-ca-2019', 'DomainMemberships': [], 'CopyTagsToSnapshot': False, 'MonitoringInterval': 60, 'EnhancedMonitoringResourceArn': 'arn:aws:logs:us-east-1: 432081807973:log-group:RDSOSMetrics:log-stream:db-LTOAXATV7MBF6FF2QLDPJDIY7I', 'MonitoringRoleArn': 'arn:aws:iam: : 432081807973:role/rds-monitoring-role', 'DBInstanceArn': 'arn:aws:rds:us-east-1: 432081807973:db:b6odb31', 'IAMDatabaseAuthenticationEnabled': False, 'PerformanceInsightsEnabled': True, 'PerformanceInsightsKMSKeyId': 'arn:aws:kms:us-east-1: 432081807973:key/b7f85338-580a-4773-aed8-d1ccdf06b81d', 'EnabledCloudwatchLogsExports': ['alert', 'audit', 'listener', 'trace'
            ], 'DeletionProtection': True, 'AssociatedRoles': [
                {'RoleArn': 'arn:aws:iam: : 432081807973:role/rds-s3-integration-role', 'FeatureName': 'S3_INTEGRATION', 'Status': 'ACTIVE'
                }
            ], 'MaxAllocatedStorage': 2500
        }
    ], 'ResponseMetadata': {'RequestId': 'e67018af-6af2-46c5-b135-eaa5f4d455c5', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e67018af-6af2-46c5-b135-eaa5f4d455c5', 'content-type': 'text/xml', 'content-length': '10466', 'vary': 'accept-encoding', 'date': 'Fri,
            01 May 2020 17: 09: 55 GMT'
        }, 'RetryAttempts': 0
    }
}