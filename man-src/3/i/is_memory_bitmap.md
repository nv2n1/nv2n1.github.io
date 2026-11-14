---
title: "is_memory_bitmap(3)"
name: "is_memory_bitmap"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_memory_bitmap/"
description: "is_memory_bitmap – Tells if a bitmap is a memory bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> is_memory_bitmap &#8211; Tells if a bitmap is a memory bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int is_memory_bitmap(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns TRUE if bmp is a memory bitmap, ie. it was created by calling create_bitmap() or loaded from a grabber datafile or image file. Memory bitmaps can be accessed directly via the line pointers in the bitmap structure, eg. bmp-&gt;line[y][x] = color. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-is_linear_bitmap/">is_linear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-is_planar_bitmap/">is_planar_bitmap</a></code>(3) </p>
<h2>Index</h2>
