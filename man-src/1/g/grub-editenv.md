---
title: "grub-editenv(1)"
name: "grub-editenv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-editenv/"
description: "grub-editenv – edit GRUB environment block"
---

<h2 class="name">NAME</h2>
<p> grub-editenv &#8211; edit GRUB environment block </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-editenv</code> [<i>,OPTION/</i>&#8230;] <i>,FILENAME COMMAND/</i></p>
<h2>DESCRIPTION</h2>
<p> Tool to edit environment block.</p>
<dl>
<dt>
<dd> Commands:</p>
<dt>create</p>
<dd> Create a blank environment block file.</p>
<dt>list</p>
<dd> List the current variables.</p>
<dt>set [NAME=VALUE &#8230;]</p>
<dd> Set variables.</p>
<dt>unset [NAME &#8230;]</p>
<dd> Delete variables.</p>
<dt>
<dd> Options:</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print verbose messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> If FILENAME is `-&#8216;, the default value <i>,/boot/grub/grubenv/</i> is used. </p>
<p> There is no `delete&#8217; command; if you want to delete the whole environment block, use `rm /boot/grub/grubenv&#8217;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub-reboot/">grub-reboot</a></code>(8), <code><a href="/docs/linux/man/8-grub-set-default/">grub-set-default</a></code>(8) </p>
<p> The full documentation for <code>grub-editenv</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-editenv</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-editenv</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
