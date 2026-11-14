---
title: "zmq_socket(3)"
name: "zmq_socket"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_socket/"
description: "zmq_socket – create 0MQ socket"
---

<p>zmq_socket &#8211; create 0MQ socket</p>
<h2>Synopsis</h2>
<pre><code>void *zmq_socket(void *context, int type);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_socket()</i> function shall create a 0MQ socket within the specified <i>context</i> and return an opaque handle to the newly created socket. The <i>type</i> argument specifies the socket type, which determines the semantics of communication over the socket. The newly created socket is initially unbound, and not associated with any endpoints. In order to establish a message flow a socket must first be connected to at least one endpoint with <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3), or at least one endpoint must be created for accepting incoming connections with <code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3). <code>Key differences to conventional sockets</code>. Generally speaking, conventional sockets present a <i>synchronous</i> interface to either connection-oriented reliable byte streams (SOCK_STREAM), or connection-less unreliable datagrams (SOCK_DGRAM). In comparison, 0MQ sockets present an abstraction of an asynchronous <i>message queue</i>, with the exact queueing semantics depending on the socket type in use. Where conventional sockets transfer streams of bytes or discrete datagrams, 0MQ sockets transfer discrete <i>messages</i>. 0MQ sockets being <i>asynchronous</i> means that the timings of the physical connection setup and tear down, reconnect and effective delivery are transparent to the user and organized by 0MQ itself. Further, messages may be <i>queued</i> in the event that a peer is unavailable to receive them. Conventional sockets allow only strict one-to-one (two peers), many-to-one (many clients, one server), or in some cases one-to-many (multicast) relationships. With the exception of <i>ZMQ_PAIR</i>, 0MQ sockets may be connected <code>to multiple endpoints</code> using <i>zmq_connect()</i>, while simultaneously accepting incoming connections <code>from multiple endpoints</code> bound to the socket using <i>zmq_bind()</i>, thus allowing many-to-many relationships. <code>Thread safety</code>. 0MQ <i>sockets</i> are <i>not</i> thread safe. Applications MUST NOT use a socket from multiple threads except after migrating a socket from one thread to another with a &quot;full fence&quot; memory barrier. <code>Socket types</code>. The following sections present the socket types defined by 0MQ, grouped by the general <i>messaging pattern</i> which is built from related socket types.</p>
<h3>Request-reply pattern</h3>
<p>The request-reply pattern is used for sending requests from a ZMQ_REQ <i>client</i> to one or more ZMQ_REP <i>services</i>, and receiving subsequent replies to each request sent. The request-reply pattern is formally defined by m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:28">http://rfc.zeromq.org/spec:28</a></code>m[].<br />
 <font SIZE="+1"> <code>ZMQ_REQ</code></p>
<dl>
<dd>A socket of type <i>ZMQ_REQ</i> is used by a <i>client</i> to send requests to and receive replies from a <i>service</i>. This socket type allows only an alternating sequence of <i>zmq_send(request)</i> and subsequent <i>zmq_recv(reply)</i> calls. Each request sent is round-robined among all <i>services</i>, and each reply received is matched with the last issued request. If no services are available, then any send operation on the socket shall block until at least one <i>service</i> becomes available. The REQ socket shall not discard messages.<br />
 <code>Table 1. Summary of ZMQ_REQ characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_REP</i>, <i>ZMQ_ROUTER</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Bidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Send, Receive, Send, Receive, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> Round-robin
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Last peer
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Block
</td>
</tr>
</table>
<p> <font SIZE="+1"><br />
 </font><font SIZE="+2"> <code>ZMQ_REP</code></p>
<dl>
<dd>A socket of type <i>ZMQ_REP</i> is used by a <i>service</i> to receive requests from and send replies to a <i>client</i>. This socket type allows only an alternating sequence of <i>zmq_recv(request)</i> and subsequent <i>zmq_send(reply)</i> calls. Each request received is fair-queued from among all <i>clients</i>, and each reply sent is routed to the <i>client</i> that issued the last request. If the original requester does not exist any more the reply is silently discarded.<br />
 <code>Table 2. Summary of ZMQ_REP characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_REQ</i>, <i>ZMQ_DEALER</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Bidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Receive, Send, Receive, Send, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> Last peer
</td>
</tr>
</table>
<p> <font SIZE="+2"><br />
 </font><font SIZE="+3"> <code>ZMQ_DEALER</code></p>
