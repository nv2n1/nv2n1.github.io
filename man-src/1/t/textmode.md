---
title: "textmode(1)"
name: "textmode"
section: "1"
letter: "t"
url: "/docs/linux/man/1-textmode/"
description: "savetextmode, textmode – save or restore the complete SVGA status for textmode."
---

<h2>NAME</h2>
<p> savetextmode, textmode &#8211; save or restore the complete SVGA status for textmode.</p>
<h2>SYNOPSIS</h2>
<p> <code>savetextmode</code><br />
 <code>textmode</code> </p>
<h2>DESCRIPTION</h2>
<p> These are simple scripts to save the SVGA register state when in textmode to the files <i>/etc/vga/fontdata</i> and <i>/etc/vga/textregs</i> (<i>$HOME/.vga/fontdata</i> and <i>$HOME/.vga/textregs</i> if directory <i>/etc/vga</i> is not writeable) or to restore it from these files. </p>
<p> The actual utilities used are <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), and <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1). </p>
<p> The purpose of these scripts program is usually to recover from a crashed console due to an svgalib, Xfree or other program bug. </p>
<p> You do this by being a smart guy and running <code>savetextmode</code> right after booting of your machine, <code>prior</code> to any problems. Then, in case the SVGA state is hosed and you sit in front of a blank or useless console, change VC (maybe login) to get to a shell. Or exist the currently running program with <code>&lt;Ctrl&gt;-C</code>, <code>&lt;Ctrl&gt;-&lt;Alt&gt;-&lt;Backspace&gt;</code>, or whatever applies. Once you got a shell, run <code>textmode</code> and it will hopefully render your console useable again. </p>
<p> To make it clear: You do all this while not seeing anything on your console screen, you enter this information blindly or after logging in from a network. Also, if the keyboard is left in raw mode, nothing can really help you as you cannot enter anything which a shell will understand. </p>
<h2>FILES</h2>
<p> <i>/etc/vga/fontdata</i> or <i>$HOME/.vga/fontdata</i><br />
 <i>/etc/vga/textregs</i> or <i>$HOME/.vga/textregs</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
