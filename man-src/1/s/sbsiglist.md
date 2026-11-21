---
title: "sbsiglist(1)"
name: "sbsiglist"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbsiglist/"
description: "sbsiglist – Create EFI_SIGNATURE_LIST signature databases"
---

<h2>SYNOPSIS</h2>
<p> <code>sbsiglist</code> [<i>,options/</i>] <i>,&#8211;owner &lt;guid&gt; &#8211;type &lt;type&gt; &lt;sig-file&gt;/</i></p>
<h2>DESCRIPTION</h2>
<p> Create an EFI_SIGNATURE_LIST from a signature file Options:</p>
<dl>
<dt><code>&#8211;owner</code> &lt;guid&gt;</dt>
<dd> Signature owner GUID</dd>
<dt><code>&#8211;type</code> &lt;type&gt;</dt>
<dd> Signature type. One of: x509 sha256</dd>
<dt><code>&#8211;output</code> &lt;file&gt;</dt>
<dd> write signed data to &lt;file&gt; (default &lt;sig-file&gt;.siglist) </dd>
</dl>
