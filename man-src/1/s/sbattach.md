---

title: "sbattach(1)"
name: "sbattach"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbattach/"
description: "sbattach – UEFI secure boot detached signature tool"
---

<p> sbattach &#8211; UEFI secure boot detached signature tool </p>
<h2>SYNOPSIS</h2>
<p> <code>sbattach</code> <i>,&#8211;attach &lt;sigfile&gt; &lt;efi-boot-image&gt;/</i><br />
 <code>sbattach</code> <i>,&#8211;detach &lt;sigfile&gt; /</i>[<i>,&#8211;remove/</i>] <i>,&lt;efi-boot-image&gt;/</i><br />
 <code>sbattach</code> <i>,&#8211;remove &lt;efi-boot-image&gt;/</i></p>
<h2>DESCRIPTION</h2>
<p> Attach or detach a signature file to/from a boot image</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;attach</code> &lt;sigfile&gt;</dt>
<dd> set &lt;sigfile&gt; as the boot image&#8217;s signature table</dd>
<dt><code>&#8211;detach</code> &lt;sigfile&gt;</dt>
<dd> copy the boot image&#8217;s signature table to &lt;sigfile&gt;</dd>
<dt><code>&#8211;remove</code></dt>
<dd> remove the boot image&#8217;s signature table from the original file</dd>
<dt><code>&#8211;signum</code></dt>
<dd> signature to operate on (defaults to first) </dd>
</dl>
