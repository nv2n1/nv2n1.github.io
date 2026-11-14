---
title: "curlopt_proxyheader(3)"
name: "curlopt_proxyheader"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxyheader/"
description: "CURLOPT_PROXYHEADER – custom HTTP headers to pass to proxy"
---

<p>CURLOPT_PROXYHEADER &#8211; custom HTTP headers to pass to proxy</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYHEADER,
 struct curl_slist *headers);</pre>
<h2>Description</h2>
<p>Pass a pointer to a linked list of HTTP headers to pass in your HTTP request sent to a proxy. The rules for this list is identical to the <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> option&#8217;s. </p>
<p> The headers set with this option is only ever used in requests sent to a proxy &#8211; when there&#8217;s also a request sent to a host. </p>
<p> The first line in a request (containing the method, usually a GET or POST) is NOT a header and cannot be replaced using this option. Only the lines following the request-line are headers. Adding this method line in this list of headers will only cause your request to send an invalid header. </p>
<p> Pass a NULL to this to reset back to no custom headers.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.37.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_headeropt/">CURLOPT_HEADEROPT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3),</p>
