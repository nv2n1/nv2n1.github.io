---
title: "sasl_server_init(3)"
name: "sasl_server_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_server_init/"
description: "sasl_server_init – SASL server authentication initialization"
---

<p>sasl_server_init &#8211; SASL server authentication initialization </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_server_init(const sasl_callback_t *callbacks,
                     const char *appname);</code></pre>
<h2>Description</h2>
<p><code>sasl_server_init()</code> initializes SASL. It must be called before any calls to sasl_server_start, and only once per process. This call initializes all SASL mechanism drivers (e.g. authentication mechanisms). These are usually found in the /usr/lib/sasl2 directory but the directory may be overridden with the SASL_PATH environment variable (or at compile time). <i>callbacks</i> specifies the base callbacks for all client connections. See the sasl_callbacks man page for more information. <i>appname</i> is the name of the application. It is used for where to find the default configuration file. </p>
<h2>Return Value</h2>
<p>sasl_server_init returns an integer which corresponds to one of the SASL error codes. SASL_OK is the only one that indicates success. All others indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_server_start/">sasl_server_start</a>(3), <a href="/docs/linux/man/3-sasl_server_step/">sasl_server_step</a>(3) </p>
