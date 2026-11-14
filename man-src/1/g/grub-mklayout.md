---
title: "grub-mklayout(1)"
name: "grub-mklayout"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mklayout/"
description: "grub-mklayout – generate a GRUB keyboard layout file"
---

<h2 class="name">NAME</h2>
<p> grub-mklayout &#8211; generate a GRUB keyboard layout file </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mklayout</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTIONS/</i>]</p>
<h2>DESCRIPTION</h2>
<p> grub-mklayout processes a keyboard layout description in <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) format into a format that can be used by GRUB&#8217;s <code>keymap</code> command. </p>
<p> Generate GRUB keyboard layout from Linux console one.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>,FILE/</i></p>
<dd> set input filename. Default is STDIN</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> set output filename. Default is STDOUT</p>
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
<p> <code><a href="/docs/linux/man/8-grub-mkconfig/">grub-mkconfig</a></code>(8) </p>
<p> The full documentation for <code>grub-mklayout</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mklayout</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-mklayout</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
