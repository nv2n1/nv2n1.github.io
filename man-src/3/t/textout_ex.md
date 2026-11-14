---
title: "textout_ex(3)"
name: "textout_ex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textout_ex/"
description: "textout_ex – Writes a string on a bitmap. Allegro game programming library."
---

<p>textout_ex &#8211; Writes a string on a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void textout_ex(BITMAP *bmp, const FONT *f, const char *s,

                int x, int y, int color, int bg);</code></pre>
<h2>Description</h2>
<p>Writes the string `s&#8217; onto the bitmap at position x, y, using the specified font, foreground color and background color. If the background color is -1, then the text is written transparently. If the foreground color is -1 and a color font is in use, it will be drawn using the colors from the original font bitmap (the one you imported into the grabber program), which allows multicolored text output. For high and true color fonts, the foreground color is ignored and always treated as -1. Example: </p>
<pre> /* Show the program's version in blue letters. */
 textout_ex(screen, font, &quot;v4.2.0-beta2&quot;, 10, 10,
 makecol(0, 0, 255), -1);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-font/">font</a></code>(3), <code><a href="/docs/linux/man/3-textout_centre_ex/">textout_centre_ex</a></code>(3), <code><a href="/docs/linux/man/3-textout_right_ex/">textout_right_ex</a></code>(3), <code><a href="/docs/linux/man/3-textout_justify_ex/">textout_justify_ex</a></code>(3), <code><a href="/docs/linux/man/3-textprintf_ex/">textprintf_ex</a></code>(3), <code><a href="/docs/linux/man/3-text_height/">text_height</a></code>(3), <code><a href="/docs/linux/man/3-text_length/">text_length</a></code>(3) </p>
