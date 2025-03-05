# ML_ECS_pipeline
A ML containerisation project which makes use of ECS to deploy a streamlit app which can query data from postgres rds in aws which is populated using a automated labmbda function by making use of a NewsAPI

![Architecture](https://github.com/user-attachments/assets/2938ad2e-226a-4c8d-9dbb-e645bd3b9b2b)

In this project

* We are making use of a NewsAPI where we get the latest news articles with help of a API_Key obtained from the news api website
  after creating a developer account

* News articles are extracted with the help of a lambda function which is triggered every 1 hr using Event bridge.

* The raw data extrated are pushed to a S3 bucket and stored in json format
  ![](https://github.com/user-attachments/assets/2bd80cb5-07c5-480b-83ed-6923027f8777)


* News description are then analyzed using the using NLTK python library w.r.t the news article topic and based on the news sentiment a positive or negative score is assigned.
  

* Analyzed  news aritcle are pushed to a rds postgres AWS instance along with timestamp.
  ![](https://github.com/user-attachments/assets/5a9b06f5-5a5b-4972-8f9e-e4abc5d824f5)

* Now a Dashboard is created using Streamlit to visualize the sentiment of the news in local system which is then converted to a docker image and pushed to ECR Registry in AWS.
  ![](https://github.com/user-attachments/assets/ae51ead2-d9b1-4b70-956a-d5e65cae1990)

* The uploaded image is run using a AWS Fargate cluster by create a task definition and using the publicIP and assigned port
  we can access the Streamlit Dashboard.
  ![]

![6](https://github.com/user-attachments/assets/0c81bada-8b71-4890-947b-95638e9f23dd)
