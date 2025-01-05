Project Name-> RESTAPI micro service for user management  

description ->
Develop a REST API microservice to handle user management 
functionalities, including user creation, retrieval, update, and deletion. The 
microservice should be independently deployable and scalable. 

Technologies-> Flask(python) 

python code explanation->
In this code we are going to see how to use python libraries like flask , jsonify

For creating API first we have to use a object called app and we should take a sample data for entering the details into this app .After initialising the app we should start creating the end point for our API
For creating the end point of our API we should start with the home route (@app.route('/') 

Lets use methods of REST API
POST->create new subordinate resources (create), 
GET->retrieve resource (read),  
PUT->to update an existing resource (update), 
PATCH->to make a partial update (	Partial Update), 
DELETE->delete the resources (delete), -->CRUD

GET is REST services use the HTTP protocol and the HTTP standard writes it explicitly,The GET method means retrieve whatever information is identified by the Request-URI.
in python code (@app.route('/items', methods=['GET'])) is used to read data  
in python code (@app.route('/items/<int:item_id>', methods=['GET'])) is used to read individual data

POST method is used to send data to a server via API. It also creates subordinate resources,
such as a file in a directory. this post method is used for adding the new item to the existing data  
in python code (@app.route('/items', methods=['POST'])) is used to add new_item 

The PUT method is an HTTP request method used in REST APIs to update an existing resource or create a new resource if it does not already exist.
in python code (@app.route('/items', methods=['PUT'])) is used to update/modify existing data

PATCH method is used to apply partial modifications to a resource. It is typically used when you want to update only a specific part of a resource
in python code (@app.route('/items/<int:item_id>', methods=['PATCH'])) is used to pratially update item according to given item_id

The DELETE method is an HTTP method used to remove or delete a resource from a server. 
It is commonly used to instruct the server to delete a specific resource identified by the provided URL or resource identifier.
in python code (@app.route('/items/<int:item_id>', methods=['DELETE'])) is used to delete item 4

jsonify is used to add message to web 

app.run() is used to run the program and allows us to decide port number  
