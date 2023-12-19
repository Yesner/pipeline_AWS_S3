# Import necessary libraries
import boto3 # Step 1: Establish the boto3 s3 Client

s3 = boto3.client('s3')

# suggested continued learning: this function can be modified to be fully dynamic
def load_data(sales_df):
    """
    Load transformed data into respective S3-AWS

    """

    # Load the DataFrame into the database as a new table
    sales_key = 'traffic/sales.csv'
    data = s3.upload_file(Filename=sales_df, Bucket=bucket_name, Key=sales_key)

    print('Data successfully written to S3.')


