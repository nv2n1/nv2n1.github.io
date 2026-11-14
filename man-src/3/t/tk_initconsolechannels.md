---
title: "tk_initconsolechannels(3)"
name: "tk_initconsolechannels"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_initconsolechannels/"
description: "Tk_InitConsoleChannels – Install the console channels as standard channels"
---

<p>Tk_InitConsoleChannels &#8211; Install the console channels as standard channels </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_InitConsoleChannels</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which the console channels are created.
</dl>
<h2>Description</h2>
<p><code>Tk_InitConsoleChannels</code> is invoked to create a set of console channels and install them as the standard channels. All I/O on these channels will be discarded until <code>Tk_CreateConsoleWindow</code> is called to attach the console to a text widget. </p>
<p> This function is for use by shell applications based on Tk, like <code>wish</code>, on platforms which have no standard channels in graphical mode, like Win32. </p>
<p> The <i>interp</i> argument is the interpreter in which to create and install the console channels. </p>
<p> <code>NOTE:</code> If this function is used it has to be called before the first call to <code>Tcl_RegisterChannel</code>, directly, or indirectly through other channel functions. Because otherwise the standard channels will be already initialized to the system defaults, which will be nonsensical for the case <code>Tk_InitConsoleChannels</code> is for.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-console/">console</a>(n)</p>
<h2>Keywords</h2>
<p>standard channels, console</p>
