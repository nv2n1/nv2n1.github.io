---
title: "tcl_chdir(3)"
name: "tcl_chdir"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_chdir/"
description: "Tcl_GetCwd, Tcl_Chdir – manipulate the current working directory"
---

<p>Tcl_GetCwd, Tcl_Chdir &#8211; manipulate the current working directory </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
char *
<code>Tcl_GetCwd</code>(<i>interp</i>, <i>bufferPtr</i>)
int
<code>Tcl_Chdir</code>(<i>path</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to report an error, if any.</p>
<dd>Tcl_DString <i>*bufferPtr</i> (in/out) This dynamic string is used to store the current working directory. At the time of the call it should be uninitialized or free. The caller must eventually call <code>Tcl_DStringFree</code> to free up anything stored here.</p>
<dd>char <i>*path</i> (in) File path in UTF-8 format. </p>
</dl>
<h2>Description</h2>
<p>These procedures may be used to manipulate the current working directory for the application. They provide C-level access to the same functionality as the Tcl <code>pwd</code> command. </p>
<p> <code>Tcl_GetCwd</code> returns a pointer to a string specifying the current directory, or NULL if the current directory could not be determined. If NULL is returned, an error message is left in the <i>interp</i>&#8216;s result. Storage for the result string is allocated in bufferPtr; the caller must call <code>Tcl_DStringFree()</code> when the result is no longer needed. The format of the path is UTF-8. </p>
<p> <code>Tcl_Chdir</code> changes the applications current working directory to the value specified in <i>path</i>. The format of the passed in string must be UTF-8. The function returns -1 on error or 0 on success. </p>
<h2>Keywords</h2>
<p>pwd</p>
