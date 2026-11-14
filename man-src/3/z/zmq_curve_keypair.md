---
title: "zmq_curve_keypair(3)"
name: "zmq_curve_keypair"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_curve_keypair/"
description: "zmq_curve_keypair – generate a new CURVE keypair"
---

<p>zmq_curve_keypair &#8211; generate a new CURVE keypair</p>
<h2>Synopsis</h2>
<pre><code>int zmq_curve_keypair(char *z85_public_key, char *z85_secret_key);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_curve_keypair()</i> function shall return a newly generated random keypair consisting of a public key and a secret key. The caller provides two buffers, each at least 41 octets large, in which this method will store the keys. The keys are encoded using <code><a href="/docs/linux/man/3-zmq_z85_encode/">zmq_z85_encode</a></code>(3).</p>
<h2>Return Value</h2>
<p>The <i>zmq_curve_keypair()</i> function shall return 0 if successful, else it shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>ENOTSUP</code></p>
<dl>
<dd>The libzmq library was not built with cryptographic support (libsodium).</dl>
<h2>Example</h2>
<p><code>Generating a new CURVE keypair</code>. </p>
<pre><code>char public_key[41];
char secret_key[41];
int rc = zmq_curve_keypair(public_key, secret_key);
assert(rc == 0);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_z85_decode/">zmq_z85_decode</a></code>(3) <code><a href="/docs/linux/man/3-zmq_z85_encode/">zmq_z85_encode</a></code>(3) <code><a href="/docs/linux/man/7-zmq_curve/">zmq_curve</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
