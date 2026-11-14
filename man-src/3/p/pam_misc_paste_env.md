---
title: "pam_misc_paste_env(3)"
name: "pam_misc_paste_env"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_misc_paste_env/"
description: "pam_misc_paste_env – transcribing an environment to that of PAM"
---

<p>pam_misc_paste_env &#8211; transcribing an environment to that of PAM</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_misc.h&gt;

int pam_misc_paste_env(pam_handle_t *pamh, const char *const *user);</code></pre>
<h2>Description</h2>
<dd>This function takes the supplied list of environment pointers and <i>uploads</i> its contents to the PAM environment. Success is indicated by PAM_SUCCESS.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_misc_paste_env</code> function is part of the <code>libpam_misc</code> Library and not defined in any standard.</p>
