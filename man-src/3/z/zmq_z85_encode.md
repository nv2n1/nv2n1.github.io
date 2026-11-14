---
title: "zmq_z85_encode(3)"
name: "zmq_z85_encode"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_z85_encode/"
description: "zmq_z85_encode – encode a binary key as Z85 printable text"
---

<p>zmq_z85_encode &#8211; encode a binary key as Z85 printable text</p>
<h2>Synopsis</h2>
<pre><code>char *zmq_z85_encode(char *dest, const uint8_t *data, size_t size);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_z85_encode()</i> function shall encode the binary block specified by <i>data</i> and <i>size</i> into a string in <i>dest</i>. The size of the binary block must be divisible by 4. The <i>dest</i> must have sufficient space for size * 1.25 plus 1 for a null terminator. A 32-byte CURVE key is encoded as 40 ASCII characters plus a null terminator. </p>
<p> The encoding shall follow the ZMQ RFC 32 specification.</p>
<h2>Return Value</h2>
<p>The <i>zmq_z85_encode()</i> function shall return <i>dest</i> if successful, else it shall return NULL.</p>
<h2>Example</h2>
<p><code>Encoding a CURVE key</code>. </p>
<pre><code>#include &lt;sodium.h&gt;
uint8_t public_key[32];
uint8_t secret_key[32];
int rc = crypto_box_keypair(public_key, secret_key);
assert(rc == 0);
char encoded[41];
zmq_z85_encode(encoded, public_key, 32);
puts(encoded);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_z85_decode/">zmq_z85_decode</a></code>(3) <code><a href="/docs/linux/man/3-zmq_curve_keypair/">zmq_curve_keypair</a></code>(3) <code><a href="/docs/linux/man/7-zmq_curve/">zmq_curve</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
