---
title: "curlmopt_content_length_penalty_size(3)"
name: "curlmopt_content_length_penalty_size"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_content_length_penalty_size/"
description: "CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE – size threshold for pipelining penalty"
---

<p>CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE &#8211; size threshold for pipelining penalty</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE, long size);</p>
<h2>Description</h2>
<p>Pass a long with a <code>size</code> in bytes. If a pipelined connection is currently processing a request with a Content-Length larger than this <i><a href="/docs/linux/man/3-curlmopt_content_length_penalty_size/">CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE</a>(3)</i>, that pipeline will then not be considered for additional requests, even if it is shorter than <i><a href="/docs/linux/man/3-curlmopt_max_pipeline_length/">CURLMOPT_MAX_PIPELINE_LENGTH</a>(3)</i>.</p>
<h2>Default</h2>
<p>The default value is 0, which means that the size penalization is inactive.</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.30.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_chunk_length_penalty_size/">CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE</a></code>(3),</p>
