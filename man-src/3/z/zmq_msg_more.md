---
title: "zmq_msg_more(3)"
name: "zmq_msg_more"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_more/"
description: "zmq_msg_more – indicate if there are more message parts to receive"
---

<p>zmq_msg_more &#8211; indicate if there are more message parts to receive</p>
<h2>Synopsis</h2>
<pre><code>int zmq_msg_more(zmq_msg_t *message);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_msg_more()</i> function indicates whether this is part of a multi-part message, and there are further parts to receive. This method can safely be called after <i>zmq_msg_close()</i>. This method is identical to <i>zmq_msg_get()</i> with an argument of ZMQ_MORE.</p>
<h2>Return Value</h2>
<p>The <i>zmq_msg_more()</i> function shall return zero if this is the final part of a multi-part message, or the only part of a single-part message. It shall return 1 if there are further parts to receive.</p>
<h2>Example</h2>
<p><code>Receiving a multi-part message</code>. </p>
<pre><code>zmq_msg_t part;
while (true) {
    //  Create an empty 0MQ message to hold the message part
    int rc = zmq_msg_init(&amp;part);
    assert(rc == 0);
    //  Block until a message is available to be received from socket
    rc = zmq_msg_recv(socket, &amp;part, 0);
    assert(rc != -1);
    if (zmq_msg_more(&amp;part))
        fprintf(stderr, &quot;more
&quot;);
    else {
        fprintf(stderr, &quot;end
&quot;);
        break;
    }
    zmq_msg_close(&amp;part);
}
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_msg_get/">zmq_msg_get</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_set/">zmq_msg_set</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></code>(3) <code><a href="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
