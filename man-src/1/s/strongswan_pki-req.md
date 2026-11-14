---
title: "strongswan_pki-req(1)"
name: "strongswan_pki-req"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-req/"
description: "pki –req – Create a PKCS#10 certificate request"
---

<p>pki &#8211;req &#8211; Create a PKCS#10 certificate request</p>
<h2>Synopsis</h2>
<p>[<code>&#8211;in</code> <i>file</i>|<i></i><code>&#8211;keyid</code> <i>hex</i>] [ <code>&#8211;type </code><i>type</i> ] <code>&#8211;dn~</code><i>distinguished-name</i> [ <code>&#8211;san </code><i>subjectAltName</i> ] [ <code>&#8211;password </code><i>password</i> ] [ <code>&#8211;digest </code><i>digest</i> ] [ <code>&#8211;outform </code><i>encoding</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) is used to create a PKCS#10 certificate request.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage information with a summary of the available options.</p>
<dt><code>-v, &#8211;debug </code><i>level</i></p>
<dd>Set debug level, default: 1.</p>
<dt><code>-+, &#8211;options </code><i>file</i></p>
<dd>Read command line options from <i>file</i>.</p>
<dt><code>-i, &#8211;in </code><i>file</i></p>
<dd>Private key input file. If not given the key is read from <i>STDIN</i>.</p>
<dt><code>-x, &#8211;keyid </code><i>hex</i></p>
<dd>Smartcard or TPM private key object handle in hex format with an optional 0x prefix.</p>
<dt><code>-t, &#8211;type </code><i>type</i></p>
<dd>Type of the input key. Either <i>priv</i>, <i>rsa</i>, <i>ecdsa</i> or <i>bliss</i>, defaults to <i>priv</i>.</p>
<dt><code>-d, &#8211;dn </code><i>distinguished-name</i></p>
<dd>Subject distinguished name (DN). Required.</p>
<dt><code>-a, &#8211;san </code><i>subjectAltName</i></p>
<dd>subjectAltName extension to include in request. Can be used multiple times.</p>
<dt><code>-p, &#8211;password </code><i>password</i></p>
<dd>The challengePassword to include in the certificate request.</p>
<dt><code>-g, &#8211;digest </code><i>digest</i></p>
<dd>Digest to use for signature creation. One of <i>md5</i>, <i>sha1</i>, <i>sha224</i>, <i>sha256</i>, <i>sha384</i>, or <i>sha512</i>. The default is determined based on the type and size of the signature key.</p>
<dt><code>-f, &#8211;outform </code><i>encoding</i></p>
<dd>Encoding of the created certificate file. Either <i>der</i> (ASN.1 DER) or <i>pem</i> (Base64 PEM), defaults to <i>der</i>.</dl>
<h2>Examples</h2>
<p>Generate a certificate request for an RSA key, with a subjectAltName extension: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;req &#8211;in key.der &#8211;dn&nbsp;<wbr>&quot;C=CH, O=strongSwan, CN=moon&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&#8211;san moon [at] strongswan.org&nbsp;<wbr>&gt;&nbsp;<wbr>req.der </p>
<p> Generate a certificate request for an ECDSA key and a different digest: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;req &#8211;in key.der &#8211;type ecdsa &#8211;digest sha256&nbsp;<wbr>\<br />
&#8211;dn&nbsp;<wbr>&quot;C=CH, O=strongSwan, CN=carol&quot;&nbsp;<wbr>&nbsp;<wbr>&gt;&nbsp;<wbr>req.der </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
