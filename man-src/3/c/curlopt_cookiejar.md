---
title: "curlopt_cookiejar(3)"
name: "curlopt_cookiejar"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_cookiejar/"
description: "CURLOPT_COOKIEJAR – file name to store cookies to"
---

<p>CURLOPT_COOKIEJAR &#8211; file name to store cookies to</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_COOKIEJAR, char *filename);</p>
<h2>Description</h2>
<p>Pass a <i>filename</i> as char *, zero terminated. This will make libcurl write all internally known cookies to the specified file when <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> is called. If no cookies are known, no file will be created. Specify &quot;-&quot; as filename to instead have the cookies written to stdout. Using this option also enables cookies for this session, so if you for example follow a location it will make matching cookies get sent accordingly. </p>
<p> Note that libcurl doesn&#8217;t read any cookies from the cookie jar. If you want to read cookies from a file, use <i><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a>(3)</i>. </p>
<p> If the cookie jar file can&#8217;t be created or written to (when the <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> is called), libcurl will not and cannot report an error for this. Using <i><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a>(3)</i> will get a warning to display, but that is the only visible feedback you get about this possibly lethal situation.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookie/">CURLOPT_COOKIE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookielist/">CURLOPT_COOKIELIST</a></code>(3),</p>
