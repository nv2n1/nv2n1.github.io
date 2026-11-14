---
title: "avc_get_initial_sid(3)"
name: "avc_get_initial_sid"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_get_initial_sid/"
description: "avc_context_to_sid, avc_sid_to_context, avc_get_initial_sid – obtain and manipulate SELinux security ID’s"
---

<h2 class="name">NAME</h2>
<p> avc_context_to_sid, avc_sid_to_context, avc_get_initial_sid &#8211; obtain and manipulate SELinux security ID&#8217;s </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>int avc_context_to_sid(char *</code><i>ctx</i><code>, security_id_t *</code><i>sid</i><code>);</code> </p>
<p> <code>int avc_sid_to_context(security_id_t </code><i>sid</i><code>, char **</code><i>ctx</i><code>);</code> </p>
<p> <code>int avc_get_initial_sid(const char *</code><i>name</i><code>, security_id_t *</code><i>sid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> Security ID&#8217;s (SID&#8217;s) are opaque representations of security contexts, managed by the userspace AVC. </p>
<p> <code>avc_context_to_sid</code>() returns a SID for the given <i>context</i> in the memory referenced by <i>sid</i>. </p>
<p> <code>avc_sid_to_context</code>() returns a copy of the context represented by <i>sid</i> in the memory referenced by <i>ctx</i>. The user must free the copy with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). </p>
<p> <code>avc_get_initial_sid</code>() returns a SID for the kernel initial security identifier specified by <i>name</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>avc_context_to_sid</code>() and <code>avc_sid_to_context</code>() return zero on success. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> An attempt to allocate memory failed.</dl>
<h2>NOTES</h2>
<p> As of libselinux version 2.0.86, SID&#8217;s are no longer reference counted. A SID will be valid from the time it is first obtained until the next call to <code><a href="/docs/linux/man/3-avc_destroy/">avc_destroy</a></code>(3). The <code><a href="/docs/linux/man/3-sidget/">sidget</a></code>(3) and <code><a href="/docs/linux/man/3-sidput/">sidput</a></code>(3) functions, formerly used to adjust the reference count, are no-ops and are deprecated.</p>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3), <code><a href="/docs/linux/man/3-avc_cache_stats/">avc_cache_stats</a></code>(3), <code><a href="/docs/linux/man/3-avc_add_callback/">avc_add_callback</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
