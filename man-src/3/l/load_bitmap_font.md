---
title: "load_bitmap_font(3)"
name: "load_bitmap_font"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_bitmap_font/"
description: "load_bitmap_font – Grabs a font from a bitmap file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_bitmap_font &#8211; Grabs a font from a bitmap file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *load_bitmap_font(const char *filename, RGB *pal, void *param)</code></p>
<h2>DESCRIPTION</h2>
<p> Tries to grab a font from a bitmap. The bitmap can be in any format that load_bitmap understands. </p>
<p> The size of each character is determined by the layout of the image, which should be a rectangular grid containing all the ASCII characters from space (32) up to the tilde (126). The way the characters are separated depends on the color depth of the image file: </p>
<p> paletted (8 bit) image file Use color 0 for the transparent portions of the characters and fill the spaces between each letter with color 255. </p>
<p> High (15/16 bit) and true (24/32 bit) color image file Use bright pink (maximum red and blue, zero green) for the transparent portions of the characters and fill the spaces between each letter with bright yellow (maximum red and green, zero blue). </p>
<p> Note that in each horizontal row the bounding boxes around the characters should align and have the same height. </p>
<p> Probably the easiest way to get to grips with how this works is to load up the `demo.dat&#8217; file and export the TITLE_FONT into a PCX file. Have a look at the resulting picture in your paint program: that is the format a font should be in. </p>
<p> Take care with high and true color fonts: Allegro will convert these to the current color depth when you load the font. If you try to use a font on a bitmap with a different color depth Allegro will do color conversions on the fly, which will be rather slow. For optimal performance you should set the color depth to the color depth you want to use before loading any fonts.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-register_font_file_type/">register_font_file_type</a></code>(3), <code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-grab_font_from_bitmap/">grab_font_from_bitmap</a></code>(3) </p>
<h2>Index</h2>
