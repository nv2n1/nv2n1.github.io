---
title: "avc_compute_create(3)"
name: "avc_compute_create"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_compute_create/"
description: "avc_compute_create, avc_compute_member – obtain SELinux label for new object"
---

<h2 class="name">NAME</h2>
<p> avc_compute_create, avc_compute_member &#8211; obtain SELinux label for new object </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>int avc_compute_create(security_id_t </code><i>ssid</i><code>, security_id_t </code><i>tsid</i><code>,</code> <code>security_class_t </code><i>tclass</i><code>, security_id_t *</code><i>newsid</i><code>);</code> </p>
<p> <code>int avc_compute_member(security_id_t </code><i>ssid</i><code>, security_id_t </code><i>tsid</i><code>,</code> <code>security_class_t </code><i>tclass</i><code>, security_id_t *</code><i>newsid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>avc_compute_create</code>() is used to compute a SID to use for labeling a new object in a particular class based on a SID pair. This call is identical to <code>security_compute_create</code>(), but does not require converting from userspace SID&#8217;s to contexts and back again. </p>
<p> <code>avc_compute_member</code>() is used to compute a SID to use for labeling a polyinstantiated object instance of a particular class based on a SID pair. This call is identical to <code>security_compute_member</code>(), but does not require converting from userspace SID&#8217;s to contexts and back again. </p>
<p> These functions return a SID for the computed context in the memory referenced by <i>sid</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>tclass</i> and/or the security contexts referenced by <i>ssid</i> and <i>tsid</i> are not recognized by the currently loaded policy.</p>
<dt><code>ENOMEM</code></p>
<dd> An attempt to allocate memory failed.</dl>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_context_to_sid/">avc_context_to_sid</a></code>(3), <code><a href="/docs/linux/man/3-security_compute_create/">security_compute_create</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
