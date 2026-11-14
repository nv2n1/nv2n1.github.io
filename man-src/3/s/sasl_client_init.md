---
title: "sasl_client_init(3)"
name: "sasl_client_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_client_init/"
description: "sasl_client_init – SASL client authentication initialization"
---

<p>sasl_client_init &#8211; SASL client authentication initialization </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_client_init(const sasl_callback_t *callbacks);</code></pre>
<h2>Description</h2>
<p><code>sasl_client_init()</code> initializes SASL. It must be called before any calls to sasl_client_start. This call initializes all SASL client drivers (e.g. authentication mechanisms). These are usually found in the /usr/lib/sasl2 directory but the directory may be overridden with the SASL_PATH environment variable. </p>
<p> <i>callbacks</i> specifies the base callbacks for all client connections. See the sasl_callbacks man page for more information</p>
<h2>Return Value</h2>
<p>sasl_client_init returns an integer which corresponds to one of the following codes. SASL_OK is the only one that indicates success. All others indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Errors</h2>
<dl>
<dt><code>SASL_OK</code></p>
<dd>Success</p>
<dt><code>SASL_BADVERS</code></p>
<dd>Mechanism version mismatch</p>
<dt><code>SASL_BADPARAM</code></p>
<dd>Error in config file</p>
<dt><code>SASL_NOMEM</code></p>
<dd>Not enough memory to complete operation </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_client_new/">sasl_client_new</a>(3), <a href="/docs/linux/man/3-sasl_client_start/">sasl_client_start</a>(3), <a href="/docs/linux/man/3-sasl_client_step/">sasl_client_step</a>(3) </p>
