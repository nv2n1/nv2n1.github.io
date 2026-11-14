---
title: "curlopt_dns_local_ip4(3)"
name: "curlopt_dns_local_ip4"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_dns_local_ip4/"
description: "CURLOPT_DNS_LOCAL_IP4 – IPv4 address to bind DNS resolves to"
---

<p>CURLOPT_DNS_LOCAL_IP4 &#8211; IPv4 address to bind DNS resolves to</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DNS_LOCAL_IP4, char *address);</p>
<h2>Description</h2>
<p>Set the local IPv4 <i>address</i> that the resolver should bind to. The argument should be of type char * and contain a single numerical IPv4 address as a string. Set this option to NULL to use the default setting (don&#8217;t bind to a specific IP address).</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option requires that libcurl was built with a resolver backend that supports this operation. The c-ares backend is the only such one. </p>
<p> Added in 7.33.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, CURLE_NOT_BUILT_IN if support was disabled at compile-time, or CURLE_BAD_FUNCTION_ARGUMENT when given a bad address.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_dns_interface/">CURLOPT_DNS_INTERFACE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_dns_local_ip4/">CURLOPT_DNS_LOCAL_IP4</a></code>(3),</p>
