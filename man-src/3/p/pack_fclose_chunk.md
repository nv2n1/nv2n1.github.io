---
title: "pack_fclose_chunk(3)"
name: "pack_fclose_chunk"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fclose_chunk/"
description: "pack_fclose_chunk – Closes a previously opened sub-chunk. Allegro game programming library."
---

<p>pack_fclose_chunk &#8211; Closes a previously opened sub-chunk. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>PACKFILE *pack_fclose_chunk(PACKFILE *f);</code></p>
<h2>Description</h2>
<p>Closes a sub-chunk of a file, previously obtained by calling pack_fopen_chunk().</p>
<h2>Return Value</h2>
<p>Returns a pointer to the parent of the sub-chunk you just closed. Returns NULL if there was some error (eg. you tried to close a PACKFILE which wasn&#8217;t sub-chunked). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3) </p>
