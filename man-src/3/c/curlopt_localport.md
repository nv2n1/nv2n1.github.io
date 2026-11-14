---
title: "curlopt_localport(3)"
name: "curlopt_localport"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_localport/"
description: "CURLOPT_LOCALPORT – set local port number to use for socket"
---

<p>CURLOPT_LOCALPORT &#8211; set local port number to use for socket</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_LOCALPORT, long port);</p>
<h2>Description</h2>
<p>Pass a long. This sets the local port number of the socket used for the connection. This can be used in combination with <i><a href="/docs/linux/man/3-curlopt_interface/">CURLOPT_INTERFACE</a>(3)</i> and you are recommended to use <i><a href="/docs/linux/man/3-curlopt_localportrange/">CURLOPT_LOCALPORTRANGE</a>(3)</i> as well when this option is set. Valid port numbers are 1 &#8211; 65535.</p>
<h2>Default</h2>
<p>0, disabled &#8211; use whatever the system thinks is fine</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.2</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_localportrange/">CURLOPT_LOCALPORTRANGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_interface/">CURLOPT_INTERFACE</a></code>(3),</p>
