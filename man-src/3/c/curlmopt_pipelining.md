---
title: "curlmopt_pipelining(3)"
name: "curlmopt_pipelining"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_pipelining/"
description: "CURLMOPT_PIPELINING – enable/disable HTTP pipelining"
---

<p>CURLMOPT_PIPELINING &#8211; enable/disable HTTP pipelining</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_PIPELINING, bool onoff);</p>
<h2>Description</h2>
<p>Set the <code>onoff</code> parameter to 1 to make libcurl use HTTP pipelining for HTTP transfers done using this multi handle, as far as possible. This means that if you add a second request that can use an already existing connection, the second request will be &quot;piped&quot; on the same connection rather than being executed in parallel. </p>
<p> When using pipelining, there are also several other related options that are interesting to tweak and adjust to alter how libcurl spreads out requests on different connections or not etc.</p>
<h2>Default</h2>
<p>0 (off)</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_max_pipeline_length/">CURLMOPT_MAX_PIPELINE_LENGTH</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_pipelining_site_bl/">CURLMOPT_PIPELINING_SITE_BL</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_content_length_penalty_size/">CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_chunk_length_penalty_size/">CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_maxconnects/">CURLMOPT_MAXCONNECTS</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a></code>(3),</p>
