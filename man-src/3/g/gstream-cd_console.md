---
title: "gstream-cd_console(3)"
name: "gstream-cd_console"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-cd_console/"
description: "cd_console"
---

<h2>NAME</h2>
<p> cd_console</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void cd_console(BITMAP *bmp, int x, int y, int w, int h, int clr, bool ins);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a normal console cursor: the insert cursor is like an _, and the overwrite cursor covers the letter. </p>
<p> The preferred dimensions (you have to set them manually) are: (gbuf::DYNAMIC_CURSOR_SIZE, gbuf::DYNAMIC_CURSOR_SIZE, gbuf::DYNAMIC_CURSOR_SIZE, gbuf::DYNAMIC_CURSOR_SIZE) but the second argument can be set manually to control where the _ will be placed &#8211; low values and the cursor will fly above the letters, high values and the cursor will float at the bottom. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-set_cursor_drawer/">gstream-set_cursor_drawer</a></code>(3), <code><a href="/docs/linux/man/3-gstream-cd_winconsole/">gstream-cd_winconsole</a></code>(3) </p>
<h2>Index</h2>
