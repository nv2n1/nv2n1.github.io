---
title: "curlopt_http200aliases(3)"
name: "curlopt_http200aliases"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_http200aliases/"
description: "CURLOPT_HTTP200ALIASES – specify alternative matches for HTTP 200 OK"
---

<p>CURLOPT_HTTP200ALIASES &#8211; specify alternative matches for HTTP 200 OK</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTP200ALIASES,
 struct curl_slist *aliases);</pre>
<h2>Description</h2>
<p>Pass a pointer to a linked list of <i>aliases</i> to be treated as valid HTTP 200 responses. Some servers respond with a custom header response line. For example, IceCast servers respond with &quot;ICY 200 OK&quot;. By including this string in your list of aliases, the response will be treated as a valid HTTP header line such as &quot;HTTP/1.0 200 OK&quot;. </p>
<p> The linked list should be a fully valid list of struct curl_slist structs, and be properly filled in. Use <i><a href="/docs/linux/man/3-curl_slist_append/">curl_slist_append</a>(3)</i> to create the list and <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> to clean up an entire list. </p>
<p> The alias itself is not parsed for any version strings. The protocol is assumed to match HTTP 1.0 when an alias match.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_http_version/">CURLOPT_HTTP_VERSION</a></code>(3),</p>
