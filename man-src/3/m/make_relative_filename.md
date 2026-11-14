---
title: "make_relative_filename(3)"
name: "make_relative_filename"
section: "3"
letter: "m"
url: "/docs/linux/man/3-make_relative_filename/"
description: "make_relative_filename – Tries to make a relative filename from absolute path and filename. Allegro game programming library."
---

<h2>NAME</h2>
<p> make_relative_filename &#8211; Tries to make a relative filename from absolute path and filename. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *make_relative_filename(char *dest, const char *path, const char *filename, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Attempts to make a relative filename from an absolute path and an absolute filename, storing at most `size&#8217; bytes into the `dest&#8217; buffer. This function won&#8217;t work if the paths are not canonical under the current platform (see canonicalize_filename()). Also, `dest&#8217; cannot be used as input value for `path&#8217; or `filename&#8217;. Example: </p>
<pre><code>
char base[] = "/long/absolute/path/program.exe";
char user_input[] = "/nice/and/short.txt";
... make_relative_filename(buf, base, user_input, sizeof(buf));
/* Under Unix buf would contain:
   ../../../nice/and/short.txt */
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the `dest&#8217; parameter if it succeeds or NULL if it fails (eg. under DOS, one path starts with &quot;C:\&quot; and another with &quot;A:\&quot;). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-make_absolute_filename/">make_absolute_filename</a></code>(3), <code><a href="/docs/linux/man/3-is_relative_filename/">is_relative_filename</a></code>(3), <code><a href="/docs/linux/man/3-canonicalize_filename/">canonicalize_filename</a></code>(3) </p>
<h2>Index</h2>
