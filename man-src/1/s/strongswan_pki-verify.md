---
title: "strongswan_pki-verify(1)"
name: "strongswan_pki-verify"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-verify/"
description: "pki –verify – Verify a certificate using a CA certificate"
---

<p>pki &#8211;verify &#8211; Verify a certificate using a CA certificate</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;cacert </code><i>file</i> ] [ <code>&#8211;crl </code><i>file</i> ] [ <code>&#8211;debug </code><i>level</i> ] [ <code>&#8211;online</code> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) verifies a certificate using an optional CA certificate.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print usage information with a summary of the available options.</dd>
<dt><code>-v, &#8211;debug </code><i>level</i></dt>
<dd>Set debug level, default: 1.</dd>
<dt><code>-+, &#8211;options </code><i>file</i></dt>
<dd>Read command line options from <i>file</i>.</dd>
<dt><code>-i, &#8211;in </code><i>file</i></dt>
<dd>X.509 certificate to verify. If not given it is read from <i>STDIN</i>.</dd>
<dt><code>-c, &#8211;cacert </code><i>file</i></dt>
<dd>CA certificate to use for trustchain verification. If not given the certificate is assumed to be self-signed.</dd>
<dt><code>-l, &#8211;crl </code><i>file</i></dt>
<dd>Local CRL to use for trustchain verification. Implies <code>-o</code>.</dd>
<dt><code>-o, &#8211;online</code></dt>
<dd>Enable online CRL/OCSP revocation checking.</dd></dl>
<h2>Exit Status</h2>
<p>The exit status is 0 if the certificate was verified successfully, 1 if the certificate is untrusted, 2 if the certificate&#8217;s lifetimes are invalid, and 3 if the certificate was verified successfully but the online revocation check indicated that it has been revoked.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
