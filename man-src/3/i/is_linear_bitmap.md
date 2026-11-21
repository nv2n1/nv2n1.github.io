---

title: "is_linear_bitmap(3)"
name: "is_linear_bitmap"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_linear_bitmap/"
description: "is_linear_bitmap – Tells if a bitmap is linear. Allegro game programming library."
---

<p> is_linear_bitmap &#8211; Tells if a bitmap is linear. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int is_linear_bitmap(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns TRUE if bmp is a linear bitmap, i.e. a bitmap that can be accessed linearly within each scanline (for example a memory bitmap, the DOS VGA or SVGA screen, Windows bitmaps, etc). Linear bitmaps can be used with the _putpixel(), _getpixel(), bmp_write_line(), and bmp_read_line() functions. </p>
<p> Historically there were only linear and planar bitmaps for Allegro, so is_linear_bitmap() is actually an alias for !is_planar_bitmap(). </p>
<h2>SEE ALSO</h2>
<p> <code>is_planar_bitmap</code>(3), <code>is_memory_bitmap</code>(3) </p>
