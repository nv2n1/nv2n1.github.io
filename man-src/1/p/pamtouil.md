---
title: "pamtouil(1)"
name: "pamtouil"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtouil/"
description: "pamtouil – convert a PNM or PNM/alpha image into a Motif UIL icon file"
---

<h2 class="name">NAME</h2>
<p> pamtouil &#8211; convert a PNM or PNM/alpha image into a Motif UIL icon file</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtouil</code> [<code>-name=</code><i>uilname</i>] [<i>pamfile</i>] </p>
<p> You may abbreviate any option to its shortest unique prefix. You may use two hyphens instead of one to delimit an option. You may separate an option from its value with whitespace instead of <code>=</code>. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtouil</code> reads a PNM or PAM image as input and produces a Motif UIL icon file as output. If the input is PAM, it may be either a regular grayscale or color image or grayscale+alpha or color+alpha. Where the alpha channel is present, <code>pamtouil</code> renders pixels that are more than half transparent as transparent in the output. </p>
<p> In the UIL&#8217;s colormap, <code>pamtouil</code> uses the color names from the RGB database &#8212; the same one <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1) </p>
<p> uses. Where a color in the input does not exactly match one of the colors named in the RGB database, <code>pamtouil</code> uses the closest color named in the RGB database. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-name</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Allows you to specify the prefix string which is printed in the<br />
&nbsp;<wbr>&nbsp;<wbr>resulting UIL output.&nbsp;<wbr>&nbsp;<wbr>If not specified, will default to the filename<br />
&nbsp;<wbr>&nbsp;<wbr>(without extension)&nbsp;<wbr>of the ppmfile argument.&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr><code>-name</code>&nbsp;<wbr>is not<br />
&nbsp;<wbr>&nbsp;<wbr>specified and no ppmfile is specified&nbsp;<wbr>(i.e. piped input), the<br />
&nbsp;<wbr>&nbsp;<wbr>prefix string will default to the string&nbsp;<wbr>&#8216;noname&#8217;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamstack/">pamstack</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> Before May 2002, <code>pamtouil</code> was called <code>ppmtouil</code> and had no way to specify transparency. </p>
<h2>AUTHOR</h2>
<p> Converted by Bryan Henderson from ppmtouil.c, which was converted by Jef Poskanzer from ppmtoxpm.c, which is Copyright (C) 1990 by Mark W. Snitily </p>
<h2>Index</h2>
