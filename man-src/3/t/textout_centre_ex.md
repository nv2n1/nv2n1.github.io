---
title: "textout_centre_ex(3)"
name: "textout_centre_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textout_centre_ex/"
description: "textout_centre_ex – Writes a centered string on a bitmap. Allegro game programming library."
---

<p>textout_centre_ex &#8211; Writes a centered string on a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textout_centre_ex(BITMAP *bmp, const FONT *f, const char *s,

                       int x, y, int color, int bg);</code></pre>
<h2>Description</h2>
<p>Like textout_ex(), but interprets the x coordinate as the centre rather than the left edge of the string. Example: </p>
<pre><code>/* Important texts go in the middle. */
width = text_length(&quot;GAME OVER&quot;);
textout_centre_ex(screen, font, &quot;GAME OVER&quot;,
SCREEN_W / 2, SCREEN_H / 2,
makecol(255, 0, 0), makecol(0, 0, 0));
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_centre_ex/">textprintf_centre_ex</a></code>(3) </p>
