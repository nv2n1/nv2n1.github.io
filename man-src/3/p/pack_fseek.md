---
title: "pack_fseek(3)"
name: "pack_fseek"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fseek/"
description: "pack_fseek – Seeks inside a stream. Allegro game programming library."
---

<p>pack_fseek &#8211; Seeks inside a stream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int pack_fseek(PACKFILE *f, int offset);</code></pre>
<h2>Description</h2>
<p>Moves the position indicator of the stream `f&#8217;. Unlike the standard fseek() function, this only supports forward movements relative to the current position and in read-only streams, so don&#8217;t use negative offsets. Note that seeking is very slow when reading compressed files, and so should be avoided unless you are sure that the file is not compressed. Example: </p>
<pre><code>input_file = pack_fopen(&quot;data.bin&quot;, &quot;r&quot;);
if (!input_file)
    abort_on_error(&quot;Couldn't open binary data!&quot;);
/* Skip some useless header before reading data. */
pack_fseek(input_file, 32);</code></pre>
<h2>Return Value</h2>
<p>Returns zero on success or a negative number on error, storing the error code in `errno&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3) </p>
