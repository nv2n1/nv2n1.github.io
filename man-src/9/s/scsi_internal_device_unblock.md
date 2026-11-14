---
title: "scsi_internal_device_unblock(9)"
name: "scsi_internal_device_unblock"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_internal_device_unblock/"
---

scsi_internal_device_unblock - resume a device after a block request

<h2>Synopsis</h2>

<pre><code>int scsi_internal_device_unblock(struct scsi_device *sdev, enum scsi_device_state new_state);</code></pre>

<h2>Arguments</h2>

<i>sdev</i>
<dl><dd><dd>device to resume</dl>
 

 <i>new_state</i>
<dl><dd>state to set devices to after unblocking</dl>

<h2>Description</h2>

Called by scsi lld's or the midlayer to restart the device queue for the previously suspended scsi device. Called from interrupt or normal process context. 

 Returns zero if successful or error if not.

<h2>Notes</h2>

This routine transitions the device to the SDEV_RUNNING state or to one of the offline states (which must be a legal transition) allowing the midlayer to goose the queue for this device.

<h2>Authors</h2>

<b>James Bottomley</b> &lt;James.Bottomley [at] hansenpartnership.com&gt;
<dl><dd>Author.</dl>
 

 <b>Rob Landley</b> &lt;rob [at] landley.net&gt;
<dl><dd>Author.</dl>

<h2>Copyright</h2>


