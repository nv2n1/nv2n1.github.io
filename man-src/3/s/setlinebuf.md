---
title: "setlinebuf(3)"
name: "setlinebuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setlinebuf/"
description: "setbuf, setbuffer, setlinebuf, setvbuf – stream buffering operations"
---

<p>setbuf, setbuffer, setlinebuf, setvbuf &#8211; stream buffering operations</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

void setbuf(FILE *stream, char *buf);

void setbuffer(FILE *stream, char *buf, size_t size);

void setlinebuf(FILE *stream);

int setvbuf(FILE *stream, char *buf, int mode, size_t size);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>setbuffer</code>(), <code>setlinebuf</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>The three types of buffering available are unbuffered, block buffered, and line buffered. When an output stream is unbuffered, information appears on the destination file or terminal as soon as written; when it is block buffered many characters are saved up and written as a block; when it is line buffered characters are saved up until a newline is output or input is read from any stream attached to a terminal device (typically <i>stdin</i>). The function <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3) may be used to force the block out early. (See <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3).) </p>
<p> Normally all files are block buffered. If a stream refers to a terminal (as <i>stdout</i> normally does), it is line buffered. The standard error stream <i>stderr</i> is always unbuffered by default. </p>
<p> The <code>setvbuf</code>() function may be used on any open stream to change its buffer. The <i>mode</i> argument must be one of the following three macros:</p>
<dl>
<dd>
<dl>
<dt><code>_IONBF</code></p>
<dd>unbuffered</p>
<dt><code>_IOLBF</code></p>
<dd>line buffered</p>
<dt><code>_IOFBF</code></p>
<dd>fully buffered</dl>
</dl>
<p> Except for unbuffered files, the <i>buf</i> argument should point to a buffer at least <i>size</i> bytes long; this buffer will be used instead of the current buffer. If the argument <i>buf</i> is NULL, only the mode is affected; a new buffer will be allocated on the next read or write operation. The <code>setvbuf</code>() function may be used only after opening a stream and before any other operations have been performed on it. </p>
<p> The other three calls are, in effect, simply aliases for calls to <code>setvbuf</code>(). The <code>setbuf</code>() function is exactly equivalent to the call </p>
<p> setvbuf(stream, buf, buf ? _IOFBF : _IONBF, BUFSIZ); </p>
<p> The <code>setbuffer</code>() function is the same, except that the size of the buffer is up to the caller, rather than being determined by the default <code>BUFSIZ</code>. The <code>setlinebuf</code>() function is exactly equivalent to the call: </p>
<p> setvbuf(stream, NULL, _IOLBF, 0);</p>
<h2>Return Value</h2>
<p>The function <code>setvbuf</code>() returns 0 on success. It returns nonzero on failure (<i>mode</i> is invalid or the request cannot be honored). It may set <i>errno</i> on failure. </p>
<p> The other functions do not return a value.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>setbuf</code>(), <code>setbuffer</code>(),<br />
 <code>setlinebuf</code>(), <code>setvbuf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The <code>setbuf</code>() and <code>setvbuf</code>() functions conform to C89 and C99.</p>
<h2>Bugs</h2>
<p>You must make sure that the space that <i>buf</i> points to still exists by the time <i>stream</i> is closed, which also happens at program termination. For example, the following is invalid: </p>
<pre><code>#include &lt;stdio.h&gt;
int main(void)
{
    char buf[BUFSIZ];
    setbuf(stdin, buf);
    printf(&quot;Hello, world!
&quot;);
    return 0;
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-stdbuf/">stdbuf</a></code>(1), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-puts/">puts</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
