---
title: "extract_font_range(3)"
name: "extract_font_range"
section: "3"
letter: "e"
url: "/docs/linux/man/3-extract_font_range/"
description: "extract_font_range – Extracts a range of characters from a font. Allegro game programming library."
---

<h2>NAME</h2>
<p> extract_font_range &#8211; Extracts a range of characters from a font. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *extract_font_range(FONT *f, int begin, int end)</code></p>
<h2>DESCRIPTION</h2>
<p> This function extracts a character range from a font and returns a new font that contains only the range of characters selected by this function. You can pass -1 for either the lower or upper bound if you want to select all characters from the start or to the end of the font. Example: </p>
<pre><code>
FONT *myfont;
FONT *capitals;
FONT *fontcopy;
...
    /* Create a font of only capital letters */
    capitals = extract_font_range(myfont, 'A', 'Z');

/* Create a copy of the font */
fontcopy = extract_font_range(myfont, -1, -1);
... destroy_font(capitals);
destroy_font(fontcopy);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the new font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_font_range_begin/">get_font_range_begin</a></code>(3), <code><a href="/docs/linux/man/3-get_font_range_end/">get_font_range_end</a></code>(3), <code><a href="/docs/linux/man/3-merge_fonts/">merge_fonts</a></code>(3), <code><a href="/docs/linux/man/3-transpose_font/">transpose_font</a></code>(3), <code><a href="/docs/linux/man/3-exfont/">exfont</a></code>(3) </p>
<h2>Index</h2>
