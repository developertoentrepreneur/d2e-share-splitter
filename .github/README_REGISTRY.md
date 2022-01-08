# Push to registry

Once the container is running, we need to push the image to the registry. How:

- `docker login -u youruser -p yourpassword`
- `docker commit django d2e-sharesplitter-django`
- `docker tag d2e-sharesplitter-django:latest alvarolloret/d2e-sharesplitter-django:latest`
- `docker push alvarolloret/d2e-sharesplitter-django:latest`

# Modify cicd to push to registry 