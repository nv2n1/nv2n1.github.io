---
title: "sasl_authorize_t(3)"
name: "sasl_authorize_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_authorize_t/"
description: "sasl_authorize_t – The SASL authorization callback"
---

<p>sasl_authorize_t &#8211; The SASL authorization callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_authorize_t(void *context,
const char *requested_user, unsigned alen,
const char *auth_identity, unsigned alen,
const char *def_realm, unsigned urlen,
struct propctx *propctx)</code></pre>
<h2>Description</h2>
<p><code>sasl_authorize_t</code> is used to check whether the authorized user <i>auth_identity</i> may act as the user <i>requested_user.</i> For example the user root may wish to authenticate with his credentials but act as the user tmartin (with all of tmartin&#8217;s rights not roots). A server application should be very careful, and probably err on the side of caution, when determining which users may proxy as whom. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3) </p>
