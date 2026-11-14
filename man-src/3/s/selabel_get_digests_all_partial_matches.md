---
title: "selabel_get_digests_all_partial_matches(3)"
name: "selabel_get_digests_all_partial_matches"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_get_digests_all_partial_matches/"
description: "selabel_get_digests_all_partial_matches – retrieve the partial matches digest and the xattr digest that applies to the supplied path – Only supported on file backend."
---

<p>selabel_get_digests_all_partial_matches &#8211; retrieve the partial matches digest and the xattr digest that applies to the supplied path &#8211; Only supported on file backend.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdbool.h&gt;


#include &lt;selinux/selinux.h&gt;


#include &lt;selinux/label.h&gt;</code></pre>
<p> <code>bool selabel_get_digests_all_partial_matches(</code> <code>struct selabel_handle *</code><i>hnd</i><code>,</code><br />
 <code>const char *</code><i>key</i><code>,</code><br />
 <code>uint8_t **</code><i>calculated_digest</i><code>,</code><br />
 <code>uint8_t **</code><i>xattr_digest</i><code>,</code><br />
 <code>size_t *</code><i>digest_len</i><code>);</code></p>
<h2>Description</h2>
<p><code>selabel_get_digests_all_partial_matches</code>() retrieves the file_contexts partial matches digest and the xattr digest that applies to the supplied path on the handle <i>hnd</i>.<br />
 The <i>key</i> parameter is the path to retrieve the digests.<br />
 The <i>calculated_digest</i> is a pointer to the <i>key</i> calculated file_contexts digest of all applicable partial matches, or NULL if none exist. The caller must <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the buffer.<br />
 The <i>xattr_digest</i> is a pointer to the <i>key</i> <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7) stored digest, or NULL if it does not exist. The caller must <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the buffer.<br />
 The <i>digest_len</i> is the length of the digests that will always be returned (even if both are NULL). Note that if both digests are returned, they will always be the same length. </p>
<h2>Return Value</h2>
<p>TRUE if the digests match or FALSE if they do not or either or both are missing. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3), <code><a href="/docs/linux/man/3-selabel_partial_match/">selabel_partial_match</a></code>(3), <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/5-selabel_file/">selabel_file</a></code>(5) </p>
