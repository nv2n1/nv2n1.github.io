---
title: "sepol_check_context(3)"
name: "sepol_check_context"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sepol_check_context/"
description: "sepol_check_context – Check the validity of a security context against a binary policy."
---

<p>sepol_check_context &#8211; Check the validity of a security context against a binary policy.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sepol/sepol.h&gt;
int sepol_check_context(const char *context);
int sepol_set_policydb_from_file(FILE *fp);
</code></pre>
<h2>Description</h2>
<p><code>sepol_check_context</code> checks the validity of a security context against a binary policy previously loaded from a file via <code>sepol_set_policydb_from_file.</code> It is used by <code>setfiles -c</code> to validate a file contexts configuration against the binary policy upon policy builds. For validating a context against the active policy on a SELinux system, use <code>security_check_context</code> from libselinux instead. </p>
<h2>Return Value</h2>
<p>Returns 0 on success or -1 with errno set otherwise. </p>
