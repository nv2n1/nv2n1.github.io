---
title: "zmq_version(3)"
name: "zmq_version"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_version/"
description: "zmq_version – report 0MQ library version"
---

<p>zmq_version &#8211; report 0MQ library version</p>
<h2>Synopsis</h2>
<pre><code>void zmq_version(int *major, int *minor, int *patch);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_version()</i> function shall fill in the integer variables pointed to by the <i>major</i>, <i>minor</i> and <i>patch</i> arguments with the major, minor and patch level components of the 0MQ library version. </p>
<p> This functionality is intended for applications or language bindings dynamically linking to the 0MQ library that wish to determine the actual version of the 0MQ library they are using.</p>
<h2>Return Value</h2>
<p>There is no return value.</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>Example</h2>
<p><code>Printing out the version of the 0MQ library</code>. </p>
<pre><code>int major, minor, patch;
zmq_version(&amp;major, &amp;minor, &amp;patch);
printf(&quot;Current 0MQ version is %d.%d.%d
&quot;, major, minor, patch);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
