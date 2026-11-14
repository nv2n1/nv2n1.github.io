---
title: "security_policyvers(3)"
name: "security_policyvers"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_policyvers/"
description: "security_policyvers – get the version of the SELinux policy"
---

<p>security_policyvers &#8211; get the version of the SELinux policy</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_policyvers();</code></pre>
<h2>Description</h2>
<p><code>security_policyvers</code>() returns the version of the policy (a positive integer) on success, or -1 on error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
