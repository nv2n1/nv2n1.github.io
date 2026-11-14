---
title: "curlopt_tcp_nodelay(3)"
name: "curlopt_tcp_nodelay"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tcp_nodelay/"
description: "CURLOPT_TCP_NODELAY – set the TCP_NODELAY option"
---

<p>CURLOPT_TCP_NODELAY &#8211; set the TCP_NODELAY option</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TCP_NODELAY, long nodelay);</p>
<h2>Description</h2>
<p>Pass a long specifying whether the TCP_NODELAY option is to be set or cleared (1 = set, 0 = clear). The option is cleared by default. This will have no effect after the connection has been established. </p>
<p> Setting this option will disable TCP&#8217;s Nagle algorithm. The purpose of this algorithm is to try to minimize the number of small packets on the network (where &quot;small packets&quot; means TCP segments less than the Maximum Segment Size (MSS) for the network). </p>
<p> Maximizing the amount of data sent per TCP segment is good because it amortizes the overhead of the send. However, in some cases small segments may need to be sent without delay. This is less efficient than sending larger amounts of data at a time, and can contribute to congestion on the network if overdone.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sockoptfunction/">CURLOPT_SOCKOPTFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tcp_keepalive/">CURLOPT_TCP_KEEPALIVE</a></code>(3),</p>
