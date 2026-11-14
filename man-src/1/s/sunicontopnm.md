---
title: "sunicontopnm(1)"
name: "sunicontopnm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sunicontopnm/"
description: "sunicontopnm – convert a Sun icon into a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> sunicontopnm &#8211; convert a Sun icon into a Netpbm image </p>
<h2>SYNOPSIS</h2>
<p> <code>sunicontopnm</code> [<i>iconfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>sunicontopnm</code> reads a Sun icon as input and produces a PBM or PGM image as output. </p>
<p> If the input is of the Depth=8 variety, the output is PGM. Otherwise, it is PBM. Before Netpbm 10.53 (December 2010), the program would not work on a Depth=8 icon. </p>
<p> If the input is color, the output is still PGM (the program can&#8217;t do any better because developers haven&#8217;t figured out how). If you know the palette used by the Sun icon image, you can use <code>pamlookup</code> to convert the PGM output to the proper color Netpbm image. </p>
<h2>ABOUT SUN ICONS</h2>
<p> It seems that this icon format was used in Sunview and was usable in its successor Openlook/Openwindows in Sun 4.1.1, which offered backward compatibility for Sunview, including the icons. Sunview&#8217;s desktop was monochrome. OpenWindows had color icons. Sun 4 came with OpenWindows. OpenWindows appears to have been an X-based gui so presumably the icons were mostly XPM files. </p>
<p> So in addition to <code>sunicontopnm</code>, you should try <code>xpmtoppm</code> and <code>xbmtopbm</code> on icons from a Sun Workstation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtosunicon/">pbmtosunicon</a></code>(1) , <code><a href="/docs/linux/man/1-winicontoppm/">winicontoppm</a></code>(1) , <code><a href="/docs/linux/man/1-xpmtoppm/">xpmtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-xbmtoppm/">xbmtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-infotopam/">infotopam</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> Jef Poskanzer wrote the program under the name <code>icontopbm</code> in 1988. </p>
<p> In October 2010, Prophet Of The Way (afu [at] wta.att.ne.jp) converted it to use the more recent &#8216;packed PBM&#8217; library functions, thus speeding it up </p>
<p> Netpbm 10.53 (December 2010) renamed the program to <code>sunicontopnm</code>. This name reflects the fact that there are lots of kinds of icons in the world besides the Sun variety, Windows ones being most popular. It also takes into account the new Depth=8 capability (see below). </p>
<p> Netpbm 10.53 (December 2010) added the ability to work with Depth=8 icon input and input with 32 bit &#8216;items.&#8217; Whereas the previous program always produced PBM output, the new program produced PGM in the Depth=8 case. </p>
<h2>Index</h2>
