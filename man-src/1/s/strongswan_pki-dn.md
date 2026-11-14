---
title: "strongswan_pki-dn(1)"
name: "strongswan_pki-dn"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-dn/"
description: "pki –dn – Extract the subject DN of an X.509 certificate"
---

<p>pki &#8211;dn &#8211; Extract the subject DN of an X.509 certificate</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;format </code><i>format</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) extracts the ASN.1-encoded subject DistinguishedName (DN) of an X.509 certificate and exports it in different formats. This may be useful when strongSwan&#8217;s identity parser is unable to produce the correct binary encoding from a string.</p>
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
<dt><code>-t, &#8211;format </code><i>format</i></p>
<dd>Output format. One of <i>config</i> (strongSwan configuration compatible), <i>hex</i> (hexadecimal encoding, no prefix), <i>base64</i> (Base64 encoding, no prefix), <i>bin</i> (raw binary data), defaults to <i>config</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
