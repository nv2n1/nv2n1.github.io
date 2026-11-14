---
title: "sasl_auxprop_request(3)"
name: "sasl_auxprop_request"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_auxprop_request/"
description: "sasl_auxprop_request – Request Auxiliary Properties from SASL"
---

<p>sasl_auxprop_request &#8211; Request Auxiliary Properties from SASL </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_auxprop_request(sasl_conn_t *conn,
const char ** propnames)</code></pre>
<h2>Description</h2>
<p><code>sasl_auxprop_request</code> will request that the SASL library obtain properties from any auxiliary property plugins that might be installed (such as the user&#8217;s home directory from an LDAP server for example). Such lookup occurs just after username canonicalization is complete. Therefore, the request should be made before the call to <a href="/docs/linux/man/3-sasl_server_start/">sasl_server_start</a>(3), but after the call to <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3). <i>conn</i> the sasl_conn_t for which the request is being made. <i>propnames</i> a NULL-terminated array of property names to request. Note that this array must persist until a call to sasl_dispose on the sasl_conn_t. </p>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. See <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) for meanings of other return codes. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_auxprop/">sasl_auxprop</a>(3), <a href="/docs/linux/man/3-sasl_auxprop_getctx/">sasl_auxprop_getctx</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_server_start/">sasl_server_start</a>(3) </p>
