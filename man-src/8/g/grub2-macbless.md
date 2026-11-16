---
title: "grub2-macbless(8)"
name: "grub2-macbless"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub2-macbless/"
description: "grub-macbless — Mac-style bless utility for HFS or HFS+"
---

<p><code>grub-macbless</code> &#8212; Mac-style bless utility for HFS or HFS+ </p>
<h2>Synopsis</h2>
<p><code>grub-macbless</code> [-p | &#8211;ppc] [-v | &#8211;verbose] [-x | &#8211;x86] <i>FILE</i> </p>
<h2>Description</h2>
<p><code>grub-mkimage</code> blesses a file on an HFS or HFS+ file system, so that it can be used to boot a Mac. </p>
<h2>Options</h2>
<dl>
<dt>&#8211;ppc</dt>
<dd>Bless the file for use on PPC-based Macs. </dd>
<dt>&#8211;verbose</dt>
<dd>Print verbose messages. </dd>
<dt>&#8211;x86</dt>
<dd>Bless the file for use on x86-based Macs. </dd>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> </p>
