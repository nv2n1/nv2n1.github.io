---
title: "fopencookie(3)"
name: "fopencookie"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fopencookie/"
description: "fopencookie – opening a custom stream"
---

<h2 class="name">NAME</h2>
<p> fopencookie &#8211; opening a custom stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;stdio.h&gt;
FILE *fopencookie(void *cookie, const char *mode,
                  cookie_io_functions_t io_funcs);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fopencookie</code>() function allows the programmer to create a custom implementation for a standard I/O stream. This implementation can store the stream&#8217;s data at a location of its own choosing; for example, <code>fopencookie</code>() is used to implement <code><a href="/docs/linux/man/3-fmemopen/">fmemopen</a></code>(3), which provides a stream interface to data that is stored in a buffer in memory. </p>
<p> In order to create a custom stream the programmer must:</p>
<dl>
<dt>*</p>
<dd> Implement four &quot;hook&quot; functions that are used internally by the standard I/O library when performing I/O on the stream.</p>
<dt>*</p>
<dd> Define a &quot;cookie&quot; data type, a structure that provides bookkeeping information (e.g., where to store data) used by the aforementioned hook functions. The standard I/O package knows nothing about the contents of this cookie (thus it is typed as <i>void&nbsp;*</i> when passed to <code>fopencookie</code>()), but automatically supplies the cookie as the first argument when calling the hook functions.</p>
<dt>*</p>
<dd> Call <code>fopencookie</code>() to open a new stream and associate the cookie and hook functions with that stream.</dl>
<p> The <code>fopencookie</code>() function serves a purpose similar to <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3): it opens a new stream and returns a pointer to a <i>FILE</i> object that is used to operate on that stream. </p>
<p> The <i>cookie</i> argument is a pointer to the caller&#8217;s cookie structure that is to be associated with the new stream. This pointer is supplied as the first argument when the standard I/O library invokes any of the hook functions described below. </p>
<p> The <i>mode</i> argument serves the same purpose as for <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3). The following modes are supported: <i>r</i>, <i>w</i>, <i>a</i>, <i>r+</i>, <i>w+</i>, and <i>a+</i>. See <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3) for details. </p>
<p> The <i>io_funcs</i> argument is a structure that contains four fields pointing to the programmer-defined hook functions that are used to implement this stream. The structure is defined as follows </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie_read_function_t&nbsp;<wbr>&nbsp;*read;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie_write_function_t&nbsp;*write;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie_seek_function_t&nbsp;<wbr>&nbsp;*seek;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie_close_function_t&nbsp;*close; } cookie_io_functions_t; </p>
<p> The four fields are as follows:</p>
<dl>
<dt><i>cookie_read_function_t *read</i></p>
<dd> This function implements read operations for the stream. When called, it receives three arguments:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t read(void&nbsp;*cookie, char&nbsp;*buf, size_t size);</p>
<dt>
<dd> The <i>buf</i> and <i>size</i> arguments are, respectively, a buffer into which input data can be placed and the size of that buffer. As its function result, the <i>read</i> function should return the number of bytes copied into <i>buf</i>, 0 on end of file, or -1 on error. The <i>read</i> function should update the stream offset appropriately.</p>
<dt>
<dd> If <i>*read</i> is a null pointer, then reads from the custom stream always return end of file.</p>
<dt><i>cookie_write_function_t *write</i></p>
<dd> This function implements write operations for the stream. When called, it receives three arguments:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t write(void&nbsp;*cookie, const char&nbsp;*buf, size_t size);</p>
<dt>
<dd> The <i>buf</i> and <i>size</i> arguments are, respectively, a buffer of data to be output to the stream and the size of that buffer. As its function result, the <i>write</i> function should return the number of bytes copied from <i>buf</i>, or 0 on error. (The function must not return a negative value.) The <i>write</i> function should update the stream offset appropriately.</p>
<dt>
<dd> If <i>*write</i> is a null pointer, then output to the stream is discarded.</p>
<dt><i>cookie_seek_function_t *seek</i></p>
<dd> This function implements seek operations on the stream. When called, it receives three arguments:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int seek(void&nbsp;*cookie, off64_t&nbsp;*offset, int whence);</p>
<dt>
<dd> The <i>*offset</i> argument specifies the new file offset depending on which of the following three values is supplied in <i>whence</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SEEK_SET</code></p>
<dd> The stream offset should be set <i>*offset</i> bytes from the start of the stream.</p>
<dt><code>SEEK_CUR</code></p>
<dd> <i>*offset</i> should be added to the current stream offset.</p>
<dt><code>SEEK_END</code></p>
<dd> The stream offset should be set to the size of the stream plus <i>*offset</i>.</dl>
</dl>
<dt>
<dd> Before returning, the <i>seek</i> function should update <i>*offset</i> to indicate the new stream offset.</p>
<dt>
<dd> As its function result, the <i>seek</i> function should return 0 on success, and -1 on error.</p>
<dt>
<dd> If <i>*seek</i> is a null pointer, then it is not possible to perform seek operations on the stream.</p>
<dt><i>cookie_close_function_t *close</i></p>
<dd> This function closes the stream. The hook function can do things such as freeing buffers allocated for the stream. When called, it receives one argument:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int close(void&nbsp;*cookie);</p>
<dt>
<dd> The <i>cookie</i> argument is the cookie that the programmer supplied when calling <code>fopencookie</code>().</p>
<dt>
<dd> As its function result, the <i>close</i> function should return 0 on success, and <code>EOF</code> on error.</p>
<dt>
<dd> If <i>*close</i> is NULL, then no special action is performed when the stream is closed.</dl>
<h2>RETURN VALUE</h2>
<p> On success <code>fopencookie</code>() returns a pointer to the new stream. On error, NULL is returned.</p>
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
<td> <code>fopencookie</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a nonstandard GNU extension.</p>
<h2>EXAMPLES</h2>
<p> The program below implements a custom stream whose functionality is similar (but not identical) to that available via <code><a href="/docs/linux/man/3-fmemopen/">fmemopen</a></code>(3). It implements a stream whose data is stored in a memory buffer. The program writes its command-line arguments to the stream, and then seeks through the stream reading two out of every five characters and writing them to standard output. The following shell session demonstrates the use of the program: </p>
<p> $<code> ./a.out &#8216;hello world&#8217;</code> /he/ / w/ /d/ Reached end of file </p>
<p> Note that a more general version of the program below could be improved to more robustly handle various error situations (e.g., opening a stream with a cookie that already has an open stream; closing a stream that has already been closed).</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;sys/types.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; </p>
<p> #define INIT_BUF_SIZE 4 </p>
<p> struct memfile_cookie {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*buf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Dynamically sized buffer for data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;allocated;&nbsp;<wbr>&nbsp;/*&nbsp;Size of buf&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;endpos;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of characters in buf&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Current file offset in buf&nbsp;*/ }; </p>
<p> ssize_t memfile_write(void *c, const char *buf, size_t size) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*new_buff;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct memfile_cookie&nbsp;*cookie&nbsp;=&nbsp;c; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Buffer too small?&nbsp;Keep doubling size until big enough&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(size&nbsp;+&nbsp;cookie-&gt;offset&nbsp;&gt;&nbsp;cookie-&gt;allocated)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_buff&nbsp;=&nbsp;realloc(cookie-&gt;buf, cookie-&gt;allocated&nbsp;*&nbsp;2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(new_buff&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;allocated&nbsp;*=&nbsp;2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;buf&nbsp;=&nbsp;new_buff;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memcpy(cookie-&gt;buf&nbsp;+&nbsp;cookie-&gt;offset, buf, size); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;offset&nbsp;+=&nbsp;size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cookie-&gt;offset&nbsp;&gt;&nbsp;cookie-&gt;endpos)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;endpos&nbsp;=&nbsp;cookie-&gt;offset; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return size; } </p>
<p> ssize_t memfile_read(void *c, char *buf, size_t size) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t xbytes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct memfile_cookie&nbsp;*cookie&nbsp;=&nbsp;c; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Fetch minimum of bytes requested and bytes available&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;xbytes&nbsp;=&nbsp;size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cookie-&gt;offset&nbsp;+&nbsp;size&nbsp;&gt;&nbsp;cookie-&gt;endpos)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;xbytes&nbsp;=&nbsp;cookie-&gt;endpos &#8211; cookie-&gt;offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(xbytes&nbsp;&lt;&nbsp;0)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;offset may be past endpos&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;xbytes&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memcpy(buf, cookie-&gt;buf&nbsp;+&nbsp;cookie-&gt;offset, xbytes); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;offset&nbsp;+=&nbsp;xbytes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return xbytes; } </p>
<p> int memfile_seek(void *c, off64_t *offset, int whence) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off64_t new_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct memfile_cookie&nbsp;*cookie&nbsp;=&nbsp;c; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(whence&nbsp;==&nbsp;SEEK_SET)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_offset&nbsp;=&nbsp;*offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else if&nbsp;(whence&nbsp;==&nbsp;SEEK_END)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_offset&nbsp;=&nbsp;cookie-&gt;endpos&nbsp;+&nbsp;*offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else if&nbsp;(whence&nbsp;==&nbsp;SEEK_CUR)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_offset&nbsp;=&nbsp;cookie-&gt;offset&nbsp;+&nbsp;*offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(new_offset&nbsp;&lt;&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;offset&nbsp;=&nbsp;new_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*offset&nbsp;=&nbsp;new_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; } </p>
<p> int memfile_close(void *c) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct memfile_cookie&nbsp;*cookie&nbsp;=&nbsp;c; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(cookie-&gt;buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;allocated&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie-&gt;buf&nbsp;=&nbsp;NULL; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cookie_io_functions_t&nbsp;<wbr>&nbsp;memfile_func&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.read&nbsp;<wbr>&nbsp;=&nbsp;memfile_read,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.write&nbsp;=&nbsp;memfile_write,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.seek&nbsp;<wbr>&nbsp;=&nbsp;memfile_seek,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.close&nbsp;=&nbsp;memfile_close<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;*stream;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct memfile_cookie mycookie;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t nread;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[1000]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Set up the cookie before calling fopencookie()&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mycookie.buf&nbsp;=&nbsp;malloc(INIT_BUF_SIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mycookie.buf&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;malloc&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mycookie.allocated&nbsp;=&nbsp;INIT_BUF_SIZE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mycookie.offset&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mycookie.endpos&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stream&nbsp;=&nbsp;fopencookie(&amp;mycookie,&quot;w+&quot;, memfile_func);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(stream&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fopencookie&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Write command-line arguments to our file&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;1;&nbsp;j&nbsp;&lt;&nbsp;argc;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fputs(argv[j], stream)&nbsp;==&nbsp;EOF)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fputs&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Read two bytes out of every five, until EOF&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(long p&nbsp;=&nbsp;0;&nbsp;;&nbsp;p&nbsp;+=&nbsp;5)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fseek(stream, p, SEEK_SET)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fseek&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;fread(buf, 1, 2, stream);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ferror(stream)&nbsp;!=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;fread failed
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Reached end of file
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;/%.*s/
&quot;,&nbsp;(int)&nbsp;nread, buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-fmemopen/">fmemopen</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
