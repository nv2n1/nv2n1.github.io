---
title: "sepol_genusers(3)"
name: "sepol_genusers"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sepol_genusers/"
description: "sepol_genusers – Generate a new binary policy image with a customized user configuration"
---

<p>sepol_genusers &#8211; Generate a new binary policy image with a customized user configuration</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sepol/sepol.h&gt;
int sepol_genusers(void *data, size_t len, const char *usersdir, void *newdata, size_t *newlen);
void sepol_set_delusers(int on);
</code></pre>
<h2>Description</h2>
<p><code>sepol_genusers</code> generates a new binary policy image from an existing binary policy image stored in the memory region described by the starting address <i>data</i> and the length <i>len</i> and a pair of user configuration files named <code>system.users </code> and <code>local.users</code> from the directory specified by <i>usersdir.</i> The resulting binary policy is placed into dynamically allocated memory and the variables <i>newdata</i> and <i>newlen</i> are set to refer to the new binary image&#8217;s starting address and length. The original binary policy image is not modified. By default, <code>sepol_genusers</code> will preserve user entries that are defined in the original binary policy image but not defined in the user configuration files. If such user entries should instead by omitted entirely from the new binary policy image, then the <code>sepol_set_delusers</code> function may be called with <i>on</i> set to 1 prior to calling <code>sepol_genusers</code> in order to enable deletion of such users. </p>
<h2>Return Value</h2>
<p>Returns 0 on success or -1 otherwise, with errno set appropriately. An errno of ENOENT indicates that one or both of the user configuration files did not exist. An errno of EINVAL indicates that either the original binary policy image or the generated one were invalid. An errno of ENOMEM indicates that insufficient memory was available to process the original binary policy image or to generate the new policy image. Invalid entries in the user configuration files are skipped with a warning. </p>
