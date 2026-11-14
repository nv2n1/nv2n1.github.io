---
title: "curlopt_sockoptfunction(3)"
name: "curlopt_sockoptfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sockoptfunction/"
description: "CURLOPT_SOCKOPTFUNCTION – set callback for setting socket options"
---

<p>CURLOPT_SOCKOPTFUNCTION &#8211; set callback for setting socket options</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
typedef enum {
 CURLSOCKTYPE_IPCXN, /* socket created for a specific IP connection */
 CURLSOCKTYPE_ACCEPT, /* socket created by accept() call */
 CURLSOCKTYPE_LAST /* never use */
} curlsocktype;
#define CURL_SOCKOPT_OK 0
#define CURL_SOCKOPT_ERROR 1 /* causes libcurl to abort and return
 CURLE_ABORTED_BY_CALLBACK */
#define CURL_SOCKOPT_ALREADY_CONNECTED 2
int sockopt_callback(void *clientp,
 curl_socket_t curlfd,
 curlsocktype purpose);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SOCKOPTFUNCTION, sockopt_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> When set, this callback function gets called by libcurl when the socket has been created, but before the connect call to allow applications to change specific socket options. The callback&#8217;s <i>purpose</i> argument identifies the exact purpose for this particular socket: </p>
<p> <i>CURLSOCKTYPE_IPCXN</i> for actively created connections or since 7.28.0 <i>CURLSOCKTYPE_ACCEPT</i> for FTP when the connection was setup with PORT/EPSV (in earlier versions these sockets weren&#8217;t passed to this callback). </p>
<p> Future versions of libcurl may support more purposes. libcurl passes the newly created socket descriptor to the callback in the <i>curlfd</i> parameter so additional setsockopt() calls can be done at the user&#8217;s discretion. </p>
<p> The <i>clientp</i> pointer contains whatever user-defined value set using the <i><a href="/docs/linux/man/3-curlopt_sockoptdata/">CURLOPT_SOCKOPTDATA</a>(3)</i> function. </p>
<p> Return <i>CURL_SOCKOPT_OK</i> from the callback on success. Return <i>CURL_SOCKOPT_ERROR</i> from the callback function to signal an unrecoverable error to the library and it will close the socket and return <i>CURLE_COULDNT_CONNECT</i>. Alternatively, the callback function can return <i>CURL_SOCKOPT_ALREADY_CONNECTED</i>, to tell libcurl that the socket is already connected and then libcurl will not attempt to connect it. This allows an application to pass in an already connected socket with <i><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a>(3)</i> and then have this function make libcurl not attempt to connect (again).</p>
<h2>Default</h2>
<p>By default, this callback is NULL and unused.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.0. The <i>CURL_SOCKOPT_ALREADY_CONNECTED</i> return code was added in 7.21.5.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sockoptdata/">CURLOPT_SOCKOPTDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a></code>(3),</p>
