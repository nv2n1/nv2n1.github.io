---
title: "sidput(3)"
name: "sidput"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sidput/"
description: "avc_context_to_sid, avc_sid_to_context, avc_get_initial_sid – obtain and manipulate SELinux security ID’s"
---

<p>avc_context_to_sid, avc_sid_to_context, avc_get_initial_sid &#8211; obtain and manipulate SELinux security ID&#8217;s</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

#include &lt;selinux/avc.h&gt;
int avc_context_to_sid(char *ctx, security_id_t *sid);
int avc_sid_to_context(security_id_t sid, char **ctx);
int avc_get_initial_sid(const char *name, security_id_t *sid);</code></pre>
<h2>Description</h2>
<p>Security ID&#8217;s (SID&#8217;s) are opaque representations of security contexts, managed by the userspace AVC. </p>
<p> <code>avc_context_to_sid</code>() returns a SID for the given <i>context</i> in the memory referenced by <i>sid</i>. </p>
<p> <code>avc_sid_to_context</code>() returns a copy of the context represented by <i>sid</i> in the memory referenced by <i>ctx</i>. The user must free the copy with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). </p>
<p> <code>avc_get_initial_sid</code>() returns a SID for the kernel initial security identifier specified by <i>name</i>.</p>
<h2>Return Value</h2>
<p><code>avc_context_to_sid</code>() and <code>avc_sid_to_context</code>() return zero on success. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>An attempt to allocate memory failed.</dl>
<h2>Notes</h2>
<p>As of libselinux version 2.0.86, SID&#8217;s are no longer reference counted. A SID will be valid from the time it is first obtained until the next call to <code><a href="/docs/linux/man/3-avc_destroy/">avc_destroy</a></code>(3). The <code><a href="/docs/linux/man/3-sidget/">sidget</a></code>(3) and <code><a href="/docs/linux/man/3-sidput/">sidput</a></code>(3) functions, formerly used to adjust the reference count, are no-ops and are deprecated.</p>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3), <code><a href="/docs/linux/man/3-avc_cache_stats/">avc_cache_stats</a></code>(3), <code><a href="/docs/linux/man/3-avc_add_callback/">avc_add_callback</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
