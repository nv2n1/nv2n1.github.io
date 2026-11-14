---
title: "tcl_geterrno(3)"
name: "tcl_geterrno"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_geterrno/"
description: "Tcl_SetErrno, Tcl_GetErrno, Tcl_ErrnoId, Tcl_ErrnoMsg – manipulate errno to store and retrieve error codes"
---

<p>Tcl_SetErrno, Tcl_GetErrno, Tcl_ErrnoId, Tcl_ErrnoMsg &#8211; manipulate errno to store and retrieve error codes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_SetErrno</code>(<i>errorCode</i>)
int
<code>Tcl_GetErrno</code>()
const char *
<code>Tcl_ErrnoId</code>()
const char *
<code>Tcl_ErrnoMsg</code>(<i>errorCode</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>errorCode</i> (in) A POSIX error code such as <code>ENOENT</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_SetErrno</code> and <code>Tcl_GetErrno</code> provide portable access to the <code>errno</code> variable, which is used to record a POSIX error code after system calls and other operations such as <code>Tcl_Gets</code>. These procedures are necessary because global variable accesses cannot be made across module boundaries on some platforms. </p>
<p> <code>Tcl_SetErrno</code> sets the <code>errno</code> variable to the value of the <i>errorCode</i> argument C procedures that wish to return error information to their callers via <code>errno</code> should call <code>Tcl_SetErrno</code> rather than setting <code>errno</code> directly. </p>
<p> <code>Tcl_GetErrno</code> returns the current value of <code>errno</code>. Procedures wishing to access <code>errno</code> should call this procedure instead of accessing <code>errno</code> directly. </p>
<p> <code>Tcl_ErrnoId</code> and <code>Tcl_ErrnoMsg</code> return string representations of <code>errno</code> values. <code>Tcl_ErrnoId</code> returns a machine-readable textual identifier such as &#8220;EACCES&#8221; that corresponds to the current value of <code>errno</code>. <code>Tcl_ErrnoMsg</code> returns a human-readable string such as &#8220;permission denied&#8221; that corresponds to the value of its <i>errorCode</i> argument. The <i>errorCode</i> argument is typically the value returned by <code>Tcl_GetErrno</code>. The strings returned by these functions are statically allocated and the caller must not free or modify them. </p>
<h2>Keywords</h2>
<p>errno, error code, global variables</p>
