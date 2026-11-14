---
title: "grub-glue-efi(1)"
name: "grub-glue-efi"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-glue-efi/"
description: "grub-glue-efi – generate a fat binary for EFI"
---

<h2 class="name">NAME</h2>
<p> grub-glue-efi &#8211; generate a fat binary for EFI </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-glue-efi</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTIONS/</i>]</p>
<h2>DESCRIPTION</h2>
<p> grub-glue-efi processes ia32 and amd64 EFI images and glues them according to Apple format. </p>
<p> Glue 32-bit and 64-bit binary into Apple universal one.</p>
<dl>
<dt><code>-3</code>, <code>&#8211;input32</code>=<i>,FILE/</i></p>
<dd> set input filename for 32-bit part.</p>
<dt><code>-6</code>, <code>&#8211;input64</code>=<i>,FILE/</i></p>
<dd> set input filename for 64-bit part.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> set output filename. Default is STDOUT</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print verbose messages.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>grub-glue-efi</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-glue-efi</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-glue-efi</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
