---
title: "avc_audit(3)"
name: "avc_audit"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_audit/"
description: "avc_has_perm, avc_has_perm_noaudit, avc_audit, avc_entry_ref_init – obtain and audit SELinux access decisions"
---

<h2 class="name">NAME</h2>
<p> avc_has_perm, avc_has_perm_noaudit, avc_audit, avc_entry_ref_init &#8211; obtain and audit SELinux access decisions </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>void avc_entry_ref_init(struct avc_entry_ref *</code><i>aeref</i><code>);</code> </p>
<p> <code>int avc_has_perm(security_id_t </code><i>ssid</i><code>, security_id_t </code><i>tsid</i><code>,</code> <code>security_class_t </code><i>tclass</i><code>, access_vector_t </code><i>requested</i><code>,</code><br />
 <code>struct avc_entry_ref *</code><i>aeref</i><code>, void *</code><i>auditdata</i><code>);</code> </p>
<p> <code>int avc_has_perm_noaudit(security_id_t </code><i>ssid</i><code>, security_id_t </code><i>tsid</i><code>,</code> <code>security_class_t </code><i>tclass</i><code>, access_vector_t </code><i>requested</i><code>,</code><br />
 <code>struct avc_entry_ref *</code><i>aeref</i><code>, struct av_decision *</code><i>avd</i><code>);</code> </p>
<p> <code>void avc_audit(security_id_t </code><i>ssid</i><code>, security_id_t </code><i>tsid</i><code>,</code> <code>security_class_t </code><i>tclass</i><code>, access_vector_t </code><i>requested</i><code>,</code><br />
 <code>struct av_decision *</code><i>avd</i><code>, int </code><i>result</i><code>, void *</code><i>auditdata</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>avc_entry_ref_init</code>() initializes an <code>avc_entry_ref</code> structure; see <code>ENTRY REFERENCES</code> below. This function may be implemented as a macro. </p>
<p> <code>avc_has_perm</code>() checks whether the <i>requested</i> permissions are granted for subject SID <i>ssid</i> and target SID <i>tsid</i>, interpreting the permissions based on <i>tclass</i> and updating <i>aeref</i>, if non-NULL, to refer to a cache entry with the resulting decision. The granting or denial of permissions is audited in accordance with the policy. The <i>auditdata</i> parameter is for supplemental auditing; see <code>avc_audit</code>() below. </p>
<p> <code>avc_has_perm_noaudit</code>() behaves as <code>avc_has_perm</code>() without producing an audit message. The access decision is returned in <i>avd</i> and can be passed to <code>avc_audit</code>() explicitly. </p>
<p> <code>avc_audit</code>() produces an audit message for the access query represented by <i>ssid</i>, <i>tsid</i>, <i>tclass</i>, and <i>requested</i>, with a decision represented by <i>avd</i>. Pass the value returned by <code>avc_has_perm_noaudit</code>() as <i>result</i>. The <i>auditdata</i> parameter is passed to the user-supplied <code>func_audit</code> callback and can be used to add supplemental information to the audit message; see <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3).</p>
<h2>ENTRY REFERENCES</h2>
<p> Entry references can be used to speed cache performance for repeated queries on the same subject and target. The userspace AVC will check the <i>aeref</i> argument, if supplied, before searching the cache on a permission query. After a query is performed, <i>aeref</i> will be updated to reference the cache entry for that query. A subsequent query on the same subject and target will then have the decision at hand without having to walk the cache. </p>
<p> After declaring an <code>avc_entry_ref</code> structure, use <code>avc_entry_ref_init</code>() to initialize it before passing it to <code>avc_has_perm</code>() or <code>avc_has_perm_noaudit</code>() for the first time. Using an uninitialized structure will produce undefined behavior.</p>
<h2>RETURN VALUE</h2>
<p> If requested permissions are granted, zero is returned. If requested permissions are denied or an error occurred, -1 is returned and <i>errno</i> is set appropriately. </p>
<p> In permissive mode, zero will be returned and <i>errno</i> unchanged even if permissions were denied. <code>avc_has_perm</code>() will still produce an audit message in this case.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> A requested permission was denied.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>tclass</i> and/or the security contexts referenced by <i>ssid</i> and <i>tsid</i> are not recognized by the currently loaded policy.</p>
<dt><code>ENOMEM</code></p>
<dd> An attempt to allocate memory failed.</dl>
<h2>NOTES</h2>
<p> Internal errors encountered by the userspace AVC may cause certain values of <i>errno</i> to be returned unexpectedly. For example, netlink socket errors may produce <code>EACCES</code> or <code>EINVAL</code>. Make sure that userspace object managers are granted appropriate access to netlink by the policy.</p>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_context_to_sid/">avc_context_to_sid</a></code>(3), <code><a href="/docs/linux/man/3-avc_cache_stats/">avc_cache_stats</a></code>(3), <code><a href="/docs/linux/man/3-avc_add_callback/">avc_add_callback</a></code>(3), <code><a href="/docs/linux/man/3-security_compute_av/">security_compute_av</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
