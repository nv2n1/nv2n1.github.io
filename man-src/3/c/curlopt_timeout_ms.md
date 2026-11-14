---
title: "curlopt_timeout_ms(3)"
name: "curlopt_timeout_ms"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_timeout_ms/"
description: "CURLOPT_TIMEOUT_MS – set maximum time the request is allowed to take"
---

<p>CURLOPT_TIMEOUT_MS &#8211; set maximum time the request is allowed to take</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TIMEOUT_MS, long timeout);</p>
<h2>Description</h2>
<p>Pass a long as parameter containing <i>timeout</i> &#8211; the maximum time in milliseconds that you allow the libcurl transfer operation to take. Normally, name lookups can take a considerable time and limiting operations to less than a few minutes risk aborting perfectly normal operations. This option may cause libcurl to use the SIGALRM signal to timeout system calls. </p>
<p> If libcurl is built to use the standard system name resolver, that portion of the transfer will still use full-second resolution for timeouts with a minimum timeout allowed of one second. </p>
<p> In unix-like systems, this might cause signals to be used unless <i><a href="/docs/linux/man/3-curlopt_nosignal/">CURLOPT_NOSIGNAL</a>(3)</i> is set. </p>
<p> If both <i><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_timeout_ms/">CURLOPT_TIMEOUT_MS</a>(3)</i> are set, the value set last will be used. </p>
<p> Since this puts a hard limit for how long time a request is allowed to take, it has limited use in dynamic use cases with varying transfer times. You are then advised to explore <i><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a>(3)</i>, <i><a href="/docs/linux/man/3-curlopt_low_speed_time/">CURLOPT_LOW_SPEED_TIME</a>(3)</i> or using <i><a href="/docs/linux/man/3-curlopt_progressfunction/">CURLOPT_PROGRESSFUNCTION</a>(3)</i> to implement your own timeout logic.</p>
<h2>Default</h2>
<p>Default timeout is 0 (zero) which means it never times out during transfer.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_timeout/">CURLOPT_TIMEOUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_connecttimeout/">CURLOPT_CONNECTTIMEOUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_low_speed_limit/">CURLOPT_LOW_SPEED_LIMIT</a></code>(3),</p>
