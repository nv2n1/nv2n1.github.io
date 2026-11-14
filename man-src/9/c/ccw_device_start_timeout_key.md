---
title: "ccw_device_start_timeout_key(9)"
name: "ccw_device_start_timeout_key"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_start_timeout_key/"
description: "ccw_device_start_timeout_key – start a s390 channel program with timeout and key"
---

<p>ccw_device_start_timeout_key &#8211; start a s390 channel program with timeout and key</p>
<h2>Synopsis</h2>
<pre><code>int ccw_device_start_timeout_key(struct ccw_device *cdev, struct ccw1 *cpa, unsigned long intparm, __u8 lpm, __u8 key, unsigned long flags, int expires);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>target ccw device</dl>
<p> <i>cpa</i></p>
<dl>
<dd>logical start address of channel program</dl>
<p> <i>intparm</i></p>
<dl>
<dd>user specific interruption parameter; will be presented back to <i>cdev</i>&#8216;s interrupt handler. Allows a device driver to associate the interrupt with a particular I/O request.</dl>
<p> <i>lpm</i></p>
<dl>
<dd>defines the channel path to be used for a specific I/O request. A value of 0 will make cio use the opm.</dl>
<p> <i>key</i></p>
<dl>
<dd>storage key to be used for the I/O</dl>
<p> <i>flags</i></p>
<dl>
<dd>additional flags; defines the action to be performed for I/O processing.</dl>
<p> <i>expires</i></p>
<dl>
<dd>timeout value in jiffies</dl>
<h2>Description</h2>
<p>Start a S/390 channel program. When the interrupt arrives, the IRQ handler is called, either immediately, delayed (dev-end missing, or sense required) or never (no IRQ handler registered). This function notifies the device driver if the channel program has not completed during the time specified by <i>expires</i>. If a timeout occurs, the channel program is terminated via xsch, hsch or csch, and the device&#8217;s interrupt handler will be called with an irb containing ERR_PTR(-<code>ETIMEDOUT</code>).</p>
<h2>Return</h2>
<p><code>0</code>, if the operation was successful; &#8211;<code>EBUSY</code>, if the device is busy, or status pending; &#8211;<code>EACCES</code>, if no path specified in <i>lpm</i> is operational; &#8211;<code>ENODEV</code>, if the device is not operational.</p>
<h2>Context</h2>
<p>Interrupts disabled, ccw device lock held</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
