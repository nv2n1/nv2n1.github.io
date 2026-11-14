---
title: "curlopt_noproxy(3)"
name: "curlopt_noproxy"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_noproxy/"
description: "CURLOPT_NOPROXY – disable proxy use for specific hosts"
---

<p>CURLOPT_NOPROXY &#8211; disable proxy use for specific hosts</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NOPROXY, char *noproxy);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string. The string consists of a comma separated list of host names that do not require a proxy to get reached, even if one is specified. The only wildcard available is a single * character, which matches all hosts, and effectively disables the proxy. Each name in this list is matched as either a domain which contains the hostname, or the hostname itself. For example, example.com would match example.com, example.com:80, and <a rel="nofollow" href="http://www.example.com">www.example.com</a>, but not <a href="http://www.notanexample.com">www.notanexample.com</a> or example.com.othertld.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a></code>(3),</p>
