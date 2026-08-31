# AWS-Serverless-Employee-Management-System-with-CloudFront-Route-53

1.This project demonstrates a complete AWS serverless event-driven architecture using S3, API Gateway, Lambda, SQS, and DynamoDB.

2.The frontend is hosted on Amazon S3 Static Website Hosting or CloudFront with ACM and WAF. 

3.API Gateway exposes REST endpoints for employee registration and retrieval.

4.Lambda Producer receives requests and sends messages to Amazon SQS for decoupled asynchronous processing. 

5.Lambda Consumer automatically processes SQS messages and stores employee data in DynamoDB.

6.The frontend then retrieves and displays employee records through API Gateway APIs.

7.Built a serverless employee management system on AWS using S3, API Gateway, Lambda, SQS, and DynamoDB with event-driven architecture and REST API integration.
**Project Flow**

1. User opens the frontend website hosted in Amazon S3.

2. User enters employee details and clicks "Add Employee".

3. Frontend sends POST request to API Gateway (/register).

4. API Gateway triggers Lambda Producer function.

5. Lambda Producer pushes employee data into Amazon SQS queue.

6. SQS asynchronously triggers Lambda Consumer function.

7. Lambda Consumer processes the message and stores employee data in DynamoDB.

8. Frontend calls GET /employees API to fetch all employees.

9. API Gateway invokes Lambda function to read data from DynamoDB.

10. Employee records are displayed in the frontend table.

    
Frontend
   ↓
API Gateway
   ↓
Lambda Producer
   ↓
SQS Queue
   ↓
Lambda Consumer
   ↓
DynamoDB
   ↓
Frontend Fetch API



| Service     | Purpose            |
| ----------- | ------------------ |
| Amazon S3   | Frontend hosting   |
| API Gateway | API management     |
| AWS Lambda  | Serverless backend |
| Amazon SQS  | Queue messaging    |
| DynamoDB    | NoSQL database     |
| CloudWatch  | Monitoring & logs  |
Flow
-----------------
Amazon S3: It has UI to input data
API Gateway: S3 cannot connect to Lambda directly hence we use API Gateway, API Gateway will send data to Lambda
employee-producer [This has logic to collect data from API Gateway and send the data to SQS]
employee-consumer [As SQS has data, SQS will trigger this lambda, this lambda has logic to store data in DynamoDB]
get-employees [To list the employees from DynamoDB]
DynamoDB: Stores the data




