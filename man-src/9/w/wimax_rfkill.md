---
title: "wimax_rfkill(9)"
name: "wimax_rfkill"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_rfkill/"
description: "wimax_rfkill – Set the software RF switch state for a WiMAX device"
---

<p>wimax_rfkill &#8211; Set the software RF switch state for a WiMAX device</p>
<h2>Synopsis</h2>
<pre><code>int wimax_rfkill(struct wimax_dev *wimax_dev, enum wimax_rf_state state);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<p> <i>state</i></p>
<dl>
<dd>New RF state.</dl>
<h2>Return</h2>
<p>&gt;= 0 toggle state if ok, &lt; 0 errno code on error. The toggle state is returned as a bitmap, bit 0 being the hardware RF state, bit 1 the software RF state. </p>
<p> 0 means disabled (<code>WIMAX_RF_ON</code>, radio on), 1 means enabled radio off (<code>WIMAX_RF_OFF</code>).</p>
<h2>Description</h2>
<p>Called by the user when he wants to request the WiMAX radio to be switched on (<code>WIMAX_RF_ON</code>) or off (<code>WIMAX_RF_OFF</code>). With <code>WIMAX_RF_QUERY</code>, just the current state is returned.</p>
<h2>Note</h2>
<p>This call will block until the operation is complete.</p>
<h2>Copyright</h2>
