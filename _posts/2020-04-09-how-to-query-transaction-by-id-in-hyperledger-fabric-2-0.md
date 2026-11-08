---
title: "Query Transaction Details by ID in Hyperledger Fabric"
date: 2020-04-09 07:48:29 +0000
layout: post
canonical: https://www.systutorials.com/how-to-query-transaction-by-id-in-hyperledger-fabric-2-0/
---

Querying transaction details from a Hyperledger Fabric ledger is critical for auditing, compliance verification, and debugging chaincode behavior. The QSCC (Query System Chaincode) provides the `GetTransactionByID` function to retrieve complete transaction metadata including endorsements, read/write sets, and validation status.

This guide uses Hyperledger Fabric 2.5+ on Ubuntu 24.04 LTS with the test-network from fabric-samples.

## Environment Setup

Navigate to the test-network directory:

``` bash
cd $GOPATH/src/github.com/hyperledger/fabric-samples/test-network
```

Configure environment variables:

``` bash
export FABRIC_CFG_PATH=../config/
source scripts/envVar.sh
setGlobals 1
```

The `setGlobals` function sets peer connection variables for a specific organization. Verify the configuration:

``` bash
echo $CORE_PEER_ADDRESS
echo $CORE_PEER_TLS_ROOTCERT_FILE
```

## Create a Transaction to Query

First, invoke a chaincode to generate a transaction. Using the fabcar example:

``` bash
peer chaincode invoke \
  -o localhost:7050 \
  --ordererTLSHostnameOverride orderer.example.com \
  --tls \
  --cafile "$ORDERER_CA" \
  -C mychannel \
  -n fabcar \
  -c '{"function":"CreateCar","Args":["abc","makeM","modelX","red","ownerO"]}' \
  --waitForEvent
```

The output includes the transaction ID in the response:

    2024-11-15 10:58:38.703 UTC [chaincodeCmd] ClientWait -> INFO 001 txid [fa0f757bc278fdf6a32d00975602eb853e23a86a156781588d99ddef5b80720f] committed with status (VALID) at localhost:7051

Save the transaction ID (the 64-character hex string) for subsequent queries.

## Query Transaction by ID

Use QSCC to retrieve the transaction details:

``` bash
peer chaincode invoke \
  -o localhost:7050 \
  --ordererTLSHostnameOverride orderer.example.com \
  --tls \
  --cafile "$ORDERER_CA" \
  -C mychannel \
  -n qscc \
  -c '{"function":"GetTransactionByID","Args":["mychannel","fa0f757bc278fdf6a32d00975602eb853e23a86a156781588d99ddef5b80720f"]}'
```

The response contains the transaction data as a serialized protobuf:

    2024-11-15 10:06:46.297 UTC [chaincodeCmd] chaincodeInvokeOrQuery -> INFO 001 Chaincode invoke successful. result: status:200 payload:"..."

## Understanding the Transaction Response

The `GetTransactionByID` function returns a `peer.ProcessedTransaction` protobuf containing:

- **Transaction ID**: Unique 64-character hex identifier
- **Channel ID**: Channel where the transaction committed
- **Endorsements**: Digital signatures from endorsing peers
- **Read Set**: Data items the transaction accessed
- **Write Set**: Data items the transaction modified
- **Validation Code**: Transaction status (VALID=0, INVALID_ENDORSEMENT_POLICY=12, UNKNOWN=255)
- **Timestamp**: Block timestamp when committed

## Parse the Transaction Payload

Extract the hex payload and deserialize it programmatically.

### Using Go

``` go
package main

import (
    "encoding/hex"
    "fmt"
    "github.com/hyperledger/fabric-protos-go/peer"
    "google.golang.org/protobuf/proto"
)

func parseTransaction(payloadHex string) (*peer.ProcessedTransaction, error) {
    payloadBytes, err := hex.DecodeString(payloadHex)
    if err != nil {
        return nil, fmt.Errorf("decode error: %w", err)
    }

    tx := &peer.ProcessedTransaction{}
    err = proto.Unmarshal(payloadBytes, tx)
    if err != nil {
        return nil, fmt.Errorf("unmarshal error: %w", err)
    }
    return tx, nil
}

func main() {
    // payloadHex from peer chaincode invoke response
    tx, err := parseTransaction(payloadHex)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Validation Code: %d\n", tx.ValidationCode)
    if tx.TransactionEnvelope != nil {
        fmt.Println("Transaction envelope present")
    }
}
```

### Using Python

``` python
from hyperledger_fabric_protos.peer import transaction_pb2
import binascii

def parse_transaction(payload_hex):
    try:
        payload_bytes = binascii.unhexlify(payload_hex)
        tx = transaction_pb2.ProcessedTransaction()
        tx.ParseFromString(payload_bytes)
        return tx
    except Exception as e:
        print(f"Parse error: {e}")
        return None

def extract_transaction_details(tx):
    if tx:
        print(f"Validation Code: {tx.validationCode}")
        if tx.transactionEnvelope:
            print("Transaction envelope present")
            # Process transaction further
```

### Using jq and Command Line Tools

Extract the payload hex and convert to binary:

