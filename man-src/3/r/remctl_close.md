---
title: "remctl_close(3)"
name: "remctl_close"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_close/"
---

remctl_close - Close a remctl connection and free the client object

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
void remctl_close(struct remctl *r);</code></pre>

<h2>Description</h2>

<i>remctl_close()</i> cleanly closes any connection to a remote server created via <i>remctl_open()</i> for the given client object and then frees the object created by <i>remctl_new()</i>. It should be called when the caller is finished with a remctl client object to avoid resource leaks. Following the call to <i>remctl_close()</i>, the <i>r</i> pointer to the remctl client object is no longer valid. 

 <i>remctl_close()</i> is always successful, even if it is unable to send a clean protocol quit command to the remote server.

<h2>Compatibility</h2>

This interface has been provided by the remctl client library since its initial release in version 2.0.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2009, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
