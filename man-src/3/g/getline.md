---
title: "getline(3)"
name: "getline"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getline/"
description: "getline, getdelim – delimited string input"
---

<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
ssize_t getline(char **lineptr, size_t *n, FILE *stream);
ssize_t getdelim(char **lineptr, size_t *n, int delim, FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getline</code>(), <code>getdelim</code>():</p>
<dl>
<dl>
<dt>Since glibc 2.10:</dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd> _GNU_SOURCE</dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>getline</code>() reads an entire line from <i>stream</i>, storing the address of the buffer containing the text into <i>*lineptr</i>. The buffer is null-terminated and includes the newline character, if one was found. </p>
<p> If <i>*lineptr</i> is set to NULL and <i>*n</i> is set 0 before the call, then <code>getline</code>() will allocate a buffer for storing the line. This buffer should be freed by the user program even if <code>getline</code>() failed. </p>
<p> Alternatively, before calling <code>getline</code>(), <i>*lineptr</i> can contain a pointer to a <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)-allocated buffer <i>*n</i> bytes in size. If the buffer is not large enough to hold the line, <code>getline</code>() resizes it with <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), updating <i>*lineptr</i> and <i>*n</i> as necessary. </p>
<p> In either case, on a successful call, <i>*lineptr</i> and <i>*n</i> will be updated to reflect the buffer address and allocated size respectively. </p>
<p> <code>getdelim</code>() works like <code>getline</code>(), except that a line delimiter other than newline can be specified as the <i>delimiter</i> argument. As with <code>getline</code>(), a delimiter character is not added if one was not present in the input before end of file was reached.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>getline</code>() and <code>getdelim</code>() return the number of characters read, including the delimiter character, but not including the terminating null byte (&#8216;\0&#8217;). This value can be used to handle embedded null bytes in the line read. </p>
<p> Both functions return -1 on failure to read a line (including end-of-file condition). In the event of an error, <i>errno</i> is set to indicate the cause.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></dt>
<dd> <p> Bad arguments (<i>n</i> or <i>lineptr</i> is NULL, or <i>stream</i> is not valid). </p>
 </dd>
<dt><code>ENOMEM</code></dt>
<dd> <p> Allocation or reallocation of the line buffer failed. </p>
 </dd></dl>
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
<td> <code>getline</code>(), <code>getdelim</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Both <code>getline</code>() and <code>getdelim</code>() were originally GNU extensions. They were standardized in POSIX.1-2008.  </p>
<h2>EXAMPLES</h2>
<p> #define _GNU_SOURCE #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;*stream; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*line&nbsp;=&nbsp;NULL; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t len&nbsp;=&nbsp;0; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nread; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;file&gt;\n&quot;, argv[0]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stream&nbsp;=&nbsp;fopen(argv[1],&nbsp;&quot;r&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(stream&nbsp;==&nbsp;NULL)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fopen&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((nread&nbsp;=&nbsp;getline(&amp;line,&nbsp;&amp;len, stream))&nbsp;!=&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Retrieved line of length&nbsp;%zd:\n&quot;, nread); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fwrite(line, nread, 1, stdout); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(line); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fclose(stream); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
