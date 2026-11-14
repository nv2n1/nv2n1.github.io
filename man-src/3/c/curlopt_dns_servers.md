---
title: "curlopt_dns_servers(3)"
name: "curlopt_dns_servers"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_dns_servers/"
description: "CURLOPT_DNS_SERVERS – set preferred DNS servers"
---

<p>CURLOPT_DNS_SERVERS &#8211; set preferred DNS servers</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DNS_SERVERS, char *servers);</p>
<h2>Description</h2>
<p>Pass a char * that is the list of DNS servers to be used instead of the system default. The format of the dns servers option is: </p>
<p> host[:port][,host[:port]]&#8230; </p>
<p> For example: </p>
<p> 192.168.1.100,192.168.1.101,3.4.5.6</p>
<h2>Default</h2>
<p>NULL &#8211; use system default</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option requires that libcurl was built with a resolver backend that supports this operation. The c-ares backend is the only such one. </p>
<p> Added in 7.24.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, CURLE_NOT_BUILT_IN if support was disabled at compile-time, CURLE_BAD_FUNCTION_ARGUMENT when given an invalid server list, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_dns_local_ip4/">CURLOPT_DNS_LOCAL_IP4</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_dns_cache_timeout/">CURLOPT_DNS_CACHE_TIMEOUT</a></code>(3),</p>
