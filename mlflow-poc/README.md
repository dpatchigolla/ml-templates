
## Perform below steps to get started:

Install virtualenv if it isnt available
> pip install virtualenv

Create a virtualenv called mlflow-poc and activate it
> virtualenv mlflow-poc

> source mlflow-poc/bin/activate

Install dependencies
> pip install mlflow gunicorn pandas sklearn xgboost boto3

Downlaod sample data using wget. If wget isn't available, install it first (using brew in macOS)
> brew install wget

> wget -N https://sagemaker-sample-data-us-west-2.s3-us-west-2.amazonaws.com/autopilot/direct_marketing/bank-additional.zip

Unzip sample data
> unzip -o bank-additional.zip

Note:
In MacOS, if there is an error saying xgboost image not found, do the following:
> brew install libomp

Once setup is done, run the python script:
> python train_xgboost.py

Post that, launch the mlflow UI to check the model params:
> mlflow ui

