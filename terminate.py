""" terminate.py This module consists code of terminating the ec2 instance  
"""
import boto3

# An EC2 client
ec2 = boto3.client('ec2')

# Terminating the ec2 machine
stop= ec2.terminate_instances(
    InstanceIds= [ "i-0642fa659b6fa0364","i-0f8d8a3c9debb95c5","i-0d4b224e6148dad37"]
)

print(" EC2 Instance Terminated ")