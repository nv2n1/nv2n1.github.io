---
title: "curlopt_private(3)"
name: "curlopt_private"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_private/"
description: "CURLOPT_PRIVATE – store a private pointer"
---

<p>CURLOPT_PRIVATE &#8211; store a private pointer</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PRIVATE, void *pointer);</p>
<h2>Description</h2>
<p>Pass a void * as parameter, pointing to data that should be associated with this curl handle. The pointer can subsequently be retrieved using <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> with the CURLINFO_PRIVATE option. libcurl itself never does nothing with this data.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3),</p>
