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
<dt><code>-a</code>, <code>&#8211;force-autohint</code></dt>
<dd> force autohint</dd>
<dt><code>-b</code>, <code>&#8211;bold</code></dt>
<dd> convert to bold font</dd>
<dt><code>-c</code>, <code>&#8211;asce</code>=<i>,NUM/</i></dt>
<dd> set font ascent</dd>
<dt><code>-d</code>, <code>&#8211;desc</code>=<i>,NUM/</i></dt>
<dd> set font descent</dd>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>,NUM/</i></dt>
<dd> select face index</dd>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>,NAME/</i></dt>
<dd> set font family name</dd>
<dt><code>&#8211;no-bitmap</code></dt>
<dd> ignore bitmap strikes when loading</dd>
<dt><code>&#8211;no-hinting</code></dt>
<dd> disable hinting</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> save output in FILE [required]</dd>
<dt><code>-r</code>, <code>&#8211;range</code>=<i>,FROM-TO[/</i>,FROM-TO]</dt>
<dd> set font range</dd>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>,SIZE/</i></dt>
<dd> set font size</dd>
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
<p> <code><a href="/docs/linux/man/8-grub-mkconfig/">grub-mkconfig</a></code>(8) </p>
<p> The full documentation for <code>grub-mkfont</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mkfont</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-mkfont</code></dd></dl>
<p> should give you access to the complete manual. </p>
