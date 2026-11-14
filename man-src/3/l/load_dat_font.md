---
title: "load_dat_font(3)"
name: "load_dat_font"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_dat_font/"
description: "load_dat_font – Loads a FONT from an Allegro datafile."
---

<h2>NAME</h2>
<p> load_dat_font &#8211; Loads a FONT from an Allegro datafile.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *load_dat_font(const char *filename, RGB *pal, void *param)</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a FONT from an Allegro datafile. You can set param parameter to point to an array that holds two strings that identify the font and the palette in the datafile by name. The first string in this list is the name of the font. You can pass NULL here to just load the first font found in the datafile. The second string can be used to specify the name of the palette associated with the font. This is only returned if the pal parameter is not NULL. If you pass NULL for the name of the palette, the last palette found before the font was found is returned. You can also pass NULL for param, which is treated as if you had passed NULL for both strings separately. In this case, the function will simply load the first font it finds from the datafile and the palette that precedes it. </p>
<p> For example, suppose you have a datafile named `fonts.dat&#8217; with the following contents: </p>
<pre>
   FONT  FONT_1_DATA
   FONT  FONT_2_DATA
   FONT  FONT_3_DATA
   PAL   FONT_1_PALETTE
   PAL   FONT_2_PALETTE
   
</pre>
<p> Then the following code will load FONT_1_DATA as a FONT and return FONT_1_PALETTE as the palette: </p>
<pre><code>
FONT *f;
PALETTE pal;
char *names[] = {"FONT_1_DATA", "FONT_1_PALETTE"}

f = load_dat_font("fonts.dat", pal, names);
</code></pre>
<p> If instead you want to load the second font, FONT_2, from the datafile, you would use: </p>
<p>FONT *f;<br />
PALETTE pal;<br />
char *names[] = {&#8220;FONT_2_DATA&#8221;, &#8220;FONT_2_PALETTE&#8221;}</p>
<p>f = load_dat_font(&#8220;fonts.dat&#8221;, pal, names);<br />
 If you want to load the third font, but not bother with a palette, use: </p>
<pre><code>
FONT *f;
char *names[] = {"FONT_3_DATA", NULL}

f = load_dat_font("fonts.dat", NULL, names);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-register_font_file_type/">register_font_file_type</a></code>(3), <code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3) </p>
<h2>Index</h2>
