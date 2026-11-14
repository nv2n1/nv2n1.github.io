---
title: "compile_et(1)"
name: "compile_et"
section: "1"
letter: "c"
url: "/docs/linux/man/1-compile_et/"
description: "compile_et – error table compiler"
---

<h2>NAME</h2>
<p> compile_et &#8211; error table compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>compile_et</code> file</p>
<h2>DESCRIPTION</h2>
<p> <code>Compile_et</code> converts a table listing error-code names and associated messages into a C source file suitable for use with the <i><a href="/docs/linux/man/3-com_err/">com_err</a></i>(3) library. </p>
<p> The source file name must end with a suffix of &#8220;.et&#8221;; the file consists of a declaration supplying the name (up to four characters long) of the error-code table: </p>
<p> <code>error_table</code> <i>name</i> </p>
<p> followed by up to 256 entries of the form: </p>
<p> <code>error_code</code> <i>name,</i> &quot; <i>string</i> &quot; </p>
<p> and a final </p>
<p> <code>end</code> </p>
<p> to indicate the end of the table. </p>
<p> The name of the table is used to construct the name of a subroutine <i>initialize_XXXX_error_table</i> which must be called in order for the <i>com_err</i> library to recognize the error table. </p>
<p> The various error codes defined are assigned sequentially increasing numbers (starting with a large number computed as a hash function of the name of the table); thus for compatibility it is suggested that new codes be added only to the end of an existing table, and that no codes be removed from tables. </p>
<p> The names defined in the table are placed into a C header file with preprocessor directives defining them as integer constants of up to 32 bits in magnitude. </p>
<p> A C source file is also generated which should be compiled and linked with the object files which reference these error codes; it contains the text of the messages and the initialization subroutine. Both C files have names derived from that of the original source file, with the &#8220;.et&#8221; suffix replaced by &#8220;.c&#8221; and &#8220;.h&#8221;. </p>
<p> A &#8220;#&#8221; in the source file is treated as a comment character, and all remaining text to the end of the source line will be ignored. </p>
<h2>BUGS</h2>
<p> Since the original <code>compile_et</code> uses a very simple parser based on <i><a href="/docs/linux/man/1-yacc/">yacc</a></i>(1), and this current version of <code>compile_et</code> uses an awk/sed combination of scripts, its error recovery leaves much to be desired. </p>
<h2>SEE ALSO</h2>
<p> com_err (3). </p>
<p> Ken Raeburn, &quot;A Common Error Description Library for UNIX&quot;. </p>
<h2>Index</h2>
