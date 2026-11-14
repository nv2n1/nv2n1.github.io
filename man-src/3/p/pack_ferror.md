---
title: "pack_ferror(3)"
name: "pack_ferror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_ferror/"
description: "pack_ferror – Tells if an error occurred during an operation on the stream. Allegro game programming library."
---

<p>pack_ferror &#8211; Tells if an error occurred during an operation on the stream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int pack_ferror(PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Since EOF is used to report errors by some functions, it&#8217;s often better to use the pack_feof() function to check explicitly for end of file and pack_ferror() to check for errors. Both functions check indicators that are part of the internal state of the stream to detect correctly the different situations.</p>
<h2>Return Value</h2>
<p>Returns nonzero if the error indicator for the stream is set, meaning that an error has occurred during a previous operation on the stream. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3) </p>
