---
title: "pbs_disconnect(3)"
name: "pbs_disconnect"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_disconnect/"
description: "pbs_disconnect – disconnect from a pbs batch server"
---

<p>pbs_disconnect &#8211; disconnect from a pbs batch server</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre>int pbs_disconnect(int connect)</pre>
<h2>Description</h2>
<p>The virtual stream connection specified by <i> which was established with a server by a call to </i><code>pbs_connect</code>(), is closed.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B)</p>
<h2>Diagnostics</h2>
<p>When the connection to batch server has been successfully closed, the routine will return zero. Otherwise, a non zero error is returned. The error number is also set in pbs_errno.</p>
