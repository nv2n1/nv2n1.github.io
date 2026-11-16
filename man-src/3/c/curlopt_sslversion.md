---
title: "curlopt_sslversion(3)"
name: "curlopt_sslversion"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslversion/"
description: "CURLOPT_SSLVERSION – set preferred TLS/SSL version"
---

<p>CURLOPT_SSLVERSION &#8211; set preferred TLS/SSL version</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLVERSION, long version);</p>
<h2>Description</h2>
<p>Pass a long as parameter to control which version of SSL/TLS to attempt to use. </p>
<p> Use one of the available defines for this purpose. The available options are:</p>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>CURL_SSLVERSION_DEFAULT</dt>
<dd>The default action. This will attempt to figure out the remote SSL protocol version.</dd>
<dt>CURL_SSLVERSION_TLSv1</dt>
<dd>TLSv1.x</dd>
<dt>CURL_SSLVERSION_SSLv2</dt>
<dd>SSLv2</dd>
<dt>CURL_SSLVERSION_SSLv3</dt>
<dd>SSLv3</dd>
<dt>CURL_SSLVERSION_TLSv1_0</dt>
<dd>TLSv1.0 (Added in 7.34.0)</dd>
<dt>CURL_SSLVERSION_TLSv1_1</dt>
<dd>TLSv1.1 (Added in 7.34.0)</dd>
<dt>CURL_SSLVERSION_TLSv1_2</dt>
<dd>TLSv1.2 (Added in 7.34.0)</dd></dl>
</dl>
<h2>Default</h2>
<p>CURL_SSLVERSION_DEFAULT</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="https://example.com">https://example.com</a>&quot;);
 /* ask libcurl to use TLS version 1.0 or later */
 curl_easy_setopt(curl, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>SSLv2 is disabled by default since 7.18.1. Other SSL versions availability may vary depending on which backend libcurl has been built to use. </p>
<p> SSLv3 is disabled by default since 7.39.0.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_use_ssl/">CURLOPT_USE_SSL</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_http_version/">CURLOPT_HTTP_VERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ipresolve/">CURLOPT_IPRESOLVE</a></code>(3)</p>
