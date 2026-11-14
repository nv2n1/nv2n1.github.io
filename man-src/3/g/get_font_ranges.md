---
title: "get_font_ranges(3)"
name: "get_font_ranges"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_font_ranges/"
description: "get_font_ranges – Returns the number of character ranges in a font. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_font_ranges &#8211; Returns the number of character ranges in a font. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_font_ranges(FONT *f)</code></p>
<h2>DESCRIPTION</h2>
<p> Use this function to find out the number of character ranges in a font. You should query each of these ranges with get_font_range_begin() and get_font_range_end() to find out what characters are available in the font. Example: </p>
<pre><code>
FONT *f;
int range;
int n;
...

    range = get_font_ranges(f);
printf("The font has %d character ranges:
", range);
for (n = 0; n &lt; range; n++)
    printf("Range %d from 0x%03x - 0x%03x
",
           get_font_range_begin(f, n),
           get_font_range_end(f, n));
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the number of continuous character ranges in a font, or -1 if that information is not available. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_font_range_begin/">get_font_range_begin</a></code>(3), <code><a href="/docs/linux/man/3-get_font_range_end/">get_font_range_end</a></code>(3), <code><a href="/docs/linux/man/3-transpose_font/">transpose_font</a></code>(3) </p>
<h2>Index</h2>
