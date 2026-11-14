---
title: "remctl_command(3)"
name: "remctl_command"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_command/"
---

remctl_command, remctl_commandv - Send a command to a remctl server

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
int remctl_command(struct remctl *r, const char **command);
#include &lt;sys/uio.h&gt;
int remctl_commandv(struct remctl *r, const struct iovec *iov,
                    size_t count);</code></pre>

<h2>Description</h2>

<i>remctl_command()</i> and <i>remctl_commandv()</i> send a command to a remote remctl server. The remctl client object <i>r</i>, created with <i>remctl_new()</i>, should have previously been passed to <i>remctl_open()</i> to open a connection to the server. 

 <i>remctl_command()</i> takes the command as a NULL-terminated array of NUL-terminated strings (the same layout as an argv array). This function is most convenient when passing simple text commands. 

 <i>remctl_commandv()</i> takes the command as an array of iovec structs of length <i>count</i>. This function is most convenient when passing arbitrary data to the command, since the iovec struct takes a pointer and a length for each chunk of data. See <i><a HREF="/docs/linux/man/2-writev/">writev</a></i>(2) for the layout of the iovec struct. 

 To control the network timeout for sending the command, see the <i><a HREF="/docs/linux/man/3-remctl_set_timeout/">remctl_set_timeout</a></i>(3) function. 

 After calling one of these functions, call <i>remctl_output()</i> to get the results of the command.

<h2>Return Value</h2>

<i>remctl_command()</i> and <i>remctl_commandv()</i> return true on success and false on failure. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message.

<h2>Compatibility</h2>

These interfaces have been provided by the remctl client library since its initial release in version 2.0.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2009, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_output/">remctl_output</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