<dl>
<dd>A socket of type <i>ZMQ_DEALER</i> is an advanced pattern used for extending request/reply sockets. Each message sent is round-robined among all connected peers, and each message received is fair-queued from all connected peers. When a <i>ZMQ_DEALER</i> socket enters the <i>mute</i> state due to having reached the high water mark for all peers, or if there are no peers at all, then any <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) operations on the socket shall block until the mute state ends or at least one peer becomes available for sending; messages are not discarded. When a <i>ZMQ_DEALER</i> socket is connected to a <i>ZMQ_REP</i> socket each message sent must consist of an empty message part, the <i>delimiter</i>, followed by one or more <i>body parts</i>.<br />
 <code>Table 3. Summary of ZMQ_DEALER characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_ROUTER</i>, <i>ZMQ_REP</i>, <i>ZMQ_DEALER</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Bidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Unrestricted
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> Round-robin
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Block
</td>
</tr>
</table>
<p> <font SIZE="+3"><br />
 </font><font SIZE="+4"> <code>ZMQ_ROUTER</code></p>
<dl>
<dd>A socket of type <i>ZMQ_ROUTER</i> is an advanced socket type used for extending request/reply sockets. When receiving messages a <i>ZMQ_ROUTER</i> socket shall prepend a message part containing the <i>identity</i> of the originating peer to the message before passing it to the application. Messages received are fair-queued from among all connected peers. When sending messages a <i>ZMQ_ROUTER</i> socket shall remove the first part of the message and use it to determine the <i>identity</i> of the peer the message shall be routed to. If the peer does not exist anymore the message shall be silently discarded by default, unless <i>ZMQ_ROUTER_MANDATORY</i> socket option is set to <i>1</i>. When a <i>ZMQ_ROUTER</i> socket enters the <i>mute</i> state due to having reached the high water mark for all peers, then any messages sent to the socket shall be dropped until the mute state ends. Likewise, any messages routed to a peer for which the individual high water mark has been reached shall also be dropped. When a <i>ZMQ_REQ</i> socket is connected to a <i>ZMQ_ROUTER</i> socket, in addition to the <i>identity</i> of the originating peer each message received shall contain an empty <i>delimiter</i> message part. Hence, the entire structure of each received message as seen by the application becomes: one or more <i>identity</i> parts, <i>delimiter</i> part, one or more <i>body parts</i>. When sending replies to a <i>ZMQ_REQ</i> socket the application must include the <i>delimiter</i> part.<br />
 <code>Table 4. Summary of ZMQ_ROUTER characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_DEALER</i>, <i>ZMQ_REQ</i>, <i>ZMQ_ROUTER</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Bidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Unrestricted
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> See text
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Drop
</td>
</tr>
</table>
<p> <font SIZE="+4"></dl>
<p> </font></p>
<h3>Publish-subscribe pattern</h3>
<p>The publish-subscribe pattern is used for one-to-many distribution of data from a single <i>publisher</i> to multiple <i>subscribers</i> in a fan out fashion. The publish-subscribe pattern is formally defined by m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:29">http://rfc.zeromq.org/spec:29</a></code>m[].<br />
 <font SIZE="+1"> <code>ZMQ_PUB</code></p>
<dl>
<dd>A socket of type <i>ZMQ_PUB</i> is used by a <i>publisher</i> to distribute data. Messages sent are distributed in a fan out fashion to all connected peers. The <code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3) function is not implemented for this socket type. When a <i>ZMQ_PUB</i> socket enters the <i>mute</i> state due to having reached the high water mark for a <i>subscriber</i>, then any messages that would be sent to the <i>subscriber</i> in question shall instead be dropped until the mute state ends. The <i>zmq_send()</i> function shall never block for this socket type.<br />
 <code>Table 5. Summary of ZMQ_PUB characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_SUB</i>, <i>ZMQ_XSUB</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Unidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Send only
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> Fan out
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Drop
</td>
</tr>
</table>
<p> <font SIZE="+1"><br />
 </font><font SIZE="+2"> <code>ZMQ_SUB</code></p>
<dl>
<dd>A socket of type <i>ZMQ_SUB</i> is used by a <i>subscriber</i> to subscribe to data distributed by a <i>publisher</i>. Initially a <i>ZMQ_SUB</i> socket is not subscribed to any messages, use the <i>ZMQ_SUBSCRIBE</i> option of <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) to specify which messages to subscribe to. The <i>zmq_send()</i> function is not implemented for this socket type.<br />
 <code>Table 6. Summary of ZMQ_SUB characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_PUB</i>, <i>ZMQ_XPUB</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Unidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Receive only
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> N/A
</td>
</tr>
</table>
<p> <font SIZE="+2"><br />
 </font><font SIZE="+3"> <code>ZMQ_XPUB</code></p>
