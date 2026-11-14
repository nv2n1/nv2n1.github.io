---
title: "grub-mknetdir(1)"
name: "grub-mknetdir"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mknetdir/"
description: "grub-mknetdir – prepare a GRUB netboot directory."
---

<h2 class="name">NAME</h2>
<p> grub-mknetdir &#8211; prepare a GRUB netboot directory. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mknetdir</code> [<i>,OPTION/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Prepares GRUB network boot images at net_directory/subdir assuming net_directory being TFTP root.</p>
<dl>
<dt><code>&#8211;compress</code>=<i>,no/</i>|xz|gz|lzo</p>
<dd> compress GRUB files [optional]</p>
<dt><code>&#8211;disable-shim-lock</code></p>
<dd> disable shim_lock verifier</p>
<dt><code>&#8211;dtb</code>=<i>,FILE/</i></p>
<dd> embed a specific DTB</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></p>
<dd> use images and modules under DIR [default=/usr/lib/grub/&lt;platform&gt;]</p>
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
<dt><code>&#8211;core-compress</code>=<i>,xz/</i>|none|auto</p>
<dd> choose the compression to use for core image</p>
<dt><code>&#8211;net-directory</code>=<i>,DIR/</i></p>
<dd> root directory of TFTP server</p>
<dt><code>&#8211;subdir</code>=<i>,DIR/</i></p>
<dd> relative subdirectory on network server</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Prepares GRUB network boot images at net_directory/subdir assuming net_directory being TFTP root.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grub-mkimage/">grub-mkimage</a></code>(1) </p>
<p> The full documentation for <code>grub-mknetdir</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mknetdir</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-mknetdir</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
