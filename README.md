# ML_ECS_pipeline
A ML containerisation project which makes use of ECS to deploy a streamlit app which can query data from postgres rds in aws which is populated using a automated labmbda function by making use of a NewsAPI

![Architecture](https://github.com/user-attachments/assets/343cd5cf-76c3-413e-8ee9-a7850f593855)


In this project

* We are making use of a NewsAPI where we get the latest news articles with help of a API_Key obtained from the news api website
  after creating a developer account

* News articles are extracted with the help of a lambda function which is triggered every 1 hr using Event bridge.

* The raw data extrated are pushed to a S3 bucket and stored in json format
  (https://github.com/user-attachments/assets/c6756701-5da8-4da5-b0fd-ad3213f6b868)


* News description are then analyzed using the using NLTK python library w.r.t the news article topic and based on the news sentiment a positive or negative score is assigned.
  ![](https://github.com/ansel9618/ML_ECS_pipeline/blob/main/images/3.0_.png)

* Analyzed  news aritcle are pushed to a rds postgres AWS instance along with timestamp.
  ![](https://github.com/user-attachments/assets/b1f5863a-b7c0-4d5d-910e-294d76c69e98)


  
* Now a Dashboard is created using Streamlit to visualize the sentiment of the news in local system which is then converted to a docker image and pushed to ECR Registry in AWS.
  ![]![11](https://github.com/user-attachments/assets/7eda41c2-fcf8-4c85-b379-dfcc0504d36b)



* The uploaded image is run using a AWS Fargate cluster by create a task definition and using the publicIP and assigned port
  we can access the Streamlit Dashboard.
  !()![6](https://github.com/user-attachments/assets/c024da2f-4202-4ff9-b476-86fd01253b74)

 
