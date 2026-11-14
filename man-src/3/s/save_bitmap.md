---
title: "save_bitmap(3)"
name: "save_bitmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-save_bitmap/"
description: "save_bitmap – Saves a bitmap into any supported file format. Allegro game programming library."
---

<p>save_bitmap &#8211; Saves a bitmap into any supported file format. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int save_bitmap(const char *filename, BITMAP *bmp, const RGB *pal);</code></pre>
<h2>Description</h2>
<p>Writes a bitmap into a file, using the specified palette, which should be an array of 256 RGB structures. The output format is determined from the filename extension: at present this function supports BMP, PCX and TGA formats. Two things to watch out for: on some video cards it may be faster to copy the screen to a memory bitmap and save the latter, and if you use this to dump the screen into a file you may end up with an image much larger than you were expecting, because Allegro often creates virtual screens larger than the visible screen. You can get around this by using a sub-bitmap to specify which part of the screen to save, eg: </p>
<pre><code>BITMAP *bmp;
PALETTE pal;
...
get_palette(pal);
bmp = create_sub_bitmap(screen, 0, 0, SCREEN_W, SCREEN_H);
save_bitmap(&quot;dump.pcx&quot;, bmp, pal);
destroy_bitmap(bmp);</code></pre>
<h2>Return Value</h2>
<p>Returns non-zero on error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-save_bmp/">save_bmp</a></code>(3), <code><a href="/docs/linux/man/3-save_pcx/">save_pcx</a></code>(3), <code><a href="/docs/linux/man/3-save_tga/">save_tga</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-register_bitmap_file_type/">register_bitmap_file_type</a></code>(3) </p>
