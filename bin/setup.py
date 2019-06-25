import os
import boto3

bin_abs_dir, filename = os.path.split(os.path.abspath(__file__))

data_root = os.path.join(bin_abs_dir, '..', 'data')
data_root = os.path.abspath(data_root)

# These credentials aren't necessarily public, but they
# are also not super sensitive since they have read only
# access to only the umd-cells bucket

AWS_ACCESS_KEY = 'AKIAJUUV26VYLK4Q4QSA'
AWS_SECRET_KEY = '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'

bucket_name = 'umd-cells'

client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

local_input_images = client.Bucket(bucket_name).list('/data/contractility/input/images/')

print local_input_images


