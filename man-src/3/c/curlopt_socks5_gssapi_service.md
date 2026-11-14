---
title: "curlopt_socks5_gssapi_service(3)"
name: "curlopt_socks5_gssapi_service"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_socks5_gssapi_service/"
description: "CURLOPT_SOCKS5_GSSAPI_SERVICE – proxy socks gssapi service name"
---

<p>CURLOPT_SOCKS5_GSSAPI_SERVICE &#8211; proxy socks gssapi service name</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SOCKS5_GSSAPI_SERVICE, char *name);</p>
<h2>Description</h2>
<p>Pass a char * as parameter to a string holding the <i>name</i> of the service. The default service name for a SOCKS5 server is rcmd/server-fqdn. This option allows you to change it.</p>
<h2>Default</h2>
<p>See above</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a></code>(3),</p>
