---
title: "grub2-reboot(8)"
name: "grub2-reboot"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub2-reboot/"
description: "grub-reboot — Set the default boot menu entry for the next boot only."
---

<p><code>grub-reboot</code> &#8212; Set the default boot menu entry for the next boot only. </p>
<h2>Synopsis</h2>
<p><code>grub-reboot</code> [&#8211;boot-directory=<i>DIR</i>] <i>MENU_ENTRY</i> </p>
<h2>Description</h2>
<p><code>grub-reboot</code> sets the default boot menu entry for the next boot, but not further boots after that. This command only works for GRUB configuration files created with <i>GRUB_DEFAULT=saved</i> in <i>/etc/default/grub</i>. </p>
<h2>Options</h2>
<dl>
<dt>&#8211;boot-directory=<i>DIR</i></p>
<dd>Find GRUB images under <i>DIR/grub</i>. The default value is <i>/boot</i>, resulting in grub images being search for at <i>/boot/grub</i>. </p>
<dt><i>MENU_ENTRY</i></p>
<dd>A number, a menu item title or a menu item identifier. </p>
</dl>
<h2>See Also</h2>
<p><code>info grub</code> </p>
