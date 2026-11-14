---
title: "sasl_getpath_t(3)"
name: "sasl_getpath_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_getpath_t/"
description: "sasl_getpath_t – The SASL callback to indicate location of the mechanism drivers"
---

<p>sasl_getpath_t &#8211; The SASL callback to indicate location of the mechanism drivers </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_getpath_t(void *context,
                   char **path);</code></pre>
<h2>Description</h2>
<p><code>sasl_getpath_t</code> is used if the application wishes to use a different location for the SASL mechanism drivers (the shared library files). If this callback is not used SASL will either use the location in the environment variable SASL_PATH or /usr/lib/sasl2 by default. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
