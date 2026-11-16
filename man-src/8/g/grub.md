---
title: "grub(8)"
name: "grub"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub/"
description: "grub – the grub shell"
---

<p>grub &#8211; the grub shell</p>
<h2>Synopsis</h2>
<p><code>grub</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>Enter the GRand Unified Bootloader command shell.</p>
<dl>
<dt><code>&#8211;batch</code></dt>
<dd>turn on batch mode for non-interactive use</dd>
<dt><code>&#8211;boot-drive</code>=<i>DRIVE</i></dt>
<dd>specify stage2 boot_drive [default=0x0]</dd>
<dt><code>&#8211;config-file</code>=<i>FILE</i></dt>
<dd>specify stage2 config_file [default=/boot/grub/grub.conf]</dd>
<dt><code>&#8211;device-map</code>=<i>FILE</i></dt>
<dd>use the device map file FILE</dd>
<dt><code>&#8211;help</code></dt>
<dd>display this message and exit</dd>
<dt><code>&#8211;hold</code></dt>
<dd>wait until a debugger will attach</dd>
<dt><code>&#8211;install-partition</code>=<i>PAR</i></dt>
<dd>specify stage2 install_partition [default=0x20000]</dd>
<dt><code>&#8211;no-config-file</code></dt>
<dd>do not use the config file</dd>
<dt><code>&#8211;no-curses</code></dt>
<dd>do not use curses</dd>
<dt><code>&#8211;no-floppy</code></dt>
<dd>do not probe any floppy drive</dd>
<dt><code>&#8211;no-pager</code></dt>
<dd>do not use internal pager</dd>
<dt><code>&#8211;preset-menu</code></dt>
<dd>use the preset menu</dd>
<dt><code>&#8211;probe-second-floppy</code></dt>
<dd>probe the second floppy drive</dd>
<dt><code>&#8211;read-only</code></dt>
<dd>do not write anything to devices</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>print verbose messages</dd>
<dt><code>&#8211;version</code></dt>
<dd>print version information and exit</dd></dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p>The full documentation for <code>grub</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub</code></dd></dl>
<p> should give you access to the complete manual. </p>
