---
title: "sasl_log_t(3)"
name: "sasl_log_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_log_t/"
description: "sasl_log_t – The SASL logging callback"
---

<p>sasl_log_t &#8211; The SASL logging callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_log_t(void *context,
               int level,
               const char *message);</code></pre>
<h2>Description</h2>
<p><code>sasl_log_t</code> is used to log warning/error messages from the SASL library. If not specified syslog will be used. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
