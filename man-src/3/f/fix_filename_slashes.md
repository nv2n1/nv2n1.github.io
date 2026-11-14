---
title: "fix_filename_slashes(3)"
name: "fix_filename_slashes"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fix_filename_slashes/"
description: "fix_filename_slashes – Converts all the directory separators to a standard character. Allegro game programming library."
---

<h2>NAME</h2>
<p> fix_filename_slashes &#8211; Converts all the directory separators to a standard character. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *fix_filename_slashes(char *path);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts all the directory separators in the filename stored in `path&#8217; to a standard character. On DOS and Windows platforms, this is a backslash. On most other platforms this is a slash. Example: </p>
<pre><code>
char buf[200] = "c:/dos\backup/weirdo\test";
... fix_filename_slashes(buf);
/* Under DOS we would have c:\dosackup\weirdo	est.
   Under Unix we would have c:/dos/backup/weirdo/test. */
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the `path&#8217; parameter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fix_filename_case/">fix_filename_case</a></code>(3), <code><a href="/docs/linux/man/3-canonicalize_filename/">canonicalize_filename</a></code>(3) </p>
<h2>Index</h2>
