---
title: "sasl_global_listmech(3)"
name: "sasl_global_listmech"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_global_listmech/"
description: "sasl_listmech – Retrieve a list of the supported SASL mechanisms"
---

<p>sasl_listmech &#8211; Retrieve a list of the supported SASL mechanisms</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


const char ** sasl_global_listmech()</code></pre>
<h2>Description</h2>
<p><code>sasl_global_listmech()</code> returns a null-terminated array of strings that lists all mechanisms that are loaded by either the client or server side of the library. </p>
<h2>Return Value</h2>
<p>Returns a pointer to the array on success. NULL on failure (sasl library uninitialized). </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_listmech/">sasl_listmech</a>(3), <a href="/docs/linux/man/3-sasl_server_init/">sasl_server_init</a>(3), <a href="/docs/linux/man/3-sasl_client_init/">sasl_client_init</a>(3) </p>
