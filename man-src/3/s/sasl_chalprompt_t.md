---
title: "sasl_chalprompt_t(3)"
name: "sasl_chalprompt_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_chalprompt_t/"
description: "sasl_chalprompt_t – Realm Acquisition Callback"
---

<p>sasl_chalprompt_t &#8211; Realm Acquisition Callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_chalprompt_t(void *context, int id,
const char *challenge,
const char *prompt, const char *defresult,
const char **result, unsigned *len)</code></pre>
<h2>Description</h2>
<p><code>sasl_chalprompt_t</code> is used to prompt for input in response to a server challenge. <i>context</i> context from the callback record <i>id</i> callback id (either SASL_CB_ECHOPROMPT or SASL_CB_NOECHOPROMPT) <i>challenge</i> the server&#8217;s challenge <i>prompt</i> A prompt for the user <i>defresult</i> Default result (may be NULL) <i>result</i> The user&#8217;s response (a NUL terminated string) <i>len</i> Length of the user&#8217;s response. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3) </p>
