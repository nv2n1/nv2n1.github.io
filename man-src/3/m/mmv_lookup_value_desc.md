---
title: "mmv_lookup_value_desc(3)"
name: "mmv_lookup_value_desc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mmv_lookup_value_desc/"
description: "mmv_lookup_value_desc – find a value in the Memory Mapped Value file"
---

<p><code>mmv_lookup_value_desc</code> &#8211; find a value in the Memory Mapped Value file</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/mmv_stats.h&gt; </p>
<p> pmAtomValue *mmv_lookup_value_desc(void *</code><i>addr</i>, const char *<i>metric</i>, const char&nbsp;<wbr>*<i>inst</i>); </p>
<p> cc &#8230; -lpcp_mmv -lpcp</p>
<h2>Description</h2>
<p><code>mmv_lookup_value_desc</code> searches for the value of the instance identified by the external instance name <i>inst</i> of the metric <i>metric</i> in the <code><a href="/docs/linux/man/5-mmv/">MMV</a></code>(5) file. <i>addr</i> is the address returned from <code>mmv_stats_init</code>(). </p>
<p> The pointer returned points to a pmAtomValue union, which is defined as follows: </p>
<pre> typedef union {
 __int32_t l; /* 32-bit signed */
 __uint32_t ul; /* 32-bit unsigned */
 __int64_t ll; /* 64-bit signed */
 __uint64_t ull; /* 64-bit unsigned */
 float f; /* 32-bit floating point */
 double d; /* 64-bit floating point */
 char *cp; /* char ptr */
 pmValueBlock *vbp; /* pmValueBlock ptr */
 } pmAtomValue;</pre>
<p>MMV string values should be set using either of the <code>mmv_set_string</code> or <code>mmv_set_strlen</code> routines.</p>
<h2>Returns</h2>
<p>The function returns the address inside of the memory mapped region on success or NULL on failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mmv_stats_init/">mmv_stats_init</a></code>(3), <code><a href="/docs/linux/man/3-mmv_inc_value/">mmv_inc_value</a></code>(3) and <code><a href="/docs/linux/man/5-mmv/">mmv</a></code>(5).</p>
