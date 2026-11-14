---
title: "sasl_auxprop_getctx(3)"
name: "sasl_auxprop_getctx"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_auxprop_getctx/"
description: "sasl_auxprop_getctx – Acquire an auxiliary property context"
---

<p>sasl_auxprop_getctx &#8211; Acquire an auxiliary property context </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_auxprop_getctx(sasl_conn_t *conn)</code></pre>
<h2>Description</h2>
<p><code>sasl_auxprop_getctx</code> will return an auxiliary property context for the given sasl_conn_t on which the functions described in <a href="/docs/linux/man/3-sasl_auxprop/">sasl_auxprop</a>(3) can operate. <i>conn</i> the sasl_conn_t for which the request is being made. </p>
<h2>Return Value</h2>
<p>Returns a pointer the the context on success. Returns NULL on failure. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_auxprop/">sasl_auxprop</a>(3), <a href="/docs/linux/man/3-sasl_auxprop_request/">sasl_auxprop_request</a>(3) </p>
