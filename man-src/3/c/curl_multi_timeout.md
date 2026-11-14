---
title: "curl_multi_timeout(3)"
name: "curl_multi_timeout"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_timeout/"
description: "curl_multi_timeout – how long to wait for action before proceeding"
---

<h2>NAME</h2>
<p> curl_multi_timeout &#8211; how long to wait for action before proceeding</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_timeout(CURLM *multi_handle, long *timeout);</p>
<h2>DESCRIPTION</h2>
<p> An application using the libcurl multi interface should call <code><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a>(3)</code> to figure out how long it should wait for socket actions &#8211; at most &#8211; before proceeding. </p>
<p> Proceeding means either doing the socket-style timeout action: call the <code><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</code> function with the <code>sockfd</code> argument set to CURL_SOCKET_TIMEOUT, or call <code><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</code> if you&#8217;re using the simpler and older multi interface approach. </p>
<p> The timeout value returned in the long <code>timeout</code> points to, is in number of milliseconds at this very moment. If 0, it means you should proceed immediately without waiting for anything. If it returns -1, there&#8217;s no timeout at all set. </p>
<p> An application that uses the multi_socket API SHOULD not use this function, but SHOULD instead use <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i> and its CURLMOPT_TIMERFUNCTION option for proper and desired behavior. </p>
<p> Note: if libcurl returns a -1 timeout here, it just means that libcurl currently has no stored timeout value. You must not wait too long (more than a few seconds perhaps) before you call curl_multi_perform() again.</p>
<h2>RETURN VALUE</h2>
<p> The standard CURLMcode for multi interface error codes.</p>
<h2>TYPICAL USAGE</h2>
<p> Call <code><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a>(3)</code>, then wait for action on the sockets. You figure out which sockets to wait for by calling <code><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a>(3)</code> or by a previous call to <code><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a>(3)</code>.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.15.4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a></code>(3) </p>
<h2>Index</h2>
