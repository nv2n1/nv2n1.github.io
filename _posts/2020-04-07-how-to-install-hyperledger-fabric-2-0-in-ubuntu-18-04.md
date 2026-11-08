---
title: "Installing Hyperledger Fabric 2.5 on Ubuntu 24.04 LTS"
date: 2020-04-07 17:44:25 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-hyperledger-fabric-2-0-in-ubuntu-18-04/
---

Hyperledger Fabric is a modular, enterprise-grade consortium blockchain platform. While its official documentation is comprehensive, deploying a test network from scratch requires configuring multiple dependencies and tools—a process that’s time-consuming for new users. This guide covers both automated and manual setup approaches to get a working Fabric network running quickly.

## Prerequisites

You’ll need:

- Ubuntu 24.04 LTS (or compatible Linux distribution)
- A user account with sudo privileges
- At least 8GB RAM and 20GB disk space
- Internet connectivity for downloading binaries and container images

## Quick Installation

The fastest way to get started is using the official bootstrap script:

``` bash
git clone https://github.com/hyperledger/fabric-samples
cd fabric-samples/test-network
curl -sSL https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh | bash -s
./network.sh up
```

If you prefer understanding each step or need to customize your installation, follow the manual steps below.

## Manual Installation Steps

### 1. Install System Dependencies

Update your system and install required packages:

``` bash
sudo apt update
sudo apt install -y git curl wget docker.io docker-compose nodejs npm build-essential python3
```

Add your user to the Docker group to avoid needing sudo for every Docker command:

``` bash
sudo usermod -aG docker $USER
newgrp docker
```

Alternatively, log out and log back in for the group change to take effect.

### 2. Install Go

Fabric requires Go 1.21 or later. Download and install the latest stable version:

``` bash
wget https://go.dev/dl/go1.23.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.23.linux-amd64.tar.gz
rm go1.23.linux-amd64.tar.gz
```

Add Go to your PATH by appending to `~/.bashrc`:

``` bash
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$PATH
```

Reload your shell:

``` bash
source ~/.bashrc
```

Verify the installation:

``` bash
go version
```

### 3. Clone Fabric Samples

Create the directory structure and clone the repository:

``` bash
mkdir -p $GOPATH/src/github.com/hyperledger
cd $GOPATH/src/github.com/hyperledger
git clone https://github.com/hyperledger/fabric-samples.git
cd fabric-samples
git checkout main
```

To use a specific release tag instead of main (e.g., v2.5.0):

``` bash
git checkout v2.5.0
```

### 4. Bootstrap Fabric Binaries and Docker Images

Navigate to the test-network directory and run the bootstrap script:

``` bash
cd test-network
curl -sSL https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh | bash -s
```

This downloads:

- Fabric peer, orderer, and CA binaries
- Fabric Docker images (peer, orderer, ccenv, baseos)
- Chaincode builder images
- Configuration tools (configtxgen, cryptogen, fabric-ca-client)

Verify binaries are available:

``` bash
ls ../bin/
```

You should see: `peer`, `orderer`, `fabric-ca-client`, `configtxgen`, `cryptogen`, and others.

### 5. Start the Test Network

In the test-network directory, bring up the network:

``` bash
./network.sh up
```

This command:

- Generates cryptographic material (certificates and keys)
- Creates orderer and peer containers
- Establishes the Fabric network with two organizations (Org1 and Org2)
- Sets up a basic channel infrastructure

Verify the network is running:

``` bash
docker ps
```

You should see three containers: one orderer node (`orderer.example.com`) and two peer nodes (`peer0.org1.example.com` and `peer0.org2.example.com`).

### 6. Create a Channel

``` bash
./network.sh createChannel -c mychannel
```

Wait for the output confirming “Channel ‘mychannel’ created.” Verify by checking the peer logs:

``` bash
docker logs peer0.org1.example.com
```

### 7. Deploy Chaincode

Deploy the sample FabCar chaincode:

``` bash
./network.sh deployCC -l go -ccn fabcar -ccv 1
```

Supported languages:

- Go: `-l go`
- JavaScript: `-l javascript`
- Java: `-l java`
- TypeScript: `-l typescript`

The deployment process includes:

- Installing the chaincode on peer nodes
- Approving the chaincode definition per organization
- Committing the chaincode definition to the channel
- Invoking the init function

This can take 1-2 minutes depending on system resources. Monitor progress with:

``` bash
docker logs peer0.org1.example.com -f
```

### 8. Interact with the Chaincode

Before running peer commands, set environment variables to point to the correct organization:

``` bash
export PATH=${PWD}/../bin:$PATH
export FABRIC_CFG_PATH=${PWD}/../config
export CORE_PEER_TLS_ENABLED=true
export CORE_PEER_LOCALMSPID=Org1MSP
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_ADDRESS=localhost:7051
```

Query the ledger:

``` bash
peer chaincode query -C mychannel -n fabcar -c '{"Args":["queryAllCars"]}'
```

Expected output: a JSON array of cars (initially empty for a new chaincode).

Invoke a transaction to create a new car:

``` bash
peer chaincode invoke -C mychannel -n fabcar \
  -c '{"Args":["createCar","CAR10","Honda","Civic","white","Alice"]}'
```

Query the car you just created:

``` bash
peer chaincode query -C mychannel -n fabcar \
  -c '{"Args":["queryCar","CAR10"]}'
```

To switch to Org2, update the environment variables:

``` bash
export CORE_PEER_LOCALMSPID=Org2MSP
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
export CORE_PEER_ADDRESS=localhost:9051
```

## Stopping and Cleaning Up

To bring down the network without removing generated artifacts:

``` bash
./network.sh down
```

To perform a complete cleanup, including removing generated certificates and channel artifacts:

``` bash
./network.sh down -c
```

To remove all Docker containers and volumes associated with Fabric:

``` bash
docker-compose down -v
docker volume rm $(docker volume ls -f label=com.docker.compose.project=test-network -q)
```

## Troubleshooting

### Docker permission denied errors

Ensure your user is in the docker group and you’ve relogged or run `newgrp docker`. Verify with:

``` bash
groups $USER
```

### Port already in use

If ports 7050, 7051, 9051, or 9052 are in use, either stop the conflicting services or modify the `docker-compose.yaml` file to use different ports. Check which process is using a port:

``` bash
sudo lsof -i :7051
```

### Chaincode installation failures

Verify Go is properly installed and `$GOPATH` is set correctly:

``` bash
go env GOPATH
which peer
```

Check that the chaincode directory structure is valid. For Go chaincodes, ensure `go.mod` exists in the chaincode directory and dependencies are resolvable.

### Container startup failures

Review Docker logs to diagnose issues:

``` bash
docker logs orderer.example.com
docker logs peer0.org1.example.com
```

Ensure you have sufficient disk space and RAM:

``` bash
df -h
free -h
```

### Module resolution errors during chaincode deployment

When deploying Go chaincodes, verify `go.mod` exists in the chaincode directory and contains correct dependency versions. If using external modules, ensure they’re publicly accessible.

### Network connectivity issues

If bootstrap fails, verify internet connectivity and that GitHub is accessible:

``` bash
curl -I https://github.com
```

## Next Steps

- Review the Fabric documentation for deeper configuration details
- Explore the FabCar chaincode implementation to understand Fabric contract patterns
- Deploy custom chaincode in your preferred language
- Set up additional organizations and configure custom endorsement policies
- Use Fabric SDKs (Go, Node.js, Java) to build client applications
- Configure CouchDB as the state database for more complex queries
- Implement access control using attributes in Fabric CA
