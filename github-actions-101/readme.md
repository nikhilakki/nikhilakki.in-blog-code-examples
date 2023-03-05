<!--
 Copyright (c) 2023 Nikhil Akki
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

## GitHub Actions 101

In this folder we have a sample NodeJS app that prints hello from a unique id. We run this flow on the GitHub Action's server.

- [GitHub Action config yaml](https://github.com/nikhilakki/nikhilakki.in-blog-code-examples/blob/main/.github/workflows/sample.yaml)
```yaml
name: Build and Test

on:
  push:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Use Node.js
        uses: actions/setup-node@v2
        with:
          node-version: 18.x

      - name: Install dependencies
        run: |
          cd github-actions-101 && npm install
          npm run start
```
![GitHub Action screenshot](GitHub%20Actions%20101%20sample.png)

[Article link](https://nikhilakki.in/github-series-actions-101)