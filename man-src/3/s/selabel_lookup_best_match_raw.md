---
title: "selabel_lookup_best_match_raw(3)"
name: "selabel_lookup_best_match_raw"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_lookup_best_match_raw/"
description: "selabel_lookup_best_match – obtain a best match SELinux security context – Only supported on file backend."
---

<p>selabel_lookup_best_match &#8211; obtain a best match SELinux security context &#8211; Only supported on file backend.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

#include &lt;selinux/label.h&gt;
int selabel_lookup_best_match(struct selabel_handle *hnd,

                              char **context,

                              const char *key,

                              const char **links,

                              int type);
int selabel_lookup_best_match_raw(struct selabel_handle *hnd,

                                  char **context,

                                  const char *key,

                                  const char **links,

                                  int type);</code></pre>
<h2>Description</h2>
<p><code>selabel_lookup_best_match</code>() performs a best match lookup operation on the handle <i>hnd</i>, returning the result in the memory pointed to by <i>context</i>, which must be freed by the caller using <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). The <i>key</i> parameter is a file path to check for best match using zero or more <i>link</i> (aliases) parameters. The order of precedence for best match is:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>An exact match for the real path (<i>key</i>) or</p>
<dt>2.</p>
<dd>An exact match for any of the <i>link</i>s (aliases), or</p>
<dt>3.</p>
<dd>The longest fixed prefix match.</dl>
</dl>
<p> The <i>type</i> parameter is an optional file <i>mode</i> argument that should be set to the mode bits of the file, as determined by <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2). <i>mode</i> may be zero, however full matching may not occur. </p>
<p> <code>selabel_lookup_best_match_raw</code>() behaves identically to <code>selabel_lookup_best_match</code>() but does not perform context translation.</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd>No context corresponding to the input <i>key</i> and <i>type</i> was found.</p>
<dt><code>EINVAL</code></p>
<dd>The <i>key</i> and/or <i>type</i> inputs are invalid, or the context being returned failed validation.</p>
<dt><code>ENOMEM</code></p>
<dd>An attempt to allocate memory failed. </p>
<h2>Notes</h2>
<p>Example usage &#8211; When a service creates a device node, it may also create one or more symlinks to the device node. These symlinks may be the only stable name for the device, e.g. if the partition is dynamically assigned. The file label backend supports this by looking up the &quot;best match&quot; for a device node based on its real path (<i>key</i>) and any <i>link</i>s to it (aliases). The order of precedence for best match is described above. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/3-selabel_stats/">selabel_stats</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2), <code><a href="/docs/linux/man/5-selabel_file/">selabel_file</a></code>(5) </p>
