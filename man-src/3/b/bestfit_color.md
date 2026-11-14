---
title: "bestfit_color(3)"
name: "bestfit_color"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bestfit_color/"
description: "bestfit_color – Finds a palette color fitting the requested RGB values. Allegro game programming library."
---

<h2>NAME</h2>
<p> bestfit_color &#8211; Finds a palette color fitting the requested RGB values. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int bestfit_color(const PALETTE pal, int r, int g, int b);</code></p>
<h2>DESCRIPTION</h2>
<p> Searches the specified palette for the closest match to the requested color, which are specified in the VGA hardware 0-63 format. Normally you should call makecol8() instead, but this lower level function may be useful if you need to use a palette other than the currently selected one, or specifically don&#8217;t want to use the rgb_map lookup table.</p>
<h2>RETURN VALUE</h2>
<p> Returns the index of the palette for the closest match to the requested color. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makecol8/">makecol8</a></code>(3) </p>
<h2>Index</h2>
