---
title: "curlopt_proxyport(3)"
name: "curlopt_proxyport"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxyport/"
description: "CURLOPT_PROXYPORT – port number the proxy listens on"
---

<p>CURLOPT_PROXYPORT &#8211; port number the proxy listens on</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYPORT, long port);</p>
<h2>Description</h2>
<p>Pass a long with this option to set the proxy port to connect to unless it is specified in the proxy string <i><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a>(3)</i> or uses the default one. </p>
<p> While this accepts a &#8216;long&#8217;, the port number is 16 bit so it can&#8217;t be larger than 65535.</p>
<h2>Default</h2>
<p>0, not specified which makes it use the default port</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a></code>(3),</p>
