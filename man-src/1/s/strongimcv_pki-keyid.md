---
title: "strongimcv_pki-keyid(1)"
name: "strongimcv_pki-keyid"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongimcv_pki-keyid/"
description: "pki –keyid – Calculate key identifiers of a key or certificate"
---

<p>pki &#8211;keyid &#8211; Calculate key identifiers of a key or certificate</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;type </code><i>type</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) calculates key identifiers of private keys and certificates.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage information with a summary of the available options.</p>
<dt><code>-v, &#8211;debug </code><i>level</i></p>
<dd>Set debug level, default: 1.</p>
<dt><code>-+, &#8211;options </code><i>file</i></p>
<dd>Read command line options from <i>file</i>.</p>
<dt><code>-i, &#8211;in </code><i>file</i></p>
<dd>Input file. If not given the input is read from <i>STDIN</i>.</p>
<dt><code>-t, &#8211;type </code><i>type</i></p>
<dd>Type of input. One of <i>rsa-priv</i> (RSA private key), <i>ecdsa-priv</i> (ECDSA private key), <i>pub</i> (public key), <i>pkcs10</i> (PKCS#10 certificate request), <i>x509</i> (X.509 certificate), defaults to <i>rsa-priv</i>.</dl>
<h2>Examples</h2>
<p>Calculate key identifiers of an RSA private key: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;keyid &#8211;in key.der<br />
&nbsp;<wbr>&nbsp;<wbr>subjectKeyIdentifier:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6a:9c:74:d1:f8:89:79:89:f6:5a:94:e9:89:f1&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>subjectPublicKeyInfo hash: 6e:55:dc:7e:9c:a5:58:d9:5b:e3:c7:13:14:e1&#8230; </p>
<p> Calculate key identifiers of an X.509 certificate: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;keyid &#8211;in cert.der &#8211;type x509<br />
&nbsp;<wbr>&nbsp;<wbr>subjectKeyIdentifier:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6a:9c:74:d1:f8:89:79:89:f6:5a:94:e9:89:f1&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>subjectPublicKeyInfo hash: 6e:55:dc:7e:9c:a5:58:d9:5b:e3:c7:13:14:e1&#8230; </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
