---

title: "grub-syslinux2cfg(1)"
name: "grub-syslinux2cfg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-syslinux2cfg/"
description: "grub-syslinux2cfg – transform syslinux config into grub.cfg"
---

<p> <code>grub-syslinux2cfg</code> [<i>,OPTION/</i>&#8230;] <i>,FILE/</i></p>
<p> Transform syslinux config into GRUB one.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;cwd</code>=<i>,DIR/</i></dt>
<dd> current directory of syslinux [default is parent directory of input file].</dd>
<dt><code>-i</code>, <code>&#8211;isolinux</code></dt>
<dd> assume input is an isolinux configuration file.</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> write output to FILE [default=stdout].</dd>
<dt><code>-p</code>, <code>&#8211;pxelinux</code></dt>
<dd> assume input is a pxelinux configuration file.</dd>
<dt><code>-r</code>, <code>&#8211;root</code>=<i>,DIR/</i></dt>
<dd> root directory of the syslinux disk [default=/].</dd>
<dt><code>-s</code>, <code>&#8211;syslinux</code></dt>
<dd> assume input is a syslinux configuration file.</dd>
<dt><code>-t</code>, <code>&#8211;target-root</code>=<i>,DIR/</i></dt>
<dd> root directory as it will be seen on runtime [default=/].</dd>
<dt><code>-T</code>, <code>&#8211;target-cwd</code>=<i>,DIR/</i></dt>
<dd> current directory of syslinux as it will be seen on runtime [default is parent directory of input file].</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print verbose messages.</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code>grub-menulst2cfg</code>(8) </p>
<p> The full documentation for <code>grub-syslinux2cfg</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-syslinux2cfg</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-syslinux2cfg</code></dd></dl>
<p> should give you access to the complete manual. </p>
