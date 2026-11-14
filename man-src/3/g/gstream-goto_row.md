---
title: "gstream-goto_row(3)"
name: "gstream-goto_row"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-goto_row/"
description: "goto_row"
---

<h2>NAME</h2>
<p> goto_row</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void goto_row(int row);</code></p>
<h2>DESCRIPTION</h2>
<p> Moves the cursor to line number ROW. If, for instance, the currently used font has a height of 12, then <a href="/docs/linux/man/4-goto_row/">goto_row</a>(4) is exactly the same as goto_y(4*12). Unless, of course, you use another line spacing than the default as the formula is </p>
<pre>
   y-coordinate = line_spacing * row
   
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-move_row/">gstream-move_row</a></code>(3), <code><a href="/docs/linux/man/3-gstream-goto_xy/">gstream-goto_xy</a></code>(3) </p>
<h2>Index</h2>
