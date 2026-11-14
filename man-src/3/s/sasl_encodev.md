---
title: "sasl_encodev(3)"
name: "sasl_encodev"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_encodev/"
description: "sasl_encode – Encode data for transport to authenticated host"
---

<p>sasl_encode &#8211; Encode data for transport to authenticated host </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_encode(sasl_conn_t *conn,
                const char *input,
                unsigned inputlen,
                const char **output,
                unsigned *outputlen);

int sasl_encodev(sasl_conn_t *conn,
                 const struct iovec *invec,
                 unsigned numiov,
                 const char **output,
                 unsigned *outputlen);</code></pre>
<h2>Description</h2>
<p><code>sasl_encode</code> encodes data to be sent to be sent to a remote host who we&#8217;ve had a successful authentication session with. If there is a negotiated security the data in signed/encrypted and the output should be sent without modification to the remote host. If there is no security layer the output is identical to the input. <code>sasl_encodev</code> does the same, but for a struct iovec instead of a character buffer. <i>output</i> contains the encoded data and is allocated/freed by the library. </p>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. See <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) for meanings of other return codes. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_decode/">sasl_decode</a>(3) </p>
