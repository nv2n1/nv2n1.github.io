---
title: "curl_multi_setopt(3)"
name: "curl_multi_setopt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_setopt/"
description: "curl_multi_setopt – set options for a curl multi handle"
---

<h2>NAME</h2>
<p> curl_multi_setopt &#8211; set options for a curl multi handle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM * multi_handle, CURLMoption option, param);</p>
<h2>DESCRIPTION</h2>
<p> curl_multi_setopt() is used to tell a libcurl multi handle how to behave. By using the appropriate options to <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i>, you can change libcurl&#8217;s behaviour when using that multi handle. All options are set with the <i>option</i> followed by the parameter <i>param</i>. That parameter can be a <code>long</code>, a <code>function pointer</code>, an <code>object pointer</code> or a <code>curl_off_t</code> type, depending on what the specific option expects. Read this manual carefully as bad input values may cause libcurl to behave badly! You can only set one option in each function call. </p>
<h2>OPTIONS</h2>
<dl>
<dt>CURLMOPT_SOCKETFUNCTION</p>
<dd> Pass a pointer to a function matching the <code>curl_socket_callback</code> prototype. The <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> function informs the application about updates in the socket (file descriptor) status by doing none, one, or multiple calls to the curl_socket_callback given in the <code>param</code> argument. They update the status with changes since the previous time a <i><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a>(3)</i> function was called. If the given callback pointer is NULL, no callback will be called. Set the callback&#8217;s <code>userp</code> argument with <i>CURLMOPT_SOCKETDATA</i>. See <i><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a>(3)</i> for more callback details.</p>
<dt>CURLMOPT_SOCKETDATA</p>
<dd> Pass a pointer to whatever you want passed to the <code>curl_socket_callback</code>&#8216;s forth argument, the userp pointer. This is not used by libcurl but only passed-thru as-is. Set the callback pointer with <i>CURLMOPT_SOCKETFUNCTION</i>.</p>
<dt>CURLMOPT_PIPELINING</p>
<dd> Pass a long set to 1 to enable or 0 to disable. Enabling pipelining on a multi handle will make it attempt to perform HTTP Pipelining as far as possible for transfers using this handle. This means that if you add a second request that can use an already existing connection, the second request will be &quot;piped&quot; on the same connection rather than being executed in parallel. (Added in 7.16.0)</p>
<dt>CURLMOPT_TIMERFUNCTION</p>
<dd> Pass a pointer to a function matching the <code>curl_multi_timer_callback</code> prototype. This function will then be called when the timeout value changes. The timeout value is at what latest time the application should call one of the &quot;performing&quot; functions of the multi interface (<i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> and <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>) &#8211; to allow libcurl to keep timeouts and retries etc to work. A timeout value of -1 means that there is no timeout at all, and 0 means that the timeout is already reached. Libcurl attempts to limit calling this only when the fixed future timeout time actually changes. See also <i>CURLMOPT_TIMERDATA</i>. This callback can be used instead of, or in addition to, <i><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a>(3)</i>. (Added in 7.16.0)</p>
<dt>CURLMOPT_TIMERDATA</p>
<dd> Pass a pointer to whatever you want passed to the <code>curl_multi_timer_callback</code>&#8216;s third argument, the userp pointer. This is not used by libcurl but only passed-thru as-is. Set the callback pointer with <i>CURLMOPT_TIMERFUNCTION</i>. (Added in 7.16.0)</p>
<dt>CURLMOPT_MAXCONNECTS</p>
<dd> Pass a long. The set number will be used as the maximum amount of simultaneously open connections that libcurl may cache. Default is 10, and libcurl will enlarge the size for each added easy handle to make it fit 4 times the number of added easy handles. </p>
<p> By setting this option, you can prevent the cache size from growing beyond the limit set by you. </p>
<p> When the cache is full, curl closes the oldest one in the cache to prevent the number of open connections from increasing. </p>
<p> This option is for the multi handle&#8217;s use only, when using the easy interface you should instead use the <i>CURLOPT_MAXCONNECTS</i> option. </p>
<p> (Added in 7.16.3)</dl>
<h2>RETURNS</h2>
<p> The standard CURLMcode for multi interface error codes. Note that it returns a CURLM_UNKNOWN_OPTION if you try setting an option that this version of libcurl doesn&#8217;t know of.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.15.4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a></code>(3) </p>
<h2>Index</h2>
