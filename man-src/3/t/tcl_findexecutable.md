---
title: "tcl_findexecutable(3)"
name: "tcl_findexecutable"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_findexecutable/"
description: "Tcl_FindExecutable, Tcl_GetNameOfExecutable – identify or return the name of the binary file containing the application"
---

<p>Tcl_FindExecutable, Tcl_GetNameOfExecutable &#8211; identify or return the name of the binary file containing the application </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_FindExecutable</code>(<i>argv0</i>)
const char *
<code>Tcl_GetNameOfExecutable</code>()</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>char <i>*argv0</i> (in) The first command-line argument to the program, which gives the application&#8217;s name. </p>
</dl>
<h2>Description</h2>
<p>The <code>Tcl_FindExecutable</code> procedure computes the full path name of the executable file from which the application was invoked and saves it for Tcl&#8217;s internal use. The executable&#8217;s path name is needed for several purposes in Tcl. For example, it is needed on some platforms in the implementation of the <code>load</code> command. It is also returned by the <code>info nameofexecutable</code> command. </p>
<p> On UNIX platforms this procedure is typically invoked as the very first thing in the application&#8217;s main program; it must be passed <i>argv[0]</i> as its argument. It is important not to change the working directory before the invocation. <code>Tcl_FindExecutable</code> uses <i>argv0</i> along with the <code>PATH</code> environment variable to find the application&#8217;s executable, if possible. If it fails to find the binary, then future calls to <code>info nameofexecutable</code> will return an empty string. </p>
<p> <code>Tcl_GetNameOfExecutable</code> simply returns a pointer to the internal full path name of the executable file as computed by <code>Tcl_FindExecutable</code>. This procedure call is the C API equivalent to the <code>info nameofexecutable</code> command. NULL is returned if the internal full path name has not been computed or unknown. </p>
<h2>Keywords</h2>
<p>binary, executable file</p>
