---

title: "sbverify(1)"
name: "sbverify"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbverify/"
description: "sbverify – UEFI secure boot verification tool"
---

<p> sbverify &#8211; UEFI secure boot verification tool </p>
<h2>SYNOPSIS</h2>
<p> <code>sbverify</code> [<i>,options/</i>] <i>,&#8211;cert &lt;certfile&gt; &lt;efi-boot-image&gt;/</i></p>
<h2>DESCRIPTION</h2>
<p> Verify a UEFI secure boot image.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cert</code> &lt;certfile&gt;</dt>
<dd> certificate (x509 certificate)</dd>
<dt><code>&#8211;list</code></dt>
<dd> list all signatures (but don&#8217;t verify)</dd>
<dt><code>&#8211;detached</code> &lt;file&gt;</dt>
<dd> read signature from &lt;file&gt;, instead of looking for an embedded signature </dd>
</dl>
