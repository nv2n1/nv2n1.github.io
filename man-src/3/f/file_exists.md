---
title: "file_exists(3)"
name: "file_exists"
section: "3"
letter: "f"
url: "/docs/linux/man/3-file_exists/"
description: "file_exists – Tells if a file exists. Allegro game programming library."
---

<h2>NAME</h2>
<p> file_exists &#8211; Tells if a file exists. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int file_exists(const char *filename, int attrib, int *aret);</code></p>
<h2>DESCRIPTION</h2>
<p> Checks whether a file matching the given name and attributes (see beginning of this chapter) exists. If `aret&#8217; is not NULL, it will be set to the attributes of the matching file. Example: </p>
<pre><code>
/* Check for a normal file. */
if (file_exists("franken.dat", 0, NULL))
    allegro_message("It is alive!
");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns non-zero if the file exists, or zero if it doesn&#8217;t or the specified attributes mask it out. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exists/">exists</a></code>(3), <code><a href="/docs/linux/man/3-file_size_ex/">file_size_ex</a></code>(3), <code><a href="/docs/linux/man/3-file_time/">file_time</a></code>(3) </p>
<h2>Index</h2>
