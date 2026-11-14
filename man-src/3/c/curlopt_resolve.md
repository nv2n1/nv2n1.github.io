---
title: "curlopt_resolve(3)"
name: "curlopt_resolve"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_resolve/"
description: "CURLOPT_RESOLVE – provide custom host name to IP address resolves"
---

<p>CURLOPT_RESOLVE &#8211; provide custom host name to IP address resolves</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RESOLVE,
 struct curl_slist *hosts);</pre>
<h2>Description</h2>
<p>Pass a pointer to a linked list of strings with host name resolve information to use for requests with this handle. The linked list should be a fully valid list of <code>struct curl_slist</code> structs properly filled in. Use <i><a href="/docs/linux/man/3-curl_slist_append/">curl_slist_append</a>(3)</i> to create the list and <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> to clean up an entire list. </p>
<p> Each single name resolve string should be written using the format HOST:PORT:ADDRESS where HOST is the name libcurl will try to resolve, PORT is the port number of the service where libcurl wants to connect to the HOST and ADDRESS is the numerical IP address. If libcurl is built to support IPv6, ADDRESS can of course be either IPv4 or IPv6 style addressing. </p>
<p> This option effectively pre-populates the DNS cache with entries for the host+port pair so redirects and everything that operations against the HOST+PORT will instead use your provided ADDRESS. Addresses to set with <i>CURL_RESOLVE</i> will not time-out from the DNS cache like ordinary entries. </p>
<p> You can remove names from the DNS cache again, to stop providing these fake resolves, by including a string in the linked list that uses the format &quot;-HOST:PORT&quot;. The host name must be prefixed with a dash, and the host name and port number must exactly match what was already added previously.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>CURL *curl;
struct curl_slist *host = NULL;
host = curl_slist_append(NULL, &quot;example.com:80:127.0.0.1&quot;);
curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_RESOLVE, host);
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 res = curl_easy_perform(curl);
 /* always cleanup */
 curl_easy_cleanup(curl);
}
curl_slist_free_all(host);</pre>
<h2>Availability</h2>
<p>Added in 7.21.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ipresolve/">CURLOPT_IPRESOLVE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_dns_cache_timeout/">CURLOPT_DNS_CACHE_TIMEOUT</a></code>(3),</p>
