---
title: "curlmopt_max_host_connections(3)"
name: "curlmopt_max_host_connections"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_max_host_connections/"
description: "CURLMOPT_MAX_HOST_CONNECTIONS – set max number of connections to a single host"
---

<p>CURLMOPT_MAX_HOST_CONNECTIONS &#8211; set max number of connections to a single host</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_MAX_HOST_CONNECTIONS, long max);</p>
<h2>Description</h2>
<p>Pass a long to indicate <code>max</code>. The set number will be used as the maximum amount of simultaneously open connections to a single host. For each new session to a host, libcurl will open a new connection up to the limit set by <i><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a>(3)</i>. When the limit is reached, the sessions will be pending until a connection becomes available. If <i><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a>(3)</i> is enabled, libcurl will try to pipeline if the host is capable of it. </p>
<p> The default <code>max</code> value is 0, unlimited. However, for backwards compatibility, setting it to 0 when <i><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a>(3)</i> is 1 will not be treated as unlimited. Instead it will open only 1 connection and try to pipeline on it.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.30.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_maxconnects/">CURLMOPT_MAXCONNECTS</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_max_total_connections/">CURLMOPT_MAX_TOTAL_CONNECTIONS</a></code>(3),</p>
