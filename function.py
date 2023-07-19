import requests
import boto3

# Utilize Instance Metadata

response = requests.get("http://< IP >/latest/meta-data/instance-id")
instance_id = response.text
print("Instance ID:", instance_id)

# Automate Instance Configuration

ec2_client = boto3.client('ec2')

response = ec2_client.modify_instance_attribute(
    InstanceId='your-instance-id',
    Attribute='disableApiTermination',
    Value='true'
)

print("Instance termination protection enabled.")

# Utilize CloudWatch Metrics

cloudwatch_client = boto3.client('cloudwatch')

response = cloudwatch_client.put_metric_alarm(
    AlarmName='CPUUtilization',
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Threshold=80.0,
    AlarmActions=[
        'arn:aws:sns:your-sns-topic-arn'
    ],
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'your-instance-id'
        }
    ]
)

print("CPUUtilization alarm created.")

# Automate Auto Scaling Group Configuration

autoscaling_client = boto3.client('autoscaling')

response = autoscaling_client.update_auto_scaling_group(
    AutoScalingGroupName='your-asg-name',
    MinSize=2,
    MaxSize=5
)

print("Auto Scaling Group updated.")
