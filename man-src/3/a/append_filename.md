---
title: "append_filename(3)"
name: "append_filename"
section: "3"
letter: "a"
url: "/docs/linux/man/3-append_filename/"
description: "append_filename – Concatenates a filename to a path. Allegro game programming library."
---

<h2>NAME</h2>
<p> append_filename &#8211; Concatenates a filename to a path. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *append_filename(char *dest, const char *path, </code> <code>const char *filename, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Concatenates the specified filename onto the end of the specified path, storing at most `size&#8217; bytes into the `dest&#8217; buffer. If `path&#8217; doesn&#8217;t have a trailing path separator, the function will append one if needed. You can use the same buffer both as input and output because Allegro internally works on a copy of the input before touching `dest&#8217;. Example: </p>
<pre>
   append_filename(buf, &quot;/home/user&quot;,
                   &quot;prog.bin&quot;, sizeof(buf));
</pre>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the `dest&#8217; parameter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-replace_filename/">replace_filename</a></code>(3) </p>
<h2>Index</h2>
