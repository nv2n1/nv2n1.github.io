---
title: "fc_remove_host(9)"
name: "fc_remove_host"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_remove_host/"
description: "fc_remove_host – called to terminate any fc_transport-related elements for a scsi host."
---

<p>fc_remove_host &#8211; called to terminate any fc_transport-related elements for a scsi host.</p>
<h2>Synopsis</h2>
<pre><code>void fc_remove_host(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>Which Scsi_Host</dl>
<h2>Description</h2>
<p>This routine is expected to be called immediately preceding the a driver&#8217;s call to <code>scsi_remove_host</code>. </p>
<p> WARNING: A driver utilizing the fc_transport, which fails to call this routine prior to <code>scsi_remove_host</code>, will leave dangling objects in /sys/class/fc_remote_ports. Access to any of these objects can result in a system crash !!!</p>
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
