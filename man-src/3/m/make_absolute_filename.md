---
title: "make_absolute_filename(3)"
name: "make_absolute_filename"
section: "3"
letter: "m"
url: "/docs/linux/man/3-make_absolute_filename/"
description: "make_absolute_filename – Makes an absolute filename from a path and relative filename. Allegro game programming library."
---

<h2>NAME</h2>
<p> make_absolute_filename &#8211; Makes an absolute filename from a path and relative filename. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *make_absolute_filename(char *dest, const char *path, const char *filename, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Makes an absolute filename from an absolute path and a relative filename, storing at most `size&#8217; bytes into the `dest&#8217; buffer. This is like calling replace_filename() and then canonicalize_filename(). Example: </p>
<pre><code>
char buf[256];
... make_absolute_filename(buf, "/usr/games/",
                           "../temp.txt", sizeof(buf));
/* This would create /usr/temp.txt */
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the `dest&#8217; parameter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-make_relative_filename/">make_relative_filename</a></code>(3), <code><a href="/docs/linux/man/3-is_relative_filename/">is_relative_filename</a></code>(3), <code><a href="/docs/linux/man/3-replace_filename/">replace_filename</a></code>(3), <code><a href="/docs/linux/man/3-canonicalize_filename/">canonicalize_filename</a></code>(3) </p>
<h2>Index</h2>
