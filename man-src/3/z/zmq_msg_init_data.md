---
title: "zmq_msg_init_data(3)"
name: "zmq_msg_init_data"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_msg_init_data/"
---

zmq_msg_init_data - initialise 0MQ message from a supplied buffer

<h2>Synopsis</h2>

<b>typedef void (zmq_free_fn) (void </b><i>*data</i><b>, void </b><i>*hint</i><b>);</b> <pre><code>int zmq_msg_init_data(zmq_msg_t *msg, void *data, size_t size, zmq_free_fn *ffn, void *hint);</code></pre>

<h2>Description</h2>

The <i>zmq_msg_init_data()</i> function shall initialise the message object referenced by <i>msg</i> to represent the content referenced by the buffer located at address <i>data</i>, <i>size</i> bytes long. No copy of <i>data</i> shall be performed and 0MQ shall take ownership of the supplied buffer. If provided, the deallocation function <i>ffn</i> shall be called once the data buffer is no longer required by 0MQ, with the <i>data</i> and <i>hint</i> arguments supplied to <i>zmq_msg_init_data()</i>.
<dl><dd><font SIZE="+1"> <b>Caution</b> </font> 
 Never access <i>zmq_msg_t</i> members directly, instead always use the <i>zmq_msg</i> family of functions. 
<dl><dd><font SIZE="+1"> <b>Caution</b> </font> 
 The deallocation function <i>ffn</i> needs to be thread-safe, since it will be called from an arbitrary thread. 
<dl><dd><font SIZE="+1"> <b>Caution</b> </font> 
 If the deallocation function is not provided, the allocated memory will not be freed, and this may cause a memory leak. 
<dl><dd><font SIZE="+1"> <b>Caution</b> </font> 
 The functions <i>zmq_msg_init()</i>, <i>zmq_msg_init_data()</i> and <i>zmq_msg_init_size()</i> are mutually exclusive. Never initialize the same <i>zmq_msg_t</i> twice. 

<h2>Return Value</h2>

The <i>zmq_msg_init_data()</i> function shall return zero if successful. Otherwise it shall return -1 and set <i>errno</i> to one of the values defined below.

<h2>Errors</h2>

<b>ENOMEM</b>
<dl><dd>Insufficient storage space is available.</dl>

<h2>Example</h2>

<b>Initialising a message from a supplied buffer</b>. <pre><code>void my_free(void *data, void *hint)
{
    free(data);
}

/*  ...  */

void *data = malloc(6);
assert(data);
memcpy(data, &quot;ABCDEF&quot;, 6);
zmq_msg_t msg;
rc = zmq_msg_init_data(&amp;msg, data, 6, my_free, NULL);
assert(rc == 0);
</code></pre>

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/3-zmq_msg_init_size/">zmq_msg_init_size</a></b>(3) <b><a HREF="/docs/linux/man/3-zmq_msg_init/">zmq_msg_init</a></b>(3) <b><a HREF="/docs/linux/man/3-zmq_msg_close/">zmq_msg_close</a></b>(3) <b><a HREF="/docs/linux/man/3-zmq_msg_data/">zmq_msg_data</a></b>(3) <b><a HREF="/docs/linux/man/3-zmq_msg_size/">zmq_msg_size</a></b>(3) <b><a HREF="/docs/linux/man/7-zmq/">zmq</a></b>(7)

<h2>Authors</h2>

This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<b><a rel="nofollow" HREF="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></b>m[].
