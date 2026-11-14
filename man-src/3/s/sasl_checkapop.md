---
title: "sasl_checkapop(3)"
name: "sasl_checkapop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_checkapop/"
description: "sasl_checkapop – Check an APOP challenge/response"
---

<p>sasl_checkapop &#8211; Check an APOP challenge/response</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_checkapop(sasl_conn_t *conn,
                   const char *challenge,
                   unsigned challen,
                   const char *response,
                   unsigned resplen);</code></pre>
<h2>Description</h2>
<p><code>sasl_checkapop()</code> will check an APOP challenge/response. APOP is an optional POP3 (RFC 1939) authentication command which uses a shared secret (password). The password is stored in the SASL secrets database. For information on the SASL shared secrets database see the <i>System Administrators Guide</i> in the doc/ directory of the SASL distribution. If called with a <code>NULL</code><i> challenge</i><code>,</code> <code>sasl_checkapop()</code> will check to see if the APOP mechanism is enabled. </p>
<h2>Return Value</h2>
<p>sasl_checkapop returns an integer which corresponds to one of the following codes. SASL_OK indicates that the authentication is complete. All other return codes indicate errors and should either be handled or the authentication session should be quit. See <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) for meanings of return codes. </p>
<h2>Conforming To</h2>
<p>RFC 4422, RFC 1939</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
