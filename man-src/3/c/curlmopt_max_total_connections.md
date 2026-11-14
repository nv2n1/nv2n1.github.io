---
title: "curlmopt_max_total_connections(3)"
name: "curlmopt_max_total_connections"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_max_total_connections/"
description: "CURLMOPT_MAX_TOTAL_CONNECTIONS – max simultaneously open connections"
---

<p>CURLMOPT_MAX_TOTAL_CONNECTIONS &#8211; max simultaneously open connections</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_MAX_TOTAL_CONNECTIONS, long amount);</p>
<h2>Description</h2>
<p>Pass a long for the <code>amount</code>. The set number will be used as the maximum number of simultaneously open connections in total using this multi handle. For each new session, libcurl will open a new connection up to the limit set by <i><a href="/docs/linux/man/3-curlmopt_max_total_connections/">CURLMOPT_MAX_TOTAL_CONNECTIONS</a>(3)</i>. When the limit is reached, the sessions will be pending until there are available connections. If <i><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a>(3)</i> is enabled, libcurl will try to pipeline if the host is capable of it.</p>
<h2>Default</h2>
<p>The default value is 0, which means that there is no limit. It is then simply controlled by the number of easy handles added.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.30.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_maxconnects/">CURLMOPT_MAXCONNECTS</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a></code>(3),</p>
