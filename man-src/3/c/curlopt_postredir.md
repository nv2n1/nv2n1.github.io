---
title: "curlopt_postredir(3)"
name: "curlopt_postredir"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_postredir/"
description: "CURLOPT_POSTREDIR – how to act on a HTTP POST redirect"
---

<p>CURLOPT_POSTREDIR &#8211; how to act on a HTTP POST redirect</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_POSTREDIR,
 long bitmask);</pre>
<h2>Description</h2>
<p>Pass a bitmask to control how libcurl acts on redirects after POSTs that get a 301, 302 or 303 response back. A parameter with bit 0 set (value <code>CURL_REDIR_POST_301</code>) tells the library to respect RFC2616/10.3.2 and not convert POST requests into GET requests when following a 301 redirection. Setting bit 1 (value <code>CURL_REDIR_POST_302</code>) makes libcurl maintain the request method after a 302 redirect whilst setting bit 2 (value <code>CURL_REDIR_POST_303</code>) makes libcurl maintain the request method after a 303 redirect. The value <code>CURL_REDIR_POST_ALL</code> is a convenience define that sets all three bits. </p>
<p> The non-RFC behaviour is ubiquitous in web browsers, so the library does the conversion by default to maintain consistency. However, a server may require a POST to remain a POST after such a redirection. This option is meaningful only when setting <i><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a>(3)</i>.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* a silly POST example */
 curl_easy_setopt(curl, CURLOPT_POSTFIELDS, &quot;data=true&quot;);
 /* example.com is redirected, so we tell libcurl to send POST on 301, 302 and
 303 HTTP response codes */
 curl_easy_setopt(curl, CURLOPT_POSTREDIR, CURL_REDIR_POST_ALL);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Added in 7.17.1. This option was known as CURLOPT_POST301 up to 7.19.0 as it only supported the 301 then. CURL_REDIR_POST_303 was added in 7.26.0.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a></code>(3),</p>
