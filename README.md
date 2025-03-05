# ML_ECS_pipeline
A ML containerisation project which makes use of ECS to deploy a streamlit app which can query data from postgres rds in aws which is populated using a automated labmbda function by making use of a NewsAPI

![Architecture](https://github.com/user-attachments/assets/0cf00bcd-1355-4d1c-b34c-038d3f7b874e)


In this project

* We are making use of a NewsAPI where we get the latest news articles with help of a API_Key obtained from the news api website
  after creating a developer account

* News articles are extracted with the help of a lambda function which is triggered every 1 hr using Event bridge.

* The raw data extrated are pushed to a S3 bucket and stored in json format
  ![]
  (https://github.com/user-attachments/assets/4bc1ae86-406d-43ce-a7d7-25df17c10e81)

* News description are then analyzed using the using NLTK python library w.r.t the news article topic and based on the news sentiment a positive or negative score is assigned.
  ![]

* Analyzed  news aritcle are pushed to a rds postgres AWS instance along with timestamp.
  ![]()(https://github.com/user-attachments/assets/e20d6541-8e69-4383-8390-f4727b5f61fa)

  
* Now a Dashboard is created using Streamlit to visualize the sentiment of the news in local system which is then converted to a docker image and pushed to ECR Registry in AWS.
  ![](!(https://github.com/user-attachments/assets/3467636d-a7ac-45f6-b9ae-5bef117ff91c)


* The uploaded image is run using a AWS Fargate cluster by create a task definition and using the publicIP and assigned port
  we can access the Streamlit Dashboard.
  ![]()

 ![6](https://github.com/user-attachments/assets/ce6dcb3b-b810-4bdb-9087-eaff915fb31c)

