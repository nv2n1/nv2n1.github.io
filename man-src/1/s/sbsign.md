---

title: "sbsign(1)"
name: "sbsign"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbsign/"
description: "sbsign – UEFI secure boot signing tool"
---

<p> <code>sbsign</code> [<i>,options/</i>] <i>,&#8211;key &lt;keyfile&gt; &#8211;cert &lt;certfile&gt; &lt;efi-boot-image&gt;/</i></p>
<p> Sign an EFI boot image for use with secure boot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;engine</code> &lt;eng&gt;</dt>
<dd> use the specified engine to load the key</dd>
<dt><code>&#8211;key</code> &lt;keyfile&gt;</dt>
<dd> signing key (PEM-encoded RSA private key)</dd>
<dt><code>&#8211;cert</code> &lt;certfile&gt;</dt>
<dd> certificate (x509 certificate)</dd>
<dt> <code>&#8211;addcert</code> &lt;addcertfile&gt; additional intermediate certificates in a file</dt>
<dt><code>&#8211;detached</code></dt>
<dd>
</dd><dd>write a detached signature, instead of a signed binary</dd>
<dt><code>&#8211;output</code> &lt;file&gt;</dt>
<dd> write signed data to &lt;file&gt; (default &lt;efi-boot-image&gt;.signed, or &lt;efi-boot-image&gt;.pk7 for detached signatures) </dd>
</dl>
