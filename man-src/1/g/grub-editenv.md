---

title: "grub-editenv(1)"
name: "grub-editenv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-editenv/"
description: "grub-editenv – edit GRUB environment block"
---

<p> grub-editenv &#8211; edit GRUB environment block </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-editenv</code> [<i>,OPTION/</i>&#8230;] <i>,FILENAME COMMAND/</i></p>
<h2>DESCRIPTION</h2>
<p> Tool to edit environment block.</p>
<dl>
<dt>
</dt><dd> Commands:</dd>
<dt>create</dt>
<dd> Create a blank environment block file.</dd>
<dt>list</dt>
<dd> List the current variables.</dd>
<dt>set [NAME=VALUE &#8230;]</dt>
<dd> Set variables.</dd>
<dt>unset [NAME &#8230;]</dt>
<dd> Delete variables.</dd>
<dt>
</dt><dd> Options:</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print verbose messages.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
<p> If FILENAME is `-&#8216;, the default value <i>,/boot/grub/grubenv/</i> is used. </p>
<p> There is no `delete&#8217; command; if you want to delete the whole environment block, use `rm /boot/grub/grubenv&#8217;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub-reboot/">grub-reboot</a></code>(8), <code><a href="/docs/linux/man/8-grub-set-default/">grub-set-default</a></code>(8) </p>
<p> The full documentation for <code>grub-editenv</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-editenv</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-editenv</code></dd></dl>
<p> should give you access to the complete manual. </p>
