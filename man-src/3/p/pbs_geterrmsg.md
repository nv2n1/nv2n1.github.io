---
title: "pbs_geterrmsg(3)"
name: "pbs_geterrmsg"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_geterrmsg/"
description: "pbs_geterrmsg – get error message for last pbs batch operation"
---

<p>pbs_geterrmsg &#8211; get error message for last pbs batch operation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre>char *pbs_geterrmsg(int connect)</pre>
<h2>Description</h2>
<p>Return the error message text associated with a batch server request. </p>
<p> If the preceding batch interface library call over the connection specified by <i> resulted in an error return from the server, there may be an associated text message. If it exists, this function will return a pointer to the null terminated text string. </i></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B)</p>
<h2>Diagnostics</h2>
<p>If an error text message was returned by a server in reply to the previous call to a batch interface library function, <code>pbs_geterrmsg</code>() will return a pointer to it. Otherwise, pbs_geterrmsg() returns the null pointer.</p>
