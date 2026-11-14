---
title: "textout_right_ex(3)"
name: "textout_right_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textout_right_ex/"
description: "textout_right_ex – Writes a right aligned string on a bitmap. Allegro game programming library."
---

<p>textout_right_ex &#8211; Writes a right aligned string on a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textout_right_ex(BITMAP *bmp, const FONT *f, const char *s,

                      int x, int y, int color, int bg);</code></pre>
<h2>Description</h2>
<p>Like textout_ex(), but interprets the x coordinate as the right rather than the left edge of the string. Example: </p>
<pre> textout_right_ex(screen, font, &quot;Look at this color!&quot;,
 SCREEN_W - 10, 10, my_yellow, -1);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_right_ex/">textprintf_right_ex</a></code>(3) </p>
