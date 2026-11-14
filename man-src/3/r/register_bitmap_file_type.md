---
title: "register_bitmap_file_type(3)"
name: "register_bitmap_file_type"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_bitmap_file_type/"
description: "register_bitmap_file_type – Registers custom bitmap loading/saving functions. Allegro game programming library."
---

<p>register_bitmap_file_type &#8211; Registers custom bitmap loading/saving functions. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_bitmap_file_type(const char *ext,

                               BITMAP *(*load)(const char *filename, RGB *pal),

                               int (*save)(const char *filename, BITMAP *bmp, const RGB *pal));</code></pre>
<h2>Description</h2>
<p>Informs the load_bitmap() and save_bitmap() functions of a new file type, providing routines to read and write images in this format (either function may be NULL). The functions you supply must follow the same prototype as load_bitmap() and save_bitmap(). Example: </p>
<pre> BITMAP *load_dump(const char *filename, RGB *pal)
 {
 ...
 }
 
 int save_dump(const char *filename, BITMAP *bmp, const RGB *pal)
 {
 ...
 }
 
 register_bitmap_file_type(&quot;dump&quot;, load_dump, save_dump);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-save_bitmap/">save_bitmap</a></code>(3) </p>
