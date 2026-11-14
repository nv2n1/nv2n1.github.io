---
title: "curlmopt_socketdata(3)"
name: "curlmopt_socketdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_socketdata/"
description: "CURLMOPT_SOCKETDATA – custom pointer passed to the socket callback"
---

<p>CURLMOPT_SOCKETDATA &#8211; custom pointer passed to the socket callback</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_SOCKETDATA, void *pointer);</pre>
<h2>Description</h2>
<p>A data <i>pointer</i> to pass to the socket callback set with the <i><a href="/docs/linux/man/3-curlmopt_socketfunction/">CURLMOPT_SOCKETFUNCTION</a>(3)</i> option. </p>
<p> This pointer will not be touched by libcurl but will only be passed in to the socket callbacks&#8217;s <code>userp</code> argument.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.4</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_socketfunction/">CURLMOPT_SOCKETFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_timerfunction/">CURLMOPT_TIMERFUNCTION</a></code>(3)</p>
