FROM golang:1.21 AS builder
WORKDIR /app
# Copy the Go Modules manifests
COPY go.mod go.sum ./
# cache deps before building and copying source so that we don't need to re-download as much
# and so that source changes don't invalidate our downloaded layer
RUN go mod download
# Copy the go source
COPY *.go ./
# Build
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o kafka-producer
# Use a Docker multi-stage build to create a lean production image.
FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/kafka-producer .
CMD ["/bin/sh", "kafka-producer"]