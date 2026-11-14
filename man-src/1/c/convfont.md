---
title: "convfont(1)"
name: "convfont"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convfont/"
description: "convfont – convert font files for svgalib"
---

<h2>NAME</h2>
<p> convfont &#8211; convert font files for svgalib</p>
<h2>SYNOPSIS</h2>
<p> <code>convfont</code><i> fontfile fontheight vgafontfile</i> </p>
<h2>DESCRIPTION</h2>
<p> convert the standard format binary fontfile name <i>fontfile</i> to the codepage format required by <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1). The converted font is written to <i>vgafontfile</i>. </p>
<p> A binary font file of any number of characters up to 256 can be used, although at least defining the first 128 characters is a good idea. The <i>fontheight</i> must be in the range <code>1</code> &#8211; <code>32</code>. </p>
<p> The <i>fontfile</i> file consist of <i>fontheight</i> bytes stored sequentially (top to bottom) for each character in your font, starting with the character with code 0. </p>
<p> The format of <i>vgafontfile</i> is that required by <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1) and described there. </p>
<p> This utility is part of svgalib and can be found in the <i>utils/</i> subdirectory of the original svgalib distribution. However, it is not installed by default, s.t. it is unclear where you can find it if your svgalib was install linux distribution. </p>
<p> In case of any such problem, simply get an svgalib distribution from the net. You don&#8217;t need to install it. Just <code>make</code> in the <i>utils/</i> subdirecty. As of this writing, <i>svgalib-1.2.12.tar.gz</i> is the latest version and can be retrieved by ftp from <i>sunsite.unc.edu</i> at <i>/pub/Linux/libs/graphics</i> and <i>tsx-11.mit.edu</i> at <i>/pub/linux/sources/libs</i> which will most probably be mirrored by a site close to you. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
