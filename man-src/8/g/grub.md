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
<dt><code>&#8211;batch</code></p>
<dd>turn on batch mode for non-interactive use</p>
<dt><code>&#8211;boot-drive</code>=<i>DRIVE</i></p>
<dd>specify stage2 boot_drive [default=0x0]</p>
<dt><code>&#8211;config-file</code>=<i>FILE</i></p>
<dd>specify stage2 config_file [default=/boot/grub/grub.conf]</p>
<dt><code>&#8211;device-map</code>=<i>FILE</i></p>
<dd>use the device map file FILE</p>
<dt><code>&#8211;help</code></p>
<dd>display this message and exit</p>
<dt><code>&#8211;hold</code></p>
<dd>wait until a debugger will attach</p>
<dt><code>&#8211;install-partition</code>=<i>PAR</i></p>
<dd>specify stage2 install_partition [default=0x20000]</p>
<dt><code>&#8211;no-config-file</code></p>
<dd>do not use the config file</p>
<dt><code>&#8211;no-curses</code></p>
<dd>do not use curses</p>
<dt><code>&#8211;no-floppy</code></p>
<dd>do not probe any floppy drive</p>
<dt><code>&#8211;no-pager</code></p>
<dd>do not use internal pager</p>
<dt><code>&#8211;preset-menu</code></p>
<dd>use the preset menu</p>
<dt><code>&#8211;probe-second-floppy</code></p>
<dd>probe the second floppy drive</p>
<dt><code>&#8211;read-only</code></p>
<dd>do not write anything to devices</p>
<dt><code>&#8211;verbose</code></p>
<dd>print verbose messages</p>
<dt><code>&#8211;version</code></p>
<dd>print version information and exit</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p>The full documentation for <code>grub</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub</code></dl>
<p> should give you access to the complete manual. </p>
