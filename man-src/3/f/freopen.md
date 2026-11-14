---
title: "freopen(3)"
name: "freopen"
section: "3"
letter: "f"
url: "/docs/linux/man/3-freopen/"
---

<h2 class="name">NAME</h2>
 

 fopen, fdopen, freopen - stream open functions 

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;stdio.h&gt;
FILE *fopen(const char *pathname, const char *mode);
FILE *fdopen(int fd, const char *mode);
FILE *freopen(const char *pathname, const char *mode, FILE *stream);
</code></pre> 

 Feature Test Macro Requirements for glibc (see <b><a HREF="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></b>(7)): 

 <b>fdopen</b>(): _POSIX_C_SOURCE

<h2>DESCRIPTION</h2>

 The <b>fopen</b>() function opens the file whose name is the string pointed to by <i>pathname</i> and associates a stream with it. 

 The argument <i>mode</i> points to a string beginning with one of the following sequences (possibly followed by additional characters, as described below):
<dl>
<dt><b>r</b>
<dd> Open text file for reading. The stream is positioned at the beginning of the file.
<dt><b>r+</b>
<dd> Open for reading and writing. The stream is positioned at the beginning of the file.
<dt><b>w</b>
<dd> Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.
<dt><b>w+</b>
<dd> Open for reading and writing. The file is created if it does not exist, otherwise it is truncated. The stream is positioned at the beginning of the file.
<dt><b>a</b>
<dd> Open for appending (writing at end of file). The file is created if it does not exist. The stream is positioned at the end of the file.
<dt><b>a+</b>
<dd> Open for reading and appending (writing at end of file). The file is created if it does not exist. Output is always appended to the end of the file. POSIX is silent on what the initial read position is when using this mode. For glibc, the initial file position for reading is at the beginning of the file, but for Android/BSD/MacOS, the initial file position for reading is at the end of the file.</dl>
 

 The <i>mode</i> string can also include the letter 'b' either as a last character or as a character between the characters in any of the two-character strings described above. This is strictly for compatibility with C89 and has no effect; the 'b' is ignored on all POSIX conforming systems, including Linux. (Other systems may treat text files and binary files differently, and adding the 'b' may be a good idea if you do I/O to a binary file and expect that your program may be ported to non-UNIX environments.) 

 See NOTES below for details of glibc extensions for <i>mode</i>. 

 Any created file will have the mode <b>S_IRUSR</b> | <b>S_IWUSR</b> | <b>S_IRGRP</b> | <b>S_IWGRP</b> | <b>S_IROTH</b> | <b>S_IWOTH</b> (0666), as modified by the process's umask value (see <b><a HREF="/docs/linux/man/2-umask/">umask</a></b>(2)). 

 Reads and writes may be intermixed on read/write streams in any order. Note that ANSI C requires that a file positioning function intervene between output and input, unless an input operation encounters end-of-file. (If this condition is not met, then a read is allowed to return the result of writes other than the most recent.) Therefore it is good practice (and indeed sometimes necessary under Linux) to put an <b><a HREF="/docs/linux/man/3-fseek/">fseek</a></b>(3) or <b><a HREF="/docs/linux/man/3-fgetpos/">fgetpos</a></b>(3) operation between write and read operations on such a stream. This operation may be an apparent no-op (as in <i>fseek(..., 0L, SEEK_CUR)</i> called for its synchronizing side effect). 

 Opening a file in append mode (<b>a</b> as the first character of <i>mode</i>) causes all subsequent write operations to this stream to occur at end-of-file, as if preceded the call: 

 fseek(stream, 0, SEEK_END); 

 The file descriptor associated with the stream is opened as if by a call to <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2) with the following flags:
<dl>
<dt>
<dd> <table BORDER> <tr VALIGN=top><td><b>fopen() mode</b></td><td><b>open() flags</b>
</td></tr> <tr VALIGN=top><td ALIGN=center><i>r</i></td><td>O_RDONLY
</td></tr> <tr VALIGN=top><td ALIGN=center><i>w</i></td><td>O_WRONLY | O_CREAT | O_TRUNC
</td></tr> <tr VALIGN=top><td ALIGN=center><i>a</i></td><td>O_WRONLY | O_CREAT | O_APPEND
</td></tr> <tr VALIGN=top><td ALIGN=center><i>r+</i></td><td>O_RDWR
</td></tr> <tr VALIGN=top><td ALIGN=center><i>w+</i></td><td>O_RDWR | O_CREAT | O_TRUNC
</td></tr> <tr VALIGN=top><td ALIGN=center><i>a+</i></td><td>O_RDWR | O_CREAT | O_APPEND
</td></tr> </table></dl>

<h3>fdopen()</h3>

 The <b>fdopen</b>() function associates a stream with the existing file descriptor, <i>fd</i>. The <i>mode</i> of the stream (one of the values &quot;r&quot;, &quot;r+&quot;, &quot;w&quot;, &quot;w+&quot;, &quot;a&quot;, &quot;a+&quot;) must be compatible with the mode of the file descriptor. The file position indicator of the new stream is set to that belonging to <i>fd</i>, and the error and end-of-file indicators are cleared. Modes &quot;w&quot; or &quot;w+&quot; do not cause truncation of the file. The file descriptor is not dup'ed, and will be closed when the stream created by <b>fdopen</b>() is closed. The result of applying <b>fdopen</b>() to a shared memory object is undefined.

<h3>freopen()</h3>

 The <b>freopen</b>() function opens the file whose name is the string pointed to by <i>pathname</i> and associates the stream pointed to by <i>stream</i> with it. The original stream (if it exists) is closed. The <i>mode</i> argument is used just as in the <b>fopen</b>() function. 

 If the <i>pathname</i> argument is a null pointer, <b>freopen</b>() changes the mode of the stream to that specified in <i>mode</i>; that is, <b>freopen</b>() reopens the pathname that is associated with the stream. The specification for this behavior was added in the C99 standard, which says: 

