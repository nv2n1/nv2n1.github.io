---
title: "wimax_dev_rm(9)"
name: "wimax_dev_rm"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_dev_rm/"
description: "wimax_dev_rm – Unregister an existing WiMAX device"
---

<p>wimax_dev_rm &#8211; Unregister an existing WiMAX device</p>
<h2>Synopsis</h2>
<pre><code>void wimax_dev_rm(struct wimax_dev *wimax_dev);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<h2>Description</h2>
<p>Unregisters a WiMAX device previously registered for use with <code>wimax_add_rm</code>. </p>
<p> IMPORTANT! Must call before calling <code>unregister_netdev</code>. </p>
<p> After this function returns, you will not get any more user space control requests (via netlink or debugfs) and thus to wimax_dev-&gt;ops. </p>
<p> Reentrancy control is ensured by setting the state to <code>__WIMAX_ST_QUIESCING</code>. rfkill operations coming through wimax_*rfkill*() will be stopped by the quiescing state; ops coming from the rfkill subsystem will be stopped by the support being removed by <code>wimax_rfkill_rm</code>.</p>
<h2>Copyright</h2>
