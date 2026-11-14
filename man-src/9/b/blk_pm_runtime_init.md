---
title: "blk_pm_runtime_init(9)"
name: "blk_pm_runtime_init"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_pm_runtime_init/"
---

blk_pm_runtime_init - Block layer runtime PM initialization routine

<h2>Synopsis</h2>

<pre><code>void blk_pm_runtime_init(struct request_queue *q, struct device *dev);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue of the device</dl>
 

 <i>dev</i>
<dl><dd>the device the queue belongs to</dl>

<h2>Description</h2>

Initialize runtime-PM-related fields for <i>q</i> and start auto suspend for <i>dev</i>. Drivers that want to take advantage of request-based runtime PM should call this function after <i>dev</i> has been initialized, and its request queue <i>q</i> has been allocated, and runtime PM for it can not happen yet(either due to disabled/forbidden or its usage_count &gt; 0). In most cases, driver should call this function before any I/O has taken place. 

 This function takes care of setting up using auto suspend for the device, the autosuspend delay is set to -1 to make runtime suspend impossible until an updated value is either set by user or by driver. Drivers do not need to touch other autosuspend settings. 

 The block layer runtime PM is request based, so only works for drivers that use request as their IO unit instead of those directly use bio's.

<h2>Copyright</h2>


