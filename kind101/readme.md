## [Kind: The Container Connoisseur for K8s Conundrums](https://nikhilakki.in/kind-the-container-connoisseur-for-k8s-conundrums)

### How to run?

- Install
    - [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
    - [Docker](https://nikhilakki.in/preview/640061db28849c00086c2e2d)
    - [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- Build container and deploy to Kind
    ```bash
    # Step 1: Build docker image
    make build
    # Step 2: Load docker image to kind repo
    make load
    # Step 3: Run kubectl to apply k8s.yaml config
    make k8s-apply
    # Step 4: Expose service to local on port 8080 (http://localhost:8080/)
    make expose-local
    ```

#### Tested with Linux & macOS 

- docker v23+
- kind v0.18+
- kubectl


[Aritcle link](https://nikhilakki.in/kind-the-container-connoisseur-for-k8s-conundrums)

> Author - [Nikhil Akki](https://nikhilakki.in)
