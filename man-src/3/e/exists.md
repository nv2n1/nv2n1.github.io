---
title: "exists(3)"
name: "exists"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exists/"
description: "exists – Shortcut version of file_exists() for normal files. Allegro game programming library."
---

<h2>NAME</h2>
<p> exists &#8211; Shortcut version of file_exists() for normal files. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int exists(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Shortcut version of file_exists(), which checks for normal files, which may have the archive or read-only bits set, but are not hidden, directories, system files, etc.</p>
<h2>RETURN VALUE</h2>
<p> Returns non-zero if the file exists, or zero if it doesn&#8217;t. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-file_exists/">file_exists</a></code>(3), <code><a href="/docs/linux/man/3-file_size_ex/">file_size_ex</a></code>(3), <code><a href="/docs/linux/man/3-file_time/">file_time</a></code>(3) </p>
<h2>Index</h2>
