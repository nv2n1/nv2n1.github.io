---
title: "zmq_msg_get(3)"
name: "zmq_msg_get"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_get/"
description: "zmq_msg_get – get message property"
---

<p>zmq_msg_get &#8211; get message property</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_get(zmq_msg_t *message, int property);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_get()</i> function shall return the value for the property specified by the <i>property</i> argument for the message pointed to by the <i>message</i> argument. </p>
<p> The following properties can be retrieved with the <i>zmq_msg_get()</i> function: </p>
<p> <code>ZMQ_MORE</code></p>
<dl>
<dd>Indicates that there are more message frames to follow after the <i>message</i>.</dl>
<p> <code>ZMQ_SRCFD</code></p>
<dl>
<dd>Returns the file descriptor of the socket the <i>message</i> was read from. This allows application to retrieve the remote endpoint via <i><a href="/docs/linux/man/2-getpeername/">getpeername</a>(2)</i>. Be aware that the respective socket might be closed already, reused even. Currently only implemented for TCP sockets.</dl>
<p> <code>ZMQ_SHARED</code></p>
<dl>
<dd>Indicates that a message MAY share underlying storage with another copy of this message.</dl>
<h2>Return Value</h2>
<p>The <i>zmq_msg_get()</i> function shall return the value for the property if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>EINVAL</code></p>
<dl>
<dd>The requested <i>property</i> is unknown.</dl>
<h2>Example</h2>
<p><code>Receiving a multi-frame message</code>. </p>
<pre><code>zmq_msg_t frame;
while (true) {
    //  Create an empty 0MQ message to hold the message frame
    int rc = zmq_msg_init(&amp;frame);
    assert(rc == 0);
    //  Block until a message is available to be received from socket
    rc = zmq_msg_recv(socket, &amp;frame, 0);
    assert(rc != -1);
    if (zmq_msg_get(&amp;frame, ZMQ_MORE))
        fprintf(stderr, &quot;more
&quot;);
    else {
        fprintf(stderr, &quot;end
&quot;);
        break;
    }
    zmq_msg_close(&amp;frame);
}
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_set/">zmq_msg_set</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
