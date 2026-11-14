---
title: "destroy_bitmap(3)"
name: "destroy_bitmap"
section: "3"
letter: "d"
url: "/docs/linux/man/3-destroy_bitmap/"
description: "destroy_bitmap – Destroys any type of created bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> destroy_bitmap &#8211; Destroys any type of created bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void destroy_bitmap(BITMAP *bitmap);</code></p>
<h2>DESCRIPTION</h2>
<p> Destroys a memory bitmap, sub-bitmap, video memory bitmap, or system bitmap when you are finished with it. If you pass a NULL pointer this function won&#8217;t do anything. See above for the restrictions as to when you are allowed to destroy the various types of bitmaps. </p>
<p> The bitmap must not have a mouse cursor shown on it at the time it is destroyed. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-load_bitmap/">load_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3) </p>
<h2>Index</h2>
