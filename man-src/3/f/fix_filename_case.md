---
title: "fix_filename_case(3)"
name: "fix_filename_case"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fix_filename_case/"
description: "fix_filename_case – Converts a filename to a standardised case. Allegro game programming library."
---

<h2>NAME</h2>
<p> fix_filename_case &#8211; Converts a filename to a standardised case. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>char *fix_filename_case(char *path);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts the filename stored in `path&#8217; to a standardised case. On DOS platforms, they will be entirely uppercase. On other platforms this function doesn&#8217;t do anything. Example: </p>
<pre><code>
get_executable_name(name, sizeof(name));
fix_filename_case(name);
allegro_message("Running `%s'
", name);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a copy of the `path&#8217; parameter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fix_filename_slashes/">fix_filename_slashes</a></code>(3), <code><a href="/docs/linux/man/3-canonicalize_filename/">canonicalize_filename</a></code>(3) </p>
<h2>Index</h2>
