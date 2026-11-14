---
title: "tcl_gethostname(3)"
name: "tcl_gethostname"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_gethostname/"
description: "Tcl_GetHostName – get the name of the local host"
---

<p>Tcl_GetHostName &#8211; get the name of the local host </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
const char *
<code>Tcl_GetHostName</code>()
<br>
<hr></pre>
<h2>Description</h2>
<p><code>Tcl_GetHostName</code> is a utility procedure used by some of the Tcl commands. It returns a pointer to a string containing the name for the current machine, or an empty string if the name cannot be determined. The string is statically allocated, and the caller must not modify of free it. </p>
<h2>Keywords</h2>
<p>hostname</p>
