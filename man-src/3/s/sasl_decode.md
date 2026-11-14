---
title: "sasl_decode(3)"
name: "sasl_decode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_decode/"
description: "sasl_decode – Decode data received"
---

<p>sasl_decode &#8211; Decode data received </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_decode(sasl_conn_t *conn,
                const char *input,
                unsigned inputlen,
                const char **output,
                unsigned *outputlen);</code></pre>
<h2>Description</h2>
<p><code>sasl_decode</code> decodes data received. After successful authentication this function should be called on all data received. It decodes the data from encrypted or signed form to plain data. If there was no security layer negotiated the output is identical to the input. <i>output</i> contains the decoded data and is allocated/freed by the library. One should not to give sasl_decode more data than the negotiated maxbufsize (see sasl_getprop). Note that sasl_decode can succeed and outputlen can be zero. If this is the case simply wait for more data and call sasl_decode again. </p>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. See <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) for meanings of other return codes. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_encode/">sasl_encode</a>(3) </p>
