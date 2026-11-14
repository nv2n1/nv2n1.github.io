---
title: "sasl_getopt_t(3)"
name: "sasl_getopt_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_getopt_t/"
description: "sasl_getopt_t – The SASL get option callback"
---

<p>sasl_getopt_t &#8211; The SASL get option callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_getopt_t(void *context,
                  const char *plugin_name,
                  const char *option,
                  const char **result,
                  unsigned *len);</code></pre>
<h2>Description</h2>
<p><code>sasl_getopt_t</code> is used to retrieve an option, often mechanism specific, from the application. An example of this is requested what KERBEROS_V4 srvtab file to use. <i>plugin_name</i> is the plugin this value if for. <i>option</i> is a string representing the option. A common option that all server applications should handle is method for checking plaintext passwords. See the administrators guide for a full description of this option. Memory management of options supplied by the getopt callback should be done by the application, however, any requested option must remain available until the callback is no longer valid. That is, when sasl_dispose is called for a the connection it is associated with, or sasl_done is called for global callbacks. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
