# aws-handson-nginx-backend-frontend
Sets up a backend in a private subnet that communicates to the frontend in a public subnet while leveraging Security Groups and Nginx.

## Description
WIP.

## Diagram
WIP.

## Steps
### In Both Public and Private Instances:
1. Create 2 EC2 instances, where one is in a public subnet and the other is in a private subnet.
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
### In the Instance that is in the Public Subnet:
14. Test the API with this command: `curl -v http://PRIVATE-IP-FROM-PRIVATE-INSTANCE/api/hello`

## Result
![result](https://github.com/user-attachments/assets/8000af35-356d-49ea-8338-f8bdca2350bc)

## AWS Certifications

### AWS Networking Basics
![awsnb](https://github.com/user-attachments/assets/b6eec38e-f54a-4bc3-8a9f-043907b1338c)

### AWS Networking Practical Approaches
![awsnpa](https://github.com/user-attachments/assets/d95bae46-af28-49ad-8688-345a06a8846b)
