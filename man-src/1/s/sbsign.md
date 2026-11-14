---
title: "sbsign(1)"
name: "sbsign"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbsign/"
description: "sbsign – UEFI secure boot signing tool"
---

<h2 class="name">NAME</h2>
<p> sbsign &#8211; UEFI secure boot signing tool </p>
<h2>SYNOPSIS</h2>
<p> <code>sbsign</code> [<i>,options/</i>] <i>,&#8211;key &lt;keyfile&gt; &#8211;cert &lt;certfile&gt; &lt;efi-boot-image&gt;/</i></p>
<h2>DESCRIPTION</h2>
<p> Sign an EFI boot image for use with secure boot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;engine</code> &lt;eng&gt;</p>
<dd> use the specified engine to load the key</p>
<dt><code>&#8211;key</code> &lt;keyfile&gt;</p>
<dd> signing key (PEM-encoded RSA private key)</p>
<dt><code>&#8211;cert</code> &lt;certfile&gt;</p>
<dd> certificate (x509 certificate)</p>
<dt> <code>&#8211;addcert</code> &lt;addcertfile&gt; additional intermediate certificates in a file</p>
<dt><code>&#8211;detached</code></p>
<dd>
<dd>write a detached signature, instead of a signed binary</p>
<dt><code>&#8211;output</code> &lt;file&gt;</p>
<dd> write signed data to &lt;file&gt; (default &lt;efi-boot-image&gt;.signed, or &lt;efi-boot-image&gt;.pk7 for detached signatures) </p>
</dl>
<h2>Index</h2>
