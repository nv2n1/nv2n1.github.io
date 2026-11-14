---
title: "remctl_set_timeout(3)"
name: "remctl_set_timeout"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_set_timeout/"
---

remctl_set_timeout - Set timeout for subsequent remctl client operations

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
int remctl_set_timeout(struct remctl *r, time_t timeout);</code></pre>

<h2>Description</h2>

<i>remctl_set_timeout()</i> sets the timeout for connections and commands to <i>timeout</i>, which should be an integer number of seconds. <i>timeout</i> may be 0 to clear a timeout that was previously set and restore the default behavior of having no timeout. All subsequent operations on the given struct remctl argument will be subject to this timeout, including <i>remctl_open()</i> if called prior to calling <i>remctl_open()</i>. 

 The timeout is a timeout on network activity from the server, not on a complete operation. So, for example, a timeout of ten seconds just requires that the server send some data every ten seconds. If the server sends only tiny amounts of data at a time, the complete operation could take much longer than ten seconds without triggering the timeout.

<h2>Return Value</h2>

<i>remctl_set_timeout()</i> returns true on success and false on failure. The only failure case is if <i>timeout</i> is negative. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message.

<h2>Compatibility</h2>

This interface was added in version 3.1.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2012, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_command/">remctl_command</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_output/">remctl_output</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
