---
title: "sepol_genbools(3)"
name: "sepol_genbools"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sepol_genbools/"
description: "sepol_genbools – Rewrite a binary policy with different boolean settings"
---

<p>sepol_genbools &#8211; Rewrite a binary policy with different boolean settings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sepol/sepol.h&gt;
int sepol_genbools(void *data, size_t len, char *boolpath);

int sepol_genbools_array(void *data, size_t len, char **names, int *values, int nel);
</code></pre>
<h2>Description</h2>
<p><code>sepol_genbools</code> rewrites a binary policy stored in the memory region described by (data, len) to use the boolean settings specified in the file named by boolpath. The boolean settings are specified by name=value lines where value may be 0 or false to disable or 1 or true to enable. The binary policy is rewritten in place in memory. <code>sepol_genbools_array</code> does likewise, but obtains the boolean settings from the parallel arrays (names, values) with nel elements each. </p>
<h2>Return Value</h2>
<p>Returns 0 on success or -1 otherwise, with errno set appropriately. An errno of ENOENT indicates that the boolean file did not exist. An errno of EINVAL indicates that one or more booleans listed in the boolean file was undefined in the policy or had an invalid value specified; in this case, the binary policy is still rewritten but any invalid boolean settings are ignored. </p>
