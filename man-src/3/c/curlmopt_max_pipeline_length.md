---
title: "curlmopt_max_pipeline_length(3)"
name: "curlmopt_max_pipeline_length"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_max_pipeline_length/"
description: "CURLMOPT_MAX_PIPELINE_LENGTH – maximum number of requests in a pipeline"
---

<p>CURLMOPT_MAX_PIPELINE_LENGTH &#8211; maximum number of requests in a pipeline</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_MAX_PIPELINE_LENGTH, long max);</p>
<h2>Description</h2>
<p>Pass a long. The set <code>max</code> number will be used as the maximum amount of outstanding requests in a pipelined connection. Only used if pipelining is enabled. </p>
<p> When this limit is reached, libcurl will use another connection to the same host (see <i><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a>(3)</i>), or queue the request until one of the pipelines to the host is ready to accept a request. Thus, the total number of requests in-flight is <i><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a>(3)</i> * <i><a href="/docs/linux/man/3-curlmopt_max_pipeline_length/">CURLMOPT_MAX_PIPELINE_LENGTH</a>(3)</i>.</p>
<h2>Default</h2>
<p>5</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.30.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_max_host_connections/">CURLMOPT_MAX_HOST_CONNECTIONS</a></code>(3),</p>
