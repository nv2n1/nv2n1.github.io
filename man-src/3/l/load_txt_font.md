---
title: "load_txt_font(3)"
name: "load_txt_font"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_txt_font/"
description: "load_txt_font – Loads a font script. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_txt_font &#8211; Loads a font script. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>FONT *load_txt_font(const char *filename, RGB *pal, void *param)</code></p>
<h2>DESCRIPTION</h2>
<p> This function can be used to load scripted fonts. The script file contains a number of lines in the format &quot;filename start end&quot;, which specify the source file for that range of characters, the Unicode value of the first character in the range, and the end character in the range (optional, if left out, the entire input file will be grabbed). If the filename is replaced by a hyphen, more characters will be grabbed from the previous input file. For example, the script: </p>
<pre>
   ascii.fnt 0x20 0x7F
   - 0xA0 0xFF
   dingbats.fnt 0x1000
   
</pre>
<p> would import the first 96 characters from ascii.fnt as the range 0x20-0x7F, the next 96 characters from ascii.fnt as the range 0xA0-0xFF, and the entire contents of dingbats.fnt starting at Unicode position 0x1000.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the font or NULL on error. Remember that you are responsible for destroying the font when you are finished with it to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-register_font_file_type/">register_font_file_type</a></code>(3), <code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3) </p>
<h2>Index</h2>
