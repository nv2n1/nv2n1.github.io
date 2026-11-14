---
title: "pam_misc_drop_env(3)"
name: "pam_misc_drop_env"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_misc_drop_env/"
description: "pam_misc_drop_env – liberating a locally saved environment"
---

<p>pam_misc_drop_env &#8211; liberating a locally saved environment</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_misc.h&gt;

int pam_misc_drop_env(char **env);</code></pre>
<h2>Description</h2>
<dd>This function is defined to complement the <code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3) function. It liberates the memory associated with <i>env</i>, <i>overwriting</i> with <i>0</i> all memory before <code>free()</code>ing it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_misc_drop_env</code> function is part of the <code>libpam_misc</code> Library and not defined in any standard.</p>
