---
title: "bswap_32(3)"
name: "bswap_32"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bswap_32/"
description: "bswap_16, bswap_32, bswap_64 – reverse order of bytes"
---

<h2 class="name">NAME</h2>
<p> bswap_16, bswap_32, bswap_64 &#8211; reverse order of bytes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;byteswap.h&gt;
bswap_16(x);
bswap_32(x);
bswap_64(x);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These macros return a value in which the order of the bytes in their 2-, 4-, or 8-byte arguments is reversed.</p>
<h2>RETURN VALUE</h2>
<p> These macros return the value of their argument with the bytes reversed.</p>
<h2>ERRORS</h2>
<p> These macros always succeed.</p>
<h2>CONFORMING TO</h2>
<p> These macros are GNU extensions.</p>
<h2>EXAMPLES</h2>
<p> The program below swaps the bytes of the 8-byte integer supplied as its command-line argument. The following shell session demonstrates the use of the program: </p>
<p> $ <code>./a.out 0x0123456789abcdef</code> 0x123456789abcdef ==&gt; 0xefcdab8967452301</p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;inttypes.h&gt; #include &lt;byteswap.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t x; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;num&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x&nbsp;=&nbsp;strtoull(argv[1], NULL, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%#&quot;&nbsp;PRIx64&nbsp;&quot;&nbsp;==&gt;&nbsp;%#&quot;&nbsp;PRIx64&nbsp;&quot;
&quot;, x, bswap_64(x)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3), <code><a href="/docs/linux/man/3-endian/">endian</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
