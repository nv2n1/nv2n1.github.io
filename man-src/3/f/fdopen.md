---
title: "fdopen(3)"
name: "fdopen"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fdopen/"
description: "fopen, fdopen, freopen – stream open functions"
---

<h2 class="name">NAME</h2>
<p> fopen, fdopen, freopen &#8211; stream open functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
FILE *fopen(const char *pathname, const char *mode);
FILE *fdopen(int fd, const char *mode);
FILE *freopen(const char *pathname, const char *mode, FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fdopen</code>(): _POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>fopen</code>() function opens the file whose name is the string pointed to by <i>pathname</i> and associates a stream with it. </p>
<p> The argument <i>mode</i> points to a string beginning with one of the following sequences (possibly followed by additional characters, as described below):</p>
<dl>
<dt><code>r</code></p>
<dd> Open text file for reading. The stream is positioned at the beginning of the file.</p>
<dt><code>r+</code></p>
<dd> Open for reading and writing. The stream is positioned at the beginning of the file.</p>
<dt><code>w</code></p>
<dd> Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.</p>
<dt><code>w+</code></p>
<dd> Open for reading and writing. The file is created if it does not exist, otherwise it is truncated. The stream is positioned at the beginning of the file.</p>
<dt><code>a</code></p>
<dd> Open for appending (writing at end of file). The file is created if it does not exist. The stream is positioned at the end of the file.</p>
<dt><code>a+</code></p>
<dd> Open for reading and appending (writing at end of file). The file is created if it does not exist. Output is always appended to the end of the file. POSIX is silent on what the initial read position is when using this mode. For glibc, the initial file position for reading is at the beginning of the file, but for Android/BSD/MacOS, the initial file position for reading is at the end of the file.</dl>
<p> The <i>mode</i> string can also include the letter &#8216;b&#8217; either as a last character or as a character between the characters in any of the two-character strings described above. This is strictly for compatibility with C89 and has no effect; the &#8216;b&#8217; is ignored on all POSIX conforming systems, including Linux. (Other systems may treat text files and binary files differently, and adding the &#8216;b&#8217; may be a good idea if you do I/O to a binary file and expect that your program may be ported to non-UNIX environments.) </p>
<p> See NOTES below for details of glibc extensions for <i>mode</i>. </p>
<p> Any created file will have the mode <code>S_IRUSR</code> | <code>S_IWUSR</code> | <code>S_IRGRP</code> | <code>S_IWGRP</code> | <code>S_IROTH</code> | <code>S_IWOTH</code> (0666), as modified by the process&#8217;s umask value (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)). </p>
<p> Reads and writes may be intermixed on read/write streams in any order. Note that ANSI C requires that a file positioning function intervene between output and input, unless an input operation encounters end-of-file. (If this condition is not met, then a read is allowed to return the result of writes other than the most recent.) Therefore it is good practice (and indeed sometimes necessary under Linux) to put an <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) or <code><a href="/docs/linux/man/3-fgetpos/">fgetpos</a></code>(3) operation between write and read operations on such a stream. This operation may be an apparent no-op (as in <i>fseek(&#8230;, 0L, SEEK_CUR)</i> called for its synchronizing side effect). </p>
<p> Opening a file in append mode (<code>a</code> as the first character of <i>mode</i>) causes all subsequent write operations to this stream to occur at end-of-file, as if preceded the call: </p>
<p> fseek(stream, 0, SEEK_END); </p>
<p> The file descriptor associated with the stream is opened as if by a call to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the following flags:</p>
<dl>
<dt>
<dd>
<table BORDER>
<tr VALIGN=top>
<td><code>fopen() mode</code></td>
<td><code>open() flags</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>r</i></td>
<td>O_RDONLY
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>w</i></td>
<td>O_WRONLY | O_CREAT | O_TRUNC
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>a</i></td>
<td>O_WRONLY | O_CREAT | O_APPEND
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>r+</i></td>
<td>O_RDWR
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>w+</i></td>
<td>O_RDWR | O_CREAT | O_TRUNC
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>a+</i></td>
<td>O_RDWR | O_CREAT | O_APPEND
</td>
</tr>
</table>
</dl>
<h3>fdopen()</h3>
<p> The <code>fdopen</code>() function associates a stream with the existing file descriptor, <i>fd</i>. The <i>mode</i> of the stream (one of the values &quot;r&quot;, &quot;r+&quot;, &quot;w&quot;, &quot;w+&quot;, &quot;a&quot;, &quot;a+&quot;) must be compatible with the mode of the file descriptor. The file position indicator of the new stream is set to that belonging to <i>fd</i>, and the error and end-of-file indicators are cleared. Modes &quot;w&quot; or &quot;w+&quot; do not cause truncation of the file. The file descriptor is not dup&#8217;ed, and will be closed when the stream created by <code>fdopen</code>() is closed. The result of applying <code>fdopen</code>() to a shared memory object is undefined.</p>
<h3>freopen()</h3>
<p> The <code>freopen</code>() function opens the file whose name is the string pointed to by <i>pathname</i> and associates the stream pointed to by <i>stream</i> with it. The original stream (if it exists) is closed. The <i>mode</i> argument is used just as in the <code>fopen</code>() function. </p>
<p> If the <i>pathname</i> argument is a null pointer, <code>freopen</code>() changes the mode of the stream to that specified in <i>mode</i>; that is, <code>freopen</code>() reopens the pathname that is associated with the stream. The specification for this behavior was added in the C99 standard, which says: </p>
<dl>
<dt>
<dd> In this case, the file descriptor associated with the stream need not be closed if the call to <code>freopen</code>() succeeds. It is implementation-defined which changes of mode are permitted (if any), and under what circumstances.</dl>
<p> The primary use of the <code>freopen</code>() function is to change the file associated with a standard text stream (<i>stderr</i>, <i>stdin</i>, or <i>stdout</i>).</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion <code>fopen</code>(), <code>fdopen</code>(), and <code>freopen</code>() return a <i>FILE</i> pointer. Otherwise, NULL is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>mode</i> provided to <code>fopen</code>(), <code>fdopen</code>(), or <code>freopen</code>() was invalid.</dl>
<p> The <code>fopen</code>(), <code>fdopen</code>(), and <code>freopen</code>() functions may also fail and set <i>errno</i> for any of the errors specified for the routine <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> The <code>fopen</code>() function may also fail and set <i>errno</i> for any of the errors specified for the routine <code><a href="/docs/linux/man/2-open/">open</a></code>(2). </p>
<p> The <code>fdopen</code>() function may also fail and set <i>errno</i> for any of the errors specified for the routine <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). </p>
<p> The <code>freopen</code>() function may also fail and set <i>errno</i> for any of the errors specified for the routines <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), and <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3).</p>
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
<td> <code>fopen</code>(), <code>fdopen</code>(), <code>freopen</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>fopen</code>(), <code>freopen</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99. </p>
<p> <code>fdopen</code>(): POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<h3>Glibc notes</h3>
<p> The GNU C library allows the following extensions for the string specified in <i>mode</i>:</p>
<dl>
<dt><code>c</code> (since glibc 2.3.3)</p>
<dd> Do not make the open operation, or subsequent read and write operations, thread cancellation points. This flag is ignored for <code>fdopen</code>().</p>
<dt><code>e</code> (since glibc 2.7)</p>
<dd> Open the file with the <code>O_CLOEXEC</code> flag. See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for more information. This flag is ignored for <code>fdopen</code>().</p>
<dt><code>m</code> (since glibc 2.3)</p>
<dd> Attempt to access the file using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), rather than I/O system calls (<code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2)). Currently, use of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) is attempted only for a file opened for reading.</p>
<dt><code>x</code></p>
<dd> Open the file exclusively (like the <code>O_EXCL</code> flag of <code><a href="/docs/linux/man/2-open/">open</a></code>(2)). If the file already exists, <code>fopen</code>() fails, and sets <i>errno</i> to <code>EEXIST</code>. This flag is ignored for <code>fdopen</code>().</dl>
<p> In addition to the above characters, <code>fopen</code>() and <code>freopen</code>() support the following syntax in <i>mode</i>: </p>
<p> <code> ,ccs=</code><i>string</i> </p>
<p> The given <i>string</i> is taken as the name of a coded character set and the stream is marked as wide-oriented. Thereafter, internal conversion functions convert I/O to and from the character set <i>string</i>. If the <code>,ccs=</code><i>string</i> syntax is not specified, then the wide-orientation of the stream is determined by the first file operation. If that operation is a wide-character operation, the stream is marked wide-oriented, and functions to convert to the coded character set are loaded.</p>
<h2>BUGS</h2>
<p> When parsing for individual flag characters in <i>mode</i> (i.e., the characters preceding the &quot;ccs&quot; specification), the glibc implementation of <code>fopen</code>() and <code>freopen</code>() limits the number of characters examined in <i>mode</i> to 7 (or, in glibc versions before 2.14, to 6, which was not enough to include possible specifications such as &quot;rb+cmxe&quot;). The current implementation of <code>fdopen</code>() parses at most 5 characters in <i>mode</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-fileno/">fileno</a></code>(3), <code><a href="/docs/linux/man/3-fmemopen/">fmemopen</a></code>(3), <code><a href="/docs/linux/man/3-fopencookie/">fopencookie</a></code>(3), <code><a href="/docs/linux/man/3-open_memstream/">open_memstream</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
