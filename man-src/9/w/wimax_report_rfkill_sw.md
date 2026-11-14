---
title: "wimax_report_rfkill_sw(9)"
name: "wimax_report_rfkill_sw"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_report_rfkill_sw/"
description: "wimax_report_rfkill_sw – Reports changes in the software RF switch"
---

<p>wimax_report_rfkill_sw &#8211; Reports changes in the software RF switch</p>
<h2>Synopsis</h2>
<pre><code>void wimax_report_rfkill_sw(struct wimax_dev *wimax_dev, enum wimax_rf_state state);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<p> <i>state</i></p>
<dl>
<dd>New state of the RF kill switch. <code>WIMAX_RF_ON</code> radio on, <code>WIMAX_RF_OFF</code> radio off.</dl>
<h2>Description</h2>
<p>Reports changes in the software RF switch state to the WiMAX stack. </p>
<p> The main use is during initialization, so the driver can query the device for its current software radio kill switch state and feed it to the system. </p>
<p> On the side, the device does not change the software state by itself. In practice, this can happen, as the device might decide to switch (in software) the radio off for different reasons.</p>
<h2>Copyright</h2>
