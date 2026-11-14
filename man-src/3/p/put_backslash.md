---
title: "put_backslash(3)"
name: "put_backslash"
section: "3"
letter: "p"
url: "/docs/linux/man/3-put_backslash/"
description: "put_backslash – Puts a path separator at the end of a path if needed. Allegro game programming library."
---

<p>put_backslash &#8211; Puts a path separator at the end of a path if needed. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void put_backslash(char *filename);</code></pre>
<h2>Description</h2>
<p>If the last character of the filename is not a `\&#8217;, `/&#8217;, `#&#8217; or a device separator (ie. `:&#8217; under DOS), this routine will concatenate either a `\&#8217; or `/&#8217; on to it (depending on the platform). Note: ignore the function name, it&#8217;s out of date. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_extension/">get_extension</a></code>(3), <code><a href="/docs/linux/man/3-get_filename/">get_filename</a></code>(3) </p>
