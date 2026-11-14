---
title: "zmq_z85_decode(3)"
name: "zmq_z85_decode"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_z85_decode/"
description: "zmq_z85_decode – decode a binary key from Z85 printable text"
---

<p>zmq_z85_decode &#8211; decode a binary key from Z85 printable text</p>
<h2>Synopsis</h2>
<p><code>uint8_t *zmq_z85_decode (uint8_t *dest, const char *string);</code></p>
<h2>Description</h2>
<p>The <i>zmq_z85_decode()</i> function shall decode <i>string</i> into <i>dest</i>. The length of <i>string</i> shall be divisible by 5. <i>dest</i> must be large enough for the decoded value (0.8 x strlen (string)). </p>
<p> The encoding shall follow the ZMQ RFC 32 specification.</p>
<h2>Return Value</h2>
<p>The <i>zmq_z85_decode()</i> function shall return <i>dest</i> if successful, else it shall return NULL.</p>
<h2>Example</h2>
<p><code>Decoding a CURVE key</code>. </p>
<pre><code>const char decoded[] = &quot;rq:rM&gt;}U?@Lns47E1%kR.o@n%FcmmsL/@{H8]yf7&quot;;
uint8_t public_key[32];
zmq_z85_decode(public_key, decoded);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_z85_decode/">zmq_z85_decode</a></code>(3) <code><a href="/docs/linux/man/3-zmq_curve_keypair/">zmq_curve_keypair</a></code>(3) <code><a href="/docs/linux/man/7-zmq_curve/">zmq_curve</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
