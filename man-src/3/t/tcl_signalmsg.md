---
title: "tcl_signalmsg(3)"
name: "tcl_signalmsg"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_signalmsg/"
description: "Tcl_SignalId, Tcl_SignalMsg – Convert signal codes"
---

<p>Tcl_SignalId, Tcl_SignalMsg &#8211; Convert signal codes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
const char *
<code>Tcl_SignalId</code>(<i>sig</i>)
const char *
<code>Tcl_SignalMsg</code>(<i>sig</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>sig</i> (in) A POSIX signal number such as <code>SIGPIPE</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_SignalId</code> and <code>Tcl_SignalMsg</code> return a string representation of the provided signal number (<i>sig</i>). <code>Tcl_SignalId</code> returns a machine-readable textual identifier such as &#8220;SIGPIPE&#8221;. <code>Tcl_SignalMsg</code> returns a human-readable string such as &#8220;bus error&#8221;. The strings returned by these functions are statically allocated and the caller must not free or modify them. </p>
<h2>Keywords</h2>
<p>signals, signal numbers</p>
