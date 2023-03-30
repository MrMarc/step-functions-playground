# Working locally with Step Functions

## Running and Debug the lambdas locally

Don't pay attention to the Start-API section, just the `start-lambda`

https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html

`sam build --use-container`

To build the deployment set.

`sam local start-lambda --warm-containers EAGER -d 5890`

Will start the lambdas. EAGER means that all the lambdas will be started and warmed as containers.

The `-d` allows connection for debugging on port 5890

I recommend doing this step on its own to validate that you can in fact debug the lambda on its own. There are different setup steps for VSCode and PyCharm (or other jetbrains products).

## Step Functions Configuration File

https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-config-options.html
See the repository for a sample file - this is a minimal set

LAMBDA_ENDPOINT=http://host.docker.internal:3001 is needed for MACOS version of Docker.

## Step Functions JSON file

NOTE All lambdas MUST have arns they can't use the CloudFormation reference...

i.e. statemachine.json vs statemachine.json.orig

## Running Step Functions

https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-docker.html

1. Start Step Functions Local:

`docker run -p 8083:8083 --env-file aws-stepfunctions-local-credentials.txt amazon/aws-stepfunctions-local`

The port enables a local connection with the aws cli. The env file is from the previous step.

2. If the lambdas aren't running, start them now...

`sam local start-lambda --warm-containers EAGER -d 5890`

3. Create a Step Function

`aws stepfunctions --endpoint http://localhost:8083 create-state-machine --name "HelloWorld" --role-arn "arn:aws:iam::012345678901:role/DummyRole" --definition "$(cat  statemachine.json)"`

This connects to step functions local and creates a state machine ... the Role is a Dummy. The definition reads the file and quotes it.

You should get an arn for the state machine as output.

4. Run the State Machine

Using the arn created in step 4, run the state machine.

`aws stepfunctions --endpoint http://localhost:8083 start-execution --name test1 --state-machine arn:aws:states:ca-central-1:123456789012:stateMachine:HelloWorld`

NOTE: Each new execution requires a new name.

If you have remote debugging set up for each lambda, you will be able to connect to the lambda with your debugger when that lambda is invoked.