---
title: "curlmopt_socketfunction(3)"
name: "curlmopt_socketfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_socketfunction/"
description: "CURLMOPT_SOCKETFUNCTION – callback informed about what to wait for"
---

<p>CURLMOPT_SOCKETFUNCTION &#8211; callback informed about what to wait for</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
int socket_callback(CURL *easy, /* easy handle */
 curl_socket_t s, /* socket */
 int what, /* see above */
 void *userp, /* private callback pointer */
 void *socketp); /* private socket pointer */
CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_SOCKETFUNCTION, socket_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> When the <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> function runs, it informs the application about updates in the socket (file descriptor) status by doing none, one, or multiple calls to the <code>socket_callback</code>. The callback gets status updates with changes since the previous time the callback was called. If the given callback pointer is NULL, no callback will be called. Set the callback&#8217;s <code>userp</code> argument with <i><a href="/docs/linux/man/3-curlmopt_socketdata/">CURLMOPT_SOCKETDATA</a>(3)</i>. See <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> for more details on how the callback is used and should work.</p>
<h2>Default</h2>
<p>NULL (no callback)</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.4</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_socketdata/">CURLMOPT_SOCKETDATA</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_timerfunction/">CURLMOPT_TIMERFUNCTION</a></code>(3)</p>
