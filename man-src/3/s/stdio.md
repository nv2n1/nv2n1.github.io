---
title: "stdio(3)"
name: "stdio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdio/"
description: "stdio – standard input/output library functions"
---

<p>stdio &#8211; standard input/output library functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;</code></pre>
<p> <code>FILE *</code><i>stdin</i><code>;</code><br />
 <code>FILE *</code><i>stdout</i><code>;</code><br />
 <code>FILE *</code><i>stderr</i><code>;</code></p>
<h2>Description</h2>
<p>The standard I/O library provides a simple and efficient buffered stream I/O interface. Input and output is mapped into logical data streams and the physical I/O characteristics are concealed. The functions and macros are listed below; more information is available from the individual man pages. </p>
<p> A stream is associated with an external file (which may be a physical device) by <i>opening</i> a file, which may involve creating a new file. Creating an existing file causes its former contents to be discarded. If a file can support positioning requests (such as a disk file, as opposed to a terminal), then a <i>file position indicator</i> associated with the stream is positioned at the start of the file (byte zero), unless the file is opened with append mode. If append mode is used, it is unspecified whether the position indicator will be placed at the start or the end of the file. The position indicator is maintained by subsequent reads, writes and positioning requests. All input occurs as if the characters were read by successive calls to the <code><a href="/docs/linux/man/3-fgetc/">fgetc</a></code>(3) function; all output takes place as if all characters were written by successive calls to the <code><a href="/docs/linux/man/3-fputc/">fputc</a></code>(3) function. </p>
<p> A file is disassociated from a stream by <i>closing</i> the file. Output streams are flushed (any unwritten buffer contents are transferred to the host environment) before the stream is disassociated from the file. The value of a pointer to a <i>FILE</i> object is indeterminate after a file is closed (garbage). </p>
<p> A file may be subsequently reopened, by the same or another program execution, and its contents reclaimed or modified (if it can be repositioned at the start). If the main function returns to its original caller, or the <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) function is called, all open files are closed (hence all output streams are flushed) before program termination. Other methods of program termination, such as <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3) do not bother about closing files properly. </p>
<p> At program startup, three text streams are predefined and need not be opened explicitly: <i>standard input</i> (for reading conventional input), <i>standard output</i> (for writing conventional output), and <i>standard error</i> (for writing diagnostic output). These streams are abbreviated <i>stdin</i>, <i>stdout</i>, and <i>stderr</i>. When opened, the standard error stream is not fully buffered; the standard input and output streams are fully buffered if and only if the streams do not refer to an interactive device. </p>
<p> Output streams that refer to terminal devices are always line buffered by default; pending output to such streams is written automatically whenever an input stream that refers to a terminal device is read. In cases where a large amount of computation is done after printing part of a line on an output terminal, it is necessary to <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3) the standard output before going off and computing so that the output will appear. </p>
<p> The <i>stdio</i> library is a part of the library <code>libc</code> and routines are automatically loaded as needed by <code><a href="/docs/linux/man/1-cc/">cc</a></code>(1). The SYNOPSIS sections of the following manual pages indicate which include files are to be used, what the compiler declaration for the function looks like and which external variables are of interest. </p>
<p> The following are defined as macros; these names may not be reused without first removing their current definitions with <code>#undef</code>: <code>BUFSIZ</code>, <code>EOF</code>, <code>FILENAME_MAX</code>, <code>FOPEN_MAX</code>, <code>L_cuserid</code>, <code>L_ctermid</code>, <code>L_tmpnam</code>, <code>NULL</code>, <code>SEEK_END</code>, <code>SEEK_SET</code>, <code>SEEK_CUR</code>, <code>TMP_MAX</code>, <code>clearerr</code>, <code>feof</code>, <code>ferror</code>, <code>fileno</code>, <code>getc</code>, <code>getchar</code>, <code>putc</code>, <code>putchar</code>, <code>stderr</code>, <code>stdin</code>, <code>stdout</code>. Function versions of the macro functions <code>feof</code>, <code>ferror</code>, <code>clearerr</code>, <code>fileno</code>, <code>getc</code>, <code>getchar</code>, <code>putc</code>, and <code>putchar</code> exist and will be used if the macros definitions are explicitly removed.</p>
<h3>List of functions</h3>
<table>
<tr VALIGN=top>
<td><code>Function</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-clearerr/">clearerr</a></code>(3)</td>
<td>check and reset stream status
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3)</td>
<td>close a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fdopen/">fdopen</a></code>(3)</td>
<td>stream open functions
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-feof/">feof</a></code>(3)</td>
<td>check and reset stream status
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3)</td>
<td>check and reset stream status
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3)</td>
<td>flush a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fgetc/">fgetc</a></code>(3)</td>
<td>get next character or word from input stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fgetpos/">fgetpos</a></code>(3)</td>
<td>reposition a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3)</td>
<td>get a line from a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fileno/">fileno</a></code>(3)</td>
<td>return the integer descriptor of the argument stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3)</td>
<td>stream open functions
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3)</td>
<td>formatted output conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fpurge/">fpurge</a></code>(3)</td>
<td>flush a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fputc/">fputc</a></code>(3)</td>
<td>output a character or word to a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fputs/">fputs</a></code>(3)</td>
<td>output a line to a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fread/">fread</a></code>(3)</td>
<td>binary stream input/output
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-freopen/">freopen</a></code>(3)</td>
<td>stream open functions
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fscanf/">fscanf</a></code>(3)</td>
<td>input format conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3)</td>
<td>reposition a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fsetpos/">fsetpos</a></code>(3)</td>
<td>reposition a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-ftell/">ftell</a></code>(3)</td>
<td>reposition a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3)</td>
<td>binary stream input/output
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-getc/">getc</a></code>(3)</td>
<td>get next character or word from input stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-getchar/">getchar</a></code>(3)</td>
<td>get next character or word from input stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-gets/">gets</a></code>(3)</td>
<td>get a line from a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-getw/">getw</a></code>(3)</td>
<td>get next character or word from input stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3)</td>
<td>make temporary filename (unique)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-perror/">perror</a></code>(3)</td>
<td>system error messages
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)</td>
<td>formatted output conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-putc/">putc</a></code>(3)</td>
<td>output a character or word to a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-putchar/">putchar</a></code>(3)</td>
<td>output a character or word to a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-puts/">puts</a></code>(3)</td>
<td>output a line to a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-putw/">putw</a></code>(3)</td>
<td>output a character or word to a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-remove/">remove</a></code>(3)</td>
<td>remove directory entry
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-rewind/">rewind</a></code>(3)</td>
<td>reposition a stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3)</td>
<td>input format conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3)</td>
<td>stream buffering operations
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-setbuffer/">setbuffer</a></code>(3)</td>
<td>stream buffering operations
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-setlinebuf/">setlinebuf</a></code>(3)</td>
<td>stream buffering operations
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-setvbuf/">setvbuf</a></code>(3)</td>
<td>stream buffering operations
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3)</td>
<td>formatted output conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sscanf/">sscanf</a></code>(3)</td>
<td>input format conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</td>
<td>system error messages
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sys_errlist/">sys_errlist</a></code>(3)</td>
<td>system error messages
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sys_nerr/">sys_nerr</a></code>(3)</td>
<td>system error messages
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3)</td>
<td>temporary file routines
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3)</td>
<td>temporary file routines
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3)</td>
<td>temporary file routines
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-ungetc/">ungetc</a></code>(3)</td>
<td>un-get character from input stream
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-vfprintf/">vfprintf</a></code>(3)</td>
<td>formatted output conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-vfscanf/">vfscanf</a></code>(3)</td>
<td>input format conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3)</td>
<td>formatted output conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-vscanf/">vscanf</a></code>(3)</td>
<td>input format conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3)</td>
<td>formatted output conversion
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-vsscanf/">vsscanf</a></code>(3)</td>
<td>input format conversion
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The <i>stdio</i> library conforms to C89.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-stdout/">stdout</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
