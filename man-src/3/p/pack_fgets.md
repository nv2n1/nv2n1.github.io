---
title: "pack_fgets(3)"
name: "pack_fgets"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fgets/"
description: "pack_fgets – Reads a line from the stream. Allegro game programming library."
---

<p>pack_fgets &#8211; Reads a line from the stream. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *pack_fgets(char *p, int max, PACKFILE *f);</code></pre>
<h2>Description</h2>
<p>Reads a line from the stream `f&#8217;, storing it at location pointed to by `p&#8217;. Stops when a linefeed is encountered, or `max&#8217; bytes have been read. The end of line is handled by detecting the right combination of characters for the platform. This supports CR-LF (DOS/Windows), LF (Unix), and CR (Mac) formats. However, the trailing carriage return is not included in the returned string, in order to provide easy code portability across platforms. If you need the carriage return, use pack_fread() and/or pack_getc() instead. Note: This function internally may make calls to pack_ungetc, so you cannot use pack_ungetc directly afterwards. Example: </p>
<pre><code>char buf[256];
... while (pack_fgets(buf, sizeof(buf), input_file))
{
    /* Process input line. */
}
fclose(input_file);</code></pre>
<h2>Return Value</h2>
<p>Returns the pointer `p&#8217; on success, or NULL on error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-pack_fread/">pack_fread</a></code>(3), <code><a href="/docs/linux/man/3-pack_getc/">pack_getc</a></code>(3), <code><a href="/docs/linux/man/3-pack_ungetc/">pack_ungetc</a></code>(3) </p>
