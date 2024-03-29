# TextCompletion-HF

Containerized Web App using Docker, Github Container Registry, FastApi and Huggingface. Uses GPT2 for Text Completion.

## Github Container Registry - GHCR
The workflow in main.yml creates a docker container and pushes it to Github Container Registry. It also creates a package as shown in the right side pane.

## Azure Container Registry - ACR
The workflow in azure-acr.yml creates a docker container and pushes it to Azure Container Registry.

    1. Create a Container Registry on Azure
    2. Open Registry and go to Access Keys under Settings.
    3. Check Admin User check box.
    4. In another window, add Action Secrets in your Github repo as follows.
      - ACR_USERNAME
      - ACR_PASSWORD
    5. Copy the login server from Access Keys page and paste it against {registry:} in yml file.
    6. In the username and password fields in yml file write ${{ secrets.ACR_USERNAME }} and  ${{ secrets.ACR_PASSWORD }}
    7. Enter registry name in tags as well.
    8. Commit and run workflow. This should push a docker container image to container registry in Azure Container Registry.

## DockerHub Container
The workflow in docker-image.yml creates a docker container and pushes it to DockerHub Registry.
    
    1. Create access token in DockerHub
    2. Update Repo Action Secrets and add Dockerhub access token and user name.
    3. Update tags and add repo name in small caps.
    4. Run workflow

## Azure Deployment

    1. Create a Container App from Azure Portal.
    2. Update Ingress from Left Side Panel (Verify Target port. It should be the same as exposed by your app.)
    3. From Settings select Containers and click on Edit and Deploy to change container specs.
    4. Azure Service Principal Registration
        A Service Principal with the following details the AppID, password, and tenant information. Create one with: `az ad sp create-for-rbac -n "REST API Service Principal"` and assign the IAM role for the subscription. Alternatively set the proper role access using the following command (use a real subscription id and replace it):
        
        ```
        az ad sp create-for-rbac --name "CICD" --role contributor --scopes /subscriptions/$AZURE_SUBSCRIPTION_ID --sdk-auth
        ```
        
    5. Add the output in github secrets under AZURE_CREDENTIALS
    6. Configure the yml file in workflows.
    7. If running into trouble, check logs in the portal or use the following with the Azure CLI:
    
    ```
    az containerapp logs  show  --name $CONTAINER_APP_NAME --resource-group $RESOURCE_GROUP_NAME --follow
    ```
    
    Update both variables to match your environment

