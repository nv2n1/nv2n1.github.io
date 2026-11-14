---
title: "grub2-glue-efi(1)"
name: "grub2-glue-efi"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-glue-efi/"
description: "grub-glue-efi — Create an Apple fat EFI binary."
---

<h2>NAME</h2>
<p> <code>grub-glue-efi</code> &#8212; Create an Apple fat EFI binary. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-glue-efi</code> &lt;-3 | &#8211;input32=<i>FILE</i>&gt; &lt;-6 | &#8211;input64=<i>FILE</i>&gt;</p>
<dl>
<dt>
<dd> &lt;-o | &#8211;output=<i>FILE</i>&gt; [-v | &#8211;verbose] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-glue-efi</code> creates an Apple fat EFI binary from two EFI binaries. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;input32</code>=<i>FILE</i></p>
<dd> Read 32-bit binary from <i>FILE</i>. </p>
<dt><code>&#8211;input64</code>=<i>FILE</i></p>
<dd> Read 64-bit binary from <i>FILE</i>. </p>
<dt><code>&#8211;output</code>=<i>FILE</i></p>
<dd> Write resulting fat binary to <i>FILE</i>. </p>
<dt><code>&#8211;verbose</code></p>
<dd> Print verbose messages. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
