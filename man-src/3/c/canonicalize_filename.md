---
title: "canonicalize_filename(3)"
name: "canonicalize_filename"
section: "3"
letter: "c"
url: "/docs/linux/man/3-canonicalize_filename/"
description: "canonicalize_filename – Converts any filename into its canonical form. Allegro game programming library."
---

<h2>NAME</h2>
<p> canonicalize_filename &#8211; Converts any filename into its canonical form. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *canonicalize_filename(char *dest, const char *filename, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts any filename into its canonical form, i.e. the minimal absolute filename describing the same file and fixing incorrect forward/backward slashes for the current platform, storing at most `size&#8217; bytes into the `dest&#8217; buffer. You can use the same buffer both as input and output because Allegro internally works on a copy of the input before touching `dest&#8217;. Example: </p>
<pre><code>
char buf[256];
... canonicalize_filename(buf, "~/../s22/..\t3st///hi.c",
                          sizeof(buf));
/* Running this under Unix would
   return: /home/t3st/hi.c */
</code></pre>
<p> Note that this function won&#8217;t work as expected if the path to canonicalize comes from another platform (eg. a &quot;c:\something&quot; path will canonicalize into something really wrong under Unix: &quot;/current/path/c:/something&quot;).</p>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the `dest&#8217; parameter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fix_filename_case/">fix_filename_case</a></code>(3), <code><a href="/docs/linux/man/3-fix_filename_slashes/">fix_filename_slashes</a></code>(3) </p>
<h2>Index</h2>
