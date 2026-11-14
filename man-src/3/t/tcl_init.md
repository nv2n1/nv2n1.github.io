---
title: "tcl_init(3)"
name: "tcl_init"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_init/"
description: "Tcl_Init – find and source initialization script"
---

<p>Tcl_Init &#8211; find and source initialization script </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_Init</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to initialize. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_Init</code> is a helper procedure that finds and <code>source</code>s the <code>init.tcl</code> script, which should exist somewhere on the Tcl library path. </p>
<p> <code>Tcl_Init</code> is typically called from <code>Tcl_AppInit</code> procedures. </p>
<h2>See Also</h2>
<p>Tcl_AppInit, Tcl_Main </p>
<h2>Keywords</h2>
<p>application, initialization, interpreter</p>
