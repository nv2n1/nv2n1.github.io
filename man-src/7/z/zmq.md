---
title: "zmq(7)"
name: "zmq"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq/"
description: "zmq – 0MQ lightweight messaging kernel"
---

<p>zmq &#8211; 0MQ lightweight messaging kernel</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zmq.h&gt;</code></pre>
<p> <code>cc</code> [<i>flags</i>] <i>files</i> <code>-lzmq</code> [<i>libraries</i>]</p>
<h2>Description</h2>
<p>The 0MQ lightweight messaging kernel is a library which extends the standard socket interfaces with features traditionally provided by specialised <i>messaging middleware</i> products. 0MQ sockets provide an abstraction of asynchronous <i>message queues</i>, multiple <i>messaging patterns</i>, message filtering (<i>subscriptions</i>), seamless access to multiple <i>transport protocols</i> and more. </p>
<p> This documentation presents an overview of 0MQ concepts, describes how 0MQ abstracts standard sockets and provides a reference manual for the functions provided by the 0MQ library.</p>
<h3>Context</h3>
<p>Before using any 0MQ library functions you must create a 0MQ <i>context</i>. When you exit your application you must destroy the <i>context</i>. These functions let you work with <i>contexts</i>: </p>
<p> Create a new 0MQ context</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_ctx_new/">zmq_ctx_new</a></code>(3)</dl>
<p> Work with context properties</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_ctx_set/">zmq_ctx_set</a></code>(3)<code><a href="/docs/linux/man/3-zmq_ctx_get/">zmq_ctx_get</a></code>(3)</dl>
<p> Destroy a 0MQ context</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_ctx_shutdown/">zmq_ctx_shutdown</a></code>(3)<code><a href="/docs/linux/man/3-zmq_ctx_term/">zmq_ctx_term</a></code>(3)</dl>
<p> <font SIZE="+1"> <code>Thread safety</code></p>
<dl>
<dd>A 0MQ <i>context</i> is thread safe and may be shared among as many application threads as necessary, without any additional locking required on the part of the caller. </p>
<p> Individual 0MQ <i>sockets</i> are <i>not</i> thread safe except in the case where full memory barriers are issued when migrating a socket from one thread to another. In practice this means applications can create a socket in one thread with <i>zmq_socket()</i> and then pass it to a <i>newly created</i> thread as part of thread initialization, for example via a structure passed as an argument to <i>pthread_create()</i>.</dl>
<p> </font><font SIZE="+2"> <code>Multiple contexts</code></p>
<dl>
<dd>Multiple <i>contexts</i> may coexist within a single application. Thus, an application can use 0MQ directly and at the same time make use of any number of additional libraries or components which themselves make use of 0MQ as long as the above guidelines regarding thread safety are adhered to.</dl>
<p> </font></p>
<h3>Messages</h3>
<p>A 0MQ message is a discrete unit of data passed between applications or components of the same application. 0MQ messages have no internal structure and from the point of view of 0MQ itself they are considered to be opaque binary data. </p>
<p> The following functions are provided to work with messages: </p>
<p> Initialise a message</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_init_data/">zmq_msg_init_data</a></code>(3)</dl>
<p> Sending and receiving a message</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_send/">zmq_msg_send</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_recv/">zmq_msg_recv</a></code>(3)</dl>
<p> Release a message</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3)</dl>
<p> Access message content</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_data/">zmq_msg_data</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_size/">zmq_msg_size</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_more/">zmq_msg_more</a></code>(3)</dl>
<p> Work with message properties</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_gets/">zmq_msg_gets</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_get/">zmq_msg_get</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_set/">zmq_msg_set</a></code>(3)</dl>
<p> Message manipulation</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_copy/">zmq_msg_copy</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_move/">zmq_msg_move</a></code>(3)</dl>
<h3>Sockets</h3>
<p>0MQ sockets present an abstraction of a asynchronous <i>message queue</i>, with the exact queueing semantics depending on the socket type in use. See <code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) for the socket types provided. </p>
<p> The following functions are provided to work with sockets: </p>
<p> Creating a socket</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3)</dl>
<p> Closing a socket</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_close/">zmq_close</a></code>(3)</dl>
<p> Manipulating socket options</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_getsockopt/">zmq_getsockopt</a></code>(3)<code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3)</dl>
<p> Establishing a message flow</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_bind/">zmq_bind</a></code>(3)<code><a href="/docs/linux/man/3-zmq_connect/">zmq_connect</a></code>(3)</dl>
<p> Sending and receiving messages</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_msg_send/">zmq_msg_send</a></code>(3)<code><a href="/docs/linux/man/3-zmq_msg_recv/">zmq_msg_recv</a></code>(3)<code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3)<code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3)<code><a href="/docs/linux/man/3-zmq_send_const/">zmq_send_const</a></code>(3)</dl>
<p> Monitoring socket events: <code><a href="/docs/linux/man/3-zmq_socket_monitor/">zmq_socket_monitor</a></code>(3) </p>
<p> <code>Input/output multiplexing</code>. 0MQ provides a mechanism for applications to multiplex input/output events over a set containing both 0MQ sockets and standard sockets. This mechanism mirrors the standard <i>poll()</i> system call, and is described in detail in <code><a href="/docs/linux/man/3-zmq_poll/">zmq_poll</a></code>(3).</p>
<h3>Transports</h3>
<p>A 0MQ socket can use multiple different underlying transport mechanisms. Each transport mechanism is suited to a particular purpose and has its own advantages and drawbacks. </p>
<p> The following transport mechanisms are provided: </p>
<p> Unicast transport using TCP</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_tcp/">zmq_tcp</a></code>(7)</dl>
<p> Reliable multicast transport using PGM</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_pgm/">zmq_pgm</a></code>(7)</dl>
<p> Local inter-process communication transport</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_ipc/">zmq_ipc</a></code>(7)</dl>
<p> Local in-process (inter-thread) communication transport</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_inproc/">zmq_inproc</a></code>(7)</dl>
<h3>Proxies</h3>
<p>0MQ provides <i>proxies</i> to create fanout and fan-in topologies. A proxy connects a <i>frontend</i> socket to a <i>backend</i> socket and switches all messages between the two sockets, opaquely. A proxy may optionally capture all traffic to a third socket. To start a proxy in an application thread, use <code><a href="/docs/linux/man/3-zmq_proxy/">zmq_proxy</a></code>(3).</p>
<h3>Security</h3>
<p>A 0MQ socket can select a security mechanism. Both peers must use the same security mechanism. </p>
<p> The following security mechanisms are provided for IPC and TCP connections: </p>
<p> Null security</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_null/">zmq_null</a></code>(7)</dl>
<p> Plain-text authentication using username and password</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_plain/">zmq_plain</a></code>(7)</dl>
<p> Elliptic curve authentication and encryption</p>
<dl>
<dd><code><a href="/docs/linux/man/7-zmq_curve/">zmq_curve</a></code>(7)</dl>
<p> Generate a CURVE keypair in armored text format: <code><a href="/docs/linux/man/3-zmq_curve_keypair/">zmq_curve_keypair</a></code>(3) </p>
<p> Convert an armored key into a 32-byte binary key: <code><a href="/docs/linux/man/3-zmq_z85_decode/">zmq_z85_decode</a></code>(3) </p>
<p> Convert a 32-byte binary CURVE key to an armored text string: <code><a href="/docs/linux/man/3-zmq_z85_encode/">zmq_z85_encode</a></code>(3)</p>
<h2>Error Handling</h2>
<p>The 0MQ library functions handle errors using the standard conventions found on POSIX systems. Generally, this means that upon failure a 0MQ library function shall return either a NULL value (if returning a pointer) or a negative value (if returning an integer), and the actual error code shall be stored in the <i>errno</i> variable. </p>
<p> On non-POSIX systems some users may experience issues with retrieving the correct value of the <i>errno</i> variable. The <i>zmq_errno()</i> function is provided to assist in these cases; for details refer to <code><a href="/docs/linux/man/3-zmq_errno/">zmq_errno</a></code>(3). </p>
<p> The <i>zmq_strerror()</i> function is provided to translate 0MQ-specific error codes into error message strings; for details refer to <code><a href="/docs/linux/man/3-zmq_strerror/">zmq_strerror</a></code>(3).</p>
<h2>Miscellaneous</h2>
<p>The following miscellaneous functions are provided: </p>
<p> Report 0MQ library version</p>
<dl>
<dd><code><a href="/docs/linux/man/3-zmq_version/">zmq_version</a></code>(3)</dl>
<h2>Language Bindings</h2>
<p>The 0MQ library provides interfaces suitable for calling from programs in any language; this documentation documents those interfaces as they would be used by C programmers. The intent is that programmers using 0MQ from other languages shall refer to this documentation alongside any documentation provided by the vendor of their language binding. </p>
<p> Language bindings (C++, Python, PHP, Ruby, Java and more) are provided by members of the 0MQ community and pointers can be found on the 0MQ website.</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
<h2>Resources</h2>
<p>Main web site: m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/">http://www.zeromq.org/</a></code>m[] </p>
<p> Report bugs to the 0MQ development mailing list: &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copying</h2>
<p>Free use of this software is granted under the terms of the GNU Lesser General Public License (LGPL). For details see the files COPYING and COPYING.LESSER included with the 0MQ distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
