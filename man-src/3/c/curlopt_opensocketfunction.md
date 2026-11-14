---
title: "curlopt_opensocketfunction(3)"
name: "curlopt_opensocketfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_opensocketfunction/"
description: "CURLOPT_OPENSOCKETFUNCTION – set callback for opening sockets"
---

<p>CURLOPT_OPENSOCKETFUNCTION &#8211; set callback for opening sockets</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
typedef enum {
 CURLSOCKTYPE_IPCXN, /* socket created for a specific IP connection */
 CURLSOCKTYPE_ACCEPT, /* socket created by accept() call */
 CURLSOCKTYPE_LAST /* never use */
} curlsocktype;
struct curl_sockaddr {
 int family;
 int socktype;
 int protocol;
 unsigned int addrlen;
 struct sockaddr addr;
};
curl_socket_t opensocket_callback(void *clientp,
 curlsocktype purpose,
 struct curl_sockaddr *address);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_OPENSOCKETFUNCTION, opensocket_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl instead of the <i><a href="/docs/linux/man/2-socket/">socket</a>(2)</i> call. The callback&#8217;s <i>purpose</i> argument identifies the exact purpose for this particular socket: <i>CURLSOCKTYPE_IPCXN</i> is for IP based connections and <i>CURLSOCKTYPE_ACCEPT</i> is for sockets created after accept() &#8211; such as when doing active FTP. Future versions of libcurl may support more purposes. </p>
<p> The <i>clientp</i> pointer contains whatever user-defined value set using the <i><a href="/docs/linux/man/3-curlopt_opensocketdata/">CURLOPT_OPENSOCKETDATA</a>(3)</i> function. </p>
<p> The callback gets the resolved peer address as the <i>address</i> argument and is allowed to modify the address or refuse to connect completely. The callback function should return the newly created socket or <i>CURL_SOCKET_BAD</i> in case no connection could be established or another error was detected. Any additional <i><a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2)</i> calls can of course be done on the socket at the user&#8217;s discretion. A <i>CURL_SOCKET_BAD</i> return value from the callback function will signal an unrecoverable error to libcurl and it will return <i>CURLE_COULDNT_CONNECT</i> from the function that triggered this callback. This return code can be used for IP address blacklisting. </p>
<p> If you want to pass in a socket with an already established connection, pass the socket back with this callback and then use <i><a href="/docs/linux/man/3-curlopt_sockoptfunction/">CURLOPT_SOCKOPTFUNCTION</a>(3)</i> to signal that it already is connected.</p>
<h2>Default</h2>
<p>The default behavior is the equivalent of this: </p>
<pre> return socket(addr-&gt;family, addr-&gt;socktype, addr-&gt;protocol);</pre>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<h2>Availability</h2>
<p>Added in 7.17.1.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_opensocketdata/">CURLOPT_OPENSOCKETDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sockoptfunction/">CURLOPT_SOCKOPTFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_closesocketfunction/">CURLOPT_CLOSESOCKETFUNCTION</a></code>(3),</p>
