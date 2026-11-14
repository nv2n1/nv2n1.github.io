---
title: "avc_sid_stats(3)"
name: "avc_sid_stats"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_sid_stats/"
description: "avc_cache_stats, avc_av_stats, avc_sid_stats – obtain userspace SELinux AVC statistics"
---

<h2 class="name">NAME</h2>
<p> avc_cache_stats, avc_av_stats, avc_sid_stats &#8211; obtain userspace SELinux AVC statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>void avc_av_stats(void);</code> </p>
<p> <code>void avc_sid_stats(void);</code> </p>
<p> <code>void avc_cache_stats(struct avc_cache_stats *</code><i>stats</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The userspace AVC maintains two internal hash tables, one to store security ID&#8217;s and one to cache access decisions. </p>
<p> <code>avc_av_stats</code>() and <code>avc_sid_stats</code>() produce log messages indicating the status of the access decision and SID tables, respectively. The messages contain the number of entries in the table, number of hash buckets and number of buckets used, and maximum number of entries in a single bucket. </p>
<p> <code>avc_cache_stats</code>() populates a structure whose fields reflect cache activity: </p>
<dl>
<dt>
<dd>
<pre><code>
struct avc_cache_stats {
    unsigned entry_lookups;
    unsigned entry_hits;
    unsigned entry_misses;
    unsigned entry_discards;
    unsigned cav_lookups;
    unsigned cav_hits;
    unsigned cav_probes;
    unsigned cav_misses;
};
</code></pre>
</dl>
<dl>
<dt><i>entry_lookups</i></p>
<dd> Number of queries made.</p>
<dt><i>entry_hits</i></p>
<dd> Number of times a decision was found in the <i>aeref</i> argument.</p>
<dt><i>entry_misses</i></p>
<dd> Number of times a decision was not found in the <i>aeref</i> argument.</p>
<dt><i>entry_discards</i></p>
<dd> Number of times a decision was not found in the <i>aeref</i> argument and the <i>aeref</i> argument was non-NULL.</p>
<dt><i>cav_lookups</i></p>
<dd> Number of cache lookups.</p>
<dt><i>cav_hits</i></p>
<dd> Number of cache hits.</p>
<dt><i>cav_misses</i></p>
<dd> Number of cache misses.</p>
<dt><i>cav_probes</i></p>
<dd> Number of entries examined while searching the cache.</dl>
<h2>NOTES</h2>
<p> When the cache is flushed as a result of a call to <code>avc_reset</code>() or a policy change notification, the statistics returned by <code>avc_cache_stats</code>() are reset to zero. The SID table, however, is left unchanged. </p>
<p> When a policy change notification is received, a call to <code>avc_av_stats</code>() is made before the cache is flushed.</p>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3), <code><a href="/docs/linux/man/3-avc_context_to_sid/">avc_context_to_sid</a></code>(3), <code><a href="/docs/linux/man/3-avc_add_callback/">avc_add_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
