---
title: "wimax_reset(9)"
name: "wimax_reset"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_reset/"
description: "wimax_reset – Reset a WiMAX device"
---

<p>wimax_reset &#8211; Reset a WiMAX device</p>
<h2>Synopsis</h2>
<pre><code>int wimax_reset(struct wimax_dev *wimax_dev);</code></pre>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<h2>Return</h2>
<p><code>0</code> if ok and a warm reset was done (the device still exists in the system). </p>
<p> &#8211;<code>ENODEV</code> if a cold/bus reset had to be done (device has disconnected and reconnected, so current handle is not valid any more). </p>
<p> &#8211;<code>EINVAL</code> if the device is not even registered. </p>
<p> Any other negative error code shall be considered as non-recoverable.</p>
<h2>Description</h2>
<p>Called when wanting to reset the device for any reason. Device is taken back to power on status. </p>
<p> This call blocks; on successful return, the device has completed the reset process and is ready to operate.</p>
<h2>Copyright</h2>
