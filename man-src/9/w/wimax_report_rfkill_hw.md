---
title: "wimax_report_rfkill_hw(9)"
name: "wimax_report_rfkill_hw"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_report_rfkill_hw/"
description: "wimax_report_rfkill_hw – Reports changes in the hardware RF switch"
---

<p>wimax_report_rfkill_hw &#8211; Reports changes in the hardware RF switch</p>
<h2>Synopsis</h2>
<pre><code>void wimax_report_rfkill_hw(struct wimax_dev *wimax_dev, enum wimax_rf_state state);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<p> <i>state</i></p>
<dl>
<dd>New state of the RF Kill switch. <code>WIMAX_RF_ON</code> radio on, <code>WIMAX_RF_OFF</code> radio off.</dl>
<h2>Description</h2>
<p>When the device detects a change in the state of thehardware RF switch, it must call this function to let the WiMAX kernel stack know that the state has changed so it can be properly propagated. </p>
<p> The WiMAX stack caches the state (the driver doesn&#8217;t need to). As well, as the change is propagated it will come back as a request to change the software state to mirror the hardware state. </p>
<p> If the device doesn&#8217;t have a hardware kill switch, just report it on initialization as always on (<code>WIMAX_RF_ON</code>, radio on).</p>
<h2>Copyright</h2>
