## To deploy and monitor selenium hub-node on minikube
```bash

$ kubectl create -f hub-deployment.yaml

$ minikube dashboard
# open the url

$ minikube service selenium-hub --url
# open the third url and copy it to testcase.py command_executor

$ kubectl create -f node-chrome-xxx.yaml

```

### To test the images with docker compose
```bash
$ docker compose up

# docker compose down
```

p.s. these image for arm64 only.

***

Reference: https://sahajamit.medium.com/spinning-up-your-own-auto-scalable-selenium-grid-in-kubernetes-part-2-15b11f228ed8