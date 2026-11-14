---
title: "sasl_setprop(3)"
name: "sasl_setprop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_setprop/"
description: "sasl_setprop – Set a SASL property"
---

<p>sasl_setprop &#8211; Set a SASL property</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_setprop(sasl_conn_t *conn,
int propnum,
const void * pvalue)</code></pre>
<h2>Description</h2>
<p><code>sasl_setprop</code> sets the value of a SASL property. For example an application should tell the SASL library about any external negotiated security layer (i.e. TLS). <i>conn</i> is the SASL connection object. <i>propnum</i> is the identifier for the property requested and <i>pvalue</i> contains a pointer to the data. It is the applications job to make sure this type is correct. This is an easy way to crash a program. </p>
<pre>SASL_AUTH_EXTERNAL - external authentication ID (const char *)
SASL_SSF_EXTERNAL - external SSF active -- (sasl_ssf_t)
SASL_DEFUSERREALM - user realm (const char *)
SASL_SEC_PROPS - sasl_security_properties_t (may be freed after call)
SASL_IPLOCALPORT - string describing the local ip and port in the form
 &quot;a.b.c.d;p&quot;, or &quot;e:f:g:h:i:j:k:l;port&quot;
SASL_IPREMOTEPORT - string describing the remote ip and port in the form
 &quot;a.b.c.d;p&quot;, or &quot;e:f:g:h:i:j:k:l;port&quot;</pre>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. SASL error code on failure. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
