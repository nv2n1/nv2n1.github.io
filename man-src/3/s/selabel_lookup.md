---
title: "selabel_lookup(3)"
name: "selabel_lookup"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_lookup/"
description: "selabel_lookup – obtain SELinux security context from a string label"
---

<p>selabel_lookup &#8211; obtain SELinux security context from a string label</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

#include &lt;selinux/label.h&gt;
int selabel_lookup(struct selabel_handle *hnd,

                   char **context,

                   const char *key, int type);
int selabel_lookup_raw(struct selabel_handle *hnd,

                       char **context,

                       const char *key, int type);</code></pre>
<h2>Description</h2>
<p><code>selabel_lookup</code>() performs a lookup operation on the handle <i>hnd</i>, returning the result in the memory pointed to by <i>context</i>, which must be freed by the caller using <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). The <i>key</i> and <i>type</i> parameters are the inputs to the lookup operation and are interpreted according to the specific backend that <i>handle</i> is open on. </p>
<p> <code>selabel_lookup_raw</code>() behaves identically to <code>selabel_lookup</code>() but does not perform context translation.</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd>No context corresponding to the input <i>key</i> and <i>type</i> was found.</p>
<dt><code>EINVAL</code></p>
<dd>The <i>key</i> and/or <i>type</i> inputs are invalid, or the context being returned failed validation.</p>
<dt><code>ENOMEM</code></p>
<dd>An attempt to allocate memory failed.</dl>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/3-selabel_stats/">selabel_stats</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
