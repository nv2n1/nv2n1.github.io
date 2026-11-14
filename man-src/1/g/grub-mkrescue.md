---
title: "grub-mkrescue(1)"
name: "grub-mkrescue"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mkrescue/"
description: "grub-mkrescue – make a GRUB rescue image"
---

<h2 class="name">NAME</h2>
<p> grub-mkrescue &#8211; make a GRUB rescue image </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkrescue</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>] <i>,SOURCE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Make GRUB CD-ROM, disk, pendrive and floppy bootable image.</p>
<dl>
<dt><code>&#8211;compress</code>=<i>,no/</i>|xz|gz|lzo</p>
<dd> compress GRUB files [optional]</p>
<dt><code>&#8211;dtb</code>=<i>,FILE/</i></p>
<dd> embed a specific DTB</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></p>
<dd> use images and modules under DIR [default=/usr/lib/grub/&lt;platform&gt;]</p>
<dt><code>&#8211;disable-shim-lock</code></p>
<dd> disable shim_lock verifier</p>
<dt><code>&#8211;fonts</code>=<i>,FONTS/</i></p>
<dd> install FONTS [default=unicode]</p>
<dt><code>&#8211;install-modules</code>=<i>,MODULES/</i></p>
<dd> install only MODULES and their dependencies [default=all]</p>
<dt><code>-k</code>, <code>&#8211;pubkey</code>=<i>,FILE/</i></p>
<dd> embed FILE as public key for signature checking</p>
<dt><code>&#8211;locale-directory</code>=<i>,DIR/</i> use translations under DIR</p>
<dd> [default=/usr/share/locale]</p>
<dt><code>&#8211;locales</code>=<i>,LOCALES/</i></p>
<dd> install only LOCALES [default=all]</p>
<dt><code>&#8211;modules</code>=<i>,MODULES/</i></p>
<dd> pre-load specified modules MODULES</p>
<dt><code>&#8211;sbat</code>=<i>,FILE/</i></p>
<dd> SBAT metadata</p>
<dt><code>&#8211;themes</code>=<i>,THEMES/</i></p>
<dd> install THEMES [default=starfield]</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print verbose messages.</p>
<dt><code>&#8211;arcs-boot</code></p>
<dd> enable ARCS (big-endian mips machines, mostly SGI) boot. Disables HFS+, APM, sparc64 and boot as disk image for i386-pc</p>
<dt><code>&#8211;core-compress</code>=<i>,xz/</i>|none|auto</p>
<dd> choose the compression to use for core image</p>
<dt><code>&#8211;label-bgcolor</code>=<i>,COLOR/</i></p>
<dd> use COLOR for label background</p>
<dt><code>&#8211;label-color</code>=<i>,COLOR/</i></p>
<dd> use COLOR for label</p>
<dt><code>&#8211;label-font</code>=<i>,FILE/</i></p>
<dd> use FILE as font for label</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> save output in FILE [required]</p>
<dt><code>&#8211;product-name</code>=<i>,STRING/</i></p>
<dd> use STRING as product name</p>
<dt><code>&#8211;product-version</code>=<i>,STRING/</i></p>
<dd> use STRING as product version</p>
<dt><code>&#8211;rom-directory</code>=<i>,DIR/</i></p>
<dd> save ROM images in DIR [optional]</p>
<dt><code>&#8211;sparc-boot</code></p>
<dd> enable sparc boot. Disables HFS+, APM, ARCS and boot as disk image for i386-pc</p>
<dt><code>&#8211;xorriso</code>=<i>,FILE/</i></p>
<dd> use FILE as xorriso [optional]</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Generates a bootable CD/USB/floppy image. Arguments other than options to this program are passed to xorriso, and indicate source files, source directories, or any of the mkisofs options listed by the output of `xorriso <code>-as</code> mkisofs <code>-help</code>&#8216;. </p>
<p> Option <code>&#8212;</code> switches to native xorriso command mode. </p>
<p> Mail xorriso support requests to &lt;bug-xorriso [at] gnu.org&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grub-mkimage/">grub-mkimage</a></code>(1) </p>
<p> The full documentation for <code>grub-mkrescue</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mkrescue</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-mkrescue</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
