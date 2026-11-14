---
title: "tcl_deletechannelhandler(3)"
name: "tcl_deletechannelhandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_deletechannelhandler/"
description: "Tcl_CreateChannelHandler, Tcl_DeleteChannelHandler – call a procedure when a channel becomes readable or writable"
---

<p>Tcl_CreateChannelHandler, Tcl_DeleteChannelHandler &#8211; call a procedure when a channel becomes readable or writable </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_CreateChannelHandler</code>(<i>channel, mask, proc, clientData</i>)
void
<code>Tcl_DeleteChannelHandler</code>(<i>channel, proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Channel <i>channel</i> (in) Tcl channel such as returned by <code>Tcl_CreateChannel</code>.</p>
<dd>int <i>mask</i> (in) Conditions under which <i>proc</i> should be called: OR-ed combination of <code>TCL_READABLE</code>, <code>TCL_WRITABLE</code> and <code>TCL_EXCEPTION</code>. Specify a zero value to temporarily disable an existing handler.</p>
<dd>Tcl_FileProc <i>*proc</i> (in) Procedure to invoke whenever the channel indicated by <i>channel</i> meets the conditions specified by <i>mask</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateChannelHandler</code> arranges for <i>proc</i> to be called in the future whenever input or output becomes possible on the channel identified by <i>channel</i>, or whenever an exceptional condition exists for <i>channel</i>. The conditions of interest under which <i>proc</i> will be invoked are specified by the <i>mask</i> argument. See the manual entry for <code>fileevent</code> for a precise description of what it means for a channel to be readable or writable. <i>Proc</i> must conform to the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_ChannelProc(
 ClientData <i>clientData</i>,
 int <i>mask</i>);</pre>
</dl>
<p> The <i>clientData</i> argument is the same as the value passed to <code>Tcl_CreateChannelHandler</code> when the handler was created. Typically, <i>clientData</i> points to a data structure containing application-specific information about the channel. <i>Mask</i> is an integer mask indicating which of the requested conditions actually exists for the channel; it will contain a subset of the bits from the <i>mask</i> argument to <code>Tcl_CreateChannelHandler</code> when the handler was created. </p>
<p> Each channel handler is identified by a unique combination of <i>channel</i>, <i>proc</i> and <i>clientData</i>. There may be many handlers for a given channel as long as they do not have the same <i>channel</i>, <i>proc</i>, and <i>clientData</i>. If <code>Tcl_CreateChannelHandler</code> is invoked when there is already a handler for <i>channel</i>, <i>proc</i>, and <i>clientData</i>, then no new handler is created; instead, the <i>mask</i> is changed for the existing handler. </p>
<p> <code>Tcl_DeleteChannelHandler</code> deletes a channel handler identified by <i>channel</i>, <i>proc</i> and <i>clientData</i>; if no such handler exists, the call has no effect. </p>
<p> Channel handlers are invoked via the Tcl event mechanism, so they are only useful in applications that are event-driven. Note also that the conditions specified in the <i>mask</i> argument to <i>proc</i> may no longer exist when <i>proc</i> is invoked: for example, if there are two handlers for <code>TCL_READABLE</code> on the same channel, the first handler could consume all of the available input so that the channel is no longer readable when the second handler is invoked. For this reason it may be useful to use nonblocking I/O on channels for which there are event handlers. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-notifier/">Notifier</a>(3), <a href="/docs/linux/man/3-tcl_createchannel/">Tcl_CreateChannel</a>(3), <a href="/docs/linux/man/3-tcl_openfilechannel/">Tcl_OpenFileChannel</a>(3), <a href="/docs/linux/man/n-vwait/">vwait</a>(n). </p>
<h2>Keywords</h2>
<p>blocking, callback, channel, events, handler, nonblocking.</p>
