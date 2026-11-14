---
title: "tcl_createfilehandler(3)"
name: "tcl_createfilehandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createfilehandler/"
description: "Tcl_CreateFileHandler, Tcl_DeleteFileHandler – associate procedure callbacks with files or devices (Unix only)"
---

<p>Tcl_CreateFileHandler, Tcl_DeleteFileHandler &#8211; associate procedure callbacks with files or devices (Unix only) </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_CreateFileHandler</code>(<i>fd, mask, proc, clientData</i>)
<code>Tcl_DeleteFileHandler</code>(<i>fd</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>fd</i> (in) Unix file descriptor for an open file or device.</p>
<dd>int <i>mask</i> (in) Conditions under which <i>proc</i> should be called: OR-ed combination of <code>TCL_READABLE</code>, <code>TCL_WRITABLE</code>, and <code>TCL_EXCEPTION</code>. May be set to 0 to temporarily disable a handler.</p>
<dd>Tcl_FileProc <i>*proc</i> (in) Procedure to invoke whenever the file or device indicated by <i>file</i> meets the conditions specified by <i>mask</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateFileHandler</code> arranges for <i>proc</i> to be invoked in the future whenever I/O becomes possible on a file or an exceptional condition exists for the file. The file is indicated by <i>fd</i>, and the conditions of interest are indicated by <i>mask</i>. For example, if <i>mask</i> is <code>TCL_READABLE</code>, <i>proc</i> will be called when the file is readable. The callback to <i>proc</i> is made by <code>Tcl_DoOneEvent</code>, so <code>Tcl_CreateFileHandler</code> is only useful in programs that dispatch events through <code>Tcl_DoOneEvent</code> or through Tcl commands such as <code>vwait</code>. </p>
<p> <i>Proc</i> should have arguments and result that match the type <code>Tcl_FileProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_FileProc(
 ClientData <i>clientData</i>,
 int <i>mask</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tcl_CreateFileHandler</code> when the callback was created. Typically, <i>clientData</i> points to a data structure containing application-specific information about the file. <i>Mask</i> is an integer mask indicating which of the requested conditions actually exists for the file; it will contain a subset of the bits in the <i>mask</i> argument to <code>Tcl_CreateFileHandler</code>. </p>
<p> There may exist only one handler for a given file at a given time. If <code>Tcl_CreateFileHandler</code> is called when a handler already exists for <i>fd</i>, then the new callback replaces the information that was previously recorded. </p>
<p> <code>Tcl_DeleteFileHandler</code> may be called to delete the file handler for <i>fd</i>; if no handler exists for the file given by <i>fd</i> then the procedure has no effect. </p>
<p> The purpose of file handlers is to enable an application to respond to events while waiting for files to become ready for I/O. For this to work correctly, the application may need to use non-blocking I/O operations on the files for which handlers are declared. Otherwise the application may block if it reads or writes too much data; while waiting for the I/O to complete the application will not be able to service other events. Use <code>Tcl_SetChannelOption</code> with <code>-blocking</code> to set the channel into blocking or nonblocking mode as required. </p>
<p> Note that these interfaces are only supported by the Unix implementation of the Tcl notifier. </p>
<h2>Keywords</h2>
<p>callback, file, handler</p>
