---
title: "create_rgb_table(3)"
name: "create_rgb_table"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_rgb_table/"
description: "create_rgb_table – Generates an RGB mapping table with lookup data for a palette. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_rgb_table &#8211; Generates an RGB mapping table with lookup data for a palette. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void create_rgb_table(RGB_MAP *table, const PALETTE pal,</code> <code>void (*callback)(int pos));</code></p>
<h2>DESCRIPTION</h2>
<p> Fills the specified RGB mapping table with lookup data for the specified palette. If the callback function is not NULL, it will be called 256 times during the calculation, allowing you to display a progress indicator. Example: </p>
<pre><code>
RGB_MAP rgb_table;

create_rgb_table(&amp;rgb_table, palette, NULL);
rgb_map = &amp;rgb_table;
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-excolmap/">excolmap</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
<h2>Index</h2>
