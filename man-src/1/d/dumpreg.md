---
title: "dumpreg(1)"
name: "dumpreg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dumpreg/"
description: "dumpreg – dump the state of the card as the svgalib chipset driver sees it."
---

<h2>NAME</h2>
<p> dumpreg &#8211; dump the state of the card as the svgalib chipset driver sees it.</p>
<h2>SYNOPSIS</h2>
<p> <code>dumpreg</code><br />
 <code>dumpreg &lt; /dev/tty</code><i>N</i> </p>
<h2>DESCRIPTION</h2>
<p> The chipset drivers of svgalib inquire the mode of the graphic card when the application is started and restore it when the svgalib application quits. <code>dumpreg</code> prints this information to stdout. </p>
<p> This is useful for debugging or adding modes to a device driver. For example you can use Xfree86 to setup a given mode timing, then run <code>dumpreg</code> and use it&#8217;s stdout to make your chipset driver use exactly this timing. </p>
<p> However, the recent change of svgalib to hunt an own free virtual console does not allow this, because it will make Xfree86 return to textmode first. You can avoid this by using the second form where <i>N</i> is the number of the virtual console on which Xfree86 runs (usually 7) as root. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/3-vga_dumpregs/">vga_dumpregs</a></code>(3), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
