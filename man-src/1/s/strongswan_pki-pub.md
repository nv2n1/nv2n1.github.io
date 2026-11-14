---
title: "strongswan_pki-pub(1)"
name: "strongswan_pki-pub"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-pub/"
description: "pki –pub – Extract a public key from a private key or certificate"
---

<p>pki &#8211;pub &#8211; Extract a public key from a private key or certificate</p>
<h2>Synopsis</h2>
<p>[<code>&#8211;in</code> <i>file</i>|<i></i><code>&#8211;keyid</code> <i>hex</i>] [ <code>&#8211;type </code><i>type</i> ] [ <code>&#8211;outform </code><i>encoding</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) extracts public keys from a private keys and certificates.</p>
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
<dt><code>-x, &#8211;keyid </code><i>hex</i></p>
<dd>Smartcard or TPM private key object handle in hex format with an optional 0x prefix.</p>
<dt><code>-t, &#8211;type </code><i>type</i></p>
<dd>Type of input. One of <i>priv</i> (private key), <i>rsa</i> (RSA private key), <i>ecdsa</i> (ECDSA private key), <i>pub</i> (public key), <i>pkcs10</i> (PKCS#10 certificate request), or <i>x509</i> (X.509 certificate), defaults to <i>priv</i>.</p>
<dt><code>-f, &#8211;outform </code><i>encoding</i></p>
<dd>Encoding of the extracted public key. One of <i>der</i> (ASN.1 DER), <i>pem</i> (Base64 PEM), <i>dnskey</i> (RFC 3110 DNS key), or <i>sshkey</i> (RFC 4253 SSH key), defaults to <i>der</i>.</dl>
<h2>Examples</h2>
<p>Extract the public key from an RSA private key: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;pub &#8211;in key.der&nbsp;<wbr>&gt;&nbsp;<wbr>pub.der </p>
<p> Extract the public key from an X.509 certificate: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;pub &#8211;in cert.der &#8211;type x509&nbsp;<wbr>&gt;&nbsp;<wbr>pub.der </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
