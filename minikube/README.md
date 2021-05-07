

TODO: this is outdated and should use an overlay as in the /kubernetes directory

Test environment for minikube



# SAGE namespace and config

```bash
kubectl apply -f sage-ui.Namespace.yaml

kubectl apply -f sage-ui.ConfigMap.yaml

kubectl apply -f ./sage-ui.Secret.yaml
```

# MySQL
```bash
kubectl apply -f ./sage-ui-db.PersistentVolumeClaim.yaml

kubectl apply -f ./sage-ui-db.Deployment.yaml

kubectl apply -f ./sage-ui-db.Service.yaml
```


# SAGE ui
```bash
kubectl apply -f ./sage-ui.Deployment.yaml

kubectl get pod -n sage

kubectl apply -f ./sage-ui.Service.yaml

```

# ingress

```bash
minikube addons enable ingress

kubectl apply -f ./sage-ui.Ingress.yaml
```

# IP address

Get IP address of minikube and open in browser on port 80
```bash
minikube ip
```


# other commands
```bash
kubectl get endpoints -n sage
kubectl get  ingress -n sage

minikube dashboard

```