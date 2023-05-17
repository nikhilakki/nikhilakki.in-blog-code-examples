build:
	docker build . -t pyapp:latest

load:
	kind load docker-image pyapp:latest

k8s-apply:
	kubectl apply -f k8s.yaml

k8s-cleanup:
	kubectl delete deployments --all
	kubectl delete service --all

expose-local:
	kubectl port-forward service/bottle-app-service 8080:80

up:
	docker run --rm -p 8080:8080 pyapp:latest
