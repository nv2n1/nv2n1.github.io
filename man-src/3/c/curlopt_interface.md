---
title: "curlopt_interface(3)"
name: "curlopt_interface"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_interface/"
description: "CURLOPT_INTERFACE – source interface for outgoing traffic"
---

<p>CURLOPT_INTERFACE &#8211; source interface for outgoing traffic</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_INTERFACE, char *interface);</p>
<h2>Description</h2>
<p>Pass a char * as parameter. This sets the <i>interface</i> name to use as outgoing network interface. The name can be an interface name, an IP address, or a host name. </p>
<p> If the parameter starts with &quot;if!&quot; then it is treated as only as interface name and no attempt will ever be named to do treat it as an IP address or to do name resolution on it. If the parameter starts with &quot;host!&quot; it is treated as either an IP address or a hostname. Hostnames are resolved synchronously. Using the if! format is highly recommended when using the multi interfaces to avoid allowing the code to block. If &quot;if!&quot; is specified but the parameter does not match an existing interface, CURLE_INTERFACE_FAILED is returned from the libcurl function used to perform the transfer.</p>
<h2>Default</h2>
<p>NULL, use whatever the TCP stack finds suitable</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>The &quot;if!&quot; and &quot;host!&quot; syntax was added in 7.24.0.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK on success or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sockoptfunction/">CURLOPT_SOCKOPTFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tcp_nodelay/">CURLOPT_TCP_NODELAY</a></code>(3),</p>
