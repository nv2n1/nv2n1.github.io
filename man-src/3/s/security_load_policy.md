---
title: "security_load_policy(3)"
name: "security_load_policy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_load_policy/"
description: "security_load_policy – load a new SELinux policy"
---

<p>security_load_policy &#8211; load a new SELinux policy</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_load_policy(void *data, size_t len);
int selinux_mkload_policy(int preservebools);
int selinux_init_load_policy(int *enforce);</code></pre>
<h2>Description</h2>
<p><code>security_load_policy</code>() loads a new policy, returns 0 for success and -1 for error. </p>
<p> <code>selinux_mkload_policy</code>() makes a policy image and loads it. This function provides a higher level interface for loading policy than <code>security_load_policy</code>(), internally determining the right policy version, locating and opening the policy file, mapping it into memory, manipulating it as needed for current boolean settings and/or local definitions, and then calling security_load_policy to load it. <i>preservebools</i> is a boolean flag indicating whether current policy boolean values should be preserved into the new policy (if 1) or reset to the saved policy settings (if 0). The former case is the default for policy reloads, while the latter case is an option for policy reloads but is primarily used for the initial policy load. <code>selinux_init_load_policy</code>() performs the initial policy load. This function determines the desired enforcing mode, sets the <i>enforce</i> argument accordingly for the caller to use, sets the SELinux kernel enforcing status to match it, and loads the policy. It also internally handles the initial selinuxfs mount required to perform these actions. </p>
<p> It should also be noted that after the initial policy load, the SELinux kernel code cannot anymore be disabled and the selinuxfs cannot be unmounted using a call to <code><a href="/docs/linux/man/3-security_disable/">security_disable</a></code>(3). Therefore, after the initial policy load, the only operational changes are those permitted by <code><a href="/docs/linux/man/3-security_setenforce/">security_setenforce</a></code>(3) (i.e. eventually setting the framework in permissive mode rather than in enforcing one).</p>
<h2>Return Value</h2>
<p>Returns zero on success or -1 on error.</p>
<h2>Author</h2>
<p>This manual page has been written by Guido Trentalancia &lt;guido [at] trentalancia.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-security_disable/">security_disable</a></code>(3), <code><a href="/docs/linux/man/8-setenforce/">setenforce</a></code>(8) </p>
