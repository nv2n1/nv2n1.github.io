---
title: "curlopt_cookiefile(3)"
name: "curlopt_cookiefile"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_cookiefile/"
description: "CURLOPT_COOKIEFILE – file name to read cookies from"
---

<p>CURLOPT_COOKIEFILE &#8211; file name to read cookies from</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_COOKIEFILE, char *filename);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It should point to the file name of your file holding cookie data to read. The cookie data can be in either the old Netscape / Mozilla cookie data format or just regular HTTP-style headers dumped to a file. </p>
<p> It also enables the cookie engine, making libcurl parse and send cookies on subsequent requests with this handle. </p>
<p> Given an empty or non-existing file or by passing the empty string (&quot;&quot;) to this option, you can enable the cookie engine without reading any initial cookies. </p>
<p> This option only <code>reads</code> cookies. To make libcurl write cookies to file, see <i><a href="/docs/linux/man/3-curlopt_cookiejar/">CURLOPT_COOKIEJAR</a>(3)</i>. </p>
<p> If you use this option multiple times, you just add more files to read. Subsequent files will add more cookies.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>As long as HTTP is supported</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cookie/">CURLOPT_COOKIE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookiejar/">CURLOPT_COOKIEJAR</a></code>(3),</p>
