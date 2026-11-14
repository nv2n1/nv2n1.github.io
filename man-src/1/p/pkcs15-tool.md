---
title: "pkcs15-tool(1)"
name: "pkcs15-tool"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcs15-tool/"
description: "pkcs15-tool – utility for manipulating PKCS #15 data structures on smart cards and similar security tokens"
---

<h2 class="name">NAME</h2>
<p> pkcs15-tool &#8211; utility for manipulating PKCS #15 data structures on smart cards and similar security tokens </p>
<h2>SYNOPSIS</h2>
<p> <code>pkcs15-tool</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pkcs15-tool</code> utility is used to manipulate the PKCS #15 data structures on smart cards and similar security tokens. Users can list and read PINs, keys and certificates stored on the token. User PIN authentication is performed for those operations that require it.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;learn-card, -L</code></p>
<dl>
<dt>
<dd> Cache PKCS #15 token data to the local filesystem. Subsequent operations are performed on the cached data where possible. If the cache becomes out-of-sync with the token state (eg. new key is generated and stored on the token), the cache should be updated or operations may show stale results.</dl>
<p> <code>&#8211;read-certificate</code> <i>cert</i>, <code>-r</code> <i>cert</i></p>
<dl>
<dt>
<dd> Reads the certificate with the given id.</dl>
<p> <code>&#8211;list-certificates, -c</code></p>
<dl>
<dt>
<dd> Lists all certificates stored on the token.</dl>
<p> <code>&#8211;list-pins</code></p>
<dl>
<dt>
<dd> Lists all PINs stored on the token. General information about each PIN is listed (eg. PIN name). Actual PIN values are not shown.</dl>
<p> <code>&#8211;change-pin</code></p>
<dl>
<dt>
<dd> Changes a PIN stored on the token. User authentication is required for this operation.</dl>
<p> <code>&#8211;unblock-pin, -u</code></p>
<dl>
<dt>
<dd> Unblocks a PIN stored on the token. Knowledge of the Pin Unblock Key (PUK) is required for this operation.</dl>
<p> <code>&#8211;list-keys, -k</code></p>
<dl>
<dt>
<dd> Lists all private keys stored on the token. General information about each private key is listed (eg. key name, id and algorithm). Actual private key values are not displayed.</dl>
<p> <code>&#8211;list-public-keys</code></p>
<dl>
<dt>
<dd> Lists all public keys stored on the token, including key name, id, algorithm and length information.</dl>
<p> <code>&#8211;read-public-key</code> <i>id</i></p>
<dl>
<dt>
<dd> Reads the public key with id <i>id</i>, allowing the user to extract and store or use the public key.</dl>
<p> <code>&#8211;read-ssh-key</code> <i>id</i></p>
<dl>
<dt>
<dd> Reads the public key with id <i>id</i>, writing the output in format suitable for $HOME/.ssh/authorized_keys.</dl>
<p> <code>&#8211;output</code> <i>filename</i>, <code>-o</code> <i>filename</i></p>
<dl>
<dt>
<dd> Specifies where key output should be written. If <i>filename</i> already exists, it will be overwritten. If this option is not given, keys will be printed to standard output.</dl>
<p> <code>&#8211;no-cache</code></p>
<dl>
<dt>
<dd> Disables token data caching.</dl>
<p> <code>&#8211;pin-id</code> <i>pin</i>, <code>-a</code> <i>pin</i></p>
<dl>
<dt>
<dd> Specifies the auth id of the PIN to use for the operation. This is useful with the &#8211;change-pin operation.</dl>
<p> <code>&#8211;reader</code> <i>num</i></p>
<dl>
<dt>
<dd> Forces <code>pkcs15-tool</code> to use reader number <i>num</i> for operations. The default is to use reader number 0, the first reader in the system.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
<dd> Causes <code>pkcs15-tool</code> to be more verbose. Specify this flag several times to enable debug output in the OpenSC library.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-opensc/">opensc</a>(7), <a href="/docs/linux/man/1-pkcs15-init/">pkcs15-init</a>(1), <a href="/docs/linux/man/1-pkcs15-crypt/">pkcs15-crypt</a>(1) </p>
<h2>Index</h2>
