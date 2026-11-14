---
title: "zmq_setsockopt(3)"
name: "zmq_setsockopt"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_setsockopt/"
---

zmq_setsockopt - set 0MQ socket options

<h2>Synopsis</h2>

<pre><code>int zmq_setsockopt(void *socket, int option_name, const void *option_value, size_t option_len);</code></pre> Caution: All options, with the exception of ZMQ_SUBSCRIBE, ZMQ_UNSUBSCRIBE, ZMQ_LINGER, ZMQ_ROUTER_HANDOVER, ZMQ_ROUTER_MANDATORY, ZMQ_PROBE_ROUTER, ZMQ_XPUB_VERBOSE, ZMQ_REQ_CORRELATE, and ZMQ_REQ_RELAXED, only take effect for subsequent socket bind/connects. Specifically, security options take effect for subsequent bind/connect calls, and can be changed at any time to affect subsequent binds and/or connects.

<h2>Description</h2>

The <i>zmq_setsockopt()</i> function shall set the option specified by the <i>option_name</i> argument to the value pointed to by the <i>option_value</i> argument for the 0MQ socket pointed to by the <i>socket</i> argument. The <i>option_len</i> argument is the size of the option value in bytes. The following socket options can be set with the <i>zmq_setsockopt()</i> function:

<h3>ZMQ_AFFINITY: Set I/O thread affinity</h3>

The <i>ZMQ_AFFINITY</i> option shall set the I/O thread affinity for newly created connections on the specified <i>socket</i>. Affinity determines which threads from the 0MQ I/O thread pool associated with the socket's <i>context</i> shall handle newly created connections. A value of zero specifies no affinity, meaning that work shall be distributed fairly among all 0MQ I/O threads in the thread pool. For non-zero values, the lowest bit corresponds to thread 1, second lowest bit to thread 2 and so on. For example, a value of 3 specifies that subsequent connections on <i>socket</i> shall be handled exclusively by I/O threads 1 and 2. See also <b><a HREF="/docs/linux/man/3-zmq_init/">zmq_init</a></b>(3) for details on allocating the number of I/O threads for a specific <i>context</i>. <table> <tr VALIGN=top><td> Option value type </td><td> uint64_t 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A (bitmap) 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> N/A 
</td></tr> </table>

<h3>ZMQ_BACKLOG: Set maximum length of the queue of outstanding connections</h3>

The <i>ZMQ_BACKLOG</i> option shall set the maximum length of the queue of outstanding peer connections for the specified <i>socket</i>; this only applies to connection-oriented transports. For details refer to your operating system documentation for the <i>listen</i> function. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> connections 
</td></tr><tr VALIGN=top><td> Default value </td><td> 100 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, only for connection-oriented transports. 
</td></tr> </table>

<h3>ZMQ_CONNECT_RID: Assign the next outbound connection id</h3>

The <i>ZMQ_CONNECT_RID</i> option sets the peer id of the next host connected via the zmq_connect() call, and immediately readies that connection for data transfer with the named id. This option applies only to the first subsequent call to zmq_connect(), calls thereafter use default connection behavior. Typical use is to set this socket option ahead of each zmq_connect() attempt to a new host. Each connection MUST be assigned a unique name. Assigning a name that is already in use is not allowed. Useful when connecting ROUTER to ROUTER, or STREAM to STREAM, as it allows for immediate sending to peers. Outbound id framing requirements for ROUTER and STREAM sockets apply. The peer id should be from 1 to 255 bytes long and MAY NOT start with binary zero. <table> <tr VALIGN=top><td> Option value type </td><td> binary data 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> NULL 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_ROUTER, ZMQ_STREAM 
</td></tr> </table>

<h3>ZMQ_CONFLATE: Keep only last message</h3>

If set, a socket shall keep only one message in its inbound/outbound queue, this message being the last message received/the last message to be sent. Ignores <i>ZMQ_RCVHWM</i> and <i>ZMQ_SNDHWM</i> options. Does not support multi-part messages, in particular, only one part of it is kept in the socket internal queue. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> boolean 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 (false) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_PULL, ZMQ_PUSH, ZMQ_SUB, ZMQ_PUB, ZMQ_DEALER 
</td></tr> </table>

<h3>ZMQ_CURVE_PUBLICKEY: Set CURVE public key</h3>

