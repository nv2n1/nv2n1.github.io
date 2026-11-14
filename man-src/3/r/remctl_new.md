---
title: "remctl_new(3)"
name: "remctl_new"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_new/"
---

remctl_new - Create a new remctl client

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
struct remctl *remctl_new(void);</code></pre>

<h2>Description</h2>

<i>remctl_new()</i> creates a new remctl client. The resulting remctl struct is opaque from the perspective of the caller, but should be the first argument to all subsequent calls into the remctl <font SIZE="-1">API. </font> Normally, the next call after <i>remctl_new()</i> would be <i>remctl_open()</i> to connect to a remote server. 

 The resulting struct should be freed by calling <i>remctl_close()</i>.

<h2>Return Value</h2>

<i>remctl_new()</i> returns a pointer to an opaque remctl struct on success and <font SIZE="-1">NULL</font> on failure. If it returns <font SIZE="-1">NULL,</font> errno will be set to an appropriate error code (normally <font SIZE="-1">ENOMEM</font>).

<h2>Compatibility</h2>

This interface has been provided by the remctl client library since its initial release in version 2.0.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2009, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_command/">remctl_command</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_commandv/">remctl_commandv</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_output/">remctl_output</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_close/">remctl_close</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
