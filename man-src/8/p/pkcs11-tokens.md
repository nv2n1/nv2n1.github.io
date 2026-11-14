---
title: "pkcs11-tokens(8)"
name: "pkcs11-tokens"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkcs11-tokens/"
description: "pkcs11-tokens – list PKCS#11 available tokens"
---

<p>pkcs11-tokens &#8211; list PKCS#11 available tokens</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pkcs11-tokens</code> [<code>-m&nbsp;<wbr></code><i>module</i>]</dl>
<h2>Description</h2>
<p><code>pkcs11-tokens</code></p>
<dd>lists the PKCS#11 available tokens with defaults from the slot/token scan performed at application initialization.</p>
<h2>Arguments</h2>
<p>-m <i>module</i></p>
<dl>
<dd>Specify the PKCS#11 provider module. This must be the full path to a shared library object implementing the PKCS#11 API for the device.</dl>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
