---
title: "security_get_boolean_active(3)"
name: "security_get_boolean_active"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_get_boolean_active/"
description: "security_set_boolean, security_commit_booleans, security_get_boolean_names, security_get_boolean_active, security_get_boolean_pending – routines for manipulating SELinux boolean values"
---

<p>security_set_boolean, security_commit_booleans, security_get_boolean_names, security_get_boolean_active, security_get_boolean_pending &#8211; routines for manipulating SELinux boolean values</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_get_boolean_names(char ***names, int *len);
int security_get_boolean_pending(const char *name);
int security_get_boolean_active(const char *name);
int security_set_boolean(const char *name, int value);
int security_set_boolean_list(size_t boolcnt, SELboolean *boollist, int permanent);
int security_commit_booleans(void);</code></pre>
<h2>Description</h2>
<p>The SELinux policy can include conditional rules that are enabled or disabled based on the current values of a set of policy booleans. These policy booleans allow runtime modification of the security policy without having to load a new policy. </p>
<p> The SELinux API allows for a transaction based update. So you can set several boolean values and then commit them all at once. </p>
<p> <code>security_get_boolean_names</code>() provides a list of boolean names, currently supported by the loaded policy. </p>
<p> <code>security_get_boolean_pending</code>() returns the pending value for boolean or -1 on failure. </p>
<p> <code>security_get_boolean_active</code>() returns the active value for boolean or -1 on failure. </p>
<p> <code>security_set_boolean</code>() sets the pending value for boolean </p>
<p> <code>security_set_boolean_list</code>() saves a list of booleans in a single transaction. Note that the <code>int</code><i> permanent </i> flag is deprecated and should be set to zero. </p>
<p> <code>security_commit_booleans</code>() commits all pending values for the booleans.</p>
<h2>Return Value</h2>
<p>Where not otherwise stated, functions described in this manual page return zero on success or -1 on error.</p>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-getsebool/">getsebool</a></code>(8), <code><a href="/docs/linux/man/8-booleans/">booleans</a></code>(8), <code><a href="/docs/linux/man/8-togglesebool/">togglesebool</a></code>(8) </p>
