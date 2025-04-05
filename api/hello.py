def handler(event, context):
    # Extract name from query parameters
    name = event.get("queryStringParameters", {}).get("name", "World")

    # Create a response
    response = {
        "statusCode": 200,
        "body": f"Hello, {name}!"
    }

    return response
