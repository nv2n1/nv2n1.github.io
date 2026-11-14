---
title: "sasl_getsimple_t(3)"
name: "sasl_getsimple_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_getsimple_t/"
description: "sasl_getsimple_t – The SASL callback for username/authname/realm"
---

<p>sasl_getsimple_t &#8211; The SASL callback for username/authname/realm </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_getsimple_t(void *context,
                     int id,
                     const char **result,
                     unsigned *len);</code></pre>
<h2>Description</h2>
<p><code>sasl_getsimple_t</code> is used to retrieve simple things from the application. In practice this is authentication name, authorization name, and realm. The <code>id</code> parameter indicates which value is being requested. Possible values include: </p>
<pre>SASL_CB_USER - Client user identity to login as
SASL_CB_AUTHNAME - Client authentication name
SASL_CB_LANGUAGE - Comma-separated list of RFC 1766 languages
SASL_CB_CNONCE - Client-nonce (for testing mostly)</pre>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
