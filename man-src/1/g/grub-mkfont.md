---
title: "grub-mkfont(1)"
name: "grub-mkfont"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mkfont/"
description: "grub-mkfont – make GRUB font files"
---

<h2 class="name">NAME</h2>
<p> grub-mkfont &#8211; make GRUB font files </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkfont</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTIONS/</i>] <i>,FONT_FILES/</i></p>
<h2>DESCRIPTION</h2>
<p> Convert common font file formats into PF2</p>
<dl>
<dt><code>-a</code>, <code>&#8211;force-autohint</code></p>
<dd> force autohint</p>
<dt><code>-b</code>, <code>&#8211;bold</code></p>
<dd> convert to bold font</p>
<dt><code>-c</code>, <code>&#8211;asce</code>=<i>,NUM/</i></p>
<dd> set font ascent</p>
<dt><code>-d</code>, <code>&#8211;desc</code>=<i>,NUM/</i></p>
<dd> set font descent</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>,NUM/</i></p>
<dd> select face index</p>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>,NAME/</i></p>
<dd> set font family name</p>
<dt><code>&#8211;no-bitmap</code></p>
<dd> ignore bitmap strikes when loading</p>
<dt><code>&#8211;no-hinting</code></p>
<dd> disable hinting</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> save output in FILE [required]</p>
<dt><code>-r</code>, <code>&#8211;range</code>=<i>,FROM-TO[/</i>,FROM-TO]</p>
<dd> set font range</p>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>,SIZE/</i></p>
<dd> set font size</p>
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
<p> The full documentation for <code>grub-mkfont</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mkfont</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-mkfont</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
