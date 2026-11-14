---
title: "tcl_gettopchannel(3)"
name: "tcl_gettopchannel"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_gettopchannel/"
description: "Tcl_StackChannel, Tcl_UnstackChannel, Tcl_GetStackedChannel, Tcl_GetTopChannel – manipulate stacked I/O channels"
---

<p>Tcl_StackChannel, Tcl_UnstackChannel, Tcl_GetStackedChannel, Tcl_GetTopChannel &#8211; manipulate stacked I/O channels </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Channel
<code>Tcl_StackChannel</code>(<i>interp, typePtr, clientData, mask, channel</i>)
int
<code>Tcl_UnstackChannel</code>(<i>interp, channel</i>)
Tcl_Channel
<code>Tcl_GetStackedChannel</code>(<i>channel</i>)
Tcl_Channel
<code>Tcl_GetTopChannel</code>(<i>channel</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter for error reporting.</p>
<dd>Tcl_ChannelType <i>*typePtr</i> (in) The new channel I/O procedures to use for <i>channel</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to channel I/O procedures.</p>
<dd>int <i>mask</i> (in) Conditions under which <i>channel</i> will be used: OR-ed combination of <code>TCL_READABLE</code>, <code>TCL_WRITABLE</code> and <code>TCL_EXCEPTION</code>. This can be a subset of the operations currently allowed on <i>channel</i>.</p>
<dd>Tcl_Channel <i>channel</i> (in) An existing Tcl channel such as returned by <code>Tcl_CreateChannel</code>. </p>
</dl>
<h2>Description</h2>
<p>These functions are for use by extensions that add processing layers to Tcl I/O channels. Examples include compression and encryption modules. These functions transparently stack and unstack a new channel on top of an existing one. Any number of channels can be stacked together. </p>
<p> The implementation of the Tcl channel code was rewritten in 8.3.2 to correct some problems with the previous implementation with regard to stacked channels. Anyone using stacked channels or creating stacked channel drivers should update to the new <code>TCL_CHANNEL_VERSION_2</code> <code>Tcl_ChannelType</code> structure. See <code>Tcl_CreateChannel</code> for details. </p>
<p> <code>Tcl_StackChannel</code> stacks a new <i>channel</i> on an existing channel with the same name that was registered for <i>channel</i> by <code>Tcl_RegisterChannel</code>. </p>
<p> <code>Tcl_StackChannel</code> works by creating a new channel structure and placing itself on top of the channel stack. EOL translation, encoding and buffering options are shared between all channels in the stack. The hidden channel does no buffering, newline translations, or character set encoding. Instead, the buffering, newline translations, and encoding functions all remain at the top of the channel stack. A pointer to the new top channel structure is returned. If an error occurs when stacking the channel, NULL is returned instead. </p>
<p> The <i>mask</i> parameter specifies the operations that are allowed on the new channel. These can be a subset of the operations allowed on the original channel. For example, a read-write channel may become read-only after the <code>Tcl_StackChannel</code> call. </p>
<p> Closing a channel closes the channels stacked below it. The close of stacked channels is executed in a way that allows buffered data to be properly flushed. </p>
<p> <code>Tcl_UnstackChannel</code> reverses the process. The old channel is associated with the channel name, and the processing module added by <code>Tcl_StackChannel</code> is destroyed. If there is no old channel, then <code>Tcl_UnstackChannel</code> is equivalent to <code>Tcl_Close</code>. If an error occurs unstacking the channel, <code>TCL_ERROR</code> is returned, otherwise <code>TCL_OK</code> is returned. </p>
<p> <code>Tcl_GetTopChannel</code> returns the top channel in the stack of channels the supplied channel is part of. </p>
<p> <code>Tcl_GetStackedChannel</code> returns the channel in the stack of channels which is just below the supplied channel. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-notifier/">Notifier</a>(3), <a href="/docs/linux/man/3-tcl_createchannel/">Tcl_CreateChannel</a>(3), <a href="/docs/linux/man/3-tcl_openfilechannel/">Tcl_OpenFileChannel</a>(3), <a href="/docs/linux/man/n-vwait/">vwait</a>(n). </p>
<h2>Keywords</h2>
<p>channel, compression</p>
