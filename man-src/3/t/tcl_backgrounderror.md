---
title: "tcl_backgrounderror(3)"
name: "tcl_backgrounderror"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_backgrounderror/"
description: "Tcl_BackgroundError – report Tcl error that occurred in background processing"
---

<p>Tcl_BackgroundError &#8211; report Tcl error that occurred in background processing </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_BackgroundError</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which the error occurred. </p>
</dl>
<h2>Description</h2>
<p>This procedure is typically invoked when a Tcl error occurs during &#8220;background processing&#8221; such as executing an event handler. When such an error occurs, the error condition is reported to Tcl or to a widget or some other C code, and there is not usually any obvious way for that code to report the error to the user. In these cases the code calls <code>Tcl_BackgroundError</code> with an <i>interp</i> argument identifying the interpreter in which the error occurred. At the time <code>Tcl_BackgroundError</code> is invoked, the interpreter&#8217;s result is expected to contain an error message. <code>Tcl_BackgroundError</code> will invoke the command registered in that interpreter to handle background errors by the <code>interp bgerror</code> command. The registered handler command is meant to report the error in an application-specific fashion. The handler command receives two arguments, the result of the interp, and the return options of the interp at the time the error occurred. If the application registers no handler command, the default handler command will attempt to call <code>bgerror</code> to report the error. If an error condition arises while invoking the handler command, then <code>Tcl_BackgroundError</code> reports the error itself by printing a message on the standard error file. </p>
<p> <code>Tcl_BackgroundError</code> does not invoke the handler command immediately because this could potentially interfere with scripts that are in process at the time the error occurred. Instead, it invokes the handler command later as an idle callback. </p>
<p> It is possible for many background errors to accumulate before the handler command is invoked. When this happens, each of the errors is processed in order. However, if the handle command returns a break exception, then all remaining error reports for the interpreter are skipped. </p>
<h2>Keywords</h2>
<p>background, bgerror, error, interp</p>
