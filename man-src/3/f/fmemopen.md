---
title: "fmemopen(3)"
name: "fmemopen"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmemopen/"
description: "fmemopen – open memory as stream"
---
<h2 class="name">NAME</h2>
<p> fmemopen - open memory as stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;stdio.h&gt; 
 FILE *fmemopen(void *buf  , size_t size  , const char *  mode  ); 
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fmemopen</code>(): </p>
<dl>
<dd>  </dd>
<dl>
<dt>Since glibc 2.10:</dt>
<dd> <p> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L </p>
 </dd>
<dt>Before glibc 2.10:</dt>
<dd> <p> _GNU_SOURCE </p>
 </dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>fmemopen</code>() function opens a stream that permits the access specified by <i>mode</i>. The stream allows I/O to be performed on the string or memory buffer pointed to by <i>buf</i>. </p>
<p> The <i>mode</i> argument specifies the semantics of I/O on the stream, and is one of the following: </p>
<dl>
<dt><i>r</i></dt>
<dd> <p> The stream is opened for reading. </p>
 </dd>
<dt><i>w</i></dt>
<dd> <p> The stream is opened for writing. </p>
 </dd>
<dt><i>a</i></dt>
<dd> <p> Append; open the stream for writing, with the initial buffer position set to the first null byte. </p>
 </dd>
<dt><i>r+</i></dt>
<dd> <p> Open the stream for reading and writing. </p>
 </dd>
