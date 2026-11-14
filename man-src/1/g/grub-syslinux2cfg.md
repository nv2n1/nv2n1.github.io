---
title: "grub-syslinux2cfg(1)"
name: "grub-syslinux2cfg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-syslinux2cfg/"
description: "grub-syslinux2cfg – transform syslinux config into grub.cfg"
---

<h2 class="name">NAME</h2>
<p> grub-syslinux2cfg &#8211; transform syslinux config into grub.cfg </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-syslinux2cfg</code> [<i>,OPTION/</i>&#8230;] <i>,FILE/</i></p>
<h2>DESCRIPTION</h2>
<p> Transform syslinux config into GRUB one.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;cwd</code>=<i>,DIR/</i></p>
<dd> current directory of syslinux [default is parent directory of input file].</p>
<dt><code>-i</code>, <code>&#8211;isolinux</code></p>
<dd> assume input is an isolinux configuration file.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> write output to FILE [default=stdout].</p>
<dt><code>-p</code>, <code>&#8211;pxelinux</code></p>
<dd> assume input is a pxelinux configuration file.</p>
<dt><code>-r</code>, <code>&#8211;root</code>=<i>,DIR/</i></p>
<dd> root directory of the syslinux disk [default=/].</p>
<dt><code>-s</code>, <code>&#8211;syslinux</code></p>
<dd> assume input is a syslinux configuration file.</p>
<dt><code>-t</code>, <code>&#8211;target-root</code>=<i>,DIR/</i></p>
<dd> root directory as it will be seen on runtime [default=/].</p>
<dt><code>-T</code>, <code>&#8211;target-cwd</code>=<i>,DIR/</i></p>
<dd> current directory of syslinux as it will be seen on runtime [default is parent directory of input file].</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print verbose messages.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub-menulst2cfg/">grub-menulst2cfg</a></code>(8) </p>
<p> The full documentation for <code>grub-syslinux2cfg</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-syslinux2cfg</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-syslinux2cfg</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
