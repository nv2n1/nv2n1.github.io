---
title: "curlopt_connecttimeout(3)"
name: "curlopt_connecttimeout"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_connecttimeout/"
description: "CURLOPT_CONNECTTIMEOUT – timeout for the connect phase"
---

<p>CURLOPT_CONNECTTIMEOUT &#8211; timeout for the connect phase</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CONNECTTIMEOUT, long timeout);</p>
<h2>Description</h2>
<p>Pass a long. It should contain the maximum time in seconds that you allow the connection phase to the server to take. This only limits the connection phase, it has no impact once it has connected. Set to zero to switch to the default built-in connection timeout &#8211; 300 seconds. See also the <i><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a>(3)</i> option. </p>
<p> In unix-like systems, this might cause signals to be used unless <i><a href="/docs/linux/man/3-curlopt_nosignal/">CURLOPT_NOSIGNAL</a>(3)</i> is set.</p>
<h2>Default</h2>
<p>300</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a></code>(3),</p>
