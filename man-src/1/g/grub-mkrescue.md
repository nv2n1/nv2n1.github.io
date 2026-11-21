---

title: "grub-mkrescue(1)"
name: "grub-mkrescue"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mkrescue/"
description: "grub-mkrescue – make a GRUB rescue image"
---

<p> <code>grub-mkrescue</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>] <i>,SOURCE/</i>&#8230;</p>
<p> Make GRUB CD-ROM, disk, pendrive and floppy bootable image.</p>
<dl>
<dt><code>&#8211;compress</code>=<i>,no/</i>|xz|gz|lzo</dt>
<dd> compress GRUB files [optional]</dd>
<dt><code>&#8211;dtb</code>=<i>,FILE/</i></dt>
<dd> embed a specific DTB</dd>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></dt>
<dd> use images and modules under DIR [default=/usr/lib/grub/&lt;platform&gt;]</dd>
<dt><code>&#8211;disable-shim-lock</code></dt>
<dd> disable shim_lock verifier</dd>
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
<dt><code>&#8211;arcs-boot</code></dt>
<dd> enable ARCS (big-endian mips machines, mostly SGI) boot. Disables HFS+, APM, sparc64 and boot as disk image for i386-pc</dd>
<dt><code>&#8211;core-compress</code>=<i>,xz/</i>|none|auto</dt>
<dd> choose the compression to use for core image</dd>
<dt><code>&#8211;label-bgcolor</code>=<i>,COLOR/</i></dt>
<dd> use COLOR for label background</dd>
<dt><code>&#8211;label-color</code>=<i>,COLOR/</i></dt>
<dd> use COLOR for label</dd>
<dt><code>&#8211;label-font</code>=<i>,FILE/</i></dt>
<dd> use FILE as font for label</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> save output in FILE [required]</dd>
<dt><code>&#8211;product-name</code>=<i>,STRING/</i></dt>
<dd> use STRING as product name</dd>
<dt><code>&#8211;product-version</code>=<i>,STRING/</i></dt>
<dd> use STRING as product version</dd>
<dt><code>&#8211;rom-directory</code>=<i>,DIR/</i></dt>
<dd> save ROM images in DIR [optional]</dd>
<dt><code>&#8211;sparc-boot</code></dt>
<dd> enable sparc boot. Disables HFS+, APM, ARCS and boot as disk image for i386-pc</dd>
<dt><code>&#8211;xorriso</code>=<i>,FILE/</i></dt>
<dd> use FILE as xorriso [optional]</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
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
</dt><dd> <code>info grub-mkrescue</code></dd></dl>
<p> should give you access to the complete manual. </p>