Sets the socket's long term public key. You must set this on CURVE client sockets, see <b><a HREF="/docs/linux/man/7-zmq_curve/">zmq_curve</a></b>(7). You can provide the key as 32 binary bytes, or as a 40-character string encoded in the Z85 encoding format and terminated in a null byte. The public key must always be used with the matching secret key. To generate a public/secret key pair, use <b><a HREF="/docs/linux/man/3-zmq_curve_keypair/">zmq_curve_keypair</a></b>(3).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 an option value size of 40 is supported for backwards compatibility, though is deprecated.  Option value type </td><td> binary data or Z85 text string 
</td></tr><tr VALIGN=top><td> Option value size </td><td> 32 or 41 
</td></tr><tr VALIGN=top><td> Default value </td><td> NULL 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_CURVE_SECRETKEY: Set CURVE secret key</h3>

Sets the socket's long term secret key. You must set this on both CURVE client and server sockets, see <b><a HREF="/docs/linux/man/7-zmq_curve/">zmq_curve</a></b>(7). You can provide the key as 32 binary bytes, or as a 40-character string encoded in the Z85 encoding format and terminated in a null byte. To generate a public/secret key pair, use <b><a HREF="/docs/linux/man/3-zmq_curve_keypair/">zmq_curve_keypair</a></b>(3).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 an option value size of 40 is supported for backwards compatibility, though is deprecated.  Option value type </td><td> binary data or Z85 text string 
</td></tr><tr VALIGN=top><td> Option value size </td><td> 32 or 41 
</td></tr><tr VALIGN=top><td> Default value </td><td> NULL 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_CURVE_SERVER: Set CURVE server role</h3>

Defines whether the socket will act as server for CURVE security, see <b><a HREF="/docs/linux/man/7-zmq_curve/">zmq_curve</a></b>(7). A value of <i>1</i> means the socket will act as CURVE server. A value of <i>0</i> means the socket will not act as CURVE server, and its security role then depends on other option settings. Setting this to <i>0</i> shall reset the socket security to NULL. When you set this you must also set the server's secret key using the ZMQ_CURVE_SECRETKEY option. A server socket does not need to know its own public key. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_CURVE_SERVERKEY: Set CURVE server key</h3>

Sets the socket's long term server key. You must set this on CURVE client sockets, see <b><a HREF="/docs/linux/man/7-zmq_curve/">zmq_curve</a></b>(7). You can provide the key as 32 binary bytes, or as a 40-character string encoded in the Z85 encoding format and terminated in a null byte. This key must have been generated together with the server's secret key. To generate a public/secret key pair, use <b><a HREF="/docs/linux/man/3-zmq_curve_keypair/">zmq_curve_keypair</a></b>(3).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 an option value size of 40 is supported for backwards compatibility, though is deprecated.  Option value type </td><td> binary data or Z85 text string 
</td></tr><tr VALIGN=top><td> Option value size </td><td> 32 or 41 
</td></tr><tr VALIGN=top><td> Default value </td><td> NULL 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_GSSAPI_PLAINTEXT: Disable GSSAPI encryption</h3>

Defines whether communications on the socket will encrypted, see <b><a HREF="/docs/linux/man/7-zmq_gssapi/">zmq_gssapi</a></b>(7). A value of <i>1</i> means that communications will be plaintext. A value of <i>0</i> means communications will be encrypted. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 (false) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_GSSAPI_PRINCIPAL: Set name of GSSAPI principal</h3>

Sets the name of the pricipal for whom GSSAPI credentials should be acquired. <table> <tr VALIGN=top><td> Option value type </td><td> character string 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> not set 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_GSSAPI_SERVER: Set GSSAPI server role</h3>

Defines whether the socket will act as server for GSSAPI security, see <b><a HREF="/docs/linux/man/7-zmq_gssapi/">zmq_gssapi</a></b>(7). A value of <i>1</i> means the socket will act as GSSAPI server. A value of <i>0</i> means the socket will act as GSSAPI client. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 (false) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_GSSAPI_SERVICE_PRINCIPAL: Set name of GSSAPI service principal</h3>

Sets the name of the pricipal of the GSSAPI server to which a GSSAPI client intends to connect. <table> <tr VALIGN=top><td> Option value type </td><td> character string 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> not set 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_HANDSHAKE_IVL: Set maximum handshake interval</h3>

