---
title: "textout_justify_ex(3)"
name: "textout_justify_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textout_justify_ex/"
description: "textout_justify_ex – Draws justified text within a region. Allegro game programming library."
---

<p>textout_justify_ex &#8211; Draws justified text within a region. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textout_justify_ex(BITMAP *bmp, const FONT *f, const char *s,

                        int x1, int x2, int y, int diff, int color,

                        int bg);</code></pre>
<h2>Description</h2>
<p>Draws justified text within the region x1-x2. If the amount of spare space is greater than the diff value, it will give up and draw regular left justified text instead. Example: </p>
<pre><code>char *lines[] = {&quot;Draws justified text&quot;,
                 &quot;within the specified&quot;,
                 &quot;x2-x1 area. But not&quot;,
                 &quot;T H I S !&quot;, NULL};
/* Show the justification marker. */
vline(screen, 200, 0, SCREEN_H - 1, makecol(0, 0, 0));
/* Draw all the lines until we reach a NULL entry. */
for (num = 0, y = 0; lines[num]; num++, y += text_height(font))
    textout_justify_ex(screen, font, lines[num], 0, 200,
                       y, 80, makecol(0, 0, 0),
                       makecol(255, 255, 255));
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_justify_ex/">textprintf_justify_ex</a></code>(3) </p>
