---
title: "grub-mkpasswd-pbkdf2(1)"
name: "grub-mkpasswd-pbkdf2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mkpasswd-pbkdf2/"
description: "grub-mkpasswd-pbkdf2 – generate hashed password for GRUB"
---

<h2 class="name">NAME</h2>
<p> grub-mkpasswd-pbkdf2 &#8211; generate hashed password for GRUB </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkpasswd-pbkdf2</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTIONS/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Generate PBKDF2 password hash.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;iteration-count</code>=<i>,NUM/</i></p>
<dd> Number of PBKDF2 iterations</p>
<dt><code>-l</code>, <code>&#8211;buflen</code>=<i>,NUM/</i></p>
<dd> Length of generated hash</p>
<dt><code>-s</code>, <code>&#8211;salt</code>=<i>,NUM/</i></p>
<dd> Length of salt</p>
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
<p> <code><a href="/docs/linux/man/8-grub-mkconfig/">grub-mkconfig</a></code>(8) </p>
<p> The full documentation for <code>grub-mkpasswd-pbkdf2</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mkpasswd-pbkdf2</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-mkpasswd-pbkdf2</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
