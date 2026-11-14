---
title: "sasl_errdetail(3)"
name: "sasl_errdetail"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_errdetail/"
description: "sasl_errdetail – Retrieve detailed information about an error"
---

<p>sasl_errdetail &#8211; Retrieve detailed information about an error </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

const char *sasl_errdetail(sasl_conn_t *conn);</code></pre>
<h2>Description</h2>
<p><code>sasl_errdetail</code> provides more detailed information about the most recent error to occur, beyond the information contained in the SASL result code. <i>conn</i> the connection context to inquire about. </p>
<h2>Return Value</h2>
<p>Returns the string describing the error that occurred, or NULL if no error has occurred, or there was an error retrieving it. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3) </p>
