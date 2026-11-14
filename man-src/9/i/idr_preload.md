---
title: "idr_preload(9)"
name: "idr_preload"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_preload/"
description: "idr_preload – preload for idr_alloc"
---

<p>idr_preload &#8211; preload for <code>idr_alloc</code></p>
<h2>Synopsis</h2>
<pre><code>void idr_preload(gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>gfp_mask</i></p>
<dl>
<dd>
<dd>allocation mask to use for preloading</dl>
<h2>Description</h2>
<p>Preload per-cpu layer buffer for <code>idr_alloc</code>. Can only be used from process context and each <code>idr_preload</code> invocation should be matched with <code>idr_preload_end</code>. Note that preemption is disabled while preloaded. The first <code>idr_alloc</code> in the preloaded section can be treated as if it were invoked with <i>gfp_mask</i> used for preloading. This allows using more permissive allocation masks for idrs protected by spinlocks. For example, if <code>idr_alloc</code> below fails, the failure can be treated as if <code>idr_alloc</code> were called with GFP_KERNEL rather than GFP_NOWAIT. idr_preload(GFP_KERNEL); spin_lock(lock); </p>
<pre><code>id = idr_alloc(idr, ptr, start, end, GFP_NOWAIT);
spin_unlock(lock);
idr_preload_end;
if (id &lt; 0)
    error;</code></pre>
<h2>Copyright</h2>
