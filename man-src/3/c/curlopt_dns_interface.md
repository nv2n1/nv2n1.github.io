---
title: "curlopt_dns_interface(3)"
name: "curlopt_dns_interface"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_dns_interface/"
description: "CURLOPT_DNS_INTERFACE – set interface to speak DNS over"
---

<p>CURLOPT_DNS_INTERFACE &#8211; set interface to speak DNS over</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DNS_INTERFACE, char *ifname);</p>
<h2>Description</h2>
<p>Pass a char * as parameter. Set the name of the network interface that the DNS resolver should bind to. This must be an interface name (not an address). Set this option to NULL to use the default setting (don&#8217;t bind to a specific interface).</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.33.0. This option also requires that libcurl was built with a resolver backend that supports this operation. The c-ares backend is the only such one.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_NOT_BUILT_IN if support was disabled at compile-time.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_dns_servers/">CURLOPT_DNS_SERVERS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_dns_local_ip4/">CURLOPT_DNS_LOCAL_IP4</a></code>(3),</p>
