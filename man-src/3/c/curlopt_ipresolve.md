---
title: "curlopt_ipresolve(3)"
name: "curlopt_ipresolve"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ipresolve/"
description: "CURLOPT_IPRESOLVE – specify which IP protocol version to use"
---

<p>CURLOPT_IPRESOLVE &#8211; specify which IP protocol version to use</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_IPRESOLVE, long resolve);</p>
<h2>Description</h2>
<p>Allows an application to select what kind of IP addresses to use when resolving host names. This is only interesting when using host names that resolve addresses using more than one version of IP. The allowed values are:</p>
<dl COMPACT>
<dt>CURL_IPRESOLVE_WHATEVER</p>
<dd>Default, resolves addresses to all IP versions that your system allows.</p>
<dt>CURL_IPRESOLVE_V4</p>
<dd>Resolve to IPv4 addresses.</p>
<dt>CURL_IPRESOLVE_V6</p>
<dd>Resolve to IPv6 addresses.</dl>
<h2>Default</h2>
<p>CURL_IPRESOLVE_WHATEVER</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_http_version/">CURLOPT_HTTP_VERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3),</p>
