---
title: "zmq_errno(3)"
name: "zmq_errno"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_errno/"
description: "zmq_errno – retrieve value of errno for the calling thread"
---

<p>zmq_errno &#8211; retrieve value of errno for the calling thread</p>
<h2>Synopsis</h2>
<pre><code>int zmq_errno(void);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_errno()</i> function shall retrieve the value of the <i>errno</i> variable for the calling thread. The <i>zmq_errno()</i> function is provided to assist users on non-POSIX systems who are experiencing issues with retrieving the correct value of <i>errno</i> directly. Specifically, users on Win32 systems whose application is using a different C run-time library from the C run-time library in use by 0MQ will need to use <i>zmq_errno()</i> for correct operation.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 Users not experiencing issues with retrieving the correct value of <i>errno</i> should not use this function and should instead access the <i>errno</i> variable directly. </p>
<h2>Return Value</h2>
<p>The <i>zmq_errno()</i> function shall return the value of the <i>errno</i> variable for the calling thread.</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
