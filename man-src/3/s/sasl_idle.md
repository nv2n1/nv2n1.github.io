---
title: "sasl_idle(3)"
name: "sasl_idle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_idle/"
description: "sasl_idle – Perform precalculations during an idle period"
---

<p>sasl_idle &#8211; Perform precalculations during an idle period </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_idle( sasl_conn_t *conn)</code></pre>
<h2>Description</h2>
<p><code>sasl_idle</code> may be called during an idle period to allow the SASL library or any mechanisms to perform any necessary precalculation. <i>conn</i> may be NULL to do precalculation prior to a connection taking place. </p>
<h2>Return Value</h2>
<p>Returns 1 if action was taken, 0 if no action was taken. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3) </p>
