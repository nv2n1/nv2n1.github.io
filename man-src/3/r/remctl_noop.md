---
title: "remctl_noop(3)"
name: "remctl_noop"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_noop/"
---

remctl_noop - Send a NOOP message to a remctl server

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
int remctl_noop(struct remctl *r);</code></pre>

<h2>Description</h2>

<i>remctl_noop()</i> sends a <font SIZE="-1">NOOP</font> message to a remctl server and reads the expected <font SIZE="-1">NOOP</font> response. This is primarily used to keep a connection to a remctl server alive, such as through a firewall with a session timeout, while waiting to issue further commands. 

 The <font SIZE="-1">NOOP</font> message requires protocol version 3 support in the server, so the caller should be prepared for this function to fail, indicating that the connection could not be kept alive and possibly that it was closed by the server. In this case, the client will need to explicitly reopen the connection with <i>remctl_open()</i>.

<h2>Return Value</h2>

<i>remctl_noop()</i> returns true on success and false on failure. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message. In addition to network errors, this function may fail if the server doesn't support protocol version 3.

<h2>Compatibility</h2>

This interface was added in version 3.0.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2011, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_command/">remctl_command</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
