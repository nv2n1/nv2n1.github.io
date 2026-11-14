---
title: "curl_easy_send(3)"
name: "curl_easy_send"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_send/"
description: "curl_easy_send – sends raw data over an \"easy\" connection"
---

<h2>NAME</h2>
<p> curl_easy_send &#8211; sends raw data over an &quot;easy&quot; connection</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/easy.h&gt;</code> </p>
<p> <code>CURLcode curl_easy_send( CURL *</code><i>curl</i><code>, const void *</code><i>buffer</i><code>,</code> <code> size_t </code><i>buflen</i><code>, size_t *</code><i>n</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This function sends arbitrary data over the established connection. You may use it together with <i><a href="/docs/linux/man/3-curl_easy_recv/">curl_easy_recv</a>(3)</i> to implement custom protocols using libcurl. This functionality can be particularly useful if you use proxies and/or SSL encryption: libcurl will take care of proxy negotiation and connection set-up. </p>
<p> <code>buffer</code> is a pointer to the data of length <code>buflen</code> that you want sent. The variable <code>n</code> points to will receive the number of sent bytes. </p>
<p> To establish the connection, set <code>CURLOPT_CONNECT_ONLY</code> option before calling <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i>. Note that <i><a href="/docs/linux/man/3-curl_easy_send/">curl_easy_send</a>(3)</i> will not work on connections that were created without this option. </p>
<p> You must ensure that the socket is writable before calling <i><a href="/docs/linux/man/3-curl_easy_send/">curl_easy_send</a>(3)</i>, otherwise the call will return <code>CURLE_AGAIN</code> &#8211; the socket is used in non-blocking mode internally. Use <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> with <code>CURLINFO_LASTSOCKET</code> to obtain the socket; use your operating system facilities like <i><a href="/docs/linux/man/2-select/">select</a>(2)</i> to check if it can be written to.</p>
<h2>AVAILABILITY</h2>
<p> Added in 7.18.2.</p>
<h2>RETURN VALUE</h2>
<p> On success, returns <code>CURLE_OK</code> and stores the number of bytes actually sent into <code>*n</code>. Note that this may very well be less than the amount you wanted to send. </p>
<p> On failure, returns the appropriate error code. </p>
<p> If there&#8217;s no socket available to use from the previous transfer, this function returns CURLE_UNSUPPORTED_PROTOCOL.</p>
<h2>EXAMPLE</h2>
<p> See <code>sendrecv.c</code> in <code>docs/examples</code> directory for usage example.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_recv/">curl_easy_recv</a></code>(3) </p>
<h2>Index</h2>
