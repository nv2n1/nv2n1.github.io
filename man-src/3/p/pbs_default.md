---
title: "pbs_default(3)"
name: "pbs_default"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_default/"
description: "pbs_default – return the pbs default server name"
---

<p>pbs_default &#8211; return the pbs default server name</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre>int pbs_default()</pre>
<h2>Description</h2>
<p>A character string is returned containing the name of the default PBS server. The default server is defined by (a) the setting of the environment variable <code>PBS_DEFAULT</code> which contains a destination, or (b) the destination in the batch administrator established file <font SIZE="-1"></font></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_disconnect/">pbs_disconnect</a>(3B), and the PBS External Reference Specification</p>
<h2>Diagnostics</h2>
<p>If the default server cannot be determined, a NULL value is returned.</p>
