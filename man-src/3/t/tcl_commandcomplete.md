---
title: "tcl_commandcomplete(3)"
name: "tcl_commandcomplete"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_commandcomplete/"
description: "Tcl_CommandComplete – Check for unmatched braces in a Tcl command"
---

<p>Tcl_CommandComplete &#8211; Check for unmatched braces in a Tcl command </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_CommandComplete</code>(<i>cmd</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const char <i>*cmd</i> (in) Command string to test for completeness. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CommandComplete</code> takes a Tcl command string as argument and determines whether it contains one or more complete commands (i.e. there are no unclosed quotes, braces, brackets, or variable references). If the command string is complete then it returns 1; otherwise it returns 0. </p>
<h2>Keywords</h2>
<p>complete command, partial command</p>
