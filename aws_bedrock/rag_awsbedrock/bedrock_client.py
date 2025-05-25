import boto3
import json

class BedrockClient:
    def __init__(self, region_name='us-east-1'):
        """
        Initialize the AWS Bedrock boto3 client.
        :param region_name: AWS region where Bedrock is available.
        """
        self.client = boto3.client('bedrock', region_name=region_name)

    def invoke_model(self, modelId, input_text):
        """
        Invoke a Bedrock model with the given input text.
        :param modelId: The Bedrock model identifier.
        :param input_text: The input text to send to the model.
        :return: The model's response as a string.
        """
        response = self.client.invoke_model(
            modelId=modelId,
            body=json.dumps({"inputText": input_text}),
            contentType='application/json',
            accept='application/json'
        )
        response_body = response['body'].read()
        response_json = json.loads(response_body)
        return response_json.get('results', [{}])[0].get('outputText', '')

if __name__ == "__main__":
    # Example usage
    bedrock = BedrockClient(region_name='us-east-1')
    model_id = "anthropic.claude-v1"  # Example model ID, replace with actual model ID
    input_text = "Hello, AWS Bedrock!"
    output = bedrock.invoke_model(model_id, input_text)
    print("Model output:", output)
