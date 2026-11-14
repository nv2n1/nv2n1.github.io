---
title: "set_matchpathcon_flags(3)"
name: "set_matchpathcon_flags"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_matchpathcon_flags/"
description: "set_matchpathcon_flags, set_matchpathcon_invalidcon, set_matchpathcon_printf – set flags controlling the operation of matchpathcon or matchpathcon_index and configure the behaviour of validity chec..."
---

<p>set_matchpathcon_flags, set_matchpathcon_invalidcon, set_matchpathcon_printf &#8211; set flags controlling the operation of matchpathcon or matchpathcon_index and configure the behaviour of validity checking and error displaying</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
void set_matchpathcon_flags(unsigned int flags);
void set_matchpathcon_invalidcon(int (*f)(const char *path, unsigned lineno, char *context));
void set_matchpathcon_printf(void (*f)(const char *fmt, ...));</code></pre>
<h2>Description</h2>
<p><code>set_matchpathcon_flags</code>() sets the flags controlling the operation of <code><a href="/docs/linux/man/3-matchpathcon_init/">matchpathcon_init</a></code>(3) and subsequently <code><a href="/docs/linux/man/3-matchpathcon_index/">matchpathcon_index</a></code>(3) or <code><a href="/docs/linux/man/3-matchpathcon/">matchpathcon</a></code>(3). If the <code>MATCHPATHCON_BASEONLY</code> flag is set, then only the base file contexts configuration file will be processed, not any dynamically generated entries or local customizations. </p>
<p> <code>set_matchpathcon_invalidcon</code>() sets the function used by <code><a href="/docs/linux/man/3-matchpathcon_init/">matchpathcon_init</a></code>(3) when checking the validity of a context in the file contexts configuration. If not set, then this defaults to a test based on <code><a href="/docs/linux/man/3-security_check_context/">security_check_context</a></code>(3), which checks validity against the active policy on a SELinux system. This can be set to instead perform checking based on a binary policy file, e.g. using <code><a href="/docs/linux/man/3-sepol_check_context/">sepol_check_context</a></code>(3), as is done by <code>setfiles -c.</code> The function is also responsible for reporting any such error, and may include the <i>path</i> and <i>lineno</i> in such error messages. </p>
<p> <code>set_matchpathcon_printf</code>() sets the function used by <code><a href="/docs/linux/man/3-matchpathcon_init/">matchpathcon_init</a></code>(3) when displaying errors about the file contexts configuration. If not set, then this defaults to fprintf(stderr, fmt, &#8230;). This can be set to redirect error reporting to a different destination.</p>
<h2>Return Value</h2>
<p>Returns zero on success or -1 otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-matchpathcon/">matchpathcon</a></code>(3), <code><a href="/docs/linux/man/3-matchpathcon_index/">matchpathcon_index</a></code>(3), <code><a href="/docs/linux/man/3-set_matchpathcon_invalidcon/">set_matchpathcon_invalidcon</a></code>(3), <code><a href="/docs/linux/man/3-set_matchpathcon_printf/">set_matchpathcon_printf</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-setfilecon/">setfilecon</a></code>(3), <code><a href="/docs/linux/man/3-setfscreatecon/">setfscreatecon</a></code>(3) </p>
