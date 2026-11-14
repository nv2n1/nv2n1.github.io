---
title: "tk_deleteerrorhandler(3)"
name: "tk_deleteerrorhandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_deleteerrorhandler/"
description: "Tk_CreateErrorHandler, Tk_DeleteErrorHandler – handle X protocol errors"
---

<p>Tk_CreateErrorHandler, Tk_DeleteErrorHandler &#8211; handle X protocol errors </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_ErrorHandler
<code>Tk_CreateErrorHandler</code>(<i>display, error, request, minor, proc, clientData</i>)
<code>Tk_DeleteErrorHandler</code>(<i>handler</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Display <i>*display</i> (in) Display whose errors are to be handled.</p>
<dd>int <i>error</i> (in) Match only error events with this value in the <i>error_code</i> field. If -1, then match any <i>error_code</i> value.</p>
<dd>int <i>request</i> (in) Match only error events with this value in the <i>request_code</i> field. If -1, then match any <i>request_code</i> value.</p>
<dd>int <i>minor</i> (in) Match only error events with this value in the <i>minor_code</i> field. If -1, then match any <i>minor_code</i> value.</p>
<dd>Tk_ErrorProc <i>*proc</i> (in) Procedure to invoke whenever an error event is received for <i>display</i> and matches <i>error</i>, <i>request</i>, and <i>minor</i>. NULL means ignore any matching errors.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>.</p>
<dd>Tk_ErrorHandler <i>handler</i> (in) Token for error handler to delete (return value from a previous call to <code>Tk_CreateErrorHandler</code>).
</dl>
<h2>Description</h2>
<p><code>Tk_CreateErrorHandler</code> arranges for a particular procedure (<i>proc</i>) to be called whenever certain protocol errors occur on a particular display (<i>display</i>). Protocol errors occur when the X protocol is used incorrectly, such as attempting to map a window that does not exist. See the Xlib documentation for <code>XSetErrorHandler</code> for more information on the kinds of errors that can occur. For <i>proc</i> to be invoked to handle a particular error, five things must occur:</p>
<dl COMPACT>
<dt>[1]</p>
<dd>The error must pertain to <i>display</i>.</p>
<dt>[2]</p>
<dd>Either the <i>error</i> argument to <code>Tk_CreateErrorHandler</code> must have been -1, or the <i>error</i> argument must match the <i>error_code</i> field from the error event.</p>
<dt>[3]</p>
<dd>Either the <i>request</i> argument to <code>Tk_CreateErrorHandler</code> must have been -1, or the <i>request</i> argument must match the <i>request_code</i> field from the error event.</p>
<dt>[4]</p>
<dd>Either the <i>minor</i> argument to <code>Tk_CreateErrorHandler</code> must have been -1, or the <i>minor</i> argument must match the <i>minor_code</i> field from the error event.</p>
<dt>[5]</p>
<dd>The protocol request to which the error pertains must have been made when the handler was active (see below for more information).</dl>
<p> <i>Proc</i> should have arguments and result that match the following type:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ErrorProc(
 ClientData <i>clientData</i>,
 XErrorEvent *<i>errEventPtr</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tcl_CreateErrorHandler</code> when the callback was created. Typically, <i>clientData</i> points to a data structure containing application-specific information that is needed to deal with the error. <i>ErrEventPtr</i> is a pointer to the X error event. The procedure <i>proc</i> should return an integer value. If it returns 0 it means that <i>proc</i> handled the error completely and there is no need to take any other action for the error. If it returns non-zero it means <i>proc</i> was unable to handle the error. </p>
<p> If a value of NULL is specified for <i>proc</i>, all matching errors will be ignored: this will produce the same result as if a procedure had been specified that always returns 0. </p>
<p> If more than more than one handler matches a particular error, then they are invoked in turn. The handlers will be invoked in reverse order of creation: most recently declared handler first. If any handler returns 0, then subsequent (older) handlers will not be invoked. If no handler returns 0, then Tk invokes X&#8217;s default error handler, which prints an error message and aborts the program. If you wish to have a default handler that deals with errors that no other handler can deal with, then declare it first. </p>
<p> The X documentation states that &#8220;the error handler should not call any functions (directly or indirectly) on the display that will generate protocol requests or that will look for input events.&#8221; This restriction applies to handlers declared by <code>Tk_CreateErrorHandler</code>; disobey it at your own risk. </p>
<p> <code>Tk_DeleteErrorHandler</code> may be called to delete a previously-created error handler. The <i>handler</i> argument identifies the error handler, and should be a value returned by a previous call to <code>Tk_CreateEventHandler</code>. </p>
<p> A particular error handler applies to errors resulting from protocol requests generated between the call to <code>Tk_CreateErrorHandler</code> and the call to <code>Tk_DeleteErrorHandler</code>. However, the actual callback to <i>proc</i> may not occur until after the <code>Tk_DeleteErrorHandler</code> call, due to buffering in the client and server. If an error event pertains to a protocol request made just before calling <code>Tk_DeleteErrorHandler</code>, then the error event may not have been processed before the <code>Tk_DeleteErrorHandler</code> call. When this situation arises, Tk will save information about the handler and invoke the handler&#8217;s <i>proc</i> later when the error event finally arrives. If an application wishes to delete an error handler and know for certain that all relevant errors have been processed, it should first call <code>Tk_DeleteErrorHandler</code> and then call <code>XSync</code>; this will flush out any buffered requests and errors, but will result in a performance penalty because it requires communication to and from the X server. After the <code>XSync</code> call Tk is guaranteed not to call any error handlers deleted before the <code>XSync</code> call. </p>
<p> For the Tk error handling mechanism to work properly, it is essential that application code never calls <code>XSetErrorHandler</code> directly; applications should use only <code>Tk_CreateErrorHandler</code>. </p>
<h2>Keywords</h2>
<p>callback, error, event, handler</p>
