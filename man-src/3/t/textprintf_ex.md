---
title: "textprintf_ex(3)"
name: "textprintf_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textprintf_ex/"
description: "textprintf_ex – Formatted output of a string. Allegro game programming library."
---

<p>textprintf_ex &#8211; Formatted output of a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textprintf_ex(BITMAP *bmp, const FONT *f, int x, int y,

                   int color, int bg, const char *fmt, ...);</code></pre>
<h2>Description</h2>
<p>Formatted text output, using a printf() style format string. Due to an internal limitation, this function can&#8217;t be used for extremely long texts. If you happen to reach this limit, you can work around it by using uszprintf() and textout_ex(), which don&#8217;t have any. Example: </p>
<pre><code>int player_score;
... textprintf_ex(screen, font, 10, 10, makecol(255, 100, 200),
                  -1, &quot;Score: %d&quot;, player_score);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-textout_ex/">textout_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_centre_ex/">textprintf_centre_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_right_ex/">textprintf_right_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_justify_ex/">textprintf_justify_ex</a></code>(3), <code><a href="/docs/linux/man/3-text_height/">text_height</a></code>(3), <code><a href="/docs/linux/man/3-text_length/">text_length</a></code>(3), <code><a href="/docs/linux/man/3-uszprintf/">uszprintf</a></code>(3) </p>
