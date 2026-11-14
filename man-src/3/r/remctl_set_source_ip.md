---
title: "remctl_set_source_ip(3)"
name: "remctl_set_source_ip"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_set_source_ip/"
---

remctl_set_source_ip - Set source IP for remctl client connections

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
int remctl_set_source_ip(struct remctl *r, const char *source);</code></pre>

<h2>Description</h2>

<i>remctl_set_source_ip()</i> sets the source <font SIZE="-1">IP</font> address for subsequent calls to <i>remctl_open()</i> on the same struct remctl object. Call this function before <i>remctl_open()</i> if remctl client connections need to come from a specific source <font SIZE="-1">IP.</font> 

 The <i>source</i> parameter may be an IPv4 or IPv6 address (assuming the host supports IPv6). 

 Be aware that if you set an IPv4 source address and then attempt to connect to an IPv6 address or IPv6-only host, or if you set an IPv6 address and then attempt to connect to an IPv4 address or IPv4-only host, you will get a connection failure error from <i>remctl_open()</i>.

<h2>Return Value</h2>

<i>remctl_set_source_ip()</i> returns true on success and false on failure. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message.

<h2>Compatibility</h2>

This interface was added in version 3.0.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2011, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