``` bash
peer chaincode invoke \
  -o localhost:7050 \
  --ordererTLSHostnameOverride orderer.example.com \
  --tls \
  --cafile "$ORDERER_CA" \
  -C mychannel \
  -n qscc \
  -c '{"function":"GetTransactionByID","Args":["mychannel","<TXID>"]}' | \
  jq -r '.payload' > transaction.hex

xxd -r -p < transaction.hex > transaction.bin
```

You can then inspect the binary file with a protobuf viewer or custom parsing logic.

## Query Across Multiple Organizations

To verify transaction data consistency across organizations, query each peer separately:

``` bash
# Query from Org1
setGlobals 1
peer chaincode invoke \
  -o localhost:7050 \
  --ordererTLSHostnameOverride orderer.example.com \
  --tls \
  --cafile "$ORDERER_CA" \
  -C mychannel \
  -n qscc \
  -c '{"function":"GetTransactionByID","Args":["mychannel","fa0f757bc278fdf6a32d00975602eb853e23a86a156781588d99ddef5b80720f"]}'

# Query from Org2
setGlobals 2
peer chaincode invoke \
  -o localhost:7050 \
  --ordererTLSHostnameOverride orderer.example.com \
  --tls \
  --cafile "$ORDERER_CA" \
  -C mychannel \
  -n qscc \
  -c '{"function":"GetTransactionByID","Args":["mychannel","fa0f757bc278fdf6a32d00975602eb853e23a86a156781588d99ddef5b80720f"]}'
```

Transaction data is identical across all peers since the ledger is immutable. Endorsement signatures may differ depending on which peers endorsed the transaction, but the transaction content remains consistent.

## Automated Query Script

Here’s a production-ready bash script for querying transactions:

``` bash
#!/bin/bash

TXID="${1}"
CHANNEL="${2:-mychannel}"
ORDERER_HOST="${3:-localhost:7050}"
ORDERER_TLS_OVERRIDE="${4:-orderer.example.com}"

if [ -z "$TXID" ]; then
    echo "Usage: $0 <TXID> [CHANNEL] [ORDERER_HOST] [ORDERER_TLS_OVERRIDE]"
    exit 1
fi

# Validate TXID format (64-character hex)
if ! [[ "$TXID" =~ ^[0-9a-f]{64}$ ]]; then
    echo "Error: Invalid transaction ID format. Expected 64-character lowercase hex string."
    echo "Got: $TXID"
    exit 1
fi

echo "Querying transaction: $TXID on channel: $CHANNEL"

RESPONSE=$(peer chaincode invoke \
  -o "$ORDERER_HOST" \
  --ordererTLSHostnameOverride "$ORDERER_TLS_OVERRIDE" \
  --tls \
  --cafile "$ORDERER_CA" \
  -C "$CHANNEL" \
  -n qscc \
  -c "{\"function\":\"GetTransactionByID\",\"Args\":[\"$CHANNEL\",\"$TXID\"]}" 2>&1)

if [ $? -eq 0 ]; then
    echo "$RESPONSE" | jq '.' || echo "$RESPONSE"
else
    echo "Error querying transaction:"
    echo "$RESPONSE"
    exit 1
fi
```

Usage:

``` bash
./query_tx.sh fa0f757bc278fdf6a32d00975602eb853e23a86a156781588d99ddef5b80720f mychannel
```

## Troubleshooting Common Issues

**Invalid or Non-existent Transaction ID**

The query returns an empty response or “not found” error. Verify the transaction ID is exactly 64 characters of lowercase hexadecimal. Transaction IDs are case-sensitive. Extract the txid from the original invoke command output exactly as displayed.

**Ledger Not Synchronized**

Peers haven’t yet committed the transaction when you query. Always use the `--waitForEvent` flag during the invoke command to ensure the transaction commits before querying:

``` bash
peer chaincode invoke ... --waitForEvent
```

Alternatively, add a delay before querying:

``` bash
sleep 2
peer chaincode invoke ... (query command)
```

**Empty or Minimal Payload**

Read-only transactions or those with no write set generate minimal payloads. Verify the transaction actually modified ledger state. Check the write set to confirm state changes occurred.

**TLS Certificate Errors**

In production, always enable TLS. Ensure the `--cafile` path points to the correct orderer CA certificate. Verify the `--ordererTLSHostnameOverride` matches your orderer’s DNS name:

``` bash
export ORDERER_CA=../organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem
```

**Large Transaction Payloads**

Transactions with extensive read/write sets produce large serialized outputs. When parsing programmatically, extract only the fields you need rather than deserializing the entire structure to reduce memory usage.

**Validation Code Interpretation**

Parse the `validationCode` field to diagnose transaction issues:

- `0 (VALID)`: Transaction successfully committed
- `12 (INVALID_ENDORSEMENT_POLICY)`: Endorsement policy not satisfied
- `13 (INVALID_COMMITMENT_CONFLICT)`: Write conflict with another transaction
- `255 (UNKNOWN)`: Unexpected error or ledger inconsistency

Filter responses by validation code in audit scripts to identify and isolate problematic transactions.
