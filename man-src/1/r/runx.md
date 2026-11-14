---
title: "runx(1)"
name: "runx"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runx/"
description: "runx – try to overcome problems of Xfree96 restoring textmode using svgalib."
---

<h2>NAME</h2>
<p> runx &#8211; try to overcome problems of Xfree96 restoring textmode using svgalib.</p>
<h2>SYNOPSIS</h2>
<p> <code>runx</code> </p>
<h2>DESCRIPTION</h2>
<p> If XFree86 corrupts your textmode font, try putting <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1) in your path and use the shell script <code>runx</code> to run X. <code>runx</code> saves the VGA font data in <i>/tmp/fontdata</i>, and restores it when you exit X. </p>
<p> The <code>runx</code> script actually is: </p>
<dl>
<dt>
<dd> <code>#!/bin/sh</code><br />
 <code>echo Saving font in /tmp/fontdata</code><br />
 <code>restorefont -w /tmp/fontdata</code><br />
 <code>startx</code><br />
 <code>echo Restoring font from /tmp/fontdata</code><br />
 <code>restorefont -r /tmp/fontdata</code></dl>
<p> Note that this doesn&#8217;t help with syncing problems. </p>
<p> A more rigorous alternative is to run the <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1) script before running X, and <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1) after. This will restore the textmode registers and the VGA palette in addition to the VGA font. </p>
<p> Assuming that <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1) and <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1) are in your <code>PATH</code> the <code>runx</code> script would then look like: </p>
<dl>
<dt>
<dd> <code>#!/bin/sh</code><br />
 <code>echo Saving SVGA state</code><br />
 <code>savetextmode</code><br />
 <code>startx</code><br />
 <code>echo restoring SVGA state</code><br />
 <code>textmode</code></dl>
<p> This utility is part of svgalib and can be found in the <i>utils/</i> subdirectory of the original svgalib distribution. However, it is not installed by default, s.t. it is unclear where you can find it if your svgalib was install by a linux distribution. </p>
<p> However, this is no big deal as it was printed out above already ;-). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
