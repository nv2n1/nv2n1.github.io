---
title: "merge_fonts(3)"
name: "merge_fonts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-merge_fonts/"
description: "merge_fonts – Merges two fonts into one font. Allegro game programming library."
---

<h2>NAME</h2>
<p> merge_fonts &#8211; Merges two fonts into one font. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *merge_fonts(FONT *f1, FONT *f2)</code></p>
<h2>DESCRIPTION</h2>
<p> This function merges the character ranges from two fonts and returns a new font containing all characters in the old fonts. In general, you cannot merge fonts of different types (eg, TrueType fonts and bitmapped fonts), but as a special case, this function can promote a monochrome bitmapped font to a color font and merge those. Example: </p>
<pre><code>
FONT *myfont;
FONT *myfancy_font;
FONT *lower_range;
FONT *upper_range;
FONT *capitals;
FONT *combined_font;
FONT *tempfont;
...
    /* Create a font that contains the capitals from  */
    /* the fancy font but other characters from myfont */
    lower_range = extract_font_range(myfont, -1, 'A' - 1);
upper_range = extract_font_range(myfont, 'Z' + 1, -1);
capitals = extract_font_range(myfancy_font, 'A', 'Z');

tempfont = merge_fonts(lower_range, capitals);
combined_font = merge_fonts(tempfont, upper_range);

/* Clean up temporary fonts */
destroy_font(lower_range);
destroy_font(upper_range);
destroy_font(capitals);
destroy_font(tempfont);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the new font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-extract_font_range/">extract_font_range</a></code>(3), <code><a href="/docs/linux/man/3-is_trans_font/">is_trans_font</a></code>(3), <code><a href="/docs/linux/man/3-is_color_font/">is_color_font</a></code>(3), <code><a href="/docs/linux/man/3-is_mono_font/">is_mono_font</a></code>(3), <code><a href="/docs/linux/man/3-exfont/">exfont</a></code>(3) </p>
<h2>Index</h2>
