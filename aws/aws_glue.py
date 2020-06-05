import boto3
glue = boto3.client(service_name='glue', region_name='us-west-2', endpoint_url='https://glue.us-west-2.amazonaws.com')
my_job = glue.create_job(Name="stock_screener_get_company_data",
                Role='stockscreener_role_glue_s3', Command={'Name':'pythonshell',
                'ScriptLocation':'s3://stock-screener-relive/scripts/script_company_data.py'},
                DefaultArguments={'--extra-py-files': 's3://stock-screener-relive/scripts/site-packages/bs4.zip, s3://stock-screener-relive/scripts/site-packages/yahoo_fin.zip'})
myNewJobRun = glue.start_job_run(JobName=my_job['Name'])