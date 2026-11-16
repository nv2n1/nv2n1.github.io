---
title: "grub-set-default(8)"
name: "grub-set-default"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub-set-default/"
description: "grub-set-default – set the saved default boot entry for GRUB"
---

<p>grub-set-default &#8211; set the saved default boot entry for GRUB</p>
<h2>Synopsis</h2>
<p><code>grub-set-default</code> [<i>,OPTION/</i>] <i>,MENU_ENTRY/</i></p>
<h2>Description</h2>
<p>Set the default boot menu entry for GRUB. This requires setting GRUB_DEFAULT=saved in <i>,/etc/default/grub/</i>.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>print this message and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>print the version information and exit</dd>
<dt><code>&#8211;boot-directory</code>=<i>,DIR/</i></dt>
<dd>expect GRUB images under the directory DIR/grub instead of the <i>,/boot/grub/</i> directory</dd></dl>
<p> MENU_ENTRY is a number, a menu item title or a menu item identifier.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub-reboot/">grub-reboot</a></code>(8), <code><a href="/docs/linux/man/1-grub-editenv/">grub-editenv</a></code>(1) The full documentation for <code>grub-set-default</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-set-default</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub-set-default</code></dd></dl>
<p> should give you access to the complete manual. </p>
