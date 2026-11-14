---
title: "curlopt_http_version(3)"
name: "curlopt_http_version"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_http_version/"
description: "CURLOPT_HTTP_VERSION – specify HTTP protocol version to use"
---

<p>CURLOPT_HTTP_VERSION &#8211; specify HTTP protocol version to use</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTP_VERSION, long version);</p>
<h2>Description</h2>
<p>Pass <i>version</i> a long, set to one of the values described below. They force libcurl to use the specific HTTP versions. This is not sensible to do unless you have a good reason. You have to set this option if you want to use libcurl&#8217;s HTTP/2 support. </p>
<dl COMPACT>
<dt>CURL_HTTP_VERSION_NONE</p>
<dd>We don&#8217;t care about what version the library uses. libcurl will use whatever it thinks fit.</p>
<dt>CURL_HTTP_VERSION_1_0</p>
<dd>Enforce HTTP 1.0 requests.</p>
<dt>CURL_HTTP_VERSION_1_1</p>
<dd>Enforce HTTP 1.1 requests.</p>
<dt>CURL_HTTP_VERSION_2_0</p>
<dd>Attempt HTTP 2.0 requests. libcurl will fall back to HTTP 1.x if HTTP 2.0 can&#8217;t be negotiated with the server.</dl>
<h2>Default</h2>
<p>CURL_HTTP_VERSION_NONE</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_http200aliases/">CURLOPT_HTTP200ALIASES</a></code>(3),</p>
