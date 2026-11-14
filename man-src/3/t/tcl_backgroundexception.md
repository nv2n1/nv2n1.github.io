---
title: "tcl_backgroundexception(3)"
name: "tcl_backgroundexception"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_backgroundexception/"
description: "Tcl_BackgroundException, Tcl_BackgroundError – report Tcl exception that occurred in background processing"
---

<p>Tcl_BackgroundException, Tcl_BackgroundError &#8211; report Tcl exception that occurred in background processing </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_BackgroundException</code>(<i>interp, code</i>)
<code>Tcl_BackgroundError</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which the exception occurred.</p>
<dd>int <i>code</i> (in) The exceptional return code to be reported. </p>
</dl>
<h2>Description</h2>
<p>This procedure is typically invoked when a Tcl exception (any return code other than TCL_OK) occurs during &#8220;background processing&#8221; such as executing an event handler. When such an exception occurs, the condition is reported to Tcl or to a widget or some other C code, and there is not usually any obvious way for that code to report the exception to the user. In these cases the code calls <code>Tcl_BackgroundException</code> with an <i>interp</i> argument identifying the interpreter in which the exception occurred, and a <i>code</i> argument holding the return code value of the exception. The state of the interpreter, including any error message in the interpreter result, and the values of any entries in the return options dictionary, is captured and saved. <code>Tcl_BackgroundException</code> then arranges for the event loop to invoke at some later time the command registered in that interpreter to handle background errors by the <code>interp bgerror</code> command, passing the captured values as arguments. The registered handler command is meant to report the exception in an application-specific fashion. The handler command receives two arguments, the result of the interp, and the return options of the interp at the time the error occurred. If the application registers no handler command, the default handler command will attempt to call <code>bgerror</code> to report the error. If an error condition arises while invoking the handler command, then <code>Tcl_BackgroundException</code> reports the error itself by printing a message on the standard error file. </p>
<p> <code>Tcl_BackgroundException</code> does not invoke the handler command immediately because this could potentially interfere with scripts that are in process at the time the error occurred. Instead, it invokes the handler command later as an idle callback. </p>
<p> It is possible for many background exceptions to accumulate before the handler command is invoked. When this happens, each of the exceptions is processed in order. However, if the handler command returns a break exception, then all remaining error reports for the interpreter are skipped. </p>
<p> The <code>Tcl_BackgroundError</code> routine is an older and simpler interface useful when the exception code reported is <code>TCL_ERROR</code>. It is equivalent to: </p>
<dl COMPACT>
<dd>
<pre>Tcl_BackgroundException(interp, TCL_ERROR);</pre>
</dl>
<h2>Keywords</h2>
<p>background, bgerror, error, interp</p>
