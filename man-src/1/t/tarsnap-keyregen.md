---
title: "tarsnap-keyregen(1)"
name: "tarsnap-keyregen"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tarsnap-keyregen/"
description: "tarsnap-keyregen – generate a key file for use with tarsnap-recrypt1"
---

<h2>NAME</h2>
<p> <code>tarsnap-keyregen</code> &#8211; generate a key file for use with tarsnap-recrypt1</p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>-keyfile </code><i>key-file</i> &#8211;<code>-oldkey </code><i>old-key-file</i> &#8211;<code>-user </code><i>user-name</i> &#8211;<code>-machine </code><i>machine-name</i> [-<code>-passphrased</code> ] [-<code>-passphrase-mem </code><i>maxmem</i> ]</p>
<h2>DESCRIPTION</h2>
<p> generates a set of cryptographic keys which are compatible with an existing set of cryptographic keys, registers with the tarsnap server, and writes a key file for use with tarsnap-recrypt1 and <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1). The term Qq compatible here means that it is possible to re-encrypt archives stored with the first set of keys to be stored with the second set of keys. </p>
<p> The &#8211;<code>-keyfile</code> &#8211;<code>-user</code> &#8211;<code>-machine</code> and &#8211;<code>-oldkey</code> parameters are all required. </p>
<p> If the &#8211;<code>-passphrased</code> option is specified, the user will be prompted to enter a passphrase (twice) to be used to encrypt the key file. </p>
<p> If the &#8211;<code>-passphrase-mem </code><i>maxmem</i> option is specified, a maximum of <i>maxmem</i> bytes of RAM will be used in the scrypt key derivation function to encrypt the key file; it may be necessary to set this option if a key file is being generated on a system with far more RAM than the system on which the key file will be used. </p>
<h2>Index</h2>
