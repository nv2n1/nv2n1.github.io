---
title: "curlopt_egdsocket(3)"
name: "curlopt_egdsocket"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_egdsocket/"
description: "CURLOPT_EGDSOCKET – set EGD socket path"
---

<p>CURLOPT_EGDSOCKET &#8211; set EGD socket path</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_EGDSOCKET, char *path);</p>
<h2>Description</h2>
<p>Pass a char * to the zero terminated path name to the Entropy Gathering Daemon socket. It will be used to seed the random engine for SSL.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled. Only the OpenSSL and GnuTLS backends will use this.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_random_file/">CURLOPT_RANDOM_FILE</a></code>(3),</p>
