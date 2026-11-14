---
title: "restorepalette(1)"
name: "restorepalette"
section: "1"
letter: "r"
url: "/docs/linux/man/1-restorepalette/"
description: "restorepalette – set the color palette for textmode."
---

<h2>NAME</h2>
<p> restorepalette &#8211; set the color palette for textmode.</p>
<h2>SYNOPSIS</h2>
<p> <code>restorepalette [</code><i>filename</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>restorepalette</code> without arguments sets the standard VGA palette. This can be useful if it is somehow messed up. </p>
<p> With a <i>filename</i> argument a custom palette can be loaded (feature added by Charles Blake &lt;chuckb [at] alice.wonderland.caltech.edu&gt;). </p>
<p> This allow a user to set up a file that looks like this one (These color map definitions are the same as the default VGA ones. Alter to suite personal tastes). The first column contains the number of the color to set, then follow three integers in range 0 &#8211; 63 (lowest to highest intensity) for red, green, blue. </p>
<dl>
<dt>
<dd> <code> 0 0 0 0 # black</code><br />
 <code> 1 0 0 42 # blue</code><br />
 <code> 2 0 42 0 # green</code><br />
 <code> 3 0 42 42 # cyan</code><br />
 <code> 4 42 0 0 # red</code><br />
 <code> 5 42 0 42 # magenta</code><br />
 <code> 6 42 21 0 # brown</code><br />
 <code> 7 42 42 42 # white</code><br />
 <code> 8 21 21 21 # bright black</code><br />
 <code> 9 21 21 63 # bright blue</code><br />
 <code>10 21 63 21 # bright green</code><br />
 <code>11 21 63 63 # bright cyan</code><br />
 <code>12 63 21 21 # bright red</code><br />
 <code>13 63 21 63 # bright magenta</code><br />
 <code>14 63 63 21 # bright brown</code><br />
 <code>15 63 63 63 # bright white</code></dl>
<p> The inline comments are the only kind of allowed, as I use a little <code><a href="/docs/linux/man/3-fscanf/">fscanf</a></code>(3) trick to get them. Blank lines are ok, but not pure comment lines. See the comments in my code, also. </p>
<p> This allows people to set up custom palettes for use in virtual console text modes. I use it all the time. When combined with a color-syntax editor like jed-0.97+ or color-ls, etc., being able to choose your own text-mode palette is quite a bonus. I set mine up via <code>restorepalette /etc/palette</code> in my <i>/etc/rc</i>. If the program is given the correct permissions, then individual users can have <code>restorepalette ~/.palette</code> or some such thing in their shell startup files. Of course, it shouldn&#8217;t be done when starting remote shells or when under X, so some kind of test that <code>TERM</code> is a virtual console is needed for that case. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/3-vga_setpalvec/">vga_setpalvec</a></code>(3), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-restorefont/">restorefont</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
