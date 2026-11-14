---
title: "ppmdcfont(1)"
name: "ppmdcfont"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmdcfont/"
description: "ppmdcfont – Turn a Ppmdfont file into C source for a builtin font"
---

<h2 class="name">NAME</h2>
<p> ppmdcfont &#8211; Turn a Ppmdfont file into C source for a builtin font</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmdcfont</code> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> (There are no arguments or options) </p>
<p> <code>ppmdcfont</code> creates a C source file that you can compile into a built-in font for use with the Netpbm PPM drawing facilities. It reads a Ppmdfont file on Standard Input and writes the C source code to Standard Output. </p>
<p> The output C source code has the font object&#8217;s name hardcoded as <code>ppmd_standardfont</code>, which you will definitely want to edit, because that is the name of the font built in to <code>libnetpbm</code>. If you don&#8217;t change it, it will conflict both cognitively and in program linking. There should obviously be an option on <code>ppmdcfont</code> to choose this, but the development effort has not been justified so far. </p>
<p> See <code>Libnetpbm</code>PPM<code>Drawing</code>Function Manual (1)<br />
&nbsp;<wbr>for details on Ppmdfont files. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmdraw/">ppmdraw</a></code>(1) , <code><a href="/docs/linux/man/1-ppmddumpfont/">ppmddumpfont</a></code>(1) , <code><a href="/docs/linux/man/1-ppmdcfont/">ppmdcfont</a></code>(1) , <code>Libnetpbm</code>PPM<code>Drawing</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) </p>
<h2>Index</h2>
