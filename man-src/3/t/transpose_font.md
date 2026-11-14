---
title: "transpose_font(3)"
name: "transpose_font"
section: "3"
letter: "t"
url: "/docs/linux/man/3-transpose_font/"
description: "transpose_font – Transposes all characters in a font. Allegro game programming library."
---

<p>transpose_font &#8211; Transposes all characters in a font. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>int transpose_font(FONT *f, int drange)</code></p>
<h2>Description</h2>
<p>This function transposes all characters in a font, effectively remapping the font. Example: </p>
<pre><code>FONT *myfont;
FONT *capitals;
...
    /* Create a font of only capital letters */
    capitals = extract_font_range(myfont, 'A', 'Z');

/* Now transpose the characters in the font so that they will be used */
/*  for the lower case letters a-z */
transpose_font(capitals, 'a' - 'A');
textout_ex(screen, capitals, &quot;allcaps&quot;,
           100, 100, makecol(255, 255, 255), 0);</code></pre>
<h2>Return Value</h2>
<p>Returns 0 on success, -1 on failure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_font_range_begin/">get_font_range_begin</a></code>(3), <code><a href="/docs/linux/man/3-get_font_range_end/">get_font_range_end</a></code>(3), <code><a href="/docs/linux/man/3-merge_fonts/">merge_fonts</a></code>(3), <code><a href="/docs/linux/man/3-extract_font_range/">extract_font_range</a></code>(3) </p>