The <i>ZMQ_HANDSHAKE_IVL</i> option shall set the maximum handshake interval for the specified <i>socket</i>. Handshaking is the exchange of socket configuration information (socket type, identity, security) that occurs when a connection is first opened, only for connection-oriented transports. If handshaking does not complete within the configured time, the connection shall be closed. The value 0 means no handshake time limit. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> 30000 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all but ZMQ_STREAM, only for connection-oriented transports 
</td></tr> </table>

<h3>ZMQ_IDENTITY: Set socket identity</h3>

The <i>ZMQ_IDENTITY</i> option shall set the identity of the specified <i>socket</i> when connecting to a ROUTER socket. The identity should be from 1 to 255 bytes long and may contain any values. If two clients use the same identity when connecting to a ROUTER, the results shall depend on the ZMQ_ROUTER_HANDOVER option setting. If that is not set (or set to the default of zero), the ROUTER socket shall reject clients trying to connect with an already-used identity. If that option is set to 1, the ROUTER socket shall hand-over the connection to the new client and disconnect the existing one. <table> <tr VALIGN=top><td> Option value type </td><td> binary data 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> NULL 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_REQ, ZMQ_REP, ZMQ_ROUTER, ZMQ_DEALER. 
</td></tr> </table>

<h3>ZMQ_IMMEDIATE: Queue messages only to completed connections</h3>

By default queues will fill on outgoing connections even if the connection has not completed. This can lead to &quot;lost&quot; messages on sockets with round-robin routing (REQ, PUSH, DEALER). If this option is set to 1, messages shall be queued only to completed connections. This will cause the socket to block if there are no other connections, but will prevent queues from filling on pipes awaiting connection. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> boolean 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 (false) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, only for connection-oriented transports. 
</td></tr> </table>

<h3>ZMQ_IPV6: Enable IPv6 on socket</h3>

Set the IPv6 option for the socket. A value of 1 means IPv6 is enabled on the socket, while 0 means the socket will use only IPv4. When IPv6 is enabled the socket will connect to, or accept connections from, both IPv4 and IPv6 hosts. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> boolean 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 (false) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transports. 
</td></tr> </table>

<h3>ZMQ_LINGER: Set linger period for socket shutdown</h3>

The <i>ZMQ_LINGER</i> option shall set the linger period for the specified <i>socket</i>. The linger period determines how long pending messages which have yet to be sent to a peer shall linger in memory after a socket is disconnected with <b><a HREF="/docs/linux/man/3-zmq_disconnect/">zmq_disconnect</a></b>(3) or closed with <b><a HREF="/docs/linux/man/3-zmq_close/">zmq_close</a></b>(3), and further affects the termination of the socket's context with <b><a HREF="/docs/linux/man/3-zmq_term/">zmq_term</a></b>(3). The following outlines the different behaviours:
<dl><dd>&bull; The default value of <i>-1</i> specifies an infinite linger period. Pending messages shall not be discarded after a call to <i>zmq_disconnect()</i> or <i>zmq_close()</i>; attempting to terminate the socket's context with <i>zmq_term()</i> shall block until all pending messages have been sent to a peer.</dl><dl><dd>&bull; The value of <i>0</i> specifies no linger period. Pending messages shall be discarded immediately after a call to <i>zmq_disconnect()</i> or <i>zmq_close()</i>.</dl><dl><dd>&bull; Positive values specify an upper bound for the linger period in milliseconds. Pending messages shall not be discarded after a call to <i>zmq_disconnect()</i> or <i>zmq_close()</i>; attempting to terminate the socket's context with <i>zmq_term()</i> shall block until either all pending messages have been sent to a peer, or the linger period expires, after which any pending messages shall be discarded. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (infinite) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table></dl>

<h3>ZMQ_MAXMSGSIZE: Maximum acceptable inbound message size</h3>

Limits the size of the inbound message. If a peer sends a message larger than ZMQ_MAXMSGSIZE it is disconnected. Value of -1 means <i>no limit</i>. <table> <tr VALIGN=top><td> Option value type </td><td> int64_t 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> bytes 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_MULTICAST_HOPS: Maximum network hops for multicast packets</h3>

Sets the time-to-live field in every multicast packet sent from this socket. The default is 1 which means that the multicast packets don't leave the local network. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> network hops 
</td></tr><tr VALIGN=top><td> Default value </td><td> 1 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using multicast transports 
</td></tr> </table>

