---
title: "textprintf_justify_ex(3)"
name: "textprintf_justify_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textprintf_justify_ex/"
description: "textprintf_justify_ex – Formatted justified output of a string. Allegro game programming library."
---

<p>textprintf_justify_ex &#8211; Formatted justified output of a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textprintf_justify_ex(BITMAP *bmp, const FONT *f, int x1, x2, y,

                           diff, color, bg, const char *fmt, ...);</code></pre>
<h2>Description</h2>
<p>Like textout_justify_ex(), but using a printf() style format string. This function shares the text length limitation of textprintf_ex(). Example: </p>
<pre><code>char *lines[] = {&quot;Line %02d: Draws justified text&quot;,
                 &quot;Line %02d: within the specified&quot;,
                 &quot;Line %02d: x2-x1 area. But not&quot;,
                 &quot;Line %02d: T H I S !&quot;, NULL};
/* Show the justification marker. */
vline(screen, 300, 0, SCREEN_H - 1, makecol(0, 0, 0));
/* Draw all the lines until we reach a NULL entry. */
for (num = 0, y = 0; lines[num]; num++, y += text_height(font))
    textprintf_justify_ex(screen, font, 0, 300, y, 180,
                          makecol(0, 0, 0), makecol(255, 255, 255),
                          lines[num], num);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3), <code><a href="/docs/linux/man/3-textout_justify_ex/">textout_justify_ex</a></code>(3) </p>
