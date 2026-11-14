---
title: "fgetln(3)"
name: "fgetln"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetln/"
description: "fgetln – get a line from a stream"
---

<h2 class="name">NAME</h2>
<p> <code>fgetln</code> &#8211; get a line from a stream </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/stdio.h Ft char * Fn fgetln FILE *stream size_t *len</p>
<h2>DESCRIPTION</h2>
<p> The Fn fgetln function returns a pointer to the next line from the stream referenced by Fa stream . This line is <i>not</i> a C string as it does not end with a terminating <code>NUL</code> character. The length of the line, including the final newline, is stored in the memory location to which Fa len points and is guaranteed to be greater than 0 upon successful completion. (Note, however, that if the line is the last in a file that does not end in a newline, the returned text will not contain a newline.)</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion a pointer is returned; this pointer becomes invalid after the next <code>I/O</code> operation on Fa stream (whether successful or not) or as soon as the stream is closed. Otherwise, <code>NULL</code> is returned. The Fn fgetln function does not distinguish between end-of-file and error; the routines <a href="/docs/linux/man/3-feof/">feof</a>(3) and <a href="/docs/linux/man/3-ferror/">ferror</a>(3) must be used to determine which occurred. If an error occurs, the global variable <i>errno</i> is set to indicate the error. The end-of-file condition is remembered, even on a terminal, and all subsequent attempts to read will return <code>NULL</code> until the condition is cleared with <a href="/docs/linux/man/3-clearerr/">clearerr</a>(3). </p>
<p> The text to which the returned pointer points may be modified, provided that no changes are made beyond the returned size. These changes are lost as soon as the pointer becomes invalid.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>Bq </code>Er EBADF</p>
<dd> The argument Fa stream is not a stream open for reading.</dl>
<p> The Fn fgetln function may also fail and set <i>errno</i> for any of the errors specified for the routines <a href="/docs/linux/man/3-fflush/">fflush</a>(3), <a href="/docs/linux/man/3-malloc/">malloc</a>(3), <a href="/docs/linux/man/2-read/">read</a>(2), <a href="/docs/linux/man/2-stat/">stat</a>(2), or <a href="/docs/linux/man/3-realloc/">realloc</a>(3).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ferror/">ferror</a>(3), <a href="/docs/linux/man/3-fgets/">fgets</a>(3), <a href="/docs/linux/man/3-fgetwln/">fgetwln</a>(3), <a href="/docs/linux/man/3-fopen/">fopen</a>(3), <a href="/docs/linux/man/3-putc/">putc</a>(3)</p>
<h2>HISTORY</h2>
<p> The Fn fgetln function first appeared in BSD 4.4 </p>
<h2>Index</h2>
