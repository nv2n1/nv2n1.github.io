---
title: "restoretextmode(1)"
name: "restoretextmode"
section: "1"
letter: "r"
url: "/docs/linux/man/1-restoretextmode/"
description: "restoretextmode – save or restore the SVGA registers for textmode."
---

<h2>NAME</h2>
<p> restoretextmode &#8211; save or restore the SVGA registers for textmode.</p>
<h2>SYNOPSIS</h2>
<p> <code>restoretextmode {-r|-w} </code><i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> The state of the SVGA is written to or restored from <i>filename</i> using the <code><a href="/docs/linux/man/3-vga_gettextmoderegs/">vga_gettextmoderegs</a></code>(3) and <code><a href="/docs/linux/man/3-vga_settextmoderegs/">vga_settextmoderegs</a></code>(3) functions. </p>
<p> As of this writing this file is 385 bytes long but this might change with future versions. </p>
<p> Please do not fiddle with the contents of the file except when you know what you do. It might even result in hardware damage. Because of that, you should think twice to make this command available to all users on your system. </p>
<p> The purpose of this program is usually to recover from a crashed console due to an svgalib, Xfree or other program bug. First save the state of the SVGA card when on a text console. After the crash restore this state. The <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1) and <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1) script makes this procedure very easy. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w </code><i>filename</i></p>
<dd> write the SVGA state to the file <i>filename</i>.</p>
<dt><code>-r </code><i>filename</i></p>
<dd> restore the SVGA state from the file <i>filename</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/3-vga_gettextmoderegs/">vga_gettextmoderegs</a></code>(3), <code><a href="/docs/linux/man/3-vga_settextmoderegs/">vga_settextmoderegs</a></code>(3), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