<h3>ZMQ_PLAIN_PASSWORD: Set PLAIN security password</h3>

Sets the password for outgoing connections over TCP or IPC. If you set this to a non-null value, the security mechanism used for connections shall be PLAIN, see <b><a HREF="/docs/linux/man/7-zmq_plain/">zmq_plain</a></b>(7). If you set this to a null value, the security mechanism used for connections shall be NULL, see <b><a HREF="/docs/linux/man/3-zmq_null/">zmq_null</a></b>(3). <table> <tr VALIGN=top><td> Option value type </td><td> character string 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> not set 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_PLAIN_SERVER: Set PLAIN server role</h3>

Defines whether the socket will act as server for PLAIN security, see <b><a HREF="/docs/linux/man/7-zmq_plain/">zmq_plain</a></b>(7). A value of <i>1</i> means the socket will act as PLAIN server. A value of <i>0</i> means the socket will not act as PLAIN server, and its security role then depends on other option settings. Setting this to <i>0</i> shall reset the socket security to NULL. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_PLAIN_USERNAME: Set PLAIN security username</h3>

Sets the username for outgoing connections over TCP or IPC. If you set this to a non-null value, the security mechanism used for connections shall be PLAIN, see <b><a HREF="/docs/linux/man/7-zmq_plain/">zmq_plain</a></b>(7). If you set this to a null value, the security mechanism used for connections shall be NULL, see <b><a HREF="/docs/linux/man/3-zmq_null/">zmq_null</a></b>(3). <table> <tr VALIGN=top><td> Option value type </td><td> character string 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> not set 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_PROBE_ROUTER: bootstrap connections to ROUTER sockets</h3>

When set to 1, the socket will automatically send an empty message when a new connection is made or accepted. You may set this on REQ, DEALER, or ROUTER sockets connected to a ROUTER socket. The application must filter such empty messages. The ZMQ_PROBE_ROUTER option in effect provides the ROUTER application with an event signaling the arrival of a new peer.
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 do not set this option on a socket that talks to any other socket types: the results are undefined.  Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_ROUTER, ZMQ_DEALER, ZMQ_REQ 
</td></tr> </table>

<h3>ZMQ_RATE: Set multicast data rate</h3>

The <i>ZMQ_RATE</i> option shall set the maximum send or receive data rate for multicast transports such as <b><a HREF="/docs/linux/man/7-zmq_pgm/">zmq_pgm</a></b>(7) using the specified <i>socket</i>. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> kilobits per second 
</td></tr><tr VALIGN=top><td> Default value </td><td> 100 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using multicast transports 
</td></tr> </table>

<h3>ZMQ_RCVBUF: Set kernel receive buffer size</h3>

The <i>ZMQ_RCVBUF</i> option shall set the underlying kernel receive buffer size for the <i>socket</i> to the specified size in bytes. A value of zero means leave the OS default unchanged. For details refer to your operating system documentation for the <i>SO_RCVBUF</i> socket option. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> bytes 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_RCVHWM: Set high water mark for inbound messages</h3>

The <i>ZMQ_RCVHWM</i> option shall set the high water mark for inbound messages on the specified <i>socket</i>. The high water mark is a hard limit on the maximum number of outstanding messages 0MQ shall queue in memory for any single peer that the specified <i>socket</i> is communicating with. A value of zero means no limit. If this limit has been reached the socket shall enter an exceptional state and depending on the socket type, 0MQ shall take appropriate action such as blocking or dropping sent messages. Refer to the individual socket descriptions in <b><a HREF="/docs/linux/man/3-zmq_socket/">zmq_socket</a></b>(3) for details on the exact action taken for each socket type. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> messages 
</td></tr><tr VALIGN=top><td> Default value </td><td> 1000 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_RCVTIMEO: Maximum time before a recv operation returns with EAGAIN</h3>

Sets the timeout for receive operation on the socket. If the value is 0, <i><a HREF="/docs/linux/man/3-zmq_recv/">zmq_recv</a>(3)</i> will return immediately, with a EAGAIN error if there is no message to receive. If the value is -1, it will block until a message is available. For all other values, it will wait for a message for that amount of time before returning with an EAGAIN error. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (infinite) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_RECONNECT_IVL: Set reconnection interval</h3>

