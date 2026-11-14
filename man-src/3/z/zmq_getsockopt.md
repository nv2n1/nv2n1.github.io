---
title: "zmq_getsockopt(3)"
name: "zmq_getsockopt"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_getsockopt/"
description: "zmq_getsockopt – get 0MQ socket options"
---

<p>zmq_getsockopt &#8211; get 0MQ socket options</p>
<h2>Synopsis</h2>
<pre><code>int zmq_getsockopt(void *socket, int option_name, void *option_value, size_t *option_len);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_getsockopt()</i> function shall retrieve the value for the option specified by the <i>option_name</i> argument for the 0MQ socket pointed to by the <i>socket</i> argument, and store it in the buffer pointed to by the <i>option_value</i> argument. The <i>option_len</i> argument is the size in bytes of the buffer pointed to by <i>option_value</i>; upon successful completion <i>zmq_getsockopt()</i> shall modify the <i>option_len</i> argument to indicate the actual size of the option value stored in the buffer. The following options can be retrieved with the <i>zmq_getsockopt()</i> function:</p>
<h3>ZMQ_AFFINITY: Retrieve I/O thread affinity</h3>
<p>The <i>ZMQ_AFFINITY</i> option shall retrieve the I/O thread affinity for newly created connections on the specified <i>socket</i>. Affinity determines which threads from the 0MQ I/O thread pool associated with the socket&#8217;s <i>context</i> shall handle newly created connections. A value of zero specifies no affinity, meaning that work shall be distributed fairly among all 0MQ I/O threads in the thread pool. For non-zero values, the lowest bit corresponds to thread 1, second lowest bit to thread 2 and so on. For example, a value of 3 specifies that subsequent connections on <i>socket</i> shall be handled exclusively by I/O threads 1 and 2. See also <code><a href="/docs/linux/man/3-zmq_init/">zmq_init</a></code>(3) for details on allocating the number of I/O threads for a specific <i>context</i>. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> uint64_t
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A (bitmap)
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> N/A
</td>
</tr>
</table>
<h3>ZMQ_BACKLOG: Retrieve maximum length of the queue of outstanding connections</h3>
<p>The <i>ZMQ_BACKLOG</i> option shall retrieve the maximum length of the queue of outstanding peer connections for the specified <i>socket</i>; this only applies to connection-oriented transports. For details refer to your operating system documentation for the <i>listen</i> function. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> connections
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 100
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, only for connection-oriented transports
</td>
</tr>
</table>
<h3>ZMQ_CURVE_PUBLICKEY: Retrieve current CURVE public key</h3>
<p>Retrieves the current long term public key for the socket. You can provide either a 32 byte buffer, to retrieve the binary key value, or a 41 byte buffer, to retrieve the key in a printable Z85 format. NOTE: to fetch a printable key, the buffer must be 41 bytes large to hold the 40-char key value and one null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> binary data or Z85 text string
</td>
</tr>
<tr VALIGN=top>
<td> Option value size </td>
<td> 32 or 41
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transport
</td>
</tr>
</table>
<h3>ZMQ_CURVE_SECRETKEY: Retrieve current CURVE secret key</h3>
<p>Retrieves the current long term secret key for the socket. You can provide either a 32 byte buffer, to retrieve the binary key value, or a 41 byte buffer, to retrieve the key in a printable Z85 format. NOTE: to fetch a printable key, the buffer must be 41 bytes large to hold the 40-char key value and one null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> binary data or Z85 text string
</td>
</tr>
<tr VALIGN=top>
<td> Option value size </td>
<td> 32 or 41
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transport
</td>
</tr>
</table>
<h3>ZMQ_CURVE_SERVERKEY: Retrieve current CURVE server key</h3>
<p>Retrieves the current server key for the client socket. You can provide either a 32 byte buffer, to retrieve the binary key value, or a 41-byte buffer, to retrieve the key in a printable Z85 format. NOTE: to fetch a printable key, the buffer must be 41 bytes large to hold the 40-char key value and one null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> binary data or Z85 text string
</td>
</tr>
<tr VALIGN=top>
<td> Option value size </td>
<td> 32 or 41
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transport
</td>
</tr>
</table>
<h3>ZMQ_EVENTS: Retrieve socket event state</h3>
<p>The <i>ZMQ_EVENTS</i> option shall retrieve the event state for the specified <i>socket</i>. The returned value is a bit mask constructed by OR&#8217;ing a combination of the following event flags: <code>ZMQ_POLLIN</code></p>
<dl>
<dd>Indicates that at least one message may be received from the specified socket without blocking.</dl>
<p> <code>ZMQ_POLLOUT</code></p>
<dl>
<dd>Indicates that at least one message may be sent to the specified socket without blocking.</dl>
<p> The combination of a file descriptor returned by the <i>ZMQ_FD</i> option being ready for reading but no actual events returned by a subsequent retrieval of the <i>ZMQ_EVENTS</i> option is valid; applications should simply ignore this case and restart their polling operation/event loop. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A (flags)
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_FD: Retrieve file descriptor associated with the socket</h3>
<p>The <i>ZMQ_FD</i> option shall retrieve the file descriptor associated with the specified <i>socket</i>. The returned file descriptor can be used to integrate the socket into an existing event loop; the 0MQ library shall signal any pending events on the socket in an <i>edge-triggered</i> fashion by making the file descriptor become ready for reading.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The ability to read from the returned file descriptor does not necessarily indicate that messages are available to be read from, or can be written to, the underlying socket; applications must retrieve the actual event state with a subsequent retrieval of the <i>ZMQ_EVENTS</i> option. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The returned file descriptor is also used internally by the <i>zmq_send</i> and <i>zmq_recv</i> functions. As the descriptor is edge triggered, applications must update the state of <i>ZMQ_EVENTS</i> after each invocation of <i>zmq_send</i> or <i>zmq_recv</i>.To be more explicit: after calling <i>zmq_send</i> the socket may become readable (and vice versa) without triggering a read event on the file descriptor. </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The returned file descriptor is intended for use with a <i>poll</i> or similar system call only. Applications must never attempt to read or write data to it directly, neither should they try to close it.  Option value type </td>
<td> int on POSIX systems, SOCKET on Windows
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_GSSAPI_PLAINTEXT: Retrieve GSSAPI plaintext or encrypted status</h3>
<p>Returns the <i>ZMQ_GSSAPI_PLAINTEXT</i> option, if any, previously set on the socket. A value of <i>1</i> means that communications will be plaintext. A value of <i>0</i> means communications will be encrypted. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> 0, 1
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0 (false)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_GSSAPI_PRINCIPAL: Retrieve the name of the GSSAPI principal</h3>
<p>The <i>ZMQ_GSSAPI_PRINCIPAL</i> option shall retrieve the principal name set for the GSSAPI security mechanism. The returned value shall be a NULL-terminated string and MAY be empty. The returned size SHALL include the terminating null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> NULL-terminated character string
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null string
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_GSSAPI_SERVER: Retrieve current GSSAPI server role</h3>
<p>Returns the <i>ZMQ_GSSAPI_SERVER</i> option, if any, previously set on the socket. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> 0, 1
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0 (false)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_GSSAPI_SERVICE_PRINCIPAL: Retrieve the name of the GSSAPI service principal</h3>
<p>The <i>ZMQ_GSSAPI_SERVICE_PRINCIPAL</i> option shall retrieve the principal name of the GSSAPI server to which a GSSAPI client socket intends to connect. The returned value shall be a NULL-terminated string and MAY be empty. The returned size SHALL include the terminating null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> NULL-terminated character string
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null string
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_HANDSHAKE_IVL: Retrieve maximum handshake interval</h3>
<p>The <i>ZMQ_HANDSHAKE_IVL</i> option shall retrieve the maximum handshake interval for the specified <i>socket</i>. Handshaking is the exchange of socket configuration information (socket type, identity, security) that occurs when a connection is first opened, only for connection-oriented transports. If handshaking does not complete within the configured time, the connection shall be closed. The value 0 means no handshake time limit. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 30000
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all but ZMQ_STREAM, only for connection-oriented transports
</td>
</tr>
</table>
<h3>ZMQ_IDENTITY: Retrieve socket identity</h3>
<p>The <i>ZMQ_IDENTITY</i> option shall retrieve the identity of the specified <i>socket</i>. Socket identity is used only by request/reply pattern. Namely, it can be used in tandem with ROUTER socket to route messages to the peer with specific identity. Identity should be at least one byte and at most 255 bytes long. Identities starting with binary zero are reserved for use by 0MQ infrastructure. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> binary data
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> NULL
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> ZMQ_REP, ZMQ_REQ, ZMQ_ROUTER, ZMQ_DEALER.
</td>
</tr>
</table>
<h3>ZMQ_IMMEDIATE: Retrieve attach-on-connect value</h3>
<p>Retrieve the state of the attach on connect value. If set to 1, will delay the attachment of a pipe on connect until the underlying connection has completed. This will cause the socket to block if there are no other connections, but will prevent queues from filling on pipes awaiting connection. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> boolean
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0 (false)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, primarily when using TCP/IPC transports.
</td>
</tr>
</table>
<h3>ZMQ_IPV4ONLY: Retrieve IPv4-only socket override status</h3>
<p>Retrieve the IPv4-only option for the socket. This option is deprecated. Please use the ZMQ_IPV6 option. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> boolean
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 1 (true)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transports.
</td>
</tr>
</table>
<h3>ZMQ_IPV6: Retrieve IPv6 socket status</h3>
<p>Retrieve the IPv6 option for the socket. A value of 1 means IPv6 is enabled on the socket, while 0 means the socket will use only IPv4. When IPv6 is enabled the socket will connect to, or accept connections from, both IPv4 and IPv6 hosts. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> boolean
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0 (false)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transports.
</td>
</tr>
</table>
<h3>ZMQ_LAST_ENDPOINT: Retrieve the last endpoint set</h3>
<p>The <i>ZMQ_LAST_ENDPOINT</i> option shall retrieve the last endpoint bound for TCP and IPC transports. The returned value will be a string in the form of a ZMQ DSN. Note that if the TCP host is INADDR_ANY, indicated by a *, then the returned address will be 0.0.0.0 (for IPv4). </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> NULL-terminated character string
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> NULL
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when binding TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_LINGER: Retrieve linger period for socket shutdown</h3>
<p>The <i>ZMQ_LINGER</i> option shall retrieve the linger period for the specified <i>socket</i>. The linger period determines how long pending messages which have yet to be sent to a peer shall linger in memory after a socket is closed with <code><a href="/docs/linux/man/3-zmq_close/">zmq_close</a></code>(3), and further affects the termination of the socket&#8217;s context with <code><a href="/docs/linux/man/3-zmq_term/">zmq_term</a></code>(3). The following outlines the different behaviours:</p>
<dl>
<dd>&bull; The default value of <i>-1</i> specifies an infinite linger period. Pending messages shall not be discarded after a call to <i>zmq_close()</i>; attempting to terminate the socket&#8217;s context with <i>zmq_term()</i> shall block until all pending messages have been sent to a peer.</dl>
<dl>
<dd>&bull; The value of <i>0</i> specifies no linger period. Pending messages shall be discarded immediately when the socket is closed with <i>zmq_close()</i>.</dl>
<dl>
<dd>&bull; Positive values specify an upper bound for the linger period in milliseconds. Pending messages shall not be discarded after a call to <i>zmq_close()</i>; attempting to terminate the socket&#8217;s context with <i>zmq_term()</i> shall block until either all pending messages have been sent to a peer, or the linger period expires, after which any pending messages shall be discarded. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (infinite)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
</dl>
<h3>ZMQ_MAXMSGSIZE: Maximum acceptable inbound message size</h3>
<p>The option shall retrieve limit for the inbound messages. If a peer sends a message larger than ZMQ_MAXMSGSIZE it is disconnected. Value of -1 means <i>no limit</i>. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int64_t
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> bytes
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_MECHANISM: Retrieve current security mechanism</h3>
<p>The <i>ZMQ_MECHANISM</i> option shall retrieve the current security mechanism for the socket. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> ZMQ_NULL, ZMQ_PLAIN, ZMQ_CURVE, or ZMQ_GSSAPI
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> ZMQ_NULL
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_MULTICAST_HOPS: Maximum network hops for multicast packets</h3>
<p>The option shall retrieve time-to-live used for outbound multicast packets. The default of 1 means that the multicast packets don&#8217;t leave the local network. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> network hops
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 1
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using multicast transports
</td>
</tr>
</table>
<h3>ZMQ_PLAIN_PASSWORD: Retrieve current password</h3>
<p>The <i>ZMQ_PLAIN_PASSWORD</i> option shall retrieve the last password set for the PLAIN security mechanism. The returned value shall be a NULL-terminated string and MAY be empty. The returned size SHALL include the terminating null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> NULL-terminated character string
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null string
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_PLAIN_SERVER: Retrieve current PLAIN server role</h3>
<p>Returns the <i>ZMQ_PLAIN_SERVER</i> option, if any, previously set on the socket. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> 0, 1
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_PLAIN_USERNAME: Retrieve current PLAIN username</h3>
<p>The <i>ZMQ_PLAIN_USERNAME</i> option shall retrieve the last username set for the PLAIN security mechanism. The returned value shall be a NULL-terminated string and MAY be empty. The returned size SHALL include the terminating null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> NULL-terminated character string
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> null string
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP or IPC transports
</td>
</tr>
</table>
<h3>ZMQ_RATE: Retrieve multicast data rate</h3>
<p>The <i>ZMQ_RATE</i> option shall retrieve the maximum send or receive data rate for multicast transports using the specified <i>socket</i>. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> kilobits per second
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 100
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using multicast transports
</td>
</tr>
</table>
<h3>ZMQ_RCVBUF: Retrieve kernel receive buffer size</h3>
<p>The <i>ZMQ_RCVBUF</i> option shall retrieve the underlying kernel receive buffer size for the specified <i>socket</i>. A value of zero means that the OS default is in effect. For details refer to your operating system documentation for the <i>SO_RCVBUF</i> socket option. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> bytes
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_RCVHWM: Retrieve high water mark for inbound messages</h3>
<p>The <i>ZMQ_RCVHWM</i> option shall return the high water mark for inbound messages on the specified <i>socket</i>. The high water mark is a hard limit on the maximum number of outstanding messages 0MQ shall queue in memory for any single peer that the specified <i>socket</i> is communicating with. A value of zero means no limit. If this limit has been reached the socket shall enter an exceptional state and depending on the socket type, 0MQ shall take appropriate action such as blocking or dropping sent messages. Refer to the individual socket descriptions in <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for details on the exact action taken for each socket type. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> messages
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 1000
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_RCVMORE: More message data parts to follow</h3>
<p>The <i>ZMQ_RCVMORE</i> option shall return True (1) if the message part last received from the <i>socket</i> was a data part with more parts to follow. If there are no data parts to follow, this option shall return False (0). Refer to <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) and <code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3) for a detailed description of multi-part messages. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> boolean
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_RCVTIMEO: Maximum time before a socket operation returns with EAGAIN</h3>
<p>Retrieve the timeout for recv operation on the socket. If the value is 0, <i><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a>(3)</i> will return immediately, with a EAGAIN error if there is no message to receive. If the value is -1, it will block until a message is available. For all other values, it will wait for a message for that amount of time before returning with an EAGAIN error. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (infinite)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_RECONNECT_IVL: Retrieve reconnection interval</h3>
<p>The <i>ZMQ_RECONNECT_IVL</i> option shall retrieve the initial reconnection interval for the specified <i>socket</i>. The reconnection interval is the period 0MQ shall wait between attempts to reconnect disconnected peers when using connection-oriented transports. The value -1 means no reconnection.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The reconnection interval may be randomized by 0MQ to prevent reconnection storms in topologies with a large number of peers per socket.  Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 100
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, only for connection-oriented transports
</td>
</tr>
</table>
<h3>ZMQ_RECONNECT_IVL_MAX: Retrieve maximum reconnection interval</h3>
<p>The <i>ZMQ_RECONNECT_IVL_MAX</i> option shall retrieve the maximum reconnection interval for the specified <i>socket</i>. This is the maximum period 0MQ shall wait between attempts to reconnect. On each reconnect attempt, the previous interval shall be doubled untill ZMQ_RECONNECT_IVL_MAX is reached. This allows for exponential backoff strategy. Default value means no exponential backoff is performed and reconnect interval calculations are only based on ZMQ_RECONNECT_IVL.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Values less than ZMQ_RECONNECT_IVL will be ignored.  Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0 (only use ZMQ_RECONNECT_IVL)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, only for connection-oriented transport
</td>
</tr>
</table>
<h3>ZMQ_RECOVERY_IVL: Get multicast recovery interval</h3>
<p>The <i>ZMQ_RECOVERY_IVL</i> option shall retrieve the recovery interval for multicast transports using the specified <i>socket</i>. The recovery interval determines the maximum time in milliseconds that a receiver can be absent from a multicast group before unrecoverable data loss will occur. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 10000
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using multicast transports
</td>
</tr>
</table>
<h3>ZMQ_SNDBUF: Retrieve kernel transmit buffer size</h3>
<p>The <i>ZMQ_SNDBUF</i> option shall retrieve the underlying kernel transmit buffer size for the specified <i>socket</i>. A value of zero means that the OS default is in effect. For details refer to your operating system documentation for the <i>SO_SNDBUF</i> socket option. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> bytes
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_SNDHWM: Retrieves high water mark for outbound messages</h3>
<p>The <i>ZMQ_SNDHWM</i> option shall return the high water mark for outbound messages on the specified <i>socket</i>. The high water mark is a hard limit on the maximum number of outstanding messages 0MQ shall queue in memory for any single peer that the specified <i>socket</i> is communicating with. A value of zero means no limit. If this limit has been reached the socket shall enter an exceptional state and depending on the socket type, 0MQ shall take appropriate action such as blocking or dropping sent messages. Refer to the individual socket descriptions in <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for details on the exact action taken for each socket type. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> messages
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 1000
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_SNDTIMEO: Maximum time before a socket operation returns with EAGAIN</h3>
<p>Retrieve the timeout for send operation on the socket. If the value is 0, <i><a href="/docs/linux/man/3-zmq_send/">zmq_send</a>(3)</i> will return immediately, with a EAGAIN error if the message cannot be sent. If the value is -1, it will block until the message is sent. For all other values, it will try to send the message for that amount of time before returning with an EAGAIN error. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> milliseconds
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (infinite)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_TCP_KEEPALIVE: Override SO_KEEPALIVE socket option</h3>
<p>Override <i>SO_KEEPALIVE</i> socket option(where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> -1,0,1
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (leave to OS default)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transports.
</td>
</tr>
</table>
<h3>ZMQ_TCP_KEEPALIVE_CNT: Override TCP_KEEPCNT socket option</h3>
<p>Override <i>TCP_KEEPCNT</i> socket option(where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> -1,&gt;0
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (leave to OS default)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transports.
</td>
</tr>
</table>
<h3>ZMQ_TCP_KEEPALIVE_IDLE: Override TCP_KEEPCNT(or TCP_KEEPALIVE on some OS)</h3>
<p>Override <i>TCP_KEEPCNT</i>(or <i>TCP_KEEPALIVE</i> on some OS) socket option (where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> -1,&gt;0
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (leave to OS default)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transports.
</td>
</tr>
</table>
<h3>ZMQ_TCP_KEEPALIVE_INTVL: Override TCP_KEEPINTVL socket option</h3>
<p>Override <i>TCP_KEEPINTVL</i> socket option(where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> -1,&gt;0
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> -1 (leave to OS default)
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transports.
</td>
</tr>
</table>
<h3>ZMQ_TOS: Retrieve the Type-of-Service socket override status</h3>
<p>Retrieve the IP_TOS option for the socket. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> &gt;0
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, only for connection-oriented transports
</td>
</tr>
</table>
<h3>ZMQ_TYPE: Retrieve socket type</h3>
<p>The <i>ZMQ_TYPE</i> option shall retrieve the socket type for the specified <i>socket</i>. The socket type is specified at socket creation time and cannot be modified afterwards. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> int
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all
</td>
</tr>
</table>
<h3>ZMQ_ZAP_DOMAIN: Retrieve RFC 27 authentication domain</h3>
<p>The <i>ZMQ_ZAP_DOMAIN</i> option shall retrieve the last ZAP domain set for the socket. The returned value shall be a NULL-terminated string and MAY be empty. The returned size SHALL include the terminating null byte. </p>
<table>
<tr VALIGN=top>
<td> Option value type </td>
<td> character string
</td>
</tr>
<tr VALIGN=top>
<td> Option value unit </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Default value </td>
<td> not set
</td>
</tr>
<tr VALIGN=top>
<td> Applicable socket types </td>
<td> all, when using TCP transport
</td>
</tr>
</table>
<h2>Return Value</h2>
<p>The <i>zmq_getsockopt()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The requested option <i>option_name</i> is unknown, or the requested <i>option_len</i> or <i>option_value</i> is invalid, or the size of the buffer pointed to by <i>option_value</i>, as specified by <i>option_len</i>, is insufficient for storing the option value.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
<p> <code>ENOTSOCK</code></p>
<dl>
<dd>The provided <i>socket</i> was invalid.</dl>
<p> <code>EINTR</code></p>
<dl>
<dd>The operation was interrupted by delivery of a signal.</dl>
<h2>Example</h2>
<p><code>Retrieving the high water mark for outgoing messages</code>. </p>
<pre><code>/* Retrieve high water mark into sndhwm */
int sndhwm;
size_t sndhwm_size = sizeof(sndhwm);
rc = zmq_getsockopt(socket, ZMQ_SNDHWM, &amp;sndhwm, &amp;sndhwm_size);
assert(rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
