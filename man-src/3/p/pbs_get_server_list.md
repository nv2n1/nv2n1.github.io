---
title: "pbs_get_server_list(3)"
name: "pbs_get_server_list"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_get_server_list/"
---

pbs_get_server_list - get a list of pbs server names

<h2>Synopsis</h2>

<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre> <pre>char pbs_get_server_list()</pre>

<h2>Description</h2>

A character string is returned containing the names of the PBS servers.

<h2>See Also</h2>

<a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_default/">pbs_default</a>(3B), <a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_fbserver/">pbs_fbserver</a>(3B)

<h2>Diagnostics</h2>

If the servers cannot be determined, a NULL value is returned.
