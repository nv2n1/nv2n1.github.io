---
title: "memtest-setup(8)"
name: "memtest-setup"
section: "8"
letter: "m"
url: "/docs/linux/man/8-memtest-setup/"
description: "memtest-setup – Install Memtest86+ into your GRUB boot loader menu"
---

<p>memtest-setup &#8211; Install Memtest86+ into your GRUB boot loader menu</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>memtest-setup</code> [<i>OPTIONS</i>]</dl>
<h2>Description</h2>
<p><code>memtest-setup</code></p>
<dd>installs Memtest86+ into your GRUB boot loader menu. It supports both GRUB 2 and GRUB Legacy (i.e. GRUB 0.9x). In case of GRUB 2 it installs GRUB 2 template into <i>/etc/grub.d</i> and GRUB 2 config needs to be regenerated manually by running <code>grub2-mkconfig -o&nbsp;<wbr></code><i>/boot/grub2/grub.cfg</i> under root. This is not done automatically because it could overwrite any custom changes in <i>/boot/grub2/grub.cfg</i>.</p>
<h2>Options</h2>
<h3>
<dt><code>-h</code>,&#8211;help</p>
<dd></h3>
<p>Shows help.</dl>
<h2>Author</h2>
<p><code>Jaroslav Škarvada</code> &lt;jskarvad [at] redhat.com&gt;</p>
<dl>
<dd>Manpage author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2014 Jaroslav Škarvada </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or (at your option) any later version published by the Free Software Foundation.</p>
