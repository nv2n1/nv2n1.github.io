---
title: "load_font(3)"
name: "load_font"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_font/"
description: "load_font – Loads a font from a file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_font &#8211; Loads a font from a file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *load_font(const char *filename, RGB *pal, void *param);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a font from a file. At present, this supports loading fonts from a GRX format .fnt file, a 8&#215;8 or 8&#215;16 BIOS format .fnt file, a datafile or any bitmap format that can be loaded by load_bitmap(). </p>
<p> If the font contains palette information, then the palette is returned in the second parameter, which should be an array of 256 RGB structures (a PALETTE). The pal argument may be NULL. In this case, the palette data, if present, is simply not returned. </p>
<p> The third parameter can be used to pass specific information to a custom loader routine. Normally, you can just leave this as NULL. Note that another way of loading fonts is embedding them into a datafile and using the datafile related functions. </p>
<p> Example: </p>
<pre><code>
FONT *myfont;
PALETTE palette;
... myfont = load_font("my_font.pcx", palette, NULL);
if (!myfont)
    abort_on_error("Couldn't load font!");
... textout_centre_ex(screen, myfont, "This is my own pretty font!",
                      SCREEN_W / 2, SCREEN_H / 2, white, black);
... destroy_font(myfont);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-register_font_file_type/">register_font_file_type</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-load_dat_font/">load_dat_font</a></code>(3), <code><a href="/docs/linux/man/3-load_bios_font/">load_bios_font</a></code>(3), <code><a href="/docs/linux/man/3-load_grx_font/">load_grx_font</a></code>(3), <code><a href="/docs/linux/man/3-load_grx_or_bios_font/">load_grx_or_bios_font</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap_font/">load_bitmap_font</a></code>(3), <code><a href="/docs/linux/man/3-load_txt_font/">load_txt_font</a></code>(3), <code><a href="/docs/linux/man/3-destroy_font/">destroy_font</a></code>(3), <code><a href="/docs/linux/man/3-exfont/">exfont</a></code>(3) </p>
<h2>Index</h2>
