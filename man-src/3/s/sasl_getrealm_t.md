---
title: "sasl_getrealm_t(3)"
name: "sasl_getrealm_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_getrealm_t/"
description: "sasl_getrealm_t – Realm Acquisition Callback"
---

<p>sasl_getrealm_t &#8211; Realm Acquisition Callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_getrealm_t(void *context, int id,
const char **availrealms,
const char **result)</code></pre>
<h2>Description</h2>
<p><code>sasl_getrealm_t</code> is used when there is an interaction with SASL_CB_GETREALM as the type. If a mechanism would use this callback, but it is not present, then the first realm listed is automatically selected. (Note that a mechanism may still force the existence of a getrealm callback by SASL_CB_GETREALM to its required_prompts list). <i>context</i> context from the callback record <i>id</i> callback ID (SASL_CB_GETREALM) <i>availrealms</i> A string list of the available realms. NULL terminated, may be empty. <i>result</i> The chosen realm. (a NUL terminated string) </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3) </p>
