import json
import random

def handle_guess(secret_number, user_guess):
    if user_guess < secret_number:
        return "Too low! Try a higher number."
    elif user_guess > secret_number:
        return "Too high! Try a lower number."
    else:
        return f"Congratulations! You guessed the number {secret_number} correctly!"

def handler(event, context):
    if event["httpMethod"] == "POST":
        data = json.loads(event["body"])
        user_guess = data["guess"]
        secret_number = data["secret_number"]
        response = handle_guess(secret_number, user_guess)

        return {
            "statusCode": 200,
            "body": json.dumps({"response": response})
        }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method Not Allowed"})
        }
