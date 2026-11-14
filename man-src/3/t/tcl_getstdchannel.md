---
title: "tcl_getstdchannel(3)"
name: "tcl_getstdchannel"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getstdchannel/"
description: "Tcl_GetStdChannel, Tcl_SetStdChannel – procedures for retrieving and replacing the standard channels"
---

<p>Tcl_GetStdChannel, Tcl_SetStdChannel &#8211; procedures for retrieving and replacing the standard channels </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Channel
<code>Tcl_GetStdChannel</code>(<i>type</i>)
<code>Tcl_SetStdChannel</code>(<i>channel, type</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>type</i> (in) The identifier for the standard channel to retrieve or modify. Must be one of <code>TCL_STDIN</code>, <code>TCL_STDOUT</code>, or <code>TCL_STDERR</code>.</p>
<dd>Tcl_Channel <i>channel</i> (in) The channel to use as the new value for the specified standard channel. </p>
</dl>
<h2>Description</h2>
<p>Tcl defines three special channels that are used by various I/O related commands if no other channels are specified. The standard input channel has a channel name of <code>stdin</code> and is used by <code>read</code> and <code>gets</code>. The standard output channel is named <code>stdout</code> and is used by <code>puts</code>. The standard error channel is named <code>stderr</code> and is used for reporting errors. In addition, the standard channels are inherited by any child processes created using <code>exec</code> or <code>open</code> in the absence of any other redirections. </p>
<p> The standard channels are actually aliases for other normal channels. The current channel associated with a standard channel can be retrieved by calling <code>Tcl_GetStdChannel</code> with one of <code>TCL_STDIN</code>, <code>TCL_STDOUT</code>, or <code>TCL_STDERR</code> as the <i>type</i>. The return value will be a valid channel, or NULL. </p>
<p> A new channel can be set for the standard channel specified by <i>type</i> by calling <code>Tcl_SetStdChannel</code> with a new channel or NULL in the <i>channel</i> argument. If the specified channel is closed by a later call to <code>Tcl_Close</code>, then the corresponding standard channel will automatically be set to NULL. </p>
<p> If a non-NULL value for <i>channel</i> is passed to <code>Tcl_SetStdChannel</code>, then that same value should be passed to <code>Tcl_RegisterChannel</code>, like so:</p>
<dl COMPACT>
<dd>
<pre>Tcl_RegisterChannel(NULL, channel);</pre>
</dl>
<p> This is a workaround for a misfeature in <code>Tcl_SetStdChannel</code> that it fails to do some reference counting housekeeping. This misfeature cannot be corrected without contradicting the assumptions of some existing code that calls <code>Tcl_SetStdChannel</code>. </p>
<p> If <code>Tcl_GetStdChannel</code> is called before <code>Tcl_SetStdChannel</code>, Tcl will construct a new channel to wrap the appropriate platform-specific standard file handle. If <code>Tcl_SetStdChannel</code> is called before <code>Tcl_GetStdChannel</code>, then the default channel will not be created. </p>
<p> If one of the standard channels is set to NULL, either by calling <code>Tcl_SetStdChannel</code> with a NULL <i>channel</i> argument, or by calling <code>Tcl_Close</code> on the channel, then the next call to <code>Tcl_CreateChannel</code> will automatically set the standard channel with the newly created channel. If more than one standard channel is NULL, then the standard channels will be assigned starting with standard input, followed by standard output, with standard error being last. </p>
<p> See <code>Tcl_StandardChannels</code> for a general treatise about standard channels and the behaviour of the Tcl library with regard to them. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_close/">Tcl_Close</a>(3), <a href="/docs/linux/man/3-tcl_createchannel/">Tcl_CreateChannel</a>(3), <a href="/docs/linux/man/3-tcl_main/">Tcl_Main</a>(3), <a href="/docs/linux/man/1-tclsh/">tclsh</a>(1) </p>
<h2>Keywords</h2>
<p>standard channel, standard input, standard output, standard error</p>
