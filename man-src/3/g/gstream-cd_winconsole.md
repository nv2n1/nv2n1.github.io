---
title: "gstream-cd_winconsole(3)"
name: "gstream-cd_winconsole"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-cd_winconsole/"
description: "cd_winconsole"
---

<h2>NAME</h2>
<p> cd_winconsole</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void cd_winconsole(BITMAP *bmp, int x, int y, int w, int h, int clr, bool ins);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a mixture of a win cursor and console cursor: the insert cursor looks like a win cursor (a vertical line: | ), whereas the overwrite cursor is like the console overwrite cursor (it covers the letter). </p>
<p> The preferred dimensions for this cursor (you have to set them manually) are: (1, gbuf::DYNAMIC_CURSOR_SIZE, gbuf::DYNAMIC_CURSOR_SIZE, gbuf::DYNAMIC_CURSOR_SIZE) but the first argument can be bigger for a broader cursor. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-set_cursor_drawer/">gstream-set_cursor_drawer</a></code>(3), <code><a href="/docs/linux/man/3-gstream-cd_console/">gstream-cd_console</a></code>(3) </p>
<h2>Index</h2>
