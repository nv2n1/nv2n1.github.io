---
title: "register_font_file_type(3)"
name: "register_font_file_type"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_font_file_type/"
description: "register_font_file_type – Register a new font loading function. Allegro game programming library."
---

<p>register_font_file_type &#8211; Register a new font loading function. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_font_file_type(const char *ext,

                             FONT *(*load)(const char *filename, RGB *pal, void *param));</code></pre>
<h2>Description</h2>
<p>Informs the load_font() functions of a new file type, providing a routine to read fonts in this format. The function you supply must follow the following prototype: </p>
<pre> FONT *load_my_font(const char *filename, RGB *pal, void *param)
 {
 ...
 }</pre>
<p>The pal parameter can optionally be used to return a palette for the FONT. The parameter param can be anything you like: you can use this to pass information to your loading routine, such as for instance the font height, the character range to load or the index number of a font in a datafile. If you choose to write your own font loading code, your function should be prepared to deal with a value of NULL for either of these parameters. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3) </p>
