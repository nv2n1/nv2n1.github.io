---
title: "get_extension(3)"
name: "get_extension"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_extension/"
description: "get_extension – Returns a pointer to the extension of a filename. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_extension &#8211; Returns a pointer to the extension of a filename. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *get_extension(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Finds out the extension of the filename (with or without path information). Example: </p>
<pre><code>
get_executable_name(name, sizeof(name));
allegro_message("The binary has the extension `%s'
",
                get_extension(name));
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the portion of `filename&#8217; where the extension starts, or a pointer to the trailing null character if there is no filename or it doesn&#8217;t have extension. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_filename/">get_filename</a></code>(3), <code><a href="/docs/linux/man/3-put_backslash/">put_backslash</a></code>(3), <code><a href="/docs/linux/man/3-replace_extension/">replace_extension</a></code>(3) </p>
<h2>Index</h2>