<dl>
<dd>Same as ZMQ_PUB except that you can receive subscriptions from the peers in form of incoming messages. Subscription message is a byte 1 (for subscriptions) or byte 0 (for unsubscriptions) followed by the subscription body. Messages without a sub/unsub prefix are also received, but have no effect on subscription status.<br />
 <code>Table 7. Summary of ZMQ_XPUB characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_SUB</i>, <i>ZMQ_XSUB</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Unidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Send messages, receive subscriptions
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> Fan out
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Drop
</td>
</tr>
</table>
<p> <font SIZE="+3"><br />
 </font><font SIZE="+4"> <code>ZMQ_XSUB</code></p>
<dl>
<dd>Same as ZMQ_SUB except that you subscribe by sending subscription messages to the socket. Subscription message is a byte 1 (for subscriptions) or byte 0 (for unsubscriptions) followed by the subscription body. Messages without a sub/unsub prefix may also be sent, but have no effect on subscription status.<br />
 <code>Table 8. Summary of ZMQ_XSUB characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_PUB</i>, <i>ZMQ_XPUB</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Unidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Receive messages, send subscriptions
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Drop
</td>
</tr>
</table>
<p> <font SIZE="+4"></dl>
<p> </font></p>
<h3>Pipeline pattern</h3>
<p>The pipeline pattern is used for distributing data to <i>nodes</i> arranged in a pipeline. Data always flows down the pipeline, and each stage of the pipeline is connected to at least one <i>node</i>. When a pipeline stage is connected to multiple <i>nodes</i> data is round-robined among all connected <i>nodes</i>. The pipeline pattern is formally defined by m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:30">http://rfc.zeromq.org/spec:30</a></code>m[].<br />
 <font SIZE="+1"> <code>ZMQ_PUSH</code></p>
<dl>
<dd>A socket of type <i>ZMQ_PUSH</i> is used by a pipeline <i>node</i> to send messages to downstream pipeline <i>nodes</i>. Messages are round-robined to all connected downstream <i>nodes</i>. The <i>zmq_recv()</i> function is not implemented for this socket type. When a <i>ZMQ_PUSH</i> socket enters the <i>mute</i> state due to having reached the high water mark for all downstream <i>nodes</i>, or if there are no downstream <i>nodes</i> at all, then any <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) operations on the socket shall block until the mute state ends or at least one downstream <i>node</i> becomes available for sending; messages are not discarded.<br />
 <code>Table 9. Summary of ZMQ_PUSH characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_PULL</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Unidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Send only
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> Round-robin
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Block
</td>
</tr>
</table>
<p> <font SIZE="+1"><br />
 </font><font SIZE="+2"> <code>ZMQ_PULL</code></p>
<dl>
<dd>A socket of type <i>ZMQ_PULL</i> is used by a pipeline <i>node</i> to receive messages from upstream pipeline <i>nodes</i>. Messages are fair-queued from among all connected upstream <i>nodes</i>. The <i>zmq_send()</i> function is not implemented for this socket type.<br />
 <code>Table 10. Summary of ZMQ_PULL characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_PUSH</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Unidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Receive only
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Block
</td>
</tr>
</table>
<p> <font SIZE="+2"></dl>
<p> </font></p>
<h3>Exclusive pair pattern</h3>
<p>The exclusive pair pattern is used to connect a peer to precisely one other peer. This pattern is used for inter-thread communication across the inproc transport. The exclusive pair pattern is formally defined by m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:31">http://rfc.zeromq.org/spec:31</a></code>m[].<br />
 <font SIZE="+1"> <code>ZMQ_PAIR</code></p>
<dl>
<dd>A socket of type <i>ZMQ_PAIR</i> can only be connected to a single peer at any one time. No message routing or filtering is performed on messages sent over a <i>ZMQ_PAIR</i> socket. When a <i>ZMQ_PAIR</i> socket enters the <i>mute</i> state due to having reached the high water mark for the connected peer, or if no peer is connected, then any <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) operations on the socket shall block until the peer becomes available for sending; messages are not discarded.</p>
<dl>
<dd></font><font SIZE="+2"> <code>Note</code> </font><font SIZE="+1"><br />
 <i>ZMQ_PAIR</i> sockets are designed for inter-thread communication across the <code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7) transport and do not implement functionality such as auto-reconnection. <i>ZMQ_PAIR</i> sockets are considered experimental and may have other missing or broken aspects.<br />
 <code>Table 11. Summary of ZMQ_PAIR characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> <i>ZMQ_PAIR</i>
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Bidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Unrestricted
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> N/A
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> Block
</td>
</tr>
</table>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h3>Native Pattern</h3>
<p>The native pattern is used for communicating with TCP peers and allows asynchronous requests and replies in either direction.<br />
 <font SIZE="+1"> <code>ZMQ_STREAM</code></p>
