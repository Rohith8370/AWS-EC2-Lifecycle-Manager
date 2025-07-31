""" run.py This module consists code of creating the ec2 instance  
"""
import boto3

# An EC2 client
ec2 = boto3.client('ec2')

# creating the ec2 machine
Running = ec2.run_instances(
    ImageId= "ami-053b12d3152c0cc71",
    InstanceType= "t2.micro",
    MinCount=1,
    MaxCount=1,
    KeyName= "rohithkrishna"
)

print("EC2 Instance Created" )
