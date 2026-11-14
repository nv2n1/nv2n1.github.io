---
title: "selabel_digest(3)"
name: "selabel_digest"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_digest/"
description: "selabel_digest – Return digest of specfiles and list of files used"
---

<p>selabel_digest &#8211; Return digest of specfiles and list of files used</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

#include &lt;selinux/label.h&gt;
int selabel_digest(struct selabel_handle *hnd,

                   unsigned char **digest,

                   size_t *digest_len,

                   char ***specfiles,

                   size_t *num_specfiles);</code></pre>
<h2>Description</h2>
<p><code>selabel_digest</code>() performs an operation on the handle <i>hnd</i>, returning the results of the SHA1 digest pointed to by <i>digest</i>, whose length will be <i>digest_len</i>. The list of specfiles used in the SHA1 digest calculation is returned in <i>specfiles</i> with the number of entries in <i>num_specfiles</i>. </p>
<p> To enable <code>selabel_digest</code>() to return this information the <code>SELABEL_OPT_DIGEST</code> option must be enable in <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3). </p>
<p> The result of <code>selabel_digest</code>() must not be used after <code><a href="/docs/linux/man/3-selabel_close/">selabel_close</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>No digest available (returned if <code>SELABEL_OPT_DIGEST</code> option not enabled).</p>
<dt><code>ENOMEM</code></p>
<dd>An attempt to allocate memory failed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
