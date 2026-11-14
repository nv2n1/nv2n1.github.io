---
title: "is_relative_filename(3)"
name: "is_relative_filename"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_relative_filename/"
description: "is_relative_filename – Returns TRUE if the filename is relative. Allegro game programming library."
---

<h2>NAME</h2>
<p> is_relative_filename &#8211; Returns TRUE if the filename is relative. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int is_relative_filename(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns TRUE if the filename is relative or FALSE if it is absolute. Note that an absolute filename under DOS (with a device separator) will be considered as relative under Unix, because there absolute paths always start with a slash. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-make_absolute_filename/">make_absolute_filename</a></code>(3), <code><a href="/docs/linux/man/3-make_relative_filename/">make_relative_filename</a></code>(3) </p>
<h2>Index</h2>