The <i>ZMQ_RECONNECT_IVL</i> option shall set the initial reconnection interval for the specified <i>socket</i>. The reconnection interval is the period 0MQ shall wait between attempts to reconnect disconnected peers when using connection-oriented transports. The value -1 means no reconnection.
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 The reconnection interval may be randomized by 0MQ to prevent reconnection storms in topologies with a large number of peers per socket.  Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> 100 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, only for connection-oriented transports 
</td></tr> </table>

<h3>ZMQ_RECONNECT_IVL_MAX: Set maximum reconnection interval</h3>

The <i>ZMQ_RECONNECT_IVL_MAX</i> option shall set the maximum reconnection interval for the specified <i>socket</i>. This is the maximum period 0MQ shall wait between attempts to reconnect. On each reconnect attempt, the previous interval shall be doubled untill ZMQ_RECONNECT_IVL_MAX is reached. This allows for exponential backoff strategy. Default value means no exponential backoff is performed and reconnect interval calculations are only based on ZMQ_RECONNECT_IVL.
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 Values less than ZMQ_RECONNECT_IVL will be ignored.  Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 (only use ZMQ_RECONNECT_IVL) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, only for connection-oriented transports 
</td></tr> </table>

<h3>ZMQ_RECOVERY_IVL: Set multicast recovery interval</h3>

The <i>ZMQ_RECOVERY_IVL</i> option shall set the recovery interval for multicast transports using the specified <i>socket</i>. The recovery interval determines the maximum time in milliseconds that a receiver can be absent from a multicast group before unrecoverable data loss will occur.
<dl><dd><font SIZE="+1"> <b>Caution</b> </font> 
 Exercise care when setting large recovery intervals as the data needed for recovery will be held in memory. For example, a 1 minute recovery interval at a data rate of 1Gbps requires a 7GB in-memory buffer.  Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> 10000 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using multicast transports 
</td></tr> </table>

<h3>ZMQ_REQ_CORRELATE: match replies with requests</h3>

The default behavior of REQ sockets is to rely on the ordering of messages to match requests and responses and that is usually sufficient. When this option is set to 1, the REQ socket will prefix outgoing messages with an extra frame containing a request id. That means the full message is (request id, identity, 0, user frames...). The REQ socket will discard all incoming messages that don't begin with these two frames. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_REQ 
</td></tr> </table>

<h3>ZMQ_REQ_RELAXED: relax strict alternation between request and reply</h3>

By default, a REQ socket does not allow initiating a new request with <i><a HREF="/docs/linux/man/3-zmq_send/">zmq_send</a>(3)</i> until the reply to the previous one has been received. When set to 1, sending another message is allowed and has the effect of disconnecting the underlying connection to the peer from which the reply was expected, triggering a reconnection attempt on transports that support it. The request-reply state machine is reset and a new request is sent to the next available peer. If set to 1, also enable ZMQ_REQ_CORRELATE to ensure correct matching of requests and replies. Otherwise a late reply to an aborted request can be reported as the reply to the superseding request. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_REQ 
</td></tr> </table>

<h3>ZMQ_ROUTER_HANDOVER: handle duplicate client identities on ROUTER sockets</h3>

If two clients use the same identity when connecting to a ROUTER, the results shall depend on the ZMQ_ROUTER_HANDOVER option setting. If that is not set (or set to the default of zero), the ROUTER socket shall reject clients trying to connect with an already-used identity. If that option is set to 1, the ROUTER socket shall hand-over the connection to the new client and disconnect the existing one. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_ROUTER 
</td></tr> </table>

<h3>ZMQ_ROUTER_MANDATORY: accept only routable messages on ROUTER sockets</h3>

Sets the ROUTER socket behavior when an unroutable message is encountered. A value of 0 is the default and discards the message silently when it cannot be routed or the peers SNDHWM is reached. A value of 1 returns an <i>EHOSTUNREACH</i> error code if the message cannot be routed or <i>EAGAIN</i> error code if the SNDHWM is reached and ZMQ_DONTWAIT was used. Without ZMQ_DONTWAIT it will block until the SNDTIMEO is reached or a spot in the send queue opens up. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_ROUTER 
</td></tr> </table>

<h3>ZMQ_ROUTER_RAW: switch ROUTER socket to raw mode</h3>

