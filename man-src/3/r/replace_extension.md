---
title: "replace_extension(3)"
name: "replace_extension"
section: "3"
letter: "r"
url: "/docs/linux/man/3-replace_extension/"
description: "replace_extension – Replaces filename+extension with a new extension tail. Allegro game programming library."
---

<p>replace_extension &#8211; Replaces filename+extension with a new extension tail. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *replace_extension(char *dest, const char *filename,

                        const char *ext, int size);</code></pre>
<h2>Description</h2>
<p>Replaces the specified filename+extension with a new extension tail, storing at most `size&#8217; bytes into the `dest&#8217; buffer. If the filename doesn&#8217;t have any extension at all, `ext&#8217; will be appended to it, adding a dot character if needed. You can use the same buffer both as input and output because Allegro internally works on a copy of the input before touching `dest&#8217;. Example: </p>
<pre> replace_extension(buf, &quot;C:\game\prog.exe&quot;,
 &quot;dat&quot;, sizeof(buf));</pre>
<h2>Return Value</h2>
<p>Returns a copy of the `dest&#8217; parameter. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_extension/">get_extension</a></code>(3), <code><a href="/docs/linux/man/3-replace_filename/">replace_filename</a></code>(3) </p>
