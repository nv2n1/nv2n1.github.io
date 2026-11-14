---
title: "fc_remote_port_add(9)"
name: "fc_remote_port_add"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_remote_port_add/"
description: "fc_remote_port_add – notify fc transport of the existence of a remote FC port."
---

<p>fc_remote_port_add &#8211; notify fc transport of the existence of a remote FC port.</p>
<h2>Synopsis</h2>
<pre><code>struct fc_rport *fc_remote_port_add(struct Scsi_Host *shost, int channel, struct fc_rport_identifiers *ids);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host the remote port is connected to.</dl>
<p> <i>channel</i></p>
<dl>
<dd>Channel on shost port connected to.</dl>
<p> <i>ids</i></p>
<dl>
<dd>The world wide names, fc address, and FC4 port roles for the remote port.</dl>
<h2>Description</h2>
<p>The LLDD calls this routine to notify the transport of the existence of a remote port. The LLDD provides the unique identifiers (wwpn,wwn) of the port, it&#8217;s FC address (port_id), and the FC4 roles that are active for the port. </p>
<p> For ports that are FCP targets (aka scsi targets), the FC transport maintains consistent target id bindings on behalf of the LLDD. A consistent target id binding is an assignment of a target id to a remote port identifier, which persists while the scsi host is attached. The remote port can disappear, then later reappear, and it&#8217;s target id assignment remains the same. This allows for shifts in FC addressing (if binding by wwpn or wwnn) with no apparent changes to the scsi subsystem which is based on scsi host number and target id values. Bindings are only valid during the attachment of the scsi host. If the host detaches, then later re-attaches, target id bindings may change. </p>
<p> This routine is responsible for returning a remote port structure. The routine will search the list of remote ports it maintains internally on behalf of consistent target id mappings. If found, the remote port structure will be reused. Otherwise, a new remote port structure will be allocated. </p>
<p> Whenever a remote port is allocated, a new fc_remote_port class device is created. </p>
<p> Should not be called from interrupt context.</p>
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
