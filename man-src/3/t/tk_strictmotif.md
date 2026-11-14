---
title: "tk_strictmotif(3)"
name: "tk_strictmotif"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_strictmotif/"
description: "Tk_StrictMotif – Return value of tk_strictMotif variable"
---

<p>Tk_StrictMotif &#8211; Return value of tk_strictMotif variable </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_StrictMotif</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window. </p>
</dl>
<h2>Description</h2>
<p>This procedure returns the current value of the <code>tk_strictMotif</code> variable in the interpreter associated with <i>tkwin</i>&#8216;s application. The value is returned as an integer that is either 0 or 1. 1 means that strict Motif compliance has been requested, so anything that is not part of the Motif specification should be avoided. 0 means that &#8220;Motif-like&#8221; is good enough, and extra features are welcome. </p>
<p> This procedure uses a link to the Tcl variable to provide much faster access to the variable&#8217;s value than could be had by calling <code>Tcl_GetVar</code>. </p>
<h2>Keywords</h2>
<p>Motif compliance, tk_strictMotif variable</p>
