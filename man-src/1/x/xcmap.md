---
title: "xcmap(1)"
name: "xcmap"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcmap/"
description: "xcmap – displays the default colormap on X11 displays"
---

<h2>NAME</h2>
<p> xcmap &#8211; displays the default colormap on X11 displays</p>
<h2>SYNTAX</h2>
<p> <code>xcmap</code> [ [-d] <i>display</i>] [ [-g] <i>geometry</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xcmap</code> is an X11 program that displays the contents of the colormap on 4, 6, and 8-bit PseudoColor (or GreyScale) displays. It displays a grid of squares, (4&#215;4, 8&#215;8, or 16&#215;16 grid, depending on the number of planes) that correspond to entries in the colormap. The squares are (of course) drawn in their corresponding color. </p>
<p> You may click (with the left button) on any of these squares. Doing so will display the pixel number corresponding to that square, and its red, green, and blue components (as 4-digit hex numbers). It will continue to do this as long as you hold the button down. </p>
<h2>BUGS</h2>
<p> This program only works on colormapped displays (PseudoColor, GreyScale, StaticColor, and StaticGrey visuals). Running it on a display that has a default visual type of &#8216;TrueColor&#8217; or &#8216;DirectColor&#8217; will do nothing of value, and may or may not work at all. </p>
<p> Also, this program only works on 4, 6, and 8-bit displays. Period. </p>
<h2>AUTHOR</h2>
<p> John Bradley &#8211; bradley [at] dccs.upenn.edu </p>
<h2>Index</h2>
