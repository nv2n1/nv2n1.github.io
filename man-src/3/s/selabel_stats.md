---
title: "selabel_stats(3)"
name: "selabel_stats"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_stats/"
description: "selabel_stats – obtain SELinux labeling statistics"
---

<p>selabel_stats &#8211; obtain SELinux labeling statistics</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

#include &lt;selinux/label.h&gt;
void selabel_stats(struct selabel_handle *hnd);</code></pre>
<h2>Description</h2>
<p><code>selabel_stats</code>() causes zero or more messages to be printed containing backend-specific information about number of queries performed, number of unused entries, or other operational information. </p>
<p> The messages are printed to standard error by default; a custom logging function can be provided via <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3).</p>
<h2>Return Value</h2>
<p>None.</p>
<h2>Errors</h2>
<p>None.</p>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/3-selabel_lookup/">selabel_lookup</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
