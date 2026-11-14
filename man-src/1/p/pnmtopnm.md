---
title: "pnmtopnm(1)"
name: "pnmtopnm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtopnm/"
description: "pnmtopnm – copy a PNM image"
---

<h2 class="name">NAME</h2>
<p> pnmtopnm &#8211; copy a PNM image </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtopnm</code> </p>
<p> [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pnmtopnm</code> simply copies a PNM image to Standard Output. The output has the same major PNM format (PBM, PGM, or PPM) and maxval as the input. This may seem an unnecessary duplication of <code>cat</code>, but it lets you convert between the plain (ASCII) and raw (binary) subformats of PNM. Use the <code>-plain</code> Netpbm common option to ensure the output is plain PNM, and don&#8217;t use <code>-plain</code> to ensure the output is raw PNM. See<br />
&nbsp;<wbr>Common Options . </p>
<p> You don&#8217;t normally need to convert between the PNM subformats, because any program that uses the Netpbm library to read a PNM image will read all of them directly. But there are a lot of programs that don&#8217;t use the Netpbm library and understand only the raw format. Plain format is nice because it is human readable; people often use it to debug programs that process PNM images. </p>
<p> <code>pnmtopnm</code> is really just another name for the program <code>pamtopnm</code>. The latter does the job because like any Netpbm program that takes PAM input via the Netpbm programming library facilities, it also takes PNM input. </p>
<h2>HISTORY</h2>
<p> <code>pnmtopnm</code> was new in Netpbm 10.23 (July 2004). It obsoleted <code>pnmtoplainpnm</code>, which specifically did the conversion to plain PNM. There was no program to explicitly convert to raw PNM, but many Netpbm programs can be made, with the right options, to be idempotent (i.e. to do the same thing as <code>pnmtopnm</code>). </p>
<p> Then David Jones realized that the existing <code>pamtopnm</code> already did everything that <code>pnmtopnm</code> did and more, so in Netpbm 10.27 (March 2005), <code>pnmtopnm</code> became simply an alternate name for <code>pamtopnm</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtoppm/">ppmtoppm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pgmtopgm/">pgmtopgm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>Index</h2>
