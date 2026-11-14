---
title: "tcl_createclosehandler(3)"
name: "tcl_createclosehandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createclosehandler/"
description: "Tcl_CreateCloseHandler, Tcl_DeleteCloseHandler – arrange for callbacks when channels are closed"
---

<p>Tcl_CreateCloseHandler, Tcl_DeleteCloseHandler &#8211; arrange for callbacks when channels are closed </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_CreateCloseHandler</code>(<i>channel, proc, clientData</i>)
void
<code>Tcl_DeleteCloseHandler</code>(<i>channel, proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Channel <i>channel</i> (in) The channel for which to create or delete a close callback.</p>
<dd>Tcl_CloseProc <i>*proc</i> (in) The procedure to call as the callback.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateCloseHandler</code> arranges for <i>proc</i> to be called when <i>channel</i> is closed with <code>Tcl_Close</code> or <code>Tcl_UnregisterChannel</code>, or using the Tcl <code>close</code> command. <i>Proc</i> should match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_CloseProc(
 ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> is the same as the value provided in the call to <code>Tcl_CreateCloseHandler</code>. </p>
<p> <code>Tcl_DeleteCloseHandler</code> removes a close callback for <i>channel</i>. The <i>proc</i> and <i>clientData</i> identify which close callback to remove; <code>Tcl_DeleteCloseHandler</code> does nothing if its <i>proc</i> and <i>clientData</i> arguments do not match the <i>proc</i> and <i>clientData</i> for a close handler for <i>channel</i>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-close/">close</a>(n), <a href="/docs/linux/man/3-tcl_close/">Tcl_Close</a>(3), <a href="/docs/linux/man/3-tcl_unregisterchannel/">Tcl_UnregisterChannel</a>(3) </p>
<h2>Keywords</h2>
<p>callback, channel closing</p>
