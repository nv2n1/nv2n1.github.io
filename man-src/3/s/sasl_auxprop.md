---
title: "sasl_auxprop(3)"
name: "sasl_auxprop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_auxprop/"
description: "sasl_auxprop – How to work with SASL auxiliary properties"
---

<p>sasl_auxprop &#8211; How to work with SASL auxiliary properties </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/prop.h&gt;

struct propctx *prop_new(unsigned estimate)

int prop_dup(struct propctx *src_ctx,
struct propctx *dst_ctx)

int prop_request(struct propctx *ctx,
const char **names)

const struct propval *prop_get(struct propctx *ctx)

int prop_getnames(struct propctx *ctx, const char **names,
struct porpval *vals)

void prop_clear(struct propctx *ctx, int requests)

void prop_erase(struct propctx *ctx, const char *name)

void prop_dispose(struct propctx **ctx)

int prop_format(struct propctx *ctx, const char *sep, int seplen,
char *outbuf, unsigned outmax, unsigned *outlen)

int prop_set(struct propctx *ctx, const char *name,
const char *value, int vallen)

int prop_setvals(struct propctx *ctx, const char *name,
const char **values)</code></pre>
<h2>Description</h2>
<p><code>SASL auxiliary properties</code> are used to obtain properties from external sources during the authentication process. For example, a mechanism might need to query an LDAP server to obtain the authentication secret. The application probably needs other information from there as well, such as home directory or UID. The auxiliary property interface allows the two to cooperate, and only results in a single query against the LDAP server (or other property sources). Property lookups take place directly after user canonicalization occurs. Therefore, all requests should be registered with he context before that time. Note that requests can also be registered using the <a href="/docs/linux/man/3-sasl_auxprop_request/">sasl_auxprop_request</a>(3) function. Most of the functions listed below, however, require a property context which can be obtained by calling <a href="/docs/linux/man/3-sasl_auxprop_getctx/">sasl_auxprop_getctx</a>(3). </p>
<h2>API Description</h2>
<dl>
<dt>struct propctx *prop_new(unsigned estimate)</p>
<dd>Create a new property context. Probably unnecessary for application developers to call this at any point. </p>
<p> <i>estimate</i> is the estimate of storage needed total for requests &amp; responses. A value of 0 will imply the library default. </p>
<dt>int prop_dup(struct propctx *src_ctx, struct propctx *dst_ctx)</p>
<dd>Duplicate a given property context. </p>
<dt>int prop_request(struct propctx *ctx, const char **names)</p>
<dd>Add properties to the request list of a given context. </p>
<p> <i>names</i> is the NULL-terminated array of property names, and must persist until the requests are cleared or the context is disposed of with a call to prop_dispose. </p>
<dt>const struct propval *prop_get(struct propctx *ctx)</p>
<dd>Returns a NULL-terminated array of struct propval from the given context. </p>
<dt>int prop_getnames(struct propctx *ctx, const char **names,</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct porpval&nbsp;<wbr>*vals) </p>
<p> Fill in a (provided) array of struct propval based on a list of property names. This implies that the vals array is at least as long as the names array. The values that are filled in by this call persist until next call to prop_request, prop_clear, or prop_dispose on context. If a name specified here was never requested, that its associated values entry will be set to NULL. </p>
<p> Returns number of matching properties that were found, or a SASL error code. </p>
<dt>void prop_clear(struct propctx *ctx, int requests)</p>
<dd>Clear values and optionally requests from a property context. </p>
<p> <i>requests</i> is 1 if the requests should be cleared, 0 otherwise. </p>
<dt>void prop_erase(struct propctx *ctx, const char *name)</p>
<dd>Securely erase the value of a property. </p>
<p> <i>name</i> is the name of the property to erase. </p>
<dt>void prop_dispose(struct propctx **ctx)</p>
<dd>Disposes of a property context and NULLifys the pointer. </p>
<dt>int prop_format(struct propctx *ctx, const char *sep, int seplen,</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>char&nbsp;<wbr>*outbuf, unsigned outmax, unsigned&nbsp;<wbr>*outlen) </p>
<p> Format the requested property names into a string. This not intended for use by the application (only by auxprop plugins). </p>
<p> <i>sep</i> Is the separator to use for the string </p>
<p> <i>outbuf</i> Is the caller-allocated buffer of length <i>outmax</i> that the resulting string will be placed in (including NUL terminator). </p>
<p> <i>outlen</i> if non-NULL, will contain the length of the resulting string (excluding NUL terminator). </p>
<dt>int prop_set(struct propctx *ctx, const char *name, const char *value,</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int vallen) </p>
<p> Adds a property value to the context. This is intended for use by auxprop plugins only. </p>
<p> <i>name</i> is the name of the property to receive the new value, or NULL, which implies that the value will be added to the same property as the last call to either prop_set or prop_setvals. </p>
<p> <i>value</i> is a value for the property of length <i>vallen</i> </p>
<dt>int prop_setvals(struct propctx *ctx, const char *name, const char **values)</p>
<dd>Adds multiple values to a single property. This is intended for use by auxprop plugins only. </p>
<p> <i>name</i> has the same meaning as in <code>prop_set</code> </p>
<p> <i>values</i> are a NULL-terminated array of values to be added the property. </p>
</dl>
<h2>Return Value</h2>
<p>The property functions that return an int return SASL error codes. See <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3). Those that return pointers will return a valid pointer on success, or NULL on any error. </p>
<h2>Conforming To</h2>
<p>RFC 4422 </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_auxprop_request/">sasl_auxprop_request</a>(3), <a href="/docs/linux/man/3-sasl_auxprop_getctx/">sasl_auxprop_getctx</a>(3) </p>
