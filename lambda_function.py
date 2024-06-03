from lambda_util.lambda_genai_util.TextCompletionUtil import generate_text_completion
from lambda_util.lambda_genai_util.prompt_service import run_service


def lambda_handler(event, context):
    """
    This block of code demonstrates how to invoke methods for generating text completions
    and running a prompt service flow based on service ID which it verifies from prompt_store.yaml file.


    example:

    If we want to directly use the FM API
    print(generate_text_completion(event['model'], event['prompt']))

    If we want to use existing prompt flow
    if "prompt_input" in event:
        print(prompt_service.run_service("getMathDetails", event['model'], event["prompt_input"]))


    1. The first line generates a text completion using the model and prompt provided in the event,
       and prints the result.
    2. The if-statement checks if the 'prompt_input' key exists in the event.
       If it does, it runs the 'getMathDetails' service using the model and prompt input from the event,
       and prints the result.    

    """



    # Run the prompt service flow if 'prompt_input' key exists in the event  
    if "prompt_input" in event:
        print(run_service("getMathDetails", event['model'], event["prompt_input"]))  


    # Generate text completion using the model and prompt from the event
    print(generate_text_completion(event['model'], event['prompt']))




    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }