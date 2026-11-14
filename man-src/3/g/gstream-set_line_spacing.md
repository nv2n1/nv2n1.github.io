---
title: "gstream-set_line_spacing(3)"
name: "gstream-set_line_spacing"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_line_spacing/"
description: "set_line_spacing"
---

<h2>NAME</h2>
<p> set_line_spacing</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_line_spacing(int ls);</code></p>
<h2>DESCRIPTION</h2>
<p> Sets the line spacing in pixels. The supplied value is added to the height of the font so if your font is 12 pixels high, and you call this function with 4, then the outputter will go 16 pixels down each time a newline is encountered, effectively making the space between the lines be 4 pixels. Note that nothing prevents you from supplying a negative value which, for instance, could cause the lines to overlap. </p>
<p> Every time you select a new font, the gstream will call this function with 1. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-get_line_spacing/">gstream-get_line_spacing</a></code>(3) </p>
<h2>Index</h2>
