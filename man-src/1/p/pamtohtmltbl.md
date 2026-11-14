---
title: "pamtohtmltbl(1)"
name: "pamtohtmltbl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtohtmltbl/"
description: "pamtohtmltbl – convert pnm/pam visual image to an HTML table"
---

<h2 class="name">NAME</h2>
<p> pamtohtmltbl &#8211; convert pnm/pam visual image to an HTML table</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtohtmltbl</code> [<code>-transparent=</code><i>color</i>] [<code>-verbose</code>] [<i>file</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtohtmltbl</code> converts a visual image to an HTML table with one cell per pixel. The cell is empty, but its background color is that of the pixel. </p>
<p> <i>file</i> is a PBM, PGM, PPM, or PAM file. If PAM, it must be a standard visual image of tuple type RGB, GRAYSCALE, or BLACKANDWHITE, or something equivalent with extra higher numbered channels, but <code>pamtohtmltbl</code> doesn&#8217;t check the tuple type; it just assumes. </p>
<p> Note that the more normal way to include a visual image in an HTML document is with a &lt;IMG&gt; tag. </p>
<p> Not all web browsers render tables as <code>pamtohtmltbl</code> expects, and therefore show a grossly distorted image. Internet Explorer 7 on Windows and Opera 9.02 on Windows have been seen to work; Firefox 2.0.0.16 on the same Windows system has been seen not to. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-transparent=</code><i>color</i></p>
<dd> This option indicates that pixels of the specified color are to be transparent in the HTML table. The table cell for a pixel of this color will have no background color specified. </p>
<p> Specify the color (<i>color</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<dt><code>-verbose</code></p>
<dd> This option causes <code>pamtohtmltbl</code> to display messages about the conversion process.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamtohtmltbl</code> was new in Netpbm 10.15 (April 2003). </p>
<h2>AUTHORS</h2>
<p> Alexander B. Ivanov (SSH) wrote a program he called <code>pnm2html</code>. Bryan Henderson adapted it to use the Netpbm libraries and handle PAM images and follow Netpbm conventions, and named it <code>pamtohtmltbl</code>. </p>
<h2>Index</h2>
