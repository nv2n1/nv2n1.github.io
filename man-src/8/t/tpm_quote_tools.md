---
title: "tpm_quote_tools(8)"
name: "tpm_quote_tools"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_quote_tools/"
description: "TPM Quote Tools"
---

<p>TPM Quote Tools</p>
<h2>Programs</h2>
<p><code>tpm_mkuuid,</code> <code>tpm_mkaik,</code> <code>tpm_loadkey,</code> <code>tpm_unloadkey,</code> <code>tpm_getpcrhash,</code> <code>tpm_updatepcrhash,</code> <code>tpm_getquote,</code> <code>tpm_verifyquote</code></p>
<h2>Description</h2>
<p>TPM Quote Tools is a collection of programs that provide support for TPM based attestation using the TPM quote operation. </p>
<p> A TPM contains a set of Platform Configuration Registers (PCRs). In a well configured machine, some of these registers are set to known values during the boot up process or at other times. For example, a PCR might contain the hash of a boot loader in memory before it is run. </p>
<p> The TPM quote operation is used to authoritatively verify the contents of a TPM&#8217;s Platform Configuration Registers (PCRs). During provisioning, a composite hash of a selected set of PCRs is computed. The TPM quote operation produces a composite hash that can be compared with the one computed while provisioning. </p>
<p> To use the TPM quote operation, keys must be generated. During provisioning, an Attestation Identity Key (AIK) is generated for each TPM, and the public part of the key is made available to entities that validate quotes. </p>
<p> The TPM quote operation returns signed data and a signature. The data that is signed contains the PCRs selected for the operation, the composite hash for the selected PCRs, and a nonce provided as input, and used to prevent replay attacks. At provisioning time, the data that is signed is stored, not just the composite hash. The signature is discarded. </p>
<p> An entity that wishes to evaluate a machine generates a nonce, and sends it along with the set of PCR used to generate the composite PCR hash at provisioning time. For this use of the TPM quote operation, the signed data is ignored, and the signature returned is used to validate the state of the TPM&#8217;s PCRs. Given the signature, the evaluating entity replaces the nonce in the signed data generated at provisioning time, and checks to see if the signature is valid for the data. If so, this check ensures the selected PCRs contain values that match the ones measured during provisioning. </p>
<p> A typical scenario for an enterprise using these tools follows. The tools expect AIKs to be referenced via one enterprise-wide Universally Unique Identifier (UUID). The program <code>tpm_mkuuid</code> creates one. </p>
<p> For each machine being checked, an AIK is created using <code>tpm_mkaik.</code> The key blob produced is bound to the UUID on its machine using <code>tpm_loadkey.</code> The public key associated with the AIK is sent to the entities that verify quotes. Finally, the expected PCR composite hash is obtained using <code>tpm_getpcrhash.</code> When the expected PCR values change, a new hash can be generated with <code>tpm_updatepcrhash.</code> </p>
<p> The program to obtain a quote, and thus measure the current state of the PCRs is <code>tpm_getquote.</code> The program that verifies the quote describes the same PCR composite hash as was measured initially is <code>tpm_verifyquote.</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_mkuuid/">tpm_mkuuid</a></code>(8), <code><a href="/docs/linux/man/8-tpm_mkaik/">tpm_mkaik</a></code>(8), <code><a href="/docs/linux/man/8-tpm_loadkey/">tpm_loadkey</a></code>(8), <code><a href="/docs/linux/man/8-tpm_unloadkey/">tpm_unloadkey</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getpcrhash/">tpm_getpcrhash</a></code>(8), <code><a href="/docs/linux/man/8-tpm_updatepcrhash/">tpm_updatepcrhash</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getquote/">tpm_getquote</a></code>(8), <code><a href="/docs/linux/man/8-tpm_verifyquote/">tpm_verifyquote</a></code>(8) </p>
