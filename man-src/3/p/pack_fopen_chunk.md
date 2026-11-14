---
title: "pack_fopen_chunk(3)"
name: "pack_fopen_chunk"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fopen_chunk/"
description: "pack_fopen_chunk – Opens a sub-chunk of a file. Allegro game programming library."
---

<p>pack_fopen_chunk &#8211; Opens a sub-chunk of a file. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>PACKFILE *pack_fopen_chunk(PACKFILE *f, int pack);</code></p>
<h2>Description</h2>
<p>Opens a sub-chunk of a file. Chunks are primarily intended for use by the datafile code, but they may also be useful for your own file routines. A chunk provides a logical view of part of a file, which can be compressed as an individual entity and will automatically insert and check length counts to prevent reading past the end of the chunk. The PACKFILE parameter is a previously opened file, and `pack&#8217; is a boolean parameter which will turn compression on for the sub-chunk if it is non-zero. Example: PACKFILE *input = pack_fopen(&quot;out.raw&quot;, &quot;rp&quot;);<br />
&#8230; input = pack_fopen_chunk(input, 1);<br />
/* Read data from the sub-chunk and close it. */<br />
&#8230; input = pack_fclose_chunk(input);</p>
<p>This sequence will read the length counts created when the chunk was<br />
    written,<br />
    and automatically decompress the contents of the chunk if it<br />
            was compressed.The length will also be used to prevent reading past the<br />
                end of the<br />
                chunk(Allegro will return EOF if you attempt this),<br />
    and to<br />
        automatically skip past any unread chunk data when you call<br />
        pack_fclose_chunk()<br />
            . To read the chunk, use the following code: </p>
<pre><code>PACKFILE *input = pack_fopen(&quot;out.raw&quot;, &quot;rp&quot;);
... input = pack_fopen_chunk(input, 1);
/* Read data from the sub-chunk and close it. */
... input = pack_fclose_chunk(input);

This sequence will read the length counts created when the chunk was
    written,
    and automatically decompress the contents of the chunk if it
            was compressed.The length will also be used to prevent reading past the
                end of the
                chunk(Allegro will return EOF if you attempt this),
    and to
        automatically skip past any unread chunk data when you call
        pack_fclose_chunk()
            .</code></pre>
<p> Chunks can be nested inside each other by making repeated calls to pack_fopen_chunk(). When writing a file, the compression status is inherited from the parent file, so you only need to set the pack flag if the parent is not compressed but you want to pack the chunk data. If the parent file is already open in packed mode, setting the pack flag will result in data being compressed twice: once as it is written to the chunk, and again as the chunk passes it on to the parent file.</p>
<h2>Return Value</h2>
<p>Returns a pointer to the sub-chunked PACKFILE, or NULL if there was some error (eg. you are using a custom PACKFILE vtable). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fclose_chunk/">pack_fclose_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3) </p>
