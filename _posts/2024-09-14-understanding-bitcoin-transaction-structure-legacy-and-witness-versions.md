---
title: "Bitcoin Transaction Formats: Legacy vs. SegWit Explained"
date: 2024-09-14 07:31:55 +0000
layout: post
canonical: https://www.systutorials.com/understanding-bitcoin-transaction-structure-legacy-and-witness-versions/
---

Every Bitcoin transaction consists of two main components:

**Inputs (UTXOs)**: Unspent Transaction Outputs from previous transactions that you’re now spending. These are references to outputs you received earlier. Think of them as specific bills from your wallet you’re handing over.

**Outputs**: The destinations and amounts for the Bitcoin. This includes the recipient’s address and the amount sent. Any unspent amount (change) is typically sent back to you in a new output.

Each transaction input includes:

- A reference to the previous transaction and which output you’re spending
- A script that proves you have the right to spend that output
- A sequence number (used for timelocks and replace-by-fee signaling)

Each output includes:

- The amount in satoshis
- A locking script that specifies conditions for spending

## Legacy Transactions (P2PKH and P2SH)

The original Bitcoin transaction format stored signatures directly in the transaction input script. This approach had significant drawbacks:

**Transaction Malleability**: The transaction ID could be altered without changing which funds moved or where they went. Attackers could modify non-signature portions of the witness data, creating different txids for the same logical transaction. This caused serious problems for early payment channels and the Lightning Network.

**Inefficient Block Space**: Signatures are large (~72 bytes per input), so legacy transactions consumed considerable block space at 1 byte = 1 weight unit.

**Fee Impact**: Since miners prioritized by transaction size, legacy transactions cost more in fees per input spent.

Legacy addresses typically start with `1` (P2PKH) or `3` (P2SH). While P2SH added flexibility for multisig and complex scripts, it still embedded witness data in the transaction input.

## SegWit (Witness) Transactions

The 2017 SegWit upgrade separated signature data from the transaction structure:

**Witness Section**: Signatures moved to a separate data structure appended to the transaction, rather than embedded in inputs. This fixed transaction malleability since the txid is calculated without the witness data.

**Efficiency Gains**: Witness data counts as 0.25 weight units instead of 1, reducing effective transaction size by ~40%. A transaction with 2 inputs and 2 outputs dropped from ~340 bytes to ~200 bytes.

**Address Format**: SegWit v0 addresses use Bech32 encoding starting with `bc1q`. These are P2WPKH (Pay to Witness PubKey Hash) and P2WSH (Pay to Witness Script Hash).

**Backward Compatibility**: Nodes updated gradually. Old nodes could still verify SegWit transactions but couldn’t validate the witness data—a deliberate design choice to avoid hard forks.

SegWit adoption solved the technical groundwork for Lightning Network, allowing reliable payment channels.

## Taproot (SegWit v1)

The 2021 Taproot upgrade introduced SegWit v1, further optimizing transaction structure:

**Key Aggregation**: Multiple signatures can be combined into a single threshold signature using Schnorr signatures. A 15-of-15 multisig looks identical to a single-signature transaction on-chain, improving privacy and reducing size.

**Scriptless Scripts**: Complex conditions (timelocks, multisig thresholds, conditional logic) can be committed without revealing them until spending. This is particularly useful for hardware wallets and institutional setups.

**Taproot Addresses**: Addresses start with `bc1p` and are smaller than earlier SegWit variants.

A standard institutional multisig treasury spending from Taproot is indistinguishable from a personal transfer, enhancing privacy for both.

## Transaction Analysis in 2026

Today, Taproot dominates new address generation:

**Adoption Rate**: Most wallets and exchanges have migrated primary addresses to P2TR. Legacy addresses still function but are considered outdated.

**Fee Efficiency**: Transaction batching—combining dozens or hundreds of outputs into a single transaction—is standard practice for exchanges. A batch withdrawal of 100 users costs roughly the same as sending 2-3 individual transactions, significantly reducing per-user fees.

**Block Space Demand**: With a 4MB effective block size (1MB base + 3MB witness), the network handles roughly 5-7 transactions per second on average, with peaks during high-volume trading or inscription activity.

**Ordinal Inscriptions**: Since 2023, significant block space has been used for Ordinals—arbitrary data stored in witness sections. These immutable on-chain records compete with payment transactions for block space, pushing base-layer fees higher during active inscription periods.

## Examining Transaction Details

Use `bitcoin-cli getrawtransaction <txid> true` to inspect transaction structure in JSON format. The `vin` (inputs) array shows previous outputs being spent. The `vout` (outputs) array lists destinations. For SegWit transactions, look for the `witness` field in each input—legacy transactions won’t have this.

Example Taproot transaction from 2026:

``` json
{
  "txid": "abc123...",
  "version": 2,
  "locktime": 0,
  "vin": [
    {
      "txid": "prev123...",
      "vout": 0,
      "scriptSig": { "asm": "", "hex": "" },
      "witness": ["3044022..."],
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 0.45000000,
      "scriptPubKey": {
        "asm": "1 a1b2c3...",
        "hex": "5120a1b2c3...",
        "address": "bc1p...",
        "type": "witness_v1_taproot"
      }
    }
  ]
}
```

The `scriptSig` is empty (witness data is elsewhere), and the `scriptPubKey` shows the Taproot address format.

## Practical Implications

When analyzing fees or optimizing transaction batching, remember that witness data is weighted differently. A transaction with 10 outputs to different addresses uses similar block space whether it has 2 inputs or 5 inputs (due to witness data efficiency), making consolidation less urgent than in the legacy era.

For cold storage setups, Taproot multisig with key aggregation reduces the data stored in backup seed phrases and speeds up signature verification on hardware wallets. Most enterprise custodians have standardized on Taproot for these reasons.
