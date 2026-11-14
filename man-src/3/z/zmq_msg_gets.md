---
title: "zmq_msg_gets(3)"
name: "zmq_msg_gets"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_gets/"
description: "zmq_msg_gets – get message metadata property"
---

<p>zmq_msg_gets &#8211; get message metadata property</p>
<h2>Synopsis</h2>
<pre><code>const char *zmq_msg_gets(zmq_msg_t *message, const char *property);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_gets()</i> function shall return the string value for the metadata property specified by the <i>property</i> argument for the message pointed to by the <i>message</i> argument. Both the <i>property</i> argument and the <i>value</i> shall be NULL-terminated UTF8-encoded strings. </p>
<p> Metadata is defined on a per-connection basis during the ZeroMQ connection handshake as specified in &lt;rfc.zeromq.org/spec:37&gt;. </p>
<p> The following ZMTP properties can be retrieved with the <i>zmq_msg_gets()</i> function: </p>
<dl>
<dd>
<pre>Socket-Type
Identity
Resource</pre>
</dl>
<p> Additionally, when available for the underlying transport, the <code>Peer-Address</code> property will return the IP address of the remote endpoint as returned by <a href="/docs/linux/man/2-getnameinfo/">getnameinfo</a>(2). </p>
<p> Other properties may be defined based on the underlying security mechanism, see ZAP authenticated connection sample below.</p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_gets()</i> function shall return the string value for the property if successful. Otherwise it shall return NULL and set <i>errno</i> to one of the values defined below. The caller shall not modify or free the returned value, which shall be owned by the message. The encoding of the property and value shall be UTF8.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The requested <i>property</i> is unknown.</dl>
<h2>Example</h2>
<p><code>Getting the ZAP authenticated user id for a message:</code>. </p>
<pre><code>zmq_msg_t msg;
zmq_msg_init(&amp;msg);
rc = zmq_msg_recv(&amp;msg, dealer, 0);
assert(rc != -1);
const char *user_id = zmq_msg_gets(&amp;msg, &quot;User-Id&quot;);
zmq_msg_close(&amp;msg);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
