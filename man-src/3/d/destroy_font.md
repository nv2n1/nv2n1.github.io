---
title: "destroy_font(3)"
name: "destroy_font"
section: "3"
letter: "d"
url: "/docs/linux/man/3-destroy_font/"
description: "destroy_font – Frees the memory being used by a font structure. Allegro game programming library."
---

<h2>NAME</h2>
<p> destroy_font &#8211; Frees the memory being used by a font structure. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void destroy_font(FONT *f);</code></p>
<h2>DESCRIPTION</h2>
<p> Frees the memory being used by a font structure. Don&#8217;t use this on the default global Allegro font or any text routines using it could crash. You should use this only on fonts you have loaded manually after you are done with them, to prevent memory leaks in your program. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-load_datafile_object/">load_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-load_font/">load_font</a></code>(3), <code><a href="/docs/linux/man/3-exfont/">exfont</a></code>(3) </p>
<h2>Index</h2>
