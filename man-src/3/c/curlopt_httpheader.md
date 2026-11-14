---
title: "curlopt_httpheader(3)"
name: "curlopt_httpheader"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_httpheader/"
description: "CURLOPT_HTTPHEADER – set custom HTTP headers"
---

<p>CURLOPT_HTTPHEADER &#8211; set custom HTTP headers</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTPHEADER, struct curl_slist *headers);</p>
<h2>Description</h2>
<p>Pass a pointer to a linked list of HTTP headers to pass to the server and/or proxy in your HTTP request. The same list can be used for both host and proxy requests! </p>
<p> The linked list should be a fully valid list of <code>struct curl_slist</code> structs properly filled in. Use <i><a href="/docs/linux/man/3-curl_slist_append/">curl_slist_append</a>(3)</i> to create the list and <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> to clean up an entire list. If you add a header that is otherwise generated and used by libcurl internally, your added one will be used instead. If you add a header with no content as in &#8216;Accept:&#8217; (no data on the right side of the colon), the internally used header will get disabled. With this option you can add new headers, replace internal headers and remove internal headers. To add a header with no content (nothing to the right side of the colon), use the form &#8216;MyHeader;&#8217; (note the ending semicolon). </p>
<p> The headers included in the linked list <code>must not</code> be CRLF-terminated, because libcurl adds CRLF after each header item. Failure to comply with this will result in strange bugs because the server will most likely ignore part of the headers you specified. </p>
<p> The first line in a request (containing the method, usually a GET or POST) is not a header and cannot be replaced using this option. Only the lines following the request-line are headers. Adding this method line in this list of headers will only cause your request to send an invalid header. Use <i><a href="/docs/linux/man/3-curlopt_customrequest/">CURLOPT_CUSTOMREQUEST</a>(3)</i> to change the method. </p>
<p> When this option is passed to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>, libcurl will not copy the entire list so you <code>must</code> keep it around until you no longer use this <i>handle</i> for a transfer before you call <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> on the list. </p>
<p> Pass a NULL to this option to reset back to no custom headers. </p>
<p> The most commonly replaced headers have &quot;shortcuts&quot; in the options <i><a href="/docs/linux/man/3-curlopt_cookie/">CURLOPT_COOKIE</a>(3)</i>, <i><a href="/docs/linux/man/3-curlopt_useragent/">CURLOPT_USERAGENT</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_referer/">CURLOPT_REFERER</a>(3)</i>. </p>
<p> There&#8217;s an alternative option that sets or replaces headers only for requests that are sent with CONNECT to a proxy: <i><a href="/docs/linux/man/3-curlopt_proxyheader/">CURLOPT_PROXYHEADER</a>(3)</i>. Use <i><a href="/docs/linux/man/3-curlopt_headeropt/">CURLOPT_HEADEROPT</a>(3)</i> to control the behavior.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>As long as HTTP is enabled</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_customrequest/">CURLOPT_CUSTOMREQUEST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_headeropt/">CURLOPT_HEADEROPT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyheader/">CURLOPT_PROXYHEADER</a></code>(3)</p>
