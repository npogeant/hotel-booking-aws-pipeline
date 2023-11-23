# An AWS Sagemaker Pipeline for Hotel Bookings Classification

The SageMaker Pipeline for Hotel Bookings Classification is designed to streamline the end-to-end machine learning workflow, from data preparation to model deployment. The pipeline uses a [hotel bookings classification dataset](https://www.sciencedirect.com/science/article/pii/S2352340918315191), stored in Amazon S3, for training and evaluation. GitHub serves as the version control system for code management.

## Stack Architecture

<p align="center">
  <img src="bookings-stack.svg" alt="Stack">
</p>

## Main Elements:

#### 1. Data Storage (Amazon S3):
Raw and processed datasets are stored in Amazon S3 buckets, providing scalable and secure data storage. This ensures accessibility and reproducibility throughout the pipeline.

#### 2. Version Control (GitHub):
GitHub is used for versioning the machine learning code and pipeline configuration. This enables collaborative development, code review, and seamless integration with continuous integration systems.

#### 3. SageMaker Instances and Concepts:
- **SageMaker Processing**: Preprocessing and feature engineering are performed using SageMaker Processing, ensuring consistency between training and inference data.

- **SageMaker Training**: Model training is executed on SageMaker instances, leveraging the distributed computing power to expedite the process.

- **SageMaker Model/Registry**: The trained model is encapsulated as a SageMaker Model artifact, ready for deployment.

- **SageMaker Endpoint**: A SageMaker Endpoint serves as the inference endpoint for deploying the model, making it accessible for real-time predictions.

#### 4. SageMaker Clarify for Bias and Explainability Metrics:

SageMaker Clarify is integrated to assess and mitigate bias in the model. Additionally, it provides explainability metrics to enhance model interpretability. This ensures that the machine learning model not only delivers accurate predictions but is also transparent and fair.

#### 5. Lambda Function for Deployment:

The Lambda function orchestrates the deployment process into a SageMaker Endpoint.

### Workflow:
- **Data Preparation**: Raw data stored in S3 is preprocessed using SageMaker Processing, creating a clean dataset for training.

- **Model Training**: The training script, version-controlled on GitHub, is executed on SageMaker instances, producing a trained model.

- **Model Evaluation**: Evaluation metrics are computed, and the deployment decision is based on whether they meet the specified threshold.

- **Deployment Automation**: The Lambda function automates the deployment process.

## Improvements

1. **Real CI/CD**:
Implement a robust continuous integration (CI) system using services like AWS CodePipeline. This ensures automatic building, testing, and validation of the pipeline whenever changes are pushed to the repository.

2. **Unit Testing**:
Develop and include comprehensive unit tests for each component of the pipeline. This ensures the correctness of each step and facilitates early detection of issues during development.

3. **Automatic Launch on New Data**:
Enable automatic triggering of the pipeline upon the arrival of new data. Utilize AWS CloudWatch Events or a similar event-driven architecture to detect data changes and initiate the pipeline accordingly.

4. **Pipeline Flexibility with Different Models**:
Generalize the pipeline to support multiple machine learning models, not limited to XGBoost. Parameterize the model type and version to facilitate easy model swapping without extensive code modifications.

5. **Multiple Branches for Staging and Production**:
Implement a branching strategy in the version control system to support distinct environments such as staging and production. Each branch should have its configuration and parameters for the SageMaker Pipeline.

6. **Automated Deployment to Staging/Production**:
Extend the CI/CD pipeline to automatically deploy the pipeline to staging and production environments post successful testing. This ensures a consistent and reliable deployment process.

7. **Monitoring and Logging**:
Enhance the logging and monitoring capabilities of the pipeline by integrating with services like AWS CloudWatch Logs and CloudWatch Metrics. This provides insights into performance and aids in proactive issue detection.