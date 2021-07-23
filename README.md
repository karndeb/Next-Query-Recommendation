# Next Query Recommendation

This is a sample application called Next Query Recommendation based on sentence similarity to predict the top next similar queries to users. The application is used to test out AWS MLOP pipeline which includes CI/CD using CodeCommit, CodeDeploy, CodePipeline. The application is dockerized and pushed into ECR which is used as the image repository. The application is finally deployed on AWS EKS Fargate.

Refer the following scripts to understand the different components

- aws-kube-cd/BuildSpec.yaml -> The CodePipeline buildspec yaml file for CI/CD. It has the install, pre-build, build and post build phases

- aws-kube-cd/prereq.sh -> The bash script to install the prerequisites on the os image. It has scripts to install kubectl, eksctl, aws-iam-authenticator, AWS CLI

- aws-kube-cd/get-image-tag.sh -> The bash sript to generate the image tag dynamically

- Dockerfile -> Docker file defiing the entry point

- nqr-deployment.yaml -> The EKS Fargate defining all the required manifests like Deployment, service and ingress for load balancing

- start.sh ->  Bash script to build the image and run the docker container. 
