---
title: "cryptoflex-tool(1)"
name: "cryptoflex-tool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cryptoflex-tool/"
description: "cryptoflex-tool – utility for manipulating Schlumberger Cryptoflex data structures"
---

<h2 class="name">NAME</h2>
<p> cryptoflex-tool &#8211; utility for manipulating Schlumberger Cryptoflex data structures </p>
<h2>SYNOPSIS</h2>
<p> <code>cryptoflex-tool</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> <code>cryptoflex-tool</code> is used to manipulate PKCS data structures on Schlumberger Cryptoflex smart cards. Users can create, list and read PINs and keys stored on the smart card. User PIN authentication is performed for those operations that require it.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;verify-pin, -V</code></p>
<dl>
<dt>
<dd> Verifies CHV1 before issuing commands</dl>
<p> <code>&#8211;list-keys, -l</code></p>
<dl>
<dt>
<dd> Lists all keys stored in a public key file</dl>
<p> <code>&#8211;create-key-files</code> <i>arg</i>, <code>-c</code> <i>arg</i></p>
<dl>
<dt>
<dd> Creates new RSA key files for <i>arg</i> keys</dl>
<p> <code>&#8211;create-pin-files</code> <i>id</i>, <code>-P</code> <i>id</i></p>
<dl>
<dt>
<dd> Creates new PIN file for CHV<i>id</i></dl>
<p> <code>&#8211;generate-key, -g</code></p>
<dl>
<dt>
<dd> Generate a new RSA key pair</dl>
<p> <code>&#8211;read-key</code></p>
<dl>
<dt>
<dd> Reads a public key from the card, allowing the user to extract and store or use the public key</dl>
<p> <code>&#8211;key-num</code> <i>num</i>, <code>-k</code> <i>num</i></p>
<dl>
<dt>
<dd> Specifies the key number to operate on. The default is key number 1.</dl>
<p> <code>&#8211;app-df</code> <i>num</i>, <code>-a</code> <i>num</i></p>
<dl>
<dt>
<dd> Specifies the DF to operate in</dl>
<p> <code>&#8211;prkey-file</code> <i>id</i>, <code>-p</code> <i>id</i></p>
<dl>
<dt>
<dd> Specifies the private key file id, <i>id</i>, to use</dl>
<p> <code>&#8211;pubkey-file</code> <i>id</i>, <code>-u</code> <i>id</i></p>
<dl>
<dt>
<dd> Specifies the public key file id, <i>id</i>, to use</dl>
<p> <code>&#8211;exponent</code> <i>exp</i>, <code>-e</code> <i>exp</i></p>
<dl>
<dt>
<dd> Specifies the RSA exponent, <i>exp</i>, to use in key generation. The default value is 3.</dl>
<p> <code>&#8211;modulus-length</code> <i>length</i>, <code>-m</code> <i>length</i></p>
<dl>
<dt>
<dd> Specifies the modulus <i>length</i> to use in key generation. The default value is 1024.</dl>
<p> <code>&#8211;reader</code> <i>num</i>, <code>-r</code> <i>num</i></p>
<dl>
<dt>
<dd> Forces <code>cryptoflex-tool</code> to use reader number <i>num</i> for operations. The default is to use reader number 0, the first reader in the system.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
<dd> Causes <code>cryptoflex-tool</code> to be more verbose. Specify this flag several times to enable debug output in the opensc library.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-opensc/">opensc</a>(7), <a href="/docs/linux/man/1-pkcs15-tool/">pkcs15-tool</a>(1) </p>
<h2>Index</h2>
