---
title: "tcl_putenv(3)"
name: "tcl_putenv"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_putenv/"
description: "Tcl_PutEnv – procedures to manipulate the environment"
---

<p>Tcl_PutEnv &#8211; procedures to manipulate the environment </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_PutEnv</code>(<i>assignment</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const char <i>*assignment</i> (in) Info about environment variable in the format &#8220;<i>NAME</i><code>=</code><i>value</i>&#8221;. The <i>assignment</i> argument is in the system encoding.
</dl>
<h2>Description</h2>
<p><code>Tcl_PutEnv</code> sets an environment variable. The information is passed in a single string of the form &#8220;<i>NAME</i><code>=</code><i>value</i>&#8221;. This procedure is intended to be a stand-in for the UNIX <code>putenv</code> system call. All Tcl-based applications using <code>putenv</code> should redefine it to <code>Tcl_PutEnv</code> so that they will interface properly to the Tcl runtime.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-tclvars/">tclvars</a>(n)</p>
<h2>Keywords</h2>
<p>environment, variable</p>
