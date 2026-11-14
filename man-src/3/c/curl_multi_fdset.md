---
title: "curl_multi_fdset(3)"
name: "curl_multi_fdset"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_fdset/"
description: "curl_multi_fdset – extracts file descriptor information from a multi handle"
---

<h2>NAME</h2>
<p> curl_multi_fdset &#8211; extracts file descriptor information from a multi handle</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;curl/curl.h&gt;
CURLMcode curl_multi_fdset(CURLM *multi_handle,
                           fd_set *read_fd_set,
                           fd_set *write_fd_set,
                           fd_set *exc_fd_set,
                           int *max_fd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function extracts file descriptor information from a given multi_handle. libcurl returns its fd_set sets. The application can use these to select() on, but be sure to FD_ZERO them before calling this function as <i><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a>(3)</i> only adds its own descriptors, it doesn&#8217;t zero or otherwise remove any others. The <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> function should be called as soon as one of them is ready to be read from or written to. </p>
<p> If no file descriptors are set by libcurl, <i>max_fd</i> will contain -1 when this function returns. Otherwise it will contain the higher descriptor number libcurl set. When libcurl returns -1 in <i>max_fd</i>, it is because libcurl currently does something that isn&#8217;t possible for your application to monitor with a socket and unfortunately you can then not know exactly when the current action is completed using select(). When max_fd returns with -1, you need to wait a while and then proceed and call <i>curl_multi_perform</i> anyway. How long to wait? I would suggest 100 milliseconds at least, but you may want to test it out in your own particular conditions to find a suitable value. </p>
<p> When doing select(), you should use <code>curl_multi_timeout</code> to figure out how long to wait for action. Call <i>curl_multi_perform</i> even if no activity has been seen on the fd_sets after the timeout expires as otherwise internal retries and timeouts may not work as you&#8217;d think and want. </p>
<p> If one of the sockets used by libcurl happens to be larger than what can be set in an fd_set, which on POSIX systems means that the file descriptor is larger than FD_SETSIZE, then libcurl will try to not set it. Setting a too large file descriptor in an fd_set implies an out of bounds write which can cause crashes, or worse. The effect of NOT storing it will possibly save you from the crash, but will make your program NOT wait for sockets it should wait for&#8230;</p>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code. See <i><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a>(3)</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a></code>(3) </p>
<h2>Index</h2>
