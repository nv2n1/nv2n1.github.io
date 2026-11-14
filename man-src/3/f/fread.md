---
title: "fread(3)"
name: "fread"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fread/"
description: "fread, fwrite – binary stream input/output"
---

<h2 class="name">NAME</h2>
<p> fread, fwrite &#8211; binary stream input/output </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t nmemb,
              FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The function <code>fread</code>() reads <i>nmemb</i> items of data, each <i>size</i> bytes long, from the stream pointed to by <i>stream</i>, storing them at the location given by <i>ptr</i>. </p>
<p> The function <code>fwrite</code>() writes <i>nmemb</i> items of data, each <i>size</i> bytes long, to the stream pointed to by <i>stream</i>, obtaining them from the location given by <i>ptr</i>. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>fread</code>() and <code>fwrite</code>() return the number of items read or written. This number equals the number of bytes transferred only when <i>size</i> is 1. If an error occurs, or the end of the file is reached, the return value is a short item count (or zero). </p>
<p> The file position indicator for the stream is advanced by the number of bytes successfully read or written. </p>
<p> <code>fread</code>() does not distinguish between end-of-file and error, and callers must use <code><a href="/docs/linux/man/3-feof/">feof</a></code>(3) and <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3) to determine which occurred.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>fread</code>(), <code>fwrite</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>fread</code>() by parsing /bin/sh ELF executable in binary mode and printing its magic and class: </p>
<p> $ <code>./a.out</code> ELF magic: 0x7f454c46 Class: 0x02</p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> #define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0])) </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;*fp&nbsp;=&nbsp;fopen(&quot;/bin/sh&quot;,&nbsp;&quot;rb&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!fp)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fopen&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return EXIT_FAILURE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char buffer[4]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t ret&nbsp;=&nbsp;fread(buffer, ARRAY_SIZE(buffer), sizeof(*buffer), fp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;!=&nbsp;sizeof(*buffer))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;fread()&nbsp;failed:&nbsp;%zu
&quot;, ret);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;ELF magic:&nbsp;%#04x%02x%02x%02x
&quot;, buffer[0], buffer[1],<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buffer[2], buffer[3]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;fread(buffer, 1, 1, fp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;!=&nbsp;1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;fread()&nbsp;failed:&nbsp;%zu
&quot;, ret);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Class:&nbsp;%#04x
&quot;, buffer[0]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fclose(fp); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-feof/">feof</a></code>(3), <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
