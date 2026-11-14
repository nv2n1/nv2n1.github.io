---
title: "tpm_createek(8)"
name: "tpm_createek"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_createek/"
description: "tpm_createek – create an Endorsement Key Pair on the TPM"
---

<p>TPM Management &#8211; tpm_createek<br />
 </center></p>
<h2>Name</h2>
<p>tpm_createek &#8211; create an Endorsement Key Pair on the TPM</p>
<h2>Synopsis</h2>
<p><code>tpm_createek</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_createek</code> creates and Endorsement Key Pair on the TPM (via the TPM_CreateEndorsementKeyPair API). This should rarely be required as the Endorsement Key is normally installed as part of manufacturing. However, you might need to run this command once if commands such as tpm_getpubek are returning error code 35 from the TPM layer.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level. </p>
<h2>Options Valid Only For Tpm Version 1.2</h2>
<dl>
<dt><code>-r</code>, <code>&#8211;revocable</code></p>
<dd>Creates a <code>revocable</code> key pair instead of non-revocable one. Requires secret data (either <code>-g</code> <code>-o</code> or <code>-i</code> &#8211; see below). .TP <code>-i</code>, <code>&#8211;infile</code> [input file] Specifies the file that contains the secret data used as revoke data do the new revocable EK pair. Only the first 20 bytes of this file are used and the remaining ones are ignored. .TP <code>-g</code>, <code>&#8211;generate-secret</code> Generates a random 20 bytes value that is used as the EK pair revocable secret data. Requires <code>-o</code> (see below). .TP <code>-o</code>, <code>&#8211;outfile</code> [output file] Specifies the file to write the generated revocable secret data to, for further use. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_getpubek/">tpm_getpubek</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
