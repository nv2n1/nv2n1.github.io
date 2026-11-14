---
title: "rps_may_expire_flow(9)"
name: "rps_may_expire_flow"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rps_may_expire_flow/"
description: "rps_may_expire_flow – check whether an RFS hardware filter may be removed"
---

<p>rps_may_expire_flow &#8211; check whether an RFS hardware filter may be removed</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool rps_may_expire_flow(struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, u16&nbsp;<wbr></code><i>rxq_index</i><code>, u32&nbsp;<wbr></code><i>flow_id</i><code>, u16&nbsp;<wbr></code><i>filter_id</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device on which the filter was set</dl>
<p> <i>rxq_index</i></p>
<dl>
<dd>RX queue index</dl>
<p> <i>flow_id</i></p>
<dl>
<dd>Flow ID passed to <code>ndo_rx_flow_steer</code></dl>
<p> <i>filter_id</i></p>
<dl>
<dd>Filter ID returned by <code>ndo_rx_flow_steer</code></dl>
<h2>Description</h2>
<p>Drivers that implement <code>ndo_rx_flow_steer</code> should periodically call this function for each installed filter and remove the filters for which it returns <code>true</code>.</p>
<h2>Copyright</h2>
