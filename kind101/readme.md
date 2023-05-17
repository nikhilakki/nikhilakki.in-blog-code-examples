## Kind: The Container Connoisseur for K8s Conundrums

[Aritcle link](https://nikhilakki.in/kind-the-container-connoisseur-for-k8s-conundrums)

> Author - [Nikhil Akki](https://nikhilakki.in)

### How to run?

- Build container and deploy to Kind
```bash
make build
make load
make k8s-apply
make expose-local
```

#### Tested with Linux & macOS 

- docker v23+
- kind v0.18+
- kubectl
