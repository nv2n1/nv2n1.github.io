---
title: "tarsnap-keygen(1)"
name: "tarsnap-keygen"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tarsnap-keygen/"
description: "tarsnap-keygen – generate a key file for use with tarsnap(1)"
---

<h2>NAME</h2>
<p> <code>tarsnap-keygen</code> &#8211; generate a key file for use with <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-user </code><i>user-name</i> &#8211;<code>-machine </code><i>machine-name</i> [-<code>-passphrased</code> ] [-<code>-passphrase-mem </code><i>maxmem</i> ]</p>
<h2>DESCRIPTION</h2>
<p> generates cryptographic keys, registers with the tarsnap server, and writes a key file for use with <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1). </p>
<p> The &#8211;<code>-keyfile</code> &#8211;<code>-user</code> and &#8211;<code>-machine</code> parameters are all required. </p>
<p> If the &#8211;<code>-passphrased</code> option is specified, the user will be prompted to enter a passphrase (twice) to be used to encrypt the key file. </p>
<p> If the &#8211;<code>-passphrase-mem </code><i>maxmem</i> option is specified, a maximum of <i>maxmem</i> bytes of RAM will be used in the scrypt key derivation function to encrypt the key file; it may be necessary to set this option if a key file is being generated on a system with far more RAM than the system on which the key file will be used. </p>
<h2>Index</h2>
