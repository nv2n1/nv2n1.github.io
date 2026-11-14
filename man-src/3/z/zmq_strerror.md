---
title: "zmq_strerror(3)"
name: "zmq_strerror"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_strerror/"
description: "zmq_strerror – get 0MQ error message string"
---

<p>zmq_strerror &#8211; get 0MQ error message string</p>
<h2>Synopsis</h2>
<pre><code>const char *zmq_strerror(int errnum);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_strerror()</i> function shall return a pointer to an error message string corresponding to the error number specified by the <i>errnum</i> argument. As 0MQ defines additional error numbers over and above those defined by the operating system, applications should use <i>zmq_strerror()</i> in preference to the standard <i>strerror()</i> function.</p>
<h2>Return Value</h2>
<p>The <i>zmq_strerror()</i> function shall return a pointer to an error message string.</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>Example</h2>
<p><code>Displaying an error message when a 0MQ context cannot be initialised</code>. </p>
<pre><code>void *ctx = zmq_init(1, 1, 0);
if (!ctx) {
    printf(&quot;Error occurred during zmq_init(): %s
&quot;, zmq_strerror(errno));
    abort();
}
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
