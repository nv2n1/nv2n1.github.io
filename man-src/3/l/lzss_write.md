---
title: "lzss_write(3)"
name: "lzss_write"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lzss_write/"
description: "lzss_write – Compresses data using LZSS. Allegro game programming library."
---

<h2>NAME</h2>
<p> lzss_write &#8211; Compresses data using LZSS. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int lzss_write(PACKFILE *file, LZSS_PACK_DATA *dat, int size,</code> <code>unsigned char *buf, int last);</code></p>
<h2>DESCRIPTION</h2>
<p> Packs `size&#8217; bytes from `buf&#8217;, using the pack information contained in `dat&#8217;. The compressed bytes will be stored in `file&#8217;.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success, or EOF if there was an error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_lzss_pack_data/">create_lzss_pack_data</a></code>(3), <code><a href="/docs/linux/man/3-free_lzss_pack_data/">free_lzss_pack_data</a></code>(3) </p>
<h2>Index</h2>