<dt><i>w+</i></dt>
<dd> <p> Open the stream for reading and writing. The buffer contents are truncated (i.e., &#8216;\0&#8217; is placed in the first byte of the buffer). </p>
 </dd>
<dt><i>a+</i></dt>
<dd> <p> Append; open the stream for reading and writing, with the initial buffer position set to the first null byte. </p>
 </dd></dl>
<p> The stream maintains the notion of a current position, the location where the next I/O operation will be performed. The current position is implicitly updated by I/O operations. It can be explicitly updated using <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3), and determined using <code><a href="/docs/linux/man/3-ftell/">ftell</a></code>(3). In all modes other than append, the initial position is set to the start of the buffer. In append mode, if no null byte is found within the buffer, then the initial position is <i>size+1</i>. </p>
<p> If <i>buf</i> is specified as NULL, then <code>fmemopen</code>() allocates a buffer of <i>size</i> bytes. This is useful for an application that wants to write data to a temporary buffer and then read it back again. The initial position is set to the start of the buffer. The buffer is automatically freed when the stream is closed. Note that the caller has no way to obtain a pointer to the temporary buffer allocated by this call (but see <code>open_memstream</code>(3)). </p>
<p> If <i>buf</i> is not NULL, then it should point to a buffer of at least <i>len</i> bytes allocated by the caller. </p>
<p> When a stream that has been opened for writing is flushed (<code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3)) or closed (<code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3)), a null byte is written at the end of the buffer if there is space. The caller should ensure that an extra byte is available in the buffer (and that <i>size</i> counts that byte) to allow for this. </p>
<p> In a stream opened for reading, null bytes (&#8216;\0&#8217;) in the buffer do not cause read operations to return an end-of-file indication. A read from the buffer will indicate end-of-file only when the current buffer position advances <i>size</i> bytes past the start of the buffer. </p>
<p> Write operations take place either at the current position (for modes other than append), or at the current size of the stream (for append modes). </p>
<p> Attempts to write more than <i>size</i> bytes to the buffer result in an error. By default, such errors will be visible (by the absence of data) only when the <i>stdio</i> buffer is flushed. Disabling buffering with the following call may be useful to detect errors at the time of an output operation: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setbuf(stream, NULL);  </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>fmemopen</code>() returns a <i>FILE</i> pointer. Otherwise, NULL is returned and <i>errno</i> is set to indicate the error.  </p>
<h2>VERSIONS</h2>
<p> <code>fmemopen</code>() was already available in glibc 1.0.x.  </p>
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
<td> <code>fmemopen</code>(), </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008. This function is not specified in POSIX.1-2001, and is not widely available on other systems. </p>
<p> POSIX.1-2008 specifies that &#8216;b&#8217; in <i>mode</i> shall be ignored. However, Technical Corrigendum 1 adjusts the standard to allow implementation-specific treatment for this case, thus permitting the glibc treatment of &#8216;b&#8217;.  </p>
<h2>NOTES</h2>
<p> There is no file descriptor associated with the file stream returned by this function (i.e., <code><a href="/docs/linux/man/3-fileno/">fileno</a></code>(3) will return an error if called on the returned stream). </p>
<p> With version 2.22, binary mode (see below) was removed, many longstanding bugs in the implementation of <code>fmemopen</code>() were fixed, and a new versioned symbol was created for this interface.  </p>
<h3>Binary mode</h3>
<p> From version 2.9 to 2.21, the glibc implementation of <code>fmemopen</code>() supported a &quot;binary&quot; mode, enabled by specifying the letter &#8216;b&#8217; as the second character in <i>mode</i>. In this mode, writes don&#8217;t implicitly add a terminating null byte, and <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) <code>SEEK_END</code> is relative to the end of the buffer (i.e., the value specified by the <i>size</i> argument), rather than the current string length. </p>
<p> An API bug afflicted the implementation of binary mode: to specify binary mode, the &#8216;b&#8217; must be the <i>second</i> character in <i>mode</i>. Thus, for example, &quot;wb+&quot; has the desired effect, but &quot;w+b&quot; does not. This is inconsistent with the treatment of <i>mode</i> by <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3). </p>
<p> Binary mode was removed in glibc 2.22; a &#8216;b&#8217; specified in <i>mode</i> has no effect.  </p>
<h2>BUGS</h2>
<p> In versions of glibc before 2.22, if <i>size</i> is specified as zero, <code>fmemopen</code>() fails with the error <code>EINVAL</code>. It would be more consistent if this case successfully created a stream that then returned end-of-file on the first attempt at reading; since version 2.22, the glibc implementation provides that behavior. </p>
<p> In versions of glibc before 2.22, specifying append mode (&quot;a&quot; or &quot;a+&quot;) for <code>fmemopen</code>() sets the initial buffer position to the first null byte, but (if the current position is reset to a location other than the end of the stream) does not force subsequent writes to append at the end of the stream. This bug is fixed in glibc 2.22. </p>
<p> In versions of glibc before 2.22, if the <i>mode</i> argument to <code>fmemopen</code>() specifies append (&quot;a&quot; or &quot;a+&quot;), and the <i>size</i> argument does not cover a null byte in <i>buf</i>, then, according to POSIX.1-2008, the initial buffer position should be set to the next byte after the end of the buffer. However, in this case the glibc <code>fmemopen</code>() sets the buffer position to -1. This bug is fixed in glibc 2.22. </p>
<p> In versions of glibc before 2.22, when a call to <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) with a <i>whence</i> value of <code>SEEK_END</code> was performed on a stream created by <code>fmemopen</code>(), the <i>offset</i> was <i>subtracted</i> from the end-of-stream position, instead of being added. This bug is fixed in glibc 2.22. </p>
<p> The glibc 2.9 addition of &quot;binary&quot; mode for <code>fmemopen</code>() silently changed the ABI: previously, <code>fmemopen</code>() ignored &#8216;b&#8217; in <i>mode</i>.  </p>
<h2>EXAMPLES</h2>
<p> The program below uses <code>fmemopen</code>() to open an input buffer, and <code>open_memstream</code>(3) to open a dynamically sized output buffer. The program scans its input string (taken from the program&#8217;s first command-line argument) reading integers, and writes the squares of these integers to the output buffer. An example of the output produced by this program is the following: </p>
<p> $<code> ./a.out &#8216;1 23 43&#8217;</code> size=11; ptr=1 529 1849  </p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;string.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> #define handle_error(msg) \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;*out,&nbsp;*in; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int v, s; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t size; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*ptr; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&#8216;&lt;num&gt;...&#8216;\n&quot;, argv[0]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in&nbsp;=&nbsp;fmemopen(argv[1], strlen(argv[1]),&nbsp;&quot;r&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(in&nbsp;==&nbsp;NULL) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;fmemopen&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;out&nbsp;=&nbsp;open_memstream(&amp;ptr,&nbsp;&amp;size); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(out&nbsp;==&nbsp;NULL) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;open_memstream&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;fscanf(in,&nbsp;&quot;%d&quot;,&nbsp;&amp;v); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;&lt;=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;fprintf(out,&nbsp;&quot;%d&nbsp;&quot;, v&nbsp;*&nbsp;v); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;-1) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;fprintf&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fclose(in); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fclose(out); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;size=%zu;&nbsp;ptr=%s\n&quot;, size, ptr); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(ptr); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fopencookie/">fopencookie</a></code>(3), <code>open_memstream</code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
