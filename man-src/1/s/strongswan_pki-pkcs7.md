---
title: "strongswan_pki-pkcs7(1)"
name: "strongswan_pki-pkcs7"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-pkcs7/"
description: "pki –pkcs7 – Provides PKCS#7 wrap/unwrap functions"
---

<p>pki &#8211;pkcs7 &#8211; Provides PKCS#7 wrap/unwrap functions</p>
<h2>Synopsis</h2>
<p><code>&#8211;sign</code>|<code>&#8211;verify</code>|<code>&#8211;encrypt</code>|<code>&#8211;decrypt</code>|<code>&#8211;show</code> [ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;cert </code><i>file</i> ] [ <code>&#8211;key </code><i>file</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) provides functions to wrap/unwrap PKCS#7 containers.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage information with a summary of the available options.</p>
<dt><code>-v, &#8211;debug </code><i>level</i></p>
<dd>Set debug level, default: 1.</p>
<dt><code>-+, &#8211;options </code><i>file</i></p>
<dd>Read command line options from <i>file</i>.</p>
<dt><code>-s, &#8211;sign</code></p>
<dd>Create PKCS#7 signed-data.</p>
<dt><code>-u, &#8211;verify</code></p>
<dd>Verify PKCS#7 signed-data.</p>
<dt><code>-e, &#8211;encrypt</code></p>
<dd>Create PKCS#7 enveloped-data.</p>
<dt><code>-e, &#8211;decrypt</code></p>
<dd>Decrypt PKCS#7 enveloped-data.</p>
<dt><code>-p, &#8211;show</code></p>
<dd>Show information about PKCS#7 container, list certificates.</p>
<dt><code>-i, &#8211;in </code><i>file</i></p>
<dd>PKCS#7 input file. If not given the input is read from <i>STDIN</i>.</p>
<dt><code>-k, &#8211;key </code><i>file</i></p>
<dd>Private key used for <code>&#8211;sign</code> and <code>&#8211;decrypt.</code></p>
<dt><code>-c, &#8211;cert </code><i>file</i></p>
<dd>Certificate for <code>&#8211;sign</code>, <code>&#8211;verify</code> and <code>&#8211;encrypt.</code> Can be used multiple times.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
