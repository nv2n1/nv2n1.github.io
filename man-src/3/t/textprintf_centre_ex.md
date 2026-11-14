---
title: "textprintf_centre_ex(3)"
name: "textprintf_centre_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textprintf_centre_ex/"
description: "textprintf_centre_ex – Formatted centered output of a string. Allegro game programming library."
---

<p>textprintf_centre_ex &#8211; Formatted centered output of a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textprintf_centre_ex(BITMAP *bmp, const FONT *f, int x, int y,

                          int color, int bg, const char *fmt, ...);</code></pre>
<h2>Description</h2>
<p>Like textprintf_ex(), but interprets the x coordinate as the centre rather than the left edge of the string. This function shares the text length limitation of textprintf_ex(). Example: </p>
<pre> textprintf_centre_ex(screen, font, SCREEN_W / 2, 120,
 makecol(0, 100, 243), -1,
 &quot;Your best score so far was %d!&quot;,
 total_max_points);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3), <code><a href="/docs/linux/man/3-textout_centre_ex/">textout_centre_ex</a></code>(3) </p>
