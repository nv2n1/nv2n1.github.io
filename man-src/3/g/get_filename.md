---
title: "get_filename(3)"
name: "get_filename"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_filename/"
description: "get_filename – Returns a pointer to the filename portion of a path. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_filename &#8211; Returns a pointer to the filename portion of a path. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *get_filename(const char *path);</code></p>
<h2>DESCRIPTION</h2>
<p> Finds out the filename portion of a completely specified file path. Both `\&#8217; and `/&#8217; are recognized as directory separators under DOS and Windows. However, only `/&#8217; is recognized as directory separator under other platforms. Example: </p>
<pre><code>
get_executable_name(name, sizeof(name));
allegro_message("Running `%s'
", get_filename(name));
</code></pre>
<p> Note that Allegro won&#8217;t perform any IO operations during the verification. This means that if you have `/a/path/like/this/&#8217;, which doesn&#8217;t have a filename, the function will return a pointer to the trailing null character. However, if you have `/a/path/like/this&#8217;, Allegro will return a pointer to `this&#8217;, even if it is a valid directory.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the portion of `path&#8217; where the filename starts, or the beginning of `path&#8217; if no valid filename is found (eg. you are processing a path with backslashes under Unix). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_extension/">get_extension</a></code>(3), <code><a href="/docs/linux/man/3-put_backslash/">put_backslash</a></code>(3), <code><a href="/docs/linux/man/3-replace_filename/">replace_filename</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3) </p>
<h2>Index</h2>
