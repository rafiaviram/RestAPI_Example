# RestAPI_Example

# In this implementation, we first prompt the user to enter a number between 1 and 99 (inclusive) using a while loop that keeps asking until a valid input is received. 

# Then, we send that number of requests to the RandomUser API using a for loop that iterates num_requests times.

# For each request, we send a GET request to the API using the requests library, and check if the response is OK. 

# If it is, we extract the name of the first user from the response using JSON parsing, and print it along with the index of the request. 

# If the response is not OK, we print an error message with the status code returned by the server.

# Note that the RandomUser API returns a random user with each request, so the names printed by this script will be different each time it is run.
