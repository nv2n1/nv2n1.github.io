---
title: "replace_filename(3)"
name: "replace_filename"
section: "3"
letter: "r"
url: "/docs/linux/man/3-replace_filename/"
description: "replace_filename – Replaces path+filename with a new filename tail. Allegro game programming library."
---

<p>replace_filename &#8211; Replaces path+filename with a new filename tail. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *replace_filename(char *dest, const char *path,

                       const char *filename, int size);</code></pre>
<h2>Description</h2>
<p>Replaces the specified path+filename with a new filename tail, storing at most `size&#8217; bytes into the `dest&#8217; buffer. You can use the same buffer both as input and output because Allegro internally works on a copy of the input before touching `dest&#8217;. Example: </p>
<pre><code>char name[200];
... get_executable_name(name, sizeof(name));
replace_filename(name, name, &quot;sound.dat&quot;, sizeof(name));</code></pre>
<h2>Return Value</h2>
<p>Returns a copy of the `dest&#8217; parameter. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_filename/">get_filename</a></code>(3), <code><a href="/docs/linux/man/3-replace_extension/">replace_extension</a></code>(3), <code><a href="/docs/linux/man/3-append_filename/">append_filename</a></code>(3) </p>
