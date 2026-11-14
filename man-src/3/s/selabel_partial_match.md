---
title: "selabel_partial_match(3)"
name: "selabel_partial_match"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_partial_match/"
description: "selabel_partial_match – determine whether a direct or partial match is possible on a file path – Only supported on file backend."
---

<p>selabel_partial_match &#8211; determine whether a direct or partial match is possible on a file path &#8211; Only supported on file backend.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdbool.h&gt;


#include &lt;selinux/selinux.h&gt;


#include &lt;selinux/label.h&gt;</code></pre>
<p> <code>bool selabel_partial_match(struct selabel_handle *</code><i>hnd</i><code>,</code> <code>const char *</code><i>key</i><code>);</code></p>
<h2>Description</h2>
<p><code>selabel_partial_match</code>() performs a partial match operation on the handle <i>hnd</i>, returning TRUE or FALSE. The <i>key</i> parameter is a file path to check for a direct or partial match. </p>
<h2>Return Value</h2>
<p>TRUE is returned if a direct or partial match is found, FALSE if not. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/3-selabel_stats/">selabel_stats</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/5-selabel_file/">selabel_file</a></code>(5) </p>
