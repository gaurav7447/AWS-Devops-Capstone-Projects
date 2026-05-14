import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instances = ec2.describe_instances()

    stopped_instances = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            state = instance['State']['Name']
            instance_id = instance['InstanceId']

            if state == "stopped":
                stopped_instances.append(instance_id)

    print("Stopped Instances:", stopped_instances)

    # OPTIONAL: stop running idle instances logic can be added

    return {
        "statusCode": 200,
        "body": f"Stopped instances found: {stopped_instances}"
    }