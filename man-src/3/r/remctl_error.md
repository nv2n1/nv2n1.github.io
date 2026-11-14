---
title: "remctl_error(3)"
name: "remctl_error"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_error/"
---

remctl_error - Retrieve the error from a failed remctl operation

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
const char *remctl_error(struct remctl *r);</code></pre>

<h2>Description</h2>

<i>remctl_error()</i> returns the error from a previously failed remctl operation. Its only argument is a remctl struct as returned by <i>remctl_new()</i>. If the previous remctl operation was successful, returns the constant string ``No error''. 

 The caller may not modify the returned string. The string may even be stored in read-only memory and attempting to modify it may cause a memory fault. The returned pointer will be invalidated by the next call to any remctl <font SIZE="-1">API</font> function with the same client object, other than <i>remctl_error()</i>.

<h2>Return Value</h2>

<i>remctl_error()</i> returns either the previous error or the constant string ``No error''. It will never return <font SIZE="-1">NULL.</font>

<h2>Compatibility</h2>

This interface has been provided by the remctl client library since its initial release in version 2.0.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2009, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_command/">remctl_command</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_commandv/">remctl_commandv</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_output/">remctl_output</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