Sets the raw mode on the ROUTER, when set to 1. When the ROUTER socket is in raw mode, and when using the tcp:// transport, it will read and write TCP data without 0MQ framing. This lets 0MQ applications talk to non-0MQ applications. When using raw mode, you cannot set explicit identities, and the ZMQ_SNDMORE flag is ignored when sending data messages. In raw mode you can close a specific connection by sending it a zero-length message (following the identity frame).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 This option is deprecated, please use ZMQ_STREAM sockets instead.  Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_ROUTER 
</td></tr> </table>

<h3>ZMQ_SNDBUF: Set kernel transmit buffer size</h3>

The <i>ZMQ_SNDBUF</i> option shall set the underlying kernel transmit buffer size for the <i>socket</i> to the specified size in bytes. A value of zero means leave the OS default unchanged. For details please refer to your operating system documentation for the <i>SO_SNDBUF</i> socket option. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> bytes 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_SNDHWM: Set high water mark for outbound messages</h3>

The <i>ZMQ_SNDHWM</i> option shall set the high water mark for outbound messages on the specified <i>socket</i>. The high water mark is a hard limit on the maximum number of outstanding messages 0MQ shall queue in memory for any single peer that the specified <i>socket</i> is communicating with. A value of zero means no limit. If this limit has been reached the socket shall enter an exceptional state and depending on the socket type, 0MQ shall take appropriate action such as blocking or dropping sent messages. Refer to the individual socket descriptions in <b><a HREF="/docs/linux/man/3-zmq_socket/">zmq_socket</a></b>(3) for details on the exact action taken for each socket type.
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 0MQ does not guarantee that the socket will accept as many as ZMQ_SNDHWM messages, and the actual limit may be as much as 60-70% lower depending on the flow of messages on the socket.  Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> messages 
</td></tr><tr VALIGN=top><td> Default value </td><td> 1000 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_SNDTIMEO: Maximum time before a send operation returns with EAGAIN</h3>

Sets the timeout for send operation on the socket. If the value is 0, <i><a HREF="/docs/linux/man/3-zmq_send/">zmq_send</a>(3)</i> will return immediately, with a EAGAIN error if the message cannot be sent. If the value is -1, it will block until the message is sent. For all other values, it will try to send the message for that amount of time before returning with an EAGAIN error. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> milliseconds 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (infinite) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all 
</td></tr> </table>

<h3>ZMQ_SUBSCRIBE: Establish message filter</h3>

The <i>ZMQ_SUBSCRIBE</i> option shall establish a new message filter on a <i>ZMQ_SUB</i> socket. Newly created <i>ZMQ_SUB</i> sockets shall filter out all incoming messages, therefore you should call this option to establish an initial message filter. An empty <i>option_value</i> of length zero shall subscribe to all incoming messages. A non-empty <i>option_value</i> shall subscribe to all messages beginning with the specified prefix. Multiple filters may be attached to a single <i>ZMQ_SUB</i> socket, in which case a message shall be accepted if it matches at least one filter. <table> <tr VALIGN=top><td> Option value type </td><td> binary data 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> N/A 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_SUB 
</td></tr> </table>

<h3>ZMQ_TCP_KEEPALIVE: Override SO_KEEPALIVE socket option</h3>

