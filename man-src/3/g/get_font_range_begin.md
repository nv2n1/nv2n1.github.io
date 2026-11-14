---
title: "get_font_range_begin(3)"
name: "get_font_range_begin"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_font_range_begin/"
description: "get_font_range_begin – Returns the start of a character range in a font. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_font_range_begin &#8211; Returns the start of a character range in a font. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_font_range_begin(FONT *f, int range)</code></p>
<h2>DESCRIPTION</h2>
<p> This function allows you to find out the start of a specific character range for a font. You can pass -1 for the `range&#8217; parameter if you want to know the start of the whole font range, or a number from 0 to (but not including) get_font_ranges(f) to get the start of a specific character range in the font. Example: </p>
<pre>
   printf(&quot;The font has a character range of %d - %d
&quot;,
          get_font_range_begin(font, -1),
          get_font_range_end(font, -1));
</pre>
<h2>RETURN VALUE</h2>
<p> Returns the first character in the font range, or -1 if that information is not available. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_font_ranges/">get_font_ranges</a></code>(3), <code><a href="/docs/linux/man/3-get_font_range_end/">get_font_range_end</a></code>(3), <code><a href="/docs/linux/man/3-transpose_font/">transpose_font</a></code>(3) </p>
<h2>Index</h2>
