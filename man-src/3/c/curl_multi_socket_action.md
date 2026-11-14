---
title: "curl_multi_socket_action(3)"
name: "curl_multi_socket_action"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_socket_action/"
description: "curl_multi_socket_action – reads/writes available data given an action"
---

<h2>NAME</h2>
<p> curl_multi_socket_action &#8211; reads/writes available data given an action</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;curl/curl.h&gt;
CURLMcode curl_multi_socket_action(CURLM *multi_handle,
                                   curl_socket_t sockfd, int ev_bitmask,
                                   int *running_handles);
</code></pre>
<h2>DESCRIPTION</h2>
<p> When the application has detected action on a socket handled by libcurl, it should call <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> with the <code>sockfd</code> argument set to the socket with the action. When the events on a socket are known, they can be passed as an events bitmask <code>ev_bitmask</code> by first setting <code>ev_bitmask</code> to 0, and then adding using bitwise OR (|) any combination of events to be chosen from CURL_CSELECT_IN, CURL_CSELECT_OUT or CURL_CSELECT_ERR. When the events on a socket are unknown, pass 0 instead, and libcurl will test the descriptor internally. </p>
<p> At return, the integer <code>running_handles</code> points to will contain the number of running easy handles within the multi handle. When this number reaches zero, all transfers are complete/done. When you call <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> on a specific socket and the counter decreases by one, it DOES NOT necessarily mean that this exact socket/transfer is the one that completed. Use <i><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a>(3)</i> to figure out which easy handle that completed. </p>
<p> The <code><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</code> functions inform the application about updates in the socket (file descriptor) status by doing none, one, or multiple calls to the socket callback function set with the CURLMOPT_SOCKETFUNCTION option to <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i>. They update the status with changes since the previous time the callback was called. </p>
<p> Get the timeout time by setting the <i>CURLMOPT_TIMERFUNCTION</i> option with <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i>. Your application will then get called with information on how long to wait for socket actions at most before doing the timeout action: call the <code><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</code> function with the <code>sockfd</code> argument set to CURL_SOCKET_TIMEOUT. You can also use the <i><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a>(3)</i> function to poll the value at any given time, but for an event-based system using the callback is far better than relying on polling the timeout value.</p>
<h2>CALLBACK DETAILS</h2>
<p> The socket <code>callback</code> function uses a prototype like this </p>
<pre><code>
int curl_socket_callback(CURL *easy,      /* easy handle */
                         curl_socket_t s, /* socket */
                         int action,      /* see values below */
                         void *userp,     /* private callback pointer */
                         void *socketp);  /* private socket pointer */
</code></pre>
<p> The callback MUST return 0. </p>
<p> The <i>easy</i> argument is a pointer to the easy handle that deals with this particular socket. Note that a single handle may work with several sockets simultaneously. </p>
<p> The <i>s</i> argument is the actual socket value as you use it within your system. </p>
<p> The <i>action</i> argument to the callback has one of five values:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CURL_POLL_NONE (0)</p>
<dd> register, not interested in readiness (yet)</p>
<dt>CURL_POLL_IN (1)</p>
<dd> register, interested in read readiness</p>
<dt>CURL_POLL_OUT (2)</p>
<dd> register, interested in write readiness</p>
<dt>CURL_POLL_INOUT (3)</p>
<dd> register, interested in both read and write readiness</p>
<dt>CURL_POLL_REMOVE (4)</p>
<dd> unregister</dl>
</dl>
<p> The <i>socketp</i> argument is a private pointer you have previously set with <i><a href="/docs/linux/man/3-curl_multi_assign/">curl_multi_assign</a>(3)</i> to be associated with the <i>s</i> socket. If no pointer has been set, socketp will be NULL. This argument is of course a service to applications that want to keep certain data or structs that are strictly associated to the given socket. </p>
<p> The <i>userp</i> argument is a private pointer you have previously set with <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i> and the CURLMOPT_SOCKETDATA option.</p>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code. </p>
<p> Before version 7.20.0: If you receive <i>CURLM_CALL_MULTI_PERFORM</i>, this basically means that you should call <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> again before you wait for more actions on libcurl&#8217;s sockets. You don&#8217;t have to do it immediately, but the return code means that libcurl may have more data available to return or that there may be more data to send off before it is &quot;satisfied&quot;. </p>
<p> The return code from this function is for the whole multi stack. Problems still might have occurred on individual transfers even when one of these functions return OK.</p>
<h2>TYPICAL USAGE</h2>
<p> 1. Create a multi handle </p>
<p> 2. Set the socket callback with CURLMOPT_SOCKETFUNCTION </p>
<p> 3. Set the timeout callback with CURLMOPT_TIMERFUNCTION, to get to know what timeout value to use when waiting for socket activities. </p>
<p> 4. Add easy handles with curl_multi_add_handle() </p>
<p> 5. Provide some means to manage the sockets libcurl is using, so you can check them for activity. This can be done through your application code, or by way of an external library such as libevent or glib. </p>
<p> 6. Call curl_multi_socket_action(&#8230;CURL_SOCKET_TIMEOUT&#8230;) to kickstart everything. To get one or more callbacks called. </p>
<p> 7. Wait for activity on any of libcurl&#8217;s sockets, use the timeout value your callback has been told </p>
<p> 8, When activity is detected, call curl_multi_socket_action() for the socket(s) that got action. If no activity is detected and the timeout expires, call <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> with <i>CURL_SOCKET_TIMEOUT</i></p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.15.4, and is deemed stable since 7.16.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a></code>(3), <code>the hiperfifo.c example</code> </p>
<h2>Index</h2>
