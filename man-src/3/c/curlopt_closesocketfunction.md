---
title: "curlopt_closesocketfunction(3)"
name: "curlopt_closesocketfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_closesocketfunction/"
description: "CURLOPT_CLOSESOCKETFUNCTION – callback to socket close replacement function"
---

<p>CURLOPT_CLOSESOCKETFUNCTION &#8211; callback to socket close replacement function</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> int closesocket_callback(void *clientp, curl_socket_t item); </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CLOSESOCKETFUNCTION, closesocket_callback);</p>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl instead of the <i><a href="/docs/linux/man/3-close/">close</a>(3)</i> or <i><a href="/docs/linux/man/3-closesocket/">closesocket</a>(3)</i> call when sockets are closed (not for any other file descriptors). This is pretty much the reverse to the <i><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a>(3)</i> option. Return 0 to signal success and 1 if there was an error. </p>
<p> The <i>clientp</i> pointer is set with <i><a href="/docs/linux/man/3-curlopt_closesocketdata/">CURLOPT_CLOSESOCKETDATA</a>(3)</i>. <i>item</i> is the socket libcurl wants to be closed.</p>
<h2>Default</h2>
<p>By default libcurl uses the standard socket close function.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.7</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_closesocketdata/">CURLOPT_CLOSESOCKETDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a></code>(3),</p>
