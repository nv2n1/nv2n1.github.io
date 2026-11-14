---
title: "scsi_track_queue_full(9)"
name: "scsi_track_queue_full"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_track_queue_full/"
description: "scsi_track_queue_full – track QUEUE_FULL events to adjust queue depth"
---

<p>scsi_track_queue_full &#8211; track QUEUE_FULL events to adjust queue depth</p>
<h2>Synopsis</h2>
<pre><code>int scsi_track_queue_full(struct scsi_device *sdev, int depth);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI Device in question</dl>
<p> <i>depth</i></p>
<dl>
<dd>Current number of outstanding SCSI commands on this device, not counting the one returned as QUEUE_FULL.</dl>
<h2>Description</h2>
<p>This function will track successive QUEUE_FULL events on a specific SCSI device to determine if and when there is a need to adjust the queue depth on the device.</p>
<h2>Return</h2>
<p>0 &#8211; No change needed, &gt;0 &#8211; Adjust queue depth to this new depth, -1 &#8211; Drop back to untagged operation using host-&gt;cmd_per_lun as the untagged command depth </p>
<p> Lock Status: None held on entry</p>
<h2>Notes</h2>
<p>Low level drivers may call this at any time and we will do &#8220;The Right Thing.&#8221; We are interrupt context safe.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
