---
title: "fparseln(3)"
name: "fparseln"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fparseln/"
description: "fparseln – return the next logical line from a stream"
---

<h2 class="name">NAME</h2>
<p> <code>fparseln</code> &#8211; return the next logical line from a stream </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/stdio.h Ft char * Fo fparseln Fa FILE *stream size_t *len size_t *lineno Fa const char delim[3] int flags Fc</p>
<h2>DESCRIPTION</h2>
<p> The Fn fparseln function returns a pointer to the next logical line from the stream referenced by Fa stream . This string is <code>NUL</code> terminated and it is dynamically allocated on each invocation. It is the responsibility of the caller to free the pointer. </p>
<p> By default, if a character is escaped, both it and the preceding escape character will be present in the returned string. Various Fa flags alter this behaviour. </p>
<p> The meaning of the arguments is as follows:</p>
<dl>
<dt><code>Fa </code>stream</p>
<dd> The stream to read from.</p>
<dt><code>Fa </code>len</p>
<dd> If not <code>NULL</code> the length of the string is stored in the memory location to which it points.</p>
<dt><code>Fa </code>lineno</p>
<dd> If not <code>NULL</code> the value of the memory location to which is pointed to, is incremented by the number of lines actually read from the file.</p>
<dt><code>Fa </code>delim</p>
<dd> Contains the escape, continuation, and comment characters. If a character is <code>NUL</code> then processing for that character is disabled. If <code>NULL</code> all characters default to values specified below. The contents of Fa delim is as follows:</p>
<dl>
<dt><code>Fa </code>delim[0]</p>
<dd> The escape character, which defaults to <code>\</code> is used to remove any special meaning from the next character.</p>
<dt><code>Fa </code>delim[1]</p>
<dd> The continuation character, which defaults to <code>\</code> is used to indicate that the next line should be concatenated with the current one if this character is the last character on the current line and is not escaped.</p>
<dt><code>Fa </code>delim[2]</p>
<dd> The comment character, which defaults to <code>#</code> if not escaped indicates the beginning of a comment that extends until the end of the current line.</dl>
<dt><code>Fa </code>flags</p>
<dd> If non-zero, alter the operation of Fn fparseln . The various flags, which may be <i>or </i><code>-ed</code> together, are:</p>
<dl>
<dt><code>FPARSELN_UNESCCOMM</code></p>
<dd> Remove escape preceding an escaped comment.</p>
<dt><code>FPARSELN_UNESCCONT</code></p>
<dd> Remove escape preceding an escaped continuation.</p>
<dt><code>FPARSELN_UNESCESC</code></p>
<dd> Remove escape preceding an escaped escape.</p>
<dt><code>FPARSELN_UNESCREST</code></p>
<dd> Remove escape preceding any other character.</p>
<dt><code>FPARSELN_UNESCALL</code></p>
<dd> All of the above.</dl>
</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion a pointer to the parsed line is returned; otherwise, <code>NULL</code> is returned. </p>
<p> The Fn fparseln function uses internally <a href="/docs/linux/man/3-fgetln/">fgetln</a>(3), so all error conditions that apply to <a href="/docs/linux/man/3-fgetln/">fgetln</a>(3), apply to Fn fparseln . In addition Fn fparseln may set <i>errno</i> to Bq Er ENOMEM and return <code>NULL</code> if it runs out of memory.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-fgetln/">fgetln</a>(3)</p>
<h2>HISTORY</h2>
<p> The Fn fparseln function first appeared in Nx 1.4 . </p>
<h2>Index</h2>
