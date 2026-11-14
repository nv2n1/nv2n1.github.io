---
title: "pbs_fbserver(3)"
name: "pbs_fbserver"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_fbserver/"
---

pbs_fbserver - get the pbs fall-back server name

<h2>Synopsis</h2>

<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre> <pre>int pbs_fbserver()</pre>

<h2>Description</h2>

A character string is returned containing the name of the fall-back PBS server. The fall-back server is the second server listed when configured to run in high-availability mode.

<h2>See Also</h2>

<a HREF="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_default/">pbs_default</a>(3B), <a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_fbserver/">pbs_fbserver</a>(3B), <a HREF="//www.systutorials.com/docs/linux/man/3B-pbs_disconnect/">pbs_disconnect</a>(3B), and the PBS External Reference Specification

<h2>Diagnostics</h2>

If the fall-back server cannot be determined, a NULL value is returned.
