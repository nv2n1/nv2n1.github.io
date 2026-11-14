---
title: "grub-reboot(8)"
name: "grub-reboot"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub-reboot/"
description: "grub-reboot – set the default boot entry for GRUB, for the next boot only"
---

<p>grub-reboot &#8211; set the default boot entry for GRUB, for the next boot only</p>
<h2>Synopsis</h2>
<p><code>grub-reboot</code> [<i>,OPTION/</i>] <i>,MENU_ENTRY/</i></p>
<h2>Description</h2>
<p>Set the default boot menu entry for GRUB, for the next boot only.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print this message and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version information and exit</p>
<dt><code>&#8211;boot-directory</code>=<i>,DIR/</i></p>
<dd>expect GRUB images under the directory DIR/grub instead of the <i>,/boot/grub/</i> directory</dl>
<p> MENU_ENTRY is a number, a menu item title or a menu item identifier. Please note that menu items in submenus or sub-submenus require specifying the submenu components and then the menu item component. The titles should be separated using the greater-than character (&gt;) with no extra spaces. Depending on your shell some characters including &gt; may need escaping. More information about this is available in the GRUB Manual in the section about the &#8216;default&#8217; command. </p>
<p> NOTE: In cases where GRUB cannot write to the environment block, such as when it is stored on an MDRAID or LVM device, the chosen boot menu entry will remain the default even after reboot.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub-set-default/">grub-set-default</a></code>(8), <code><a href="/docs/linux/man/1-grub-editenv/">grub-editenv</a></code>(1) The full documentation for <code>grub-reboot</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-reboot</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub-reboot</code></dl>
<p> should give you access to the complete manual. </p>
