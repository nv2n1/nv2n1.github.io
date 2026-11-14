---
title: "setmclk(1)"
name: "setmclk"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setmclk/"
description: "setmclk – adjust the memory timing of certain Cirrus cards."
---

<h2>NAME</h2>
<p> setmclk &#8211; adjust the memory timing of certain Cirrus cards.</p>
<h2>SYNOPSIS</h2>
<p> <code>setmclk</code> </p>
<h2>DESCRIPTION</h2>
<p> This program sets the <code>memory clock</code> of Cirrus 5424/26/28 cards. </p>
<p> The first three values could be set by utility programs that came with my card (AVGA3), but somewhat higher values seem to work (on my card at least). It may be that better and more recent Cirrus cards use a higher value as boot-up default. It should depend on DRAM speed, but it seems to be more dependant on the card logic. </p>
<p> I have the impression that many Cirrus 542x cards suffer from horrible BIOS version/DRAM timing misconfigurations. Perhaps even some versions of MS-Windows drivers change the MCLK register. In any case, the boot-up BIOS default (0x1c) may be inappropriately low for the type of DRAM timing most cards use. </p>
<p> Using a higher memory clock gives a very significant performance improvement; with high dot clock modes (like 640x480x16M or 1150x900x256) performance can be more than twice that of the standard 50 MHz clock. This goes for both (VLB) framebuffer access and accelerated features (bitblt). This also helps XFree86 server performance, but only if the XFree86 Cirrus driver doesn&#8217;t set the memory clock register (it should work for XFree86 1.3 and 2.0). Use at your own risk! </p>
<p> Note that the <code>dot clock</code> is something entirely different. There does not seem to be much correlation between the two (i.e. if a high dot clock gives screen problems, using a high memory clock is not likely to fix it, other than improving speed). </p>
<p> The actual <code>memory clock</code> is hard compiled into the program. It defaults to 0x1c. You can change this value and some suggestiong come in th source of the utility. </p>
<p> This utility is part of svgalib and can be found in the <i>utils/</i> subdirectory of the original svgalib distribution. However, it is not installed by default, s.t. it is unclear where you can find it if your svgalib was install linux distribution. </p>
<p> In case of any such problem, simply get an svgalib distribution from the net. You don&#8217;t need to install it. Just <code>make</code> in the <i>utils/</i> subdirecty. As of this writing, <i>svgalib-1.2.12.tar.gz</i> is the latest version and can be retrieved by ftp from <i>sunsite.unc.edu</i> at <i>/pub/Linux/libs/graphics</i> and <i>tsx-11.mit.edu</i> at <i>/pub/linux/sources/libs</i> which will most probably be mirrored by a site close to you. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
