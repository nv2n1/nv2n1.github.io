---
title: "tcl_getopenfile(3)"
name: "tcl_getopenfile"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getopenfile/"
description: "Tcl_GetOpenFile – Return a FILE* for a channel registered in the given interpreter (Unix only)"
---

<p>Tcl_GetOpenFile &#8211; Return a FILE* for a channel registered in the given interpreter (Unix only) </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_GetOpenFile</code>(<i>interp, chanID, write, checkUsage, filePtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter from which file handle is to be obtained.</p>
<dd>const char <i>*chanID</i> (in) String identifying channel, such as <code>stdin</code> or <code>file4</code>.</p>
<dd>int <i>write</i> (in) Non-zero means the file will be used for writing, zero means it will be used for reading.</p>
<dd>int <i>checkUsage</i> (in) If non-zero, then an error will be generated if the file was not opened for the access indicated by <i>write</i>.</p>
<dd>ClientData <i>*filePtr</i> (out) Points to word in which to store pointer to FILE structure for the file given by <i>chanID</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_GetOpenFile</code> takes as argument a file identifier of the form returned by the <code>open</code> command and returns at <i>*filePtr</i> a pointer to the FILE structure for the file. The <i>write</i> argument indicates whether the FILE pointer will be used for reading or writing. In some cases, such as a channel that connects to a pipeline of subprocesses, different FILE pointers will be returned for reading and writing. <code>Tcl_GetOpenFile</code> normally returns <code>TCL_OK</code>. If an error occurs in <code>Tcl_GetOpenFile</code> (e.g. <i>chanID</i> did not make any sense or <i>checkUsage</i> was set and the file was not opened for the access specified by <i>write</i>) then <code>TCL_ERROR</code> is returned and the interpreter&#8217;s result will contain an error message. In the current implementation <i>checkUsage</i> is ignored and consistency checks are always performed. </p>
<p> Note that this interface is only supported on the Unix platform. </p>
<h2>Keywords</h2>
<p>channel, file handle, permissions, pipeline, read, write</p>