<dl>
<dd>A socket of type <i>ZMQ_STREAM</i> is used to send and receive TCP data from a non-0MQ peer, when using the tcp:// transport. A <i>ZMQ_STREAM</i> socket can act as client and/or server, sending and/or receiving TCP data asynchronously. When receiving TCP data, a <i>ZMQ_STREAM</i> socket shall prepend a message part containing the <i>identity</i> of the originating peer to the message before passing it to the application. Messages received are fair-queued from among all connected peers. When sending TCP data, a <i>ZMQ_STREAM</i> socket shall remove the first part of the message and use it to determine the <i>identity</i> of the peer the message shall be routed to, and unroutable messages shall cause an EHOSTUNREACH or EAGAIN error. To open a connection to a server, use the zmq_connect call, and then fetch the socket identity using the ZMQ_IDENTITY zmq_getsockopt call. To close a specific connection, send the identity frame followed by a zero-length message (see EXAMPLE section). When a connection is made, a zero-length message will be received by the application. Similarly, when the peer disconnects (or the connection is lost), a zero-length message will be received by the application. The ZMQ_SNDMORE flag is ignored on data frames. You must send one identity frame followed by one data frame. Also, please note that omitting the ZMQ_SNDMORE flag will prevent sending further data (from any client) on the same socket.<br />
 <code>Table 12. Summary of ZMQ_STREAM characteristics</code> </font></p>
<table>
<tr VALIGN=top>
<td> Compatible peer sockets </td>
<td> none.
</td>
</tr>
<tr VALIGN=top>
<td> Direction </td>
<td> Bidirectional
</td>
</tr>
<tr VALIGN=top>
<td> Send/receive pattern </td>
<td> Unrestricted
</td>
</tr>
<tr VALIGN=top>
<td> Outgoing routing strategy </td>
<td> See text
</td>
</tr>
<tr VALIGN=top>
<td> Incoming routing strategy </td>
<td> Fair-queued
</td>
</tr>
<tr VALIGN=top>
<td> Action in mute state </td>
<td> EAGAIN
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<h2>Return Value</h2>
<p>The <i>zmq_socket()</i> function shall return an opaque handle to the newly created socket if successful. Otherwise, it shall return NULL and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The requested socket <i>type</i> is invalid.</dl>
<p> <code>EFAULT</code></p>
<dl>
<dd>The provided <i>context</i> is invalid.</dl>
<p> <code>EMFILE</code></p>
<dl>
<dd>The limit on the total number of open 0MQ sockets has been reached.</dl>
<p> <code>ETERM</code></p>
<dl>
<dd>The context specified was terminated.</dl>
<h2>Example</h2>
<p><code>Creating a simple HTTP server using ZMQ_STREAM</code>. </p>
<pre><code>void *ctx = zmq_ctx_new();
assert(ctx);
/* Create ZMQ_STREAM socket */
void *socket = zmq_socket(ctx, ZMQ_STREAM);
assert(socket);
int rc = zmq_bind(socket, &quot;tcp://*:8080&quot;);
assert(rc == 0);
/* Data structure to hold the ZMQ_STREAM ID */
uint8_t id[256];
size_t id_size = 256;
/* Data structure to hold the ZMQ_STREAM received data */
uint8_t raw[256];
size_t raw_size = 256;
while (1) {
    /*  Get HTTP request; ID frame and then request */
    id_size = zmq_recv(socket, id, 256, 0);
    assert(id_size &gt; 0);
    do {
        raw_size = zmq_recv(socket, raw, 256, 0);
        assert(raw_size &gt;= 0);
    } while (raw_size == 256);
    /* Prepares the response */
    char http_response[] =
        &quot;HTTP/1.0 200 OK
&quot;
        &quot;Content-Type: text/plain
&quot;
        &quot;
&quot;
        &quot;Hello, World!&quot;;
    /* Sends the ID frame followed by the response */
    zmq_send(socket, id, id_size, ZMQ_SNDMORE);
    zmq_send(socket, http_response, strlen(http_response), ZMQ_SNDMORE);
    /* Closes the connection by sending the ID frame followed by a zero response */
    zmq_send(socket, id, id_size, ZMQ_SNDMORE);
    zmq_send(socket, 0, 0, ZMQ_SNDMORE);
    /* NOTE: If we don't use ZMQ_SNDMORE, then we won't be able to send more */
    /* message to any client */
}
zmq_close(socket);
zmq_ctx_destroy(ctx);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_init/">zmq_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) <code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3) <code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3) <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) <code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3) <code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
