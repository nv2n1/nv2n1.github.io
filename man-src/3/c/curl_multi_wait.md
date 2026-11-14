---
title: "curl_multi_wait(3)"
name: "curl_multi_wait"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_wait/"
description: "curl_multi_wait – polls on all easy handles in a multi handle"
---

<h2>NAME</h2>
<p> curl_multi_wait &#8211; polls on all easy handles in a multi handle</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;curl/curl.h&gt;
CURLMcode curl_multi_wait(CURLM *multi_handle,
                          struct curl_waitfd extra_fds[],
                          unsigned int extra_nfds,
                          int timeout_ms,
                          int *numfds);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function polls on all file descriptors used by the curl easy handles contained in the given multi handle set. It will block until activity is detected on at least one of the handles or <i>timeout_ms</i> has passed. Alternatively, if the multi handle has a pending internal timeout that has a shorter expiry time than <i>timeout_ms</i>, that shorter time will be used instead to make sure timeout accuracy is reasonably kept. </p>
<p> The calling application may pass additional curl_waitfd structures which are similar to <i><a href="/docs/linux/man/2-poll/">poll</a>(2)</i>&#8216;s pollfd structure to be waited on in the same call. </p>
<p> On completion, if <i>numfds</i> is supplied, it will be populated with the number of file descriptors on which interesting events occured. </p>
<p> If no extra file descriptors are provided and libcurl has no file descriptor to offer to wait for, this function will return immediately. </p>
<p> This function is encouraged to be used instead of <a href="/docs/linux/man/3-select/">select</a>(3) when using the multi interface to allow applications to easier circumvent the common problem with 1024 maximum file descriptors.</p>
<h2>curl_waitfd</h2>
<pre><code>
struct curl_waitfd {
    curl_socket_t fd;
    short events;
    short revents;
};
</code></pre>
<dl>
<dt>CURL_WAIT_POLLIN</p>
<dd> Bit flag to curl_waitfd.events indicating the socket should poll on read events such as new data received.</p>
<dt>CURL_WAIT_POLLPRI</p>
<dd> Bit flag to curl_waitfd.events indicating the socket should poll on high priority read events such as out of band data.</p>
<dt>CURL_WAIT_POLLOUT</p>
<dd> Bit flag to curl_waitfd.events indicating the socket should poll on write events such as the socket being clear to write without blocking.</dl>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code. See <i><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a>(3)</i></p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.28.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a></code>(3) </p>
<h2>Index</h2>
