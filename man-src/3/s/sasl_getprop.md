---
title: "sasl_getprop(3)"
name: "sasl_getprop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_getprop/"
description: "sasl_getprop – Get a SASL property"
---

<p>sasl_getprop &#8211; Get a SASL property </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_getprop(sasl_conn_t *conn,
                 int propnum,
                 const void **pvalue);</code></pre>
<h2>Description</h2>
<p><code>sasl_getprop</code> gets the value of a SASL property. For example after successful authentication a server may wish to know the authorization name. Or a client application may wish to know the strength of the negotiated security layer. <i>conn</i> is the SASL connection object. <i>propnum</i> is the identifier for the property requested and <i>pvalue</i> is filled in on success. List of properties follows: </p>
<pre>SASL_USERNAME - pointer to NUL terminated user name 
SASL_SSF - security layer security strength factor,
 if 0, call to sasl_encode, sasl_decode unnecessary
SASL_MAXOUTBUF - security layer max output buf unsigned 
SASL_DEFUSERREALM - server authentication realm used 
SASL_GETOPTCTX - context for getopt callback 
SASL_IPLOCALPORT - local address string
SASL_IPREMOTEPORT - remote address string
SASL_SERVICE - service passed to sasl_*_new
SASL_SERVERFQDN - serverFQDN passed to sasl_*_new
SASL_AUTHSOURCE - name of auth source last used, useful for failed
 authentication tracking
SASL_MECHNAME - active mechanism name, if any
SASL_PLUGERR - similar to sasl_errdetail</pre>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. SASL error code on failure. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_client_new/">sasl_client_new</a>(3) </p>
