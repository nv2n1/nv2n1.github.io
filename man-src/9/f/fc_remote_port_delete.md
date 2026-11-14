---
title: "fc_remote_port_delete(9)"
name: "fc_remote_port_delete"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_remote_port_delete/"
description: "fc_remote_port_delete – notifies the fc transport that a remote port is no longer in existence."
---

<p>fc_remote_port_delete &#8211; notifies the fc transport that a remote port is no longer in existence.</p>
<h2>Synopsis</h2>
<pre><code>void fc_remote_port_delete(struct fc_rport *rport);</code></pre>
<h2>Arguments</h2>
<p><i>rport</i></p>
<dl>
<dd>
<dd>The remote port that no longer exists</dl>
<h2>Description</h2>
<p>The LLDD calls this routine to notify the transport that a remote port is no longer part of the topology. Note: Although a port may no longer be part of the topology, it may persist in the remote ports displayed by the fc_host. We do this under 2 conditions: 1) If the port was a scsi target, we delay its deletion by &#8220;blocking&#8221; it. This allows the port to temporarily disappear, then reappear without disrupting the SCSI device tree attached to it. During the &#8220;blocked&#8221; period the port will still exist. 2) If the port was a scsi target and disappears for longer than we expect, we&#8217;ll delete the port and the tear down the SCSI device tree attached to it. However, we want to semi-persist the target id assigned to that port if it eventually does exist. The port structure will remain (although with minimal information) so that the target id bindings remails. </p>
<p> If the remote port is not an FCP Target, it will be fully torn down and deallocated, including the fc_remote_port class device. </p>
<p> If the remote port is an FCP Target, the port will be placed in a temporary blocked state. From the LLDD&#8217;s perspective, the rport no longer exists. From the SCSI midlayer&#8217;s perspective, the SCSI target exists, but all sdevs on it are blocked from further I/O. The following is then expected. </p>
<p> If the remote port does not return (signaled by a LLDD call to <code>fc_remote_port_add</code>) within the dev_loss_tmo timeout, then the scsi target is removed &#8211; killing all outstanding i/o and removing the scsi devices attached ot it. The port structure will be marked Not Present and be partially cleared, leaving only enough information to recognize the remote port relative to the scsi target id binding if it later appears. The port will remain as long as there is a valid binding (e.g. until the user changes the binding type or unloads the scsi host with the binding). </p>
<p> If the remote port returns within the dev_loss_tmo value (and matches according to the target id binding type), the port structure will be reused. If it is no longer a SCSI target, the target will be torn down. If it continues to be a SCSI target, then the target will be unblocked (allowing i/o to be resumed), and a scan will be activated to ensure that all luns are detected. </p>
<p> Called from normal process context only &#8211; cannot be called from interrupt.</p>
<h2>Notes</h2>
<p>This routine assumes no locks are held on entry.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
