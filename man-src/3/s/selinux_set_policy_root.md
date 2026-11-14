---
title: "selinux_set_policy_root(3)"
name: "selinux_set_policy_root"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_set_policy_root/"
description: "selinux_policy_root – return the path of the SELinux policy files for this machine selinux_set_policy_root – Set an alternate SELinux root path for the SELinux policy files for this machine."
---

<p>selinux_policy_root &#8211; return the path of the SELinux policy files for this machine selinux_set_policy_root &#8211; Set an alternate SELinux root path for the SELinux policy files for this machine.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
const char *selinux_policy_root(void);
int selinux_set_policy_root(const char *policypath);</code></pre>
<h2>Description</h2>
<p><code>selinux_policy_root</code>() reads the contents of the <i>/etc/selinux/config</i> file to determine which policy files should be used for this machine. <code>selinux_set_policy_root</code>() sets up all policy paths based on the alternate root </p>
<p> <i>/etc/selinux/config</i> file to determine which policy files should be used for this machine.</p>
<h2>Return Value</h2>
<p>On success, selinux_policy_root returns a directory path containing the SELinux policy files. On failure, selinux_policy_root returns NULL. On success, selinux_set_policy_root returns 0 on success -1 on failure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
