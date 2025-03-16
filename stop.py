""" stop.py This module consists code of stopping the ec2 instance  
"""
import boto3

# An EC2 client
ec2 = boto3.client('ec2')

# Stopping the ec2 machine
stop= ec2.stop_instances(
    InstanceIds= [ "i-0642fa659b6fa0364","i-0f8d8a3c9debb95c5"]
)

print("EC2 Instance Stopped")