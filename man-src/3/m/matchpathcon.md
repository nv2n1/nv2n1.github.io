---
title: "matchpathcon(3)"
name: "matchpathcon"
section: "3"
letter: "m"
url: "/docs/linux/man/3-matchpathcon/"
description: "matchpathcon, matchpathcon_index – get the default SELinux security context for the specified path from the file contexts configuration"
---

<h2 class="name">NAME</h2>
<p> matchpathcon, matchpathcon_index &#8211; get the default SELinux security context for the specified path from the file contexts configuration </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int matchpathcon_init(const char *</code><i>path</i><code>);</code> </p>
<p> <code>int matchpathcon_init_prefix(const char *</code><i>path</i><code>, const char *</code><i>prefix</i><code>);</code> </p>
<p> <code>int matchpathcon_fini(void);</code> </p>
<p> <code>int matchpathcon(const char *</code><i>path</i><code>, mode_t </code><i>mode</i><code>, char **</code><i>con</i><code>);</code> </p>
<p> <code>int matchpathcon_index(const char *</code><i>name</i><code>, mode_t </code><i>mode</i><code>, char **</code><i>con</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This family of functions is deprecated. For new code, please use <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3) with the <code>SELABEL_CTX_FILE</code> backend in place of <code>matchpathcon_init</code>(), use <code><a href="/docs/linux/man/3-selabel_close/">selabel_close</a></code>(3) in place of <code>matchpathcon_fini</code>(), and use <code><a href="/docs/linux/man/3-selabel_lookup/">selabel_lookup</a></code>(3) in place of <code>matchpathcon</code>(). </p>
<p> The remaining description below is for the legacy interface. </p>
<p> <code>matchpathcon_init</code>() loads the file contexts configuration specified by <i>path</i> into memory for use by subsequent <code>matchpathcon</code>() calls. If <i>path</i> is NULL, then the active file contexts configuration is loaded by default, i.e. the path returned by <code><a href="/docs/linux/man/3-selinux_file_context_path/">selinux_file_context_path</a></code>(3). Unless the <code>MATCHPATHCON_BASEONLY </code> flag has been set via <code><a href="/docs/linux/man/3-set_matchpathcon_flags/">set_matchpathcon_flags</a></code>(3), files with the same path prefix but a <code>.homedirs</code> and <code>.local</code> suffix are also looked up and loaded if present. These files provide dynamically generated entries for user home directories and for local customizations. </p>
<p> <code>matchpathcon_init_prefix</code>() is the same as <code>matchpathcon_init</code>() but only loads entries with regular expressions whose first pathname component is a prefix of <i>prefix</i> , e.g. pass &quot;/dev&quot; if you only intend to call <code>matchpathcon</code>() with pathnames beginning with /dev. However, this optimization is no longer necessary due to the use of <i>file_contexts.bin</i> files with precompiled regular expressions, so use of this interface is deprecated. </p>
<p> <code>matchpathcon_fini</code>() frees the memory allocated by a prior call to <code>matchpathcon_init.</code>() This function can be used to free and reset the internal state between multiple <code>matchpathcon_init</code>() calls, or to free memory when finished using <code>matchpathcon</code>(). </p>
<p> <code>matchpathcon</code>() matches the specified <i>pathname,</i> after transformation via <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3) excepting any final symbolic link component if S_IFLNK was specified as the <i>mode,</i> and <i>mode</i> against the <i>file contexts</i> configuration and sets the security context <i>con </i> to refer to the resulting context. The caller must free the returned security context <i>con</i> using <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) when finished using it. <i>mode</i> can be 0 to disable mode matching, but should be provided whenever possible, as it may affect the matching. Only the file format bits (i.e. the file type) of the <i>mode </i> are used. If <code>matchpathcon_init</code>() has not already been called, then this function will call it upon its first invocation with a NULL <i>path,</i> defaulting to the active file contexts configuration. </p>
<p> <code>matchpathcon_index</code>() is the same as <code>matchpathcon</code>() but returns a specification index that can later be used in a <code><a href="/docs/linux/man/3-matchpathcon_filespec_add/">matchpathcon_filespec_add</a></code>(3) call.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success or -1 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-set_matchpathcon_flags/">set_matchpathcon_flags</a></code>(3), <code><a href="/docs/linux/man/3-set_matchpathcon_invalidcon/">set_matchpathcon_invalidcon</a></code>(3), <code><a href="/docs/linux/man/3-set_matchpathcon_printf/">set_matchpathcon_printf</a></code>(3), <code><a href="/docs/linux/man/3-matchpathcon_filespec_add/">matchpathcon_filespec_add</a></code>(3), <code><a href="/docs/linux/man/3-matchpathcon_checkmatches/">matchpathcon_checkmatches</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-setfilecon/">setfilecon</a></code>(3), <code><a href="/docs/linux/man/3-setfscreatecon/">setfscreatecon</a></code>(3) </p>
<h2>Index</h2>
