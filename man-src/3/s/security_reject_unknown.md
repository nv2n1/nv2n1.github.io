---
title: "security_reject_unknown(3)"
name: "security_reject_unknown"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_reject_unknown/"
description: "security_getenforce, security_setenforce, security_deny_unknown, security_reject_unknown, security_get_checkreqprot – get or set the enforcing state of SELinux"
---

<p>security_getenforce, security_setenforce, security_deny_unknown, security_reject_unknown, security_get_checkreqprot &#8211; get or set the enforcing state of SELinux</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_getenforce(void);
int security_setenforce(int value);
int security_deny_unknown(void);
int security_reject_unknown(void);
int security_get_checkreqprot(void);</code></pre>
<h2>Description</h2>
<p><code>security_getenforce</code>() returns 0 if SELinux is running in permissive mode, 1 if it is running in enforcing mode, and -1 on error. </p>
<p> <code>security_setenforce</code>() sets SELinux to enforcing mode if the value 1 is passed in, and sets it to permissive mode if 0 is passed in. On success 0 is returned, on error -1 is returned. </p>
<p> <code>security_deny_unknown</code>() returns 0 if SELinux treats policy queries on undefined object classes or permissions as being allowed, 1 if such queries are denied, and -1 on error. </p>
<p> <code>security_reject_unknown</code>() returns 1 if the current policy was built with handle-unknown=reject and SELinux would reject loading it, if it did not define all kernel object classes and permissions. In this state, when <code>selinux_set_mapping()</code> and <code>selinux_check_access()</code> are used with an undefined userspace class or permission, an error is returned and errno is set to EINVAL. </p>
<p> It returns 0 if the current policy was built with handle-unknown=allow or handle-unknown=deny. In this state, policy queries are treated according to <code>security_deny_unknown().</code> -1 is returned on error. </p>
<p> <code>security_get_checkreqprot</code>() can be used to determine whether SELinux is configured to check the protection requested by the application or the actual protection that will be applied by the kernel (including the effects of READ_IMPLIES_EXEC) on mmap and mprotect calls. It returns 0 if SELinux checks the actual protection, 1 if it checks the requested protection, and -1 on error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
