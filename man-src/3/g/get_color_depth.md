---
title: "get_color_depth(3)"
name: "get_color_depth"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_color_depth/"
description: "get_color_depth – Returns the current pixel color depth. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_color_depth &#8211; Returns the current pixel color depth. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_color_depth(void);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns the current pixel format. This can be very useful to know in order to write generic functions which select a different code path internally depending on the color depth being used. </p>
<p> Note that the function returns whatever value you may have set previously with set_color_depth(), which can be different from the current color depth of the screen global variable. If you really need to know the color depth of the screen, use bitmap_color_depth(). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_color_depth/">bitmap_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
<h2>Index</h2>
