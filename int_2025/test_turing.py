


Implement a global exception handler for a custom error class.

Requirements:

Define a custom exception InvalidOrderException with fields order_id and reason.
Raise this exception from endpoint /orders/{order_id} if order_id < 1000.
Use FastAPI’s app.exception_handler to handle this globally.
Return a structured JSON response:

{

"error": "Invalid Order",
"order_id": 123,
"reason": "Order ID must be >= 1000"
}


class InvalidOrderException(Exception):
    
    def __str__

app.get("/orders/<>")
def order():
    order_id = request
    try:
        if order_id < 1000:
           raise 
        else:
           result = perform_operation()
    excep InvalidOrderException as e:
        return {
            "error": "Invalid Order",
            "order_id": order_id,
            "reason": "Order ID must be >= 1000"
            }


#################



Implement a custom rate limiter middleware for FastAPI.

Requirements:

Limit each client (by IP) to 5 requests per 10 seconds.
If the limit is exceeded, return 429 Too Many Requests with a message.
Use an in-memory cache (like a Python dict) for tracking counts (no Redis/DB).
Demonstrate with a sample endpoint /data that returns "Request successful".



########################




How does Python manage memory internally (reference counting, garbage collection)?


tune garbage collection ?

How would you detect and fix a memory leak in a long-running Python service?


How does Python handle multithreading given the Global Interpreter Lock (GIL)?


How does Python’s import system and module caching work?



How would you handle circular imports in a large codebase?





######################################




How do you design fault-tolerant systems?


integration, contract testing ?




How do you manage CI/CD pipelines to support rapid and safe releases?


How would you introduce quality gates for production deployment without blocking innovation?




How do you manage technical debt while still delivering on new feature commitments?

How do you ensure accountability and ownership in your team?


How do you handle disagreements or conflicts within the team (technical or personal)?