Override <i>SO_KEEPALIVE</i> socket option (where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> -1,0,1 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (leave to OS default) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transports. 
</td></tr> </table>

<h3>ZMQ_TCP_KEEPALIVE_CNT: Override TCP_KEEPCNT socket option</h3>

Override <i>TCP_KEEPCNT</i> socket option (where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> -1,&gt;0 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (leave to OS default) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transports. 
</td></tr> </table>

<h3>ZMQ_TCP_KEEPALIVE_IDLE: Override TCP_KEEPCNT (or TCP_KEEPALIVE on some OS)</h3>

Override <i>TCP_KEEPCNT</i> (or <i>TCP_KEEPALIVE</i> on some OS) socket option (where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> -1,&gt;0 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (leave to OS default) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transports. 
</td></tr> </table>

<h3>ZMQ_TCP_KEEPALIVE_INTVL: Override TCP_KEEPINTVL socket option</h3>

Override <i>TCP_KEEPINTVL</i> socket option(where supported by OS). The default value of -1 means to skip any overrides and leave it to OS default. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> -1,&gt;0 
</td></tr><tr VALIGN=top><td> Default value </td><td> -1 (leave to OS default) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transports. 
</td></tr> </table>

<h3>ZMQ_TOS: Set the Type-of-Service on socket</h3>

Sets the ToS fields (Differentiated services (DS) and Explicit Congestion Notification (ECN) field of the IP header. The ToS field is typically used to specify a packets priority. The availability of this option is dependent on intermediate network equipment that inspect the ToS field andprovide a path for low-delay, high-throughput, highly-reliable service, etc. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> &gt;0 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, only for connection-oriented transports 
</td></tr> </table>

<h3>ZMQ_UNSUBSCRIBE: Remove message filter</h3>

The <i>ZMQ_UNSUBSCRIBE</i> option shall remove an existing message filter on a <i>ZMQ_SUB</i> socket. The filter specified must match an existing filter previously established with the <i>ZMQ_SUBSCRIBE</i> option. If the socket has several instances of the same filter attached the <i>ZMQ_UNSUBSCRIBE</i> option shall remove only one instance, leaving the rest in place and functional. <table> <tr VALIGN=top><td> Option value type </td><td> binary data 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> N/A 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_SUB 
</td></tr> </table>

<h3>ZMQ_XPUB_VERBOSE: provide all subscription messages on XPUB sockets</h3>

Sets the <i>XPUB</i> socket behavior on new subscriptions and unsubscriptions. A value of <i>0</i> is the default and passes only new subscription messages to upstream. A value of <i>1</i> passes all subscription messages upstream. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> 0, 1 
</td></tr><tr VALIGN=top><td> Default value </td><td> 0 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> ZMQ_XPUB 
</td></tr> </table>

<h3>ZMQ_ZAP_DOMAIN: Set RFC 27 authentication domain</h3>

Sets the domain for ZAP (ZMQ RFC 27) authentication. For NULL security (the default on all tcp:// connections), ZAP authentication only happens if you set a non-empty domain. For PLAIN and CURVE security, ZAP requests are always made, if there is a ZAP handler present. See m[blue]<b><a rel="nofollow" HREF="http://rfc.zeromq.org/spec:27">http://rfc.zeromq.org/spec:27</a></b>m[] for more details. <table> <tr VALIGN=top><td> Option value type </td><td> character string 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> not set 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transport 
</td></tr> </table>

<h3>ZMQ_TCP_ACCEPT_FILTER: Assign filters to allow new TCP connections</h3>

Assign an arbitrary number of filters that will be applied for each new TCP transport connection on a listening socket. If no filters are applied, then the TCP transport allows connections from any IP address. If at least one filter is applied then new connection source ip should be matched. To clear all filters call zmq_setsockopt(socket, ZMQ_TCP_ACCEPT_FILTER, NULL, 0). Filter is a null-terminated string with ipv6 or ipv4 CIDR.
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 This option is deprecated, please use authentication via the ZAP API and IP address whitelisting / blacklisting.  Option value type </td><td> binary data 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> no filters (allow from all) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all listening sockets, when using TCP transports. 
</td></tr> </table>

<h3>ZMQ_IPC_FILTER_GID: Assign group ID filters to allow new IPC connections</h3>

Assign an arbitrary number of filters that will be applied for each new IPC transport connection on a listening socket. If no IPC filters are applied, then the IPC transport allows connections from any process. If at least one UID, GID, or PID filter is applied then new connection credentials should be matched. To clear all GID filters call zmq_setsockopt(socket, ZMQ_IPC_FILTER_GID, NULL, 0).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 GID filters are only available on platforms supporting SO_PEERCRED or LOCAL_PEERCRED socket options (currently only Linux and later versions of OS X). 
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 This option is deprecated, please use authentication via the ZAP API and IPC whitelisting / blacklisting.  Option value type </td><td> gid_t 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> no filters (allow from all) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all listening sockets, when using IPC transports. 
</td></tr> </table>

<h3>ZMQ_IPC_FILTER_PID: Assign process ID filters to allow new IPC connections</h3>

Assign an arbitrary number of filters that will be applied for each new IPC transport connection on a listening socket. If no IPC filters are applied, then the IPC transport allows connections from any process. If at least one UID, GID, or PID filter is applied then new connection credentials should be matched. To clear all PID filters call zmq_setsockopt(socket, ZMQ_IPC_FILTER_PID, NULL, 0).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 PID filters are only available on platforms supporting the SO_PEERCRED socket option (currently only Linux). 
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 This option is deprecated, please use authentication via the ZAP API and IPC whitelisting / blacklisting.  Option value type </td><td> pid_t 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> no filters (allow from all) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all listening sockets, when using IPC transports. 
</td></tr> </table>

<h3>ZMQ_IPC_FILTER_UID: Assign user ID filters to allow new IPC connections</h3>

Assign an arbitrary number of filters that will be applied for each new IPC transport connection on a listening socket. If no IPC filters are applied, then the IPC transport allows connections from any process. If at least one UID, GID, or PID filter is applied then new connection credentials should be matched. To clear all UID filters call zmq_setsockopt(socket, ZMQ_IPC_FILTER_UID, NULL, 0).
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 UID filters are only available on platforms supporting SO_PEERCRED or LOCAL_PEERCRED socket options (currently only Linux and later versions of OS X). 
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 This option is deprecated, please use authentication via the ZAP API and IPC whitelisting / blacklisting.  Option value type </td><td> uid_t 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> N/A 
</td></tr><tr VALIGN=top><td> Default value </td><td> no filters (allow from all) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all listening sockets, when using IPC transports. 
</td></tr> </table>

<h3>ZMQ_IPV4ONLY: Use IPv4-only on socket</h3>

Set the IPv4-only option for the socket. This option is deprecated. Please use the ZMQ_IPV6 option. <table> <tr VALIGN=top><td> Option value type </td><td> int 
</td></tr><tr VALIGN=top><td> Option value unit </td><td> boolean 
</td></tr><tr VALIGN=top><td> Default value </td><td> 1 (true) 
</td></tr><tr VALIGN=top><td> Applicable socket types </td><td> all, when using TCP transports. 
</td></tr> </table> 

<h2>Return Value</h2>

The <i>zmq_setsockopt()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.

<h2>Errors</h2>

<b>EINVAL</b>
<dl><dd>The requested option <i>option_name</i> is unknown, or the requested <i>option_len</i> or <i>option_value</i> is invalid.</dl>
 

 <b>ETERM</b>
<dl><dd>The 0MQ <i>context</i> associated with the specified <i>socket</i> was terminated.</dl>
 

 <b>ENOTSOCK</b>
<dl><dd>The provided <i>socket</i> was invalid.</dl>
 

 <b>EINTR</b>
<dl><dd>The operation was interrupted by delivery of a signal.</dl>

<h2>Example</h2>

<b>Subscribing to messages on a ZMQ_SUB socket</b>. /* Subscribe to all messages */
rc = zmq_setsockopt (socket, ZMQ_SUBSCRIBE, &quot;&quot;, 0);
assert (rc == 0);
/* Subscribe to messages prefixed with &quot;ANIMALS.CATS&quot; */
rc = zmq_setsockopt (socket, ZMQ_SUBSCRIBE, &quot;ANIMALS.CATS&quot;, 12); <b>Setting I/O thread affinity</b>. <pre><code>int64_t affinity;
/* Incoming connections on TCP port 5555 shall be handled by I/O thread 1 */
affinity = 1;
rc = zmq_setsockopt (socket, ZMQ_AFFINITY, &amp;affinity, sizeof (affinity));
assert (rc);
rc = zmq_bind (socket, &quot;tcp://lo:5555&quot;);
assert (rc);
/* Incoming connections on TCP port 5556 shall be handled by I/O thread 2 */
affinity = 2;
rc = zmq_setsockopt (socket, ZMQ_AFFINITY, &amp;affinity, sizeof (affinity));
assert (rc);
rc = zmq_bind (socket, &quot;tcp://lo:5556&quot;);
assert (rc);
</code></pre>

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></b>(3) <b><a HREF="/docs/linux/man/3-zmq_socket/">zmq_socket</a></b>(3) <b><a HREF="/docs/linux/man/7-zmq_plain/">zmq_plain</a></b>(7) <b><a HREF="/docs/linux/man/7-zmq_curve/">zmq_curve</a></b>(7) <b><a HREF="/docs/linux/man/7-zmq/">zmq</a></b>(7)

<h2>Authors</h2>

This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<b><a rel="nofollow" HREF="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></b>m[].
