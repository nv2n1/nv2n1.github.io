---
title: "tcl_sourcercfile(3)"
name: "tcl_sourcercfile"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_sourcercfile/"
description: "Tcl_SourceRCFile – source the Tcl rc file"
---

<p>Tcl_SourceRCFile &#8211; source the Tcl rc file </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_SourceRCFile</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter to source rc file into. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_SourceRCFile</code> is used to source the Tcl rc file at startup. It is typically invoked by Tcl_Main or Tk_Main. The name of the file sourced is obtained from the global variable <code>tcl_rcFileName</code> in the interpreter given by <i>interp</i>. If this variable is not defined, or if the file it indicates cannot be found, no action is taken. </p>
<h2>Keywords</h2>
<p>application-specific initialization, main program, rc file</p>
