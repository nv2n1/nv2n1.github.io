---
title: "strongimcv_pki-print(1)"
name: "strongimcv_pki-print"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongimcv_pki-print/"
description: "pki –print – Print a credential (key, certificate etc.) in human readable form"
---

<p>pki &#8211;print &#8211; Print a credential (key, certificate etc.) in human readable form</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;type </code><i>type</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) prints credentials (keys, certificates etc.) in human readable form.</p>
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
<dd>Type of input. One of <i>rsa-priv</i> (RSA private key), <i>ecdsa-priv</i> (ECDSA private key), <i>pub</i> (public key), <i>x509</i> (X.509 certificate), <i>crl</i> (Certificate Revocation List, CRL), <i>ac</i> (Attribute Certificate), defaults to <i>x509</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
