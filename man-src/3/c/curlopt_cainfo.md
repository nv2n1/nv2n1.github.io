---
title: "curlopt_cainfo(3)"
name: "curlopt_cainfo"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_cainfo/"
description: "CURLOPT_CAINFO – path to Certificate Authority (CA) bundle"
---

<p>CURLOPT_CAINFO &#8211; path to Certificate Authority (CA) bundle</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CAINFO, char *path);</p>
<h2>Description</h2>
<p>Pass a char * to a zero terminated string naming a file holding one or more certificates to verify the peer with. </p>
<p> If <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> is zero and you avoid verifying the server&#8217;s certificate, <i><a href="/docs/linux/man/3-curlopt_cainfo/">CURLOPT_CAINFO</a>(3)</i> need not even indicate an accessible file. </p>
<p> This option is by default set to the system path where libcurl&#8217;s cacert bundle is assumed to be stored, as established at build time. </p>
<p> If curl is built against the NSS SSL library, the NSS PEM PKCS#11 module (libnsspem.so) needs to be available for this option to work properly.</p>
<h2>Default</h2>
<p>Built-in system specific</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_capath/">CURLOPT_CAPATH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a></code>(3),</p>
