---
title: "curlmopt_timerfunction(3)"
name: "curlmopt_timerfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_timerfunction/"
description: "CURLMOPT_TIMERFUNCTION – set callback to receive timeout values"
---

<p>CURLMOPT_TIMERFUNCTION &#8211; set callback to receive timeout values</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
int timer_callback(CURLM *multi, /* multi handle */
 long timeout_ms, /* see above */
 void *userp); /* private callback pointer */
CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_TIMERFUNCTION, timer_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function will be called when the timeout value changes. The <code>timeout_ms</code> value is at what latest time the application should call one of the &quot;performing&quot; functions of the multi interface (<i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> and <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>) &#8211; to allow libcurl to keep timeouts and retries etc to work. A <code>timeout_ms</code> value of -1 means that there is no timeout at all, and 0 means that the timeout is already expired. libcurl attempts to limit calling this only when the fixed future timeout time actually changes. </p>
<p> The <code>userp</code> pointer is set with <i><a href="/docs/linux/man/3-curlmopt_timerdata/">CURLMOPT_TIMERDATA</a>(3)</i>. </p>
<p> The timer callback should return 0 on success, and -1 on error. This callback can be used instead of, or in addition to, <i><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_timerdata/">CURLMOPT_TIMERDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_socketfunction/">CURLMOPT_SOCKETFUNCTION</a></code>(3),</p>
