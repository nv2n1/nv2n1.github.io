---
title: "curlopt_connect_only(3)"
name: "curlopt_connect_only"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_connect_only/"
description: "CURLOPT_CONNECT_ONLY – stop when connected to target server"
---

<p>CURLOPT_CONNECT_ONLY &#8211; stop when connected to target server</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CONNECT_ONLY, long only);</p>
<h2>Description</h2>
<p>Pass a long. If the parameter equals 1, it tells the library to perform all the required proxy authentication and connection setup, but no data transfer, and then return. </p>
<p> The option can be used to simply test a connection to a server, but is more useful when used with the <i>CURLINFO_LASTSOCKET</i> option to <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> as the library can set up the connection and then the application can obtain the most recently used socket for special data transfers.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP, SMTP, POP3 and IMAP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.2</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpproxytunnel/">CURLOPT_HTTPPROXYTUNNEL</a></code>(3),</p>
