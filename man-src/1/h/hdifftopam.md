---
title: "hdifftopam(1)"
name: "hdifftopam"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hdifftopam/"
description: "hdifftopam – convert horizontal difference image to original PAM image"
---

<h2 class="name">NAME</h2>
<p> hdifftopam &#8211; convert horizontal difference image to original PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>hdifftopam</code>[<i>pamfile</i>] [<code>-pnm</code>] [<code>-verbose</code>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>hdifftopam</code> undoes what <code>pamtohdiff</code> does. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-pnm</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>This option tells&nbsp;<wbr><code>hdifftopam</code>&nbsp;<wbr>to create a PNM image&nbsp;<wbr>(i.e. PGM or<br />
&nbsp;<wbr>&nbsp;<wbr>PPM).&nbsp;<wbr>&nbsp;<wbr>Without it,&nbsp;<wbr><code>hdifftopam</code>&nbsp;<wbr>creates a PAM image&nbsp;<wbr>(with a<br />
&nbsp;<wbr>&nbsp;<wbr>tuple type of&nbsp;<wbr>&quot;unhdiff&quot;).&nbsp;<wbr>&nbsp;<wbr>If the PAM does not have the proper depth<br />
&nbsp;<wbr>&nbsp;<wbr>to be a PGM or PPM&nbsp;<wbr>(i.e. 1 or 3)&nbsp;<wbr>and you specify&nbsp;<wbr><code>-pnm</code>,<br />
&nbsp;<wbr>&nbsp;<wbr><code>hdifftopam</code>&nbsp;<wbr>fails. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtohdiff/">pamtohdiff</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Bryan Henderson </p>
<h2>Index</h2>
