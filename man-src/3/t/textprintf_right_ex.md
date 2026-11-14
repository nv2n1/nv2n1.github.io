---
title: "textprintf_right_ex(3)"
name: "textprintf_right_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textprintf_right_ex/"
description: "textprintf_right_ex – Formatted right aligned output of a string. Allegro game programming library."
---

<p>textprintf_right_ex &#8211; Formatted right aligned output of a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textprintf_right_ex(BITMAP *bmp, const FONT *f, int x, y, color, bg,

                         const char *fmt, ...);</code></pre>
<h2>Description</h2>
<p>Like textprintf_ex(), but interprets the x coordinate as the right rather than the left edge of the string. This function shares the text length limitation of textprintf_ex(). Example: </p>
<pre> textprintf_right_ex(screen, font, SCREEN_W - 10, 10,
 makecol(200, 200, 20), -1,
 &quot;%d bullets left&quot;, player_ammo);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3), <code><a href="/docs/linux/man/3-textout_right_ex/">textout_right_ex</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3) </p>
