---
title: "mmv_inc_value(3)"
name: "mmv_inc_value"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mmv_inc_value/"
description: "mmv_inc_value – update a value in a Memory Mapped Value file"
---

<p><code>mmv_inc_value</code> &#8211; update a value in a Memory Mapped Value file</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/mmv_stats.h&gt; </p>
<p> void mmv_inc_value(void *</code><i>addr</i>, pmAtomValue *<i>val</i>, double <i>inc</i>); </p>
<p> cc &#8230; -lpcp_mmv -lpcp</p>
<h2>Description</h2>
<p><code>mmv_inc_value</code> provides a convenient way of updating a value returned by the <code>mmv_lookup_value_desc</code>. <i>addr</i> is the address returned from <code>mmv_stats_init</code>(). </p>
<p> The value of the <i>inc</i> is internally cast to match the type of the metric and then added to the previous value of the metric.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mmv_stats_init/">mmv_stats_init</a></code>(3), <code><a href="/docs/linux/man/3-mmv_lookup_value_desc/">mmv_lookup_value_desc</a></code>(3) and <code><a href="/docs/linux/man/5-mmv/">mmv</a></code>(5).</p>
