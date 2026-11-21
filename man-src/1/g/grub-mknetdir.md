---
title: "grub-mknetdir(1)"
name: "grub-mknetdir"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mknetdir/"
description: "grub-mknetdir – prepare a GRUB netboot directory."
---

<h2>SYNOPSIS</h2>
<p> <code>grub-mknetdir</code> [<i>,OPTION/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Prepares GRUB network boot images at net_directory/subdir assuming net_directory being TFTP root.</p>
<dl>
<dt><code>&#8211;compress</code>=<i>,no/</i>|xz|gz|lzo</dt>
<dd> compress GRUB files [optional]</dd>
<dt><code>&#8211;disable-shim-lock</code></dt>
<dd> disable shim_lock verifier</dd>
<dt><code>&#8211;dtb</code>=<i>,FILE/</i></dt>
<dd> embed a specific DTB</dd>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></dt>
<dd> use images and modules under DIR [default=/usr/lib/grub/&lt;platform&gt;]</dd>
<dt><code>&#8211;fonts</code>=<i>,FONTS/</i></dt>
<dd> install FONTS [default=unicode]</dd>
<dt><code>&#8211;install-modules</code>=<i>,MODULES/</i></dt>
<dd> install only MODULES and their dependencies [default=all]</dd>
<dt><code>-k</code>, <code>&#8211;pubkey</code>=<i>,FILE/</i></dt>
<dd> embed FILE as public key for signature checking</dd>
<dt><code>&#8211;locale-directory</code>=<i>,DIR/</i> use translations under DIR</dt>
<dd> [default=/usr/share/locale]</dd>
<dt><code>&#8211;locales</code>=<i>,LOCALES/</i></dt>
<dd> install only LOCALES [default=all]</dd>
<dt><code>&#8211;modules</code>=<i>,MODULES/</i></dt>
<dd> pre-load specified modules MODULES</dd>
<dt><code>&#8211;sbat</code>=<i>,FILE/</i></dt>
<dd> SBAT metadata</dd>
<dt><code>&#8211;themes</code>=<i>,THEMES/</i></dt>
<dd> install THEMES [default=starfield]</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print verbose messages.</dd>
<dt><code>&#8211;core-compress</code>=<i>,xz/</i>|none|auto</dt>
<dd> choose the compression to use for core image</dd>
<dt><code>&#8211;net-directory</code>=<i>,DIR/</i></dt>
<dd> root directory of TFTP server</dd>
<dt><code>&#8211;subdir</code>=<i>,DIR/</i></dt>
<dd> relative subdirectory on network server</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Prepares GRUB network boot images at net_directory/subdir assuming net_directory being TFTP root.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grub-mkimage/">grub-mkimage</a></code>(1) </p>
<p> The full documentation for <code>grub-mknetdir</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mknetdir</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-mknetdir</code></dd></dl>
<p> should give you access to the complete manual. </p>
