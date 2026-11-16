---
title: "grub-mkdevicemap(8)"
name: "grub-mkdevicemap"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub-mkdevicemap/"
description: "grub-mkdevicemap – make a device map file automatically"
---

<p>grub-mkdevicemap &#8211; make a device map file automatically</p>
<h2>Synopsis</h2>
<p><code>grub-mkdevicemap</code> [<i>,OPTION/</i>]&#8230;</p>
<h2>Description</h2>
<p>Generate a device map file automatically.</p>
<dl>
<dt><code>-n</code>, <code>&#8211;no-floppy</code></dt>
<dd>do not probe any floppy drive</dd>
<dt> <code>-s</code>, <code>&#8211;probe-second-floppy</code> probe the second floppy drive</dt>
<dt><code>-m</code>, <code>&#8211;device-map</code>=<i>,FILE/</i></dt>
<dd>
</dd><dd>use FILE as the device map [default=/boot/grub/device.map]</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>display this message and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>print version information and exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>print verbose messages</dd></dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub-probe/">grub-probe</a></code>(8) The full documentation for <code>grub-mkdevicemap</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mkdevicemap</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub-mkdevicemap</code></dd></dl>
<p> should give you access to the complete manual. </p>
