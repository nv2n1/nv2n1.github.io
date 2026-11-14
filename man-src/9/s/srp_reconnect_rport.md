---
title: "srp_reconnect_rport(9)"
name: "srp_reconnect_rport"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_reconnect_rport/"
description: "srp_reconnect_rport – reconnect to an SRP target port"
---

<p>srp_reconnect_rport &#8211; reconnect to an SRP target port</p>
<h2>Synopsis</h2>
<pre><code>int srp_reconnect_rport(struct srp_rport *rport);</code></pre>
<h2>Arguments</h2>
<p><i>rport</i></p>
<dl>
<dd>
<dd>SRP target port.</dl>
<h2>Description</h2>
<p>Blocks SCSI command queueing before invoking <code>reconnect</code> such that <code>queuecommand</code> won&#8217;t be invoked concurrently with <code>reconnect</code> from outside the SCSI EH. This is important since a <code>reconnect</code> implementation may reallocate resources needed by <code>queuecommand</code>.</p>
<h2>Notes</h2>
<p>&#8211; This function neither waits until outstanding requests have finished nor tries to abort these. It is the responsibility of the <code>reconnect</code> function to finish outstanding commands before reconnecting to the target port. &#8211; It is the responsibility of the caller to ensure that the resources reallocated by the <code>reconnect</code> function won&#8217;t be used while this function is in progress. One possible strategy is to invoke this function from the context of the SCSI EH thread only. Another possible strategy is to lock the rport mutex inside each SCSI LLD callback that can be invoked by the SCSI EH (the scsi_host_template.eh_*() functions and also the scsi_host_template.<code>queuecommand</code> function).</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
