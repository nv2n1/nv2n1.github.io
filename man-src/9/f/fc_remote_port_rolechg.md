---
title: "fc_remote_port_rolechg(9)"
name: "fc_remote_port_rolechg"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_remote_port_rolechg/"
description: "fc_remote_port_rolechg – notifies the fc transport that the roles on a remote may have changed."
---

<p>fc_remote_port_rolechg &#8211; notifies the fc transport that the roles on a remote may have changed.</p>
<h2>Synopsis</h2>
<pre><code>void fc_remote_port_rolechg(struct fc_rport *rport, u32 roles);</code></pre>
<h2>Arguments</h2>
<p><i>rport</i></p>
<dl>
<dd>
<dd>The remote port that changed.</dl>
<p> <i>roles</i></p>
<dl>
<dd>New roles for this port.</dl>
<h2>Description</h2>
<p>The LLDD calls this routine to notify the transport that the roles on a remote port may have changed. The largest effect of this is if a port now becomes a FCP Target, it must be allocated a scsi target id. If the port is no longer a FCP target, any scsi target id value assigned to it will persist in case the role changes back to include FCP Target. No changes in the scsi midlayer will be invoked if the role changes (in the expectation that the role will be resumed. If it doesn&#8217;t normal error processing will take place). </p>
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
