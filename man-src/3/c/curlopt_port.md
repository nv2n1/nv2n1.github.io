---
title: "curlopt_port(3)"
name: "curlopt_port"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_port/"
description: "CURLOPT_PORT – set remote port number to work with"
---

<p>CURLOPT_PORT &#8211; set remote port number to work with</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PORT, long number);</p>
<h2>Description</h2>
<p>This option sets <i>number</i> to be the remote port number to connect to, instead of the one specified in the URL or the default port for the used protocol. </p>
<p> Usually, you just let the URL decide which port to use but this allows the application to override that. </p>
<p> While this option accepts a &#8216;long&#8217;, a port number is usually a 16 bit number and therefore using a port number over 65535 will cause a run-time error.</p>
<h2>Default</h2>
<p>By default this is 0 which makes it not used.</p>
<h2>Protocols</h2>
<p>Used for all protocols that speak to a port number.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