<dl>
<dt>
<dd> In this case, the file descriptor associated with the stream need not be closed if the call to <b>freopen</b>() succeeds. It is implementation-defined which changes of mode are permitted (if any), and under what circumstances.</dl>
 

 The primary use of the <b>freopen</b>() function is to change the file associated with a standard text stream (<i>stderr</i>, <i>stdin</i>, or <i>stdout</i>).

<h2>RETURN VALUE</h2>

 Upon successful completion <b>fopen</b>(), <b>fdopen</b>(), and <b>freopen</b>() return a <i>FILE</i> pointer. Otherwise, NULL is returned and <i>errno</i> is set to indicate the error.

<h2>ERRORS</h2>

<dl>
<dt><b>EINVAL</b>
<dd> The <i>mode</i> provided to <b>fopen</b>(), <b>fdopen</b>(), or <b>freopen</b>() was invalid.</dl>
 

 The <b>fopen</b>(), <b>fdopen</b>(), and <b>freopen</b>() functions may also fail and set <i>errno</i> for any of the errors specified for the routine <b><a HREF="/docs/linux/man/3-malloc/">malloc</a></b>(3). 

 The <b>fopen</b>() function may also fail and set <i>errno</i> for any of the errors specified for the routine <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2). 

 The <b>fdopen</b>() function may also fail and set <i>errno</i> for any of the errors specified for the routine <b><a HREF="/docs/linux/man/2-fcntl/">fcntl</a></b>(2). 

 The <b>freopen</b>() function may also fail and set <i>errno</i> for any of the errors specified for the routines <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2), <b><a HREF="/docs/linux/man/3-fclose/">fclose</a></b>(3), and <b><a HREF="/docs/linux/man/3-fflush/">fflush</a></b>(3).

<h2>ATTRIBUTES</h2>

 For an explanation of the terms used in this section, see <b><a HREF="/docs/linux/man/7-attributes/">attributes</a></b>(7). <table BORDER> <tr VALIGN=top><td><b>Interface</b></td><td><b>Attribute</b></td><td><b>Value</b>
</td></tr> <tr VALIGN=top><td> <b>fopen</b>(), <b>fdopen</b>(), <b>freopen</b>() </td><td>Thread safety</td><td>MT-Safe
</td></tr> </table>

<h2>CONFORMING TO</h2>

 <b>fopen</b>(), <b>freopen</b>(): POSIX.1-2001, POSIX.1-2008, C89, C99. 

 <b>fdopen</b>(): POSIX.1-2001, POSIX.1-2008.

<h2>NOTES</h2>

<h3>Glibc notes</h3>

 The GNU C library allows the following extensions for the string specified in <i>mode</i>:
<dl>
<dt><b>c</b> (since glibc 2.3.3)
<dd> Do not make the open operation, or subsequent read and write operations, thread cancellation points. This flag is ignored for <b>fdopen</b>().
<dt><b>e</b> (since glibc 2.7)
<dd> Open the file with the <b>O_CLOEXEC</b> flag. See <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2) for more information. This flag is ignored for <b>fdopen</b>().
<dt><b>m</b> (since glibc 2.3)
<dd> Attempt to access the file using <b><a HREF="/docs/linux/man/2-mmap/">mmap</a></b>(2), rather than I/O system calls (<b><a HREF="/docs/linux/man/2-read/">read</a></b>(2), <b><a HREF="/docs/linux/man/2-write/">write</a></b>(2)). Currently, use of <b><a HREF="/docs/linux/man/2-mmap/">mmap</a></b>(2) is attempted only for a file opened for reading.
<dt><b>x</b>
<dd> Open the file exclusively (like the <b>O_EXCL</b> flag of <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2)). If the file already exists, <b>fopen</b>() fails, and sets <i>errno</i> to <b>EEXIST</b>. This flag is ignored for <b>fdopen</b>().</dl>
 

 In addition to the above characters, <b>fopen</b>() and <b>freopen</b>() support the following syntax in <i>mode</i>: 

 <b> ,ccs=</b><i>string</i> 

 The given <i>string</i> is taken as the name of a coded character set and the stream is marked as wide-oriented. Thereafter, internal conversion functions convert I/O to and from the character set <i>string</i>. If the <b>,ccs=</b><i>string</i> syntax is not specified, then the wide-orientation of the stream is determined by the first file operation. If that operation is a wide-character operation, the stream is marked wide-oriented, and functions to convert to the coded character set are loaded.

<h2>BUGS</h2>

 When parsing for individual flag characters in <i>mode</i> (i.e., the characters preceding the &quot;ccs&quot; specification), the glibc implementation of <b>fopen</b>() and <b>freopen</b>() limits the number of characters examined in <i>mode</i> to 7 (or, in glibc versions before 2.14, to 6, which was not enough to include possible specifications such as &quot;rb+cmxe&quot;). The current implementation of <b>fdopen</b>() parses at most 5 characters in <i>mode</i>.

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/2-open/">open</a></b>(2), <b><a HREF="/docs/linux/man/3-fclose/">fclose</a></b>(3), <b><a HREF="/docs/linux/man/3-fileno/">fileno</a></b>(3), <b><a HREF="/docs/linux/man/3-fmemopen/">fmemopen</a></b>(3), <b><a HREF="/docs/linux/man/3-fopencookie/">fopencookie</a></b>(3), <b><a HREF="/docs/linux/man/3-open_memstream/">open_memstream</a></b>(3)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 

<h2>Index</h2>


