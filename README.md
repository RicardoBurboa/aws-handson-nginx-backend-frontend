# aws-handson-nginx-backend-frontend
Sets up a backend in a private subnet that communicates to the frontend in a public subnet while leveraging Security Groups and Nginx.

## Description
This project creates a backend server in an instance that is located in a private subnet. An RDS Database that uses MySQL is also in this private subnet. The backend establishes communication with the frontend that is located in an instance on a private subnet, while leveraging Nginx. The purpose of this project is to test if a request can be done with an API and also if the frontend can have the data be served through the Internet with a NAT Gateway, Route Table and Internet Gateway.

## Diagram
![NginxBackendFrontend](https://github.com/user-attachments/assets/83ece077-9e18-43df-ae3c-ed242a8404b8)

## Steps
### In Both Public and Private Instances:
1. Create 2 EC2 instances, where one is in a public subnet and the other is in a private subnet. Remember to get both .pem files in order to connect with SSH.
2. Perform `sudo apt-get update` and `sudo apt-get upgrade`.
3. Install Nginx.
### In the Instance that is in the Public Subnet:
4. Edit your `default` with this command: `sudo nano /etc/nginx/sites-available/default`
5. Edit your `html` with this command: `sudo nano /var/www/html/index.html`
6. After you are done, restart Nginx with this command: `sudo systemctl restart nginx`
### In the Instance that is in the Private Subnet:
7. Create a virtual environment for Python and create a `main.py` file that can be edited with this command: `sudo nano /home/USER/main.py`
8. Edit your `default` with this command: `sudo nano /etc/nginx/sites-available/default`
9. Install Flask and Flask CORS in your Python Virtual Environment with this command: `pip install flask-cors flask`
10. Run this command: `nohup python3 main.py > flask.log 2>&1 &`
11. Run this command as well: `ps aux | grep python`
12. After you are done, restart Nginx with this command: `sudo systemctl restart nginx`
13. Run the development server with this command: `python3 main.py`
### Establish Network Configurations
14. Create a NAT Gateway in AWS so your private subnet can get Internet access.
15. Create a Route Table for your NAT Gateway.
### RDS Instance
16. Create an RDS instance that uses MySQL in the private subnet. 
### In the Instance that is in the Public Subnet:
17. Connect the API with the RDS database.
18. Test the API with this command: `curl -v http://PRIVATE-IP-FROM-PRIVATE-INSTANCE/api/hello`

## Result
### "Hello World" Test
![result](https://github.com/user-attachments/assets/8000af35-356d-49ea-8338-f8bdca2350bc)

### Query Result
![WhatsApp Image 2025-02-11 at 4 33 50 PM (1)](https://github.com/user-attachments/assets/619ccf5b-8226-4b02-8c7c-296c3677641d)

## AWS Certifications

### AWS Networking Basics
![awsnb](https://github.com/user-attachments/assets/b6eec38e-f54a-4bc3-8a9f-043907b1338c)

### AWS Networking Practical Approaches
![awsnpa](https://github.com/user-attachments/assets/d95bae46-af28-49ad-8688-345a06a8846b)
